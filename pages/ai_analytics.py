import streamlit as st
from llama_cpp import Llama
import pandas as pd

st.set_page_config(page_title="AI Analytics Q&A", layout="wide")
st.title("Ask Your Data Anything (Powered by LLM)")

# Cache the model so it's loaded only once per user session
@st.cache_resource
def load_llm(model_path):
    return Llama(model_path=model_path, n_ctx=2048)

MODEL_PATH = "./Meta-Llama-3-8B-Instruct.Q4_0.gguf"
try:
    llm = load_llm(MODEL_PATH)
except Exception as e:
    st.error(f"Could not load model: {e}")
    llm = None

# DataFrame should be in session_state from the upload/preview page
if "data" not in st.session_state:
    st.warning("Upload and preview data first on the Data Preview page.")
else:
    df = st.session_state["data"]
    question = st.text_area("Type analytics question or instruction:")
    if st.button("Get AI Answer") and question and llm is not None:
        
        try:
            rows_text = df.head(5).to_markdown()
        except Exception:
            rows_text = df.head(5).to_string()
        cols_text = ', '.join(df.columns)
        prompt = f"Dataset columns: {cols_text}\nSample rows:\n{rows_text}\nQuestion: {question}\nOutput clear answer or pandas code if analysis needed."
        try:
            response = llm(prompt, max_tokens=256)
            st.write(response['choices'][0]['text'])
        except Exception as e:
            st.error(f"LLM error: {e}")

