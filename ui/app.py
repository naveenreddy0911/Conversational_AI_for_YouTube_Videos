import streamlit as st
import requests

st.title("Conversational AI for YouTube Videos")
st.write("Ask me any question about the video's content!")

def response_generator(query):
    try:
        response = requests.post("http://localhost:8000/query", json={"query": query})
        if response.ok:
            result = response.json()
            yield result["result"]["output"]
        else:
            st.error(f"Server responded with {response.status_code}")
    except Exception as e:
        st.error(f"Error contacting API: {e}")
    
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if query := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(query))

    st.session_state.messages.append({"role": "assistant", "content": response})