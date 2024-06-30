# langchain
# FastAPI Text Summarizer
A Test Task for AI Pickels - for the position of Junior Python Developer

## Setup instrictions:
### 1. Create a virtual environment:

`python -m venv env
source env/bin/activate`  # On Windows use `env\Scripts\activate`

### 2. Install dependencies:

`pip install fastapi uvicorn langchain`

## Run instructions:
### 1. Run the application:

`uvicorn main:app --reload`

### 2. Test the endpoint:

Send a POST request to http://127.0.0.1:8000/summarize with a JSON body containing the text to be summarized.
