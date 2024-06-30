from fastapi import FastAPI, Request
import uvicorn
import os
from langchain.chains.summarize import load_summarize_chain
from langchain_openai import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document

API_KEY = "your_api_key"

openai_api_key = os.getenv("OPENAI_API_KEY", API_KEY)
app = FastAPI()

@app.post("/summarize")
async def summarize(request: Request):
    data = await request.json()

    text = data.get("text", "")
    
    text_splitter = CharacterTextSplitter()
    texts = text_splitter.split_text(text)
    # Create multiple documents
    docs = [Document(page_content=t) for t in texts]
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106", openai_api_key=openai_api_key)
    # Text summarization
    chain = load_summarize_chain(llm, chain_type='map_reduce')
    result = chain.invoke(docs)

    return {"summary": result["output_text"]}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
