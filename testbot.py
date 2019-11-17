import os
import slack
import json

with open('auth.json') as fp:
    config = json.load(fp)

token = config['bot_token']

client = slack.WebClient(token=token)

response = client.chat_postMessage(channel='#automaters',
                                   text='this is a *bot* post')

print(response)
