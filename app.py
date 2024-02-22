from flask import Flask, request, jsonify, Response, send_file, abort
from dotenv import load_dotenv
import requests
from chat_completion import run_conversation

app = Flask(__name__)

@app.route('/smi/chatbot', methods=['GET'])
def chatbot():
    try:
        query = request.args.get('query')
        result = run_conversation(query)
        response = {
            "message": {
                "content": result.choices[0].message.content,
                "role": result.choices[0].message.role
            },
            "usage": vars(result.usage)
        }
        return jsonify(response) 
    except Exception as e:
        error_message = {'error': str(e)}
        return jsonify(error_message), 400
    
@app.route('/smi/chatbot', methods=['POST'])
def chatbot_with_history():
    try:
        query = request.args.get('query')
        history = request.json.get('history')
        result = run_conversation(query, history)
        response = {
            "message": {
                "content": result.choices[0].message.content,
                "role": result.choices[0].message.role
            },
            "usage": vars(result.usage)
        }
        return jsonify(response) 
    except Exception as e:
        error_message = {'error': str(e)}
        return jsonify(error_message), 400
    

@app.route('/', methods=['GET'])
def info():
    return 'Server is Running on port 5000'

if __name__ == '__main__':
    app.run(debug=True, port=5002)
