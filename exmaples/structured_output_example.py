from http.client import responses

import anthropic
from pydantic import BaseModel
from typing import List

client = anthropic.Anthropic()

class ContactInfo(BaseModel):
    name: str
    email: str
    plan: str
    interests: list[str]

def main():

    response = client.messages.parse(
        model='claude-haiku-4-5',
        max_tokens=1024,
        messages=[{'role': 'user', 'content': "Extract: Jane Doe (jane@co.com) wants Enterprise, interested in API and SDKs"}],
        output_format=ContactInfo
    )

    output: ContactInfo = response.parsed_output
    print(output.name)
    print(output.interests)


if __name__ == '__main__':
    main()