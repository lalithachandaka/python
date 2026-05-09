import streamlit as st
import ollama
st.title("Prompt Library")
tabs = st.tabs(["Developer","QA","Scrum Master","Financial","Scorecard","Member"])
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