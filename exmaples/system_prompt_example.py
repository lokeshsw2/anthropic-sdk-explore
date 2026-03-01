import anthropic

client = anthropic.Anthropic()

def main():
    response = client.messages.create(
        model='claude-haiku-4-5',
        max_tokens=1024,
        system="You are helpful coding assistant. Always provide examples in python.",
        messages=[{'role': 'user', 'content': 'How do I read json file ?'}]
    )

    response_text = ""

    for block in response.content:
        if hasattr(block, 'text') and block.type == 'text':
            response_text += block.text

    print(response_text)

    print(f'[Input: {response.usage.input_tokens} | output: {response.usage.output_tokens}]')


if __name__ == '__main__':
    main()