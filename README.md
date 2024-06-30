# langchain
# FastAPI Text Summarizer
A Test Task for AI Pickels - for the position of Junior Python Developer

## Setup instrictions:
### 1. Create a virtual environment:

`python3 -m venv env`

`source env/bin/activate`  # On Windows use `env\Scripts\activate`

### 2. Install dependencies:

`pip install fastapi uvicorn langchain langchain_openai`
### 3. Insert your OpenAI API Key.
Open the file `main.py` in a text editor, and in line 9 replace `"your_api_key"` with your OpenAI API Key.
## Run instructions:
### 1. Run the application:
Navigate to virtualenv: 
`cd env`

`uvicorn main:app --reload`

### 2. Test the endpoint:

Send a POST request to http://127.0.0.1:8000/summarize with a JSON body containing the text to be summarized.

### Details:
You can run the program test_application.py: navigate to the folder that contains test_application.py;

`python3 test_application.py`
