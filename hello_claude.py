import os
import anthropic
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
user_input = input("Ask Claude anything: ")
while user_input.lower() != "quit":


                    message = client.messages.create(model="claude-haiku-4-5-20251001", 
                                                    max_tokens=100,
                                                    messages=[{"role": "user", "content": user_input}])
                    print(message.content[0].text)
                    user_input = input("Ask Claude anything: ")

                                