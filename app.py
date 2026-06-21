import streamlit as st
from google import genai

# Create Gemini client using Streamlit Secrets
client = genai.Client(api_key=st.secrets["API_KEY"])

# App title
st.title("🧠 AI Research Assistant")

# User input
topic = st.text_input("Enter a topic")

# Button
if st.button("Research"):

    if topic:

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"Explain {topic} in simple terms with examples."
            )

            st.subheader("Research Result")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter a topic.")