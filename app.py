from flask import Flask, request, jsonify, Response, send_file, abort
from dotenv import load_dotenv
import requests
from chat_completion import chat_completion

app = Flask(__name__)

api_query_url = r'http://10.10.6.69:5000/smi/api/embedding/query'


def fecth_query_api(query):
    try:
        response = requests.get(api_query_url, params={'query': query})
        return response.json()
    except Exception as e:
        abort(400, str(e))


@app.route('/smi/chatbot', methods=['GET'])
def chatbot():
    try:
        query = request.args.get('query')
        query_result = fecth_query_api(query)
        result = chat_completion(query, query_result['result'])
        return jsonify(result) 
    except Exception as e:
        error_message = {'error': str(e)}
        return jsonify(error_message), 400

if __name__ == '__main__':
    app.run(debug=True, port=5002)