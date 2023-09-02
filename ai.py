from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

english_api_key = "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"
english_model_name = "davinci:ft-personal-2023-09-01-13-31-52"

korean_api_key = "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"
korean_model_name = "davinci:ft-personal-2023-09-01-13-31-52"
conversation_history = []

@app.route('/get_answer', methods=['POST'])
def get_answer():
    data = request.get_json()
    prompt = data.get('prompt')
    language = data.get('language')

    if language == 'en':
        openai.api_key = english_api_key
        model_name = english_model_name
        
    elif language == 'ko':
        openai.api_key = korean_api_key
        model_name = korean_model_name

    else:
        return jsonify({"error": "Unsupported language"}), 400

    conversation_history.append(prompt)
    conversation = "\n".join(conversation_history)

    response = openai.Completion.create(
        engine=model_name,
        prompt=conversation,
        max_tokens=30,
        temperature=0.3,
        n=100
    )
    return jsonify({"answer": response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(port=5003)
