import pypdf
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import ollama
import numpy as np

#Step 1: Load PDF and extract text
def load_pdf(file_path):
    reader = pypdf.PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

#Step 2: Convert text to chuncks
def chunk_text(text, chunk_size=500):
    words = text.split()
    chunks = []
    for i in range(0,len(words), chunk_size):
        chunk = " ".join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks

#Step 3: Embed Checks
def embed_chunks(chunks, model):
    embeddings = model.encode(chunks)
    return embeddings

# Step 4: Find relevant chunks
def get_relevant_chunks(question, chunks, embeddings, model,top_k=3):
    question_embedding = model.encode([question])
    similarities = cosine_similarity(question_embedding, embeddings)[0]
    top_indices = np.argsort(similarities)[::-1][:top_k]
    return [chunks[i] for i in top_indices]
# Step 5: Ask Ollama
def ask_ollama(question, context_chunks):
    context = "\n\n".join(context_chunks)
    prompt = f"""You are a healthcare VBC analyst. Answer based only on this context:

{context}
Question: {question}
Answer:"""
    response = ollama.chat(model="llama3.2", messages=[{"role":"user","content":prompt}])
    return response['message']['content']

#main
model = SentenceTransformer('all-MiniLM-L6-v2')
pdf_text = load_pdf("AsthmaDBR2025v110.pdf")
chunks = chunk_text(pdf_text)
print(f"Total chunks: {len(chunks)}")
embeddings = embed_chunks(chunks, model)
print("Embeddings ready.")
user_input = input("Ask a question about the asthma episode: ")
while user_input.lower() != "quit":
    relevant = get_relevant_chunks(user_input, chunks, embeddings, model)
    answer = ask_ollama(user_input, relevant)
    print(f"\nQuestion: {user_input}")
    print(f"\nAnswer: {answer}")
    user_input = input("Ask a question about the asthma episode (or type 'quit' to exit): ")

