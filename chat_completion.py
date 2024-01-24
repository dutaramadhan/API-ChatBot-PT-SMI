from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import requests

load_dotenv()

client = OpenAI(api_key = os.getenv('API_KEY'))

url = "https://api.openai.com/v1/chat/completions"

def chat_completion(query, query_result):
    system_prompt = ""
    for i, content in enumerate(query_result):
        system_prompt += '\ndata ' + str(i+1) + '\n' + query_result[i]['source_title'] + '\n' + query_result[i]['content'] + '\n' + "URL Sumber: " + query_result[i]['source_uri'] + '\n'

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON. Your name is chatS MI. You only answer question that related to PT SMI and i will include data that will be inserted as a additional knwoledge for you. Please include the source name and URL from on answer"},
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
        ]
    )
    print (response)
    return response.choices[0].message.content

    # payload = json.dumps({
    #     "model": "gpt-3.5-turbo",
    #     "temperature": 0.25,
    #     "messages": [
    #         {
    #             "role": "system",
    #             "content": "You are a helpful assistant. Your name is chatS MI. You only answer question that related to PT SMI and i will include data that will be inserted as a additional knwoledge for you. Please include the source name and URL from on answer"
    #         },    
    #         {
    #             "role": "system",
    #             "content": system_prompt
    #         },
    #         {
    #             "role": "user",
    #             "content": query
    #         }
    #     ]
    # })
    # headers = {
    #     'Authorization': 'Bearer ' + os.getenv('API_KEY'),
    #     'Content-Type': 'application/json'
    # }

    # response = requests.request("POST", url, headers=headers, data=payload)

    # return response.json()['choices'][0]['message']['content']