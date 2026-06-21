import streamlit as st
from google import genai

API_KEY = "AQ.Ab8RN6LVKt_2odP9cNmMwq3D7deEX-GjJcAD4h8lzNwKGSuX1A"

client = genai.Client(api_key=API_KEY)

st.title("🧠 AI Research Assistant")

topic = st.text_input("Enter a topic")

if st.button("Research"):
    if topic:
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"Explain {topic} in simple terms with examples."
            )

            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter a topic")