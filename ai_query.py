import openai
import json
import os
import file_util as fu

script_dir = os.path.dirname(os.path.realpath(__file__))
secret_file = os.path.join(script_dir, 'secret_key.json')

    
secret = json.loads(fu.read_file(secret_file))
openai.api_key = secret['openai_key']

is_online = 'online' == secret['env']

# completion = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[{"role": "user", "content": "知乎是什么？"}]
# )


def query_openai(content):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}]
    )
    return completion


def query(content):
    if is_online:
        return query_openai(content)
    else:
        fake_file = os.path.join(script_dir, 'fake.txt')
        return fu.read_file(fake_file)


