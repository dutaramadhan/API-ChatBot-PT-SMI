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
        return jsonify(result) 
    except Exception as e:
        error_message = {'error': str(e)}
        return jsonify(error_message), 400

if __name__ == '__main__':
    app.run(debug=True, port=5002)