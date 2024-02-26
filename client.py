import requests
import json

def generate_chat_name(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        question = data['question']
    url = "http://127.0.0.1:5000/generate_chat_name"
    data = {"question": question}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()['chat_name']
    else:
        print(f"Failed to generate chat name. Status code: {response.status_code}")

file_path = "example_input.json"
chat_name = generate_chat_name(file_path)
print("Generated Chat Name:", chat_name)