import openai
import json


def register_chat_gpt():
    openai.api_key = "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"


def chat_gpt_chat_completion_content(text_content) -> str:
    register_chat_gpt()
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text_content}]
    )

    # Convert the OpenAI object to a JSON-formatted string
    completion_json = json.dumps(completion)

    # Convert the JSON-formatted string back to a Python object
    completion_obj = json.loads(completion_json)

    content = completion_obj['choices'][0]['message']['content']
    return content


def translator(translating_text, translating_from, translating_to) -> str:
    return chat_gpt_chat_completion_content(
        f'{translating_text}.This text is in {translating_from} and translate it to {translating_to}. Just translation.'
    )
