import streamlit as st

st.set_page_config(page_title="Library Assistant Chatbot", page_icon="📚")

st.title("📚 Library Assistant Chatbot")
st.write("Ask me anything about books or library rules!")

# Simple chatbot logic
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "python" in user_input:
        return "Yes, we have several Python programming books available."
    elif "hours" in user_input:
        return "The library is open from 9 AM to 6 PM, Monday to Friday."
    elif "borrow" in user_input:
        return "You can borrow up to 3 books for a period of 14 days."
    elif "fine" in user_input:
        return "The fine is ₹2 per day for late returns."
    elif "renew" in user_input:
        return "Yes, books can be renewed once if no one else has reserved them."
    else:
        return "Sorry, I couldn’t understand that. Please ask about books or library rules."

user_query = st.text_input("💬 Enter your question:")

if user_query:
    response = chatbot_response(user_query)
    st.success(response)
