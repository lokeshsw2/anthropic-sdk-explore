import anthropic

client = anthropic.Anthropic()

def main():

    messages = [
        {'role': 'user', 'content': 'My name is Alice.'},
        {'role': 'assistant', 'content': 'Hello Alice! Nice to meet you.'},
        {'role': 'user', 'content': 'Whats my name ?'}
    ]

    response = client.messages.create(
        model='claude-haiku-4-5',
        max_tokens=1024,
        messages=messages
    )

    response_text = '\n'.join(block.text for block in response.content if hasattr(block, 'text') and block.type == 'text')

    print(response_text)

    print(f'Tokens [Input {response.usage.input_tokens} | Output {response.usage.output_tokens}]')

if __name__ == '__main__':
    main()