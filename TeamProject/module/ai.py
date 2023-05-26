import openai
from database.base import get_all_ai_account

model_id = 'gpt-3.5-turbo'

user_key = {}
user_conv = {}


def add_user(name, key):
    user_key[name] = key
    user_conv[name] = []


def init_ai():
    user_list = get_all_ai_account()
    for user in user_list:
        add_user(user.name, user.gpt_key)


def use_ai(name, content):
    openai.api_key = user_key[name]
    user_conv[name].append({"role": "user", "content": content})
    result = ChatGPT_conversation(user_conv[name])
    answer = result.choices[0].message.content
    user_conv[name].append({"role": "assistant", "content": answer})
    return answer


def ChatGPT_conversation(conversation):
    response = openai.ChatCompletion.create(
        model=model_id,
        messages=conversation
    )
    api_usage = response['usage']
    print('Total token consumed: {0}'.format(api_usage['total_tokens']))
    # stop means complete
    print(response['choices'][0].finish_reason)
    print(response['choices'][0].index)

    return response

