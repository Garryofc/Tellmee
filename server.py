from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = ""

def generate_chat_name(question):
    prompt = f'Generate a conversation name based on the question: {question}'
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "system", "content": "You are a helpful assistant. Your name is Karel"},
              {"role": "user", "content": prompt}],
    max_tokens=500,
    temperature=1,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
).choices[0].message['content']

    return response

@app.route('/generate_chat_name', methods=['POST'])
def generate_chat_name_route():
    try:
        data = request.get_json()
        if 'question' not in data:
            return jsonify({'error': 'Missing "question" in JSON body'}), 400
        question = data['question']
        chat_name = generate_chat_name(question)
        return jsonify({'chat_name': chat_name}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
