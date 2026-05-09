import os
import anthropic
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
user_input = input("Ask Claude anything: ")
old_memory = []

while user_input.lower() != "quit":

                    old_memory.append({"role": "user", "content": user_input})
                    message = client.messages.create(model="claude-haiku-4-5-20251001", 
                                                    max_tokens=100,
                                                    messages= old_memory)
                    
                    response = message.content[0].text
                    print(response) 
                    old_memory.append({"role": "assistant", "content": response})
                    user_input = input("Ask Claude anything: ")
                    