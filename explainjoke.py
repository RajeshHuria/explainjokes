import os
import streamlit as st
import openai
from openai import OpenAI


token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

def get_joke_explanation(joke):
    """Function to get explanation for a joke using OpenAI GPT-4 model."""
    
    response = client.chat.completions.create(
    messages=[
            {"role": "user", "content": f"Explain this joke: {joke}"}
        ],
    model="gpt-4o-mini")

    explanation = response.choices[0].message.content
    return explanation

# Streamlit application layout
st.title("Joke Explainer")
st.write("Enter a joke below, and I'll explain it to you!")

# User input for the joke
user_joke = st.text_input("Your Joke:")

if st.button("Explain Joke"):
    if user_joke:
        with st.spinner("Getting explanation..."):
            # Get the joke explanation
            explanation = get_joke_explanation(user_joke)
            # Display the explanation
            st.write("### Explanation:")
            st.write(explanation)
    else:
        st.error("Please enter a joke before clicking the button.")