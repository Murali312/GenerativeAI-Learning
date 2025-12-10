import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate


# 1. Page Configuration 
st.set_page_config(page_title="Achievement Finder", page_icon="🤖", layout="centered")

# 2. Header and Discription
st.title("🤖 Achievement Finder")
st.markdown("This AI tool helps you to find the key professional highlights of any individual.")

# 3. Sidebar for Model Selection
with st.sidebar:
    st.header("Model Selection")
    model_name = st.selectbox("Choose a model : ", ["phi3:3.8b", "llama3.2:3b"])
    st.info("Ensure Ollama is running locally with he selected model.")

# 4. User Input
# We need two inputs to make it generic : Who is it? and What is their role?
col1, col2 = st.columns(2)

with col1:
    person_name = st.text_input("Who is the individual")

with col2:
    person_role = st.text_input("Enter the person's role")

# 5. Logic to generate Achievements
if st.button("Find Achievements", type="primary"):
    if person_name and person_role:
        with st.spinner("Searching internal knowledge base for {person_name}"):
            try:
                # langchain logic
                llm = ChatOllama(model = model_name)

                # Dynamic Prompt Template : We pass both variables into the template
                template = """
                    You are a expert research assistant.
                    Please list the top 5 key achievements of {name} specifically in their role as {role}

                    Format the output as :
                        - A brief one sentence summary intro
                        - Bullet point list of achievements
                        - Keep the tone professional

                """

                prompt = PromptTemplate.from_template(template)

                # Create the chain

                chain = prompt | llm #LCEL

                # Invoke the chain with dictionary containing both variables

                response = chain.invoke({
                    'name' : person_name,
                    'role' : person_role
                })

                # Display the response
                st.markdown("-------")
                st.subheader(f"Result for {person_name}")
                st.success("Data retrieved successfully")
                st.markdown(response.content)

            except Exception as e:
                st.error(f"Error : Could not connect to Ollama.{e}")
    else:
        st.warning("Please provide both the person's name and role   ")


