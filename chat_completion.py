from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import requests
from flask import abort

load_dotenv()

client = OpenAI(api_key = os.getenv('API_KEY'))

def search_data(query):
    try:
        response = requests.get(os.getenv('API_QUERY_URL'), params={'query': query})
        result = response.json().get('result')
        data = ""
        for i, res in enumerate(sorted(result, key=lambda x: x['similarity'], reverse=True)[0:6]):
            data += "\n\ndata " + str(i+1) + '\n'
            #data += "\nsource title : " + res.get('source_title')
            uri = 'http://10.10.6.69:5000/files/' + res.get('source_uri')
            data += "\nsource url : " + uri + '\n'
            #data += "\ncontent : " + res.get('content')
            data += res.get('source_title') + ' ' + res.get('content')
        return data
    except Exception as e:
        abort(400, str(e))

def run_conversation(query):
    messages = [{"role": "system", "content": "You are professional assistant. answer question based on data. you can search data with function call. Dont search multiple data in 1 query instead split into multiple query. always include the source on answer and source url. DON'T ANSWER a question that didnt relate to PT SMI and the data that have been given"},
                {"role": "user", "content": query}]
    tools = [
        {
            "type": "function",
            "function": {
                "name": "search_data",
                "description": "Get relevan data from knowledge base with vector search",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "query to search data"
                        }
                    }, 
                    "required": ["query"]
                }
            }
            
    }
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    if tool_calls:
        available_functions = {
            "search_data": search_data,
        }
        messages.append(response_message)

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(query = function_args.get("query"))
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )
        second_response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=messages,
        )
        second_response = {
            "finish_reason": second_response.choices[0].finish_reason,
            "index": second_response.choices[0].index,
            "logprobs": second_response.choices[0].logprobs,
            "message": {
                "content": second_response.choices[0].message.content,
                "role": second_response.choices[0].message.role,
                "function_call": second_response.choices[0].message.function_call,
                "tool_calls": second_response.choices[0].message.tool_calls
            }
        }

        return second_response
    else:
        response = {
            "finish_reason": response.choices[0].finish_reason,
            "index": response.choices[0].index,
            "logprobs": response.choices[0].logprobs,
            "message": {
                "content": response.choices[0].message.content,
                "role": response.choices[0].message.role,
                "function_call": response.choices[0].message.function_call,
                "tool_calls": response.choices[0].message.tool_calls
            }
        }
        return response