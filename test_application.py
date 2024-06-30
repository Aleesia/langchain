import requests
import json

url = "http://127.0.0.1:8000/summarize"
data = {"text": """Some example text to illustrate that the code is working. You can add any text you wish here. My goldfish has eaten my hedgehog and felt sick. The doctor could not help her. So today we have the goldfish's funeral. It is very sad."""}

data = json.dumps(data)
response = requests.post(url, data=data).json()
print("response: ", response['summary'])
