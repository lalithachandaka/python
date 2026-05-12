import streamlit as st
import ollama
st.title("Prompt Library")
tabs = st.tabs(["Developer","QA","Scrum Master","Financial","Scorecard","Member","Upload","Generate"])
if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""
with tabs[0]:
    st.header("Deevloper Prompts")
    prompt_choice = st.selectbox("Select a prompt:",["Review SQL query for Snowflake",
        "Debug Python script for claims processing",
        "Write data pipeline for member attribution"])
    user_input = st.text_area("Add your code details here", key="developer_input")
    if st.button("Submit", key="developer_button"):
        if user_input:
            full_prompt = f"{prompt_choice}:\n\n{user_input}"
            response = ollama.chat(
                model = "llama3.2",messages = [
                    {"role":"user","content":full_prompt}
                ]
            )
            st.write(response['message']['content'])
        else:
            st.warning("Please add some details before submitting.")

with tabs[1]:
    st.header("QA Prompts")
    prompts_choice = st.selectbox("Select a prpmpt:",["Write test cases for this VBC measure calculation",
        "Validate this claims dataset for missing or incorrect values",
        "Review this scorecard output for data quality issues"])
    user_input = st.text_area("Add your details here",key="qa_input")
    if st.button("Submit" ,key="qa_button"):
        if user_input:
            full_prompt = f"{prompts_choice}:\n\n{user_input}"
            response = ollama.chat(model = "llama3.2",messages = [
                {"role":"user","content":full_prompt}
            ])
            st.write(response['message']['content'])
        else:
            st.warning("Please add some details before submitting.")
with tabs[2]:
    st.header("Scrum Master Prompts")
    prompt_choice = st.selectbox("Select a prompt:",["Write user stories for this project",
        "Create a sprint plan for this backlog",
        "Generate a retrospective summary for this sprint"])
    user_input = st.text_area("Add your details here",key="scrum_input")
    if st.button("Submit",key="scrum_button"):
        if user_input:
            full_prompt = f"{prompt_choice}:\n\n{user_input}"
            response = ollama.chat(model = "llama3.2",messages = [
                {"role":"user","content":full_prompt}
            ])
            st.write(response['message']['content'])
        else:
            st.warning("Please add some details before submitting.")
with tabs[3]:
    st.header("Financial Prompts")
    prompt_choice = st.selectbox("Select a prompt:",["Analyze this financial statement",
        "Generate a budget forecast for this project",
        "Review this investment proposal"])
    user_input = st.text_area("Add your details here", key="financial_input")
    if st.button("Submit", key="financial_button"):
        if user_input:
            full_prompt = f"{prompt_choice}:\n\n{user_input}"
            response = ollama.chat(model = "llama3.2",messages = [
                {"role":"user","content":full_prompt}
            ])
            st.write(response['message']['content'])
        else:
            st.warning("Please add some details before submitting.")
with tabs[4]:
    st.header("Scorecard Prompts")
    prompt_choice = st.selectbox("Select a prompt:",["Review this scorecard for data quality issues",
        "Generate insights from this scorecard output",
        "Create a presentation slide summarizing this scorecard"])
    user_input = st.text_area("Add your details here", key="scorecard_input")
    if st.button("Submit" ,key="scorecard_button"):
        if user_input:
            full_prompt = f"{prompt_choice}:\n\n{user_input}"
            response = ollama.chat(model = "llama3.2",messages = [
                {"role":"user","content":full_prompt}
            ])
            st.write(response['message']['content'])
        else:
            st.warning("Please add some details before submitting.")
with tabs[5]:
    st.header("Member Prompts")
    prompt_choice = st.selectbox("Select a prompt:",["Generate a personalized health recommendation",
        "Create a summary of this member's health history",
        "Review this member's claims data for potential issues"])
    user_input = st.text_area("Add your details here", key="member_input")
    if st.button("Submit" ,key="member_button"):
        if user_input:
            full_prompt = f"{prompt_choice}:\n\n{user_input}"
            response = ollama.chat(model = "llama3.2",messages = [
                {"role":"user","content":full_prompt}
            ])
            st.write(response['message']['content'])
        else:
            st.warning("Please add some details before submitting.")

with tabs[6]:
    st.header("Upload Prompts")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file:
        import pypdf
        reader  = pypdf.PdfReader(uploaded_file)
        pdf_text = ""
        for page in reader.pages:
            pdf_text += page.extract_text()
        st.session_state.pdf_text = pdf_text
        st.success("PDF uploaded successfully!")

with tabs[7]:
    st.header("Generate Prompts")
    team_keywords = {
        "Scorecard": ["quality", "scorecard", "provider", "numerator", "denominator", "measures", "inclusion", "exclusion"],
        "Member": ["member", "eligibility", "inclusion", "exclusion"],
        "Financial": ["CFF", "savings", "amounts", "payments", "provider"],
        "Developer": ["pipeline", "data", "schema", "table", "query", "snowflake"],
        "QA": ["validation", "test", "error", "missing", "duplicate", "quality"],
        "Scrum Master": ["sprint", "backlog", "story", "milestone", "deadline"]
    }
    team = st.selectbox("Select a team:",list(team_keywords.keys()))
    default_keywords = ", ".join(team_keywords[team])
    keywords_input = st.text_input("Keywords (edit if needed):", value=default_keywords)
    
    if st.button("Generate Prompt", key="generate_button"):
        if st.session_state.pdf_text:
            keywords = [k.strip()for k in keywords_input.split(",")]
            relevant = []
            for sentence in st.session_state.pdf_text.split("."):
                for keyword in keywords:
                    if keyword.lower() in sentence.lower():
                        relevant.append(sentence.strip())
                        break
            filtered_text = ". ".join(relevant)
            if filtered_text:
                full_prompt = f"You are analyzing a VBC healthcare document for the {team} team. Extract and summarize relevant information:\n\n{filtered_text}"
                response = ollama.chat(model = "llama3.2",messages = [{"role": "user", "content": full_prompt}])
                answer = response['message']['content']
                md_content = f"# {team} Team Report\n\n{answer}"
                st.write(answer)
                st.download_button("Download MD", md_content, f"{team}_report.md", key="download_button")
            else:
                st.warning("No relevant information found in the PDF based on the provided keywords.")
    else:
        st.warning("Please upload a PDF file first.")
