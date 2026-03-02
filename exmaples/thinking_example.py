import anthropic

client = anthropic.Anthropic()
def main():

    messages = [{'role': 'user', 'content': 'solve this step by step. what is 127 ^ 3 ?'}]

    response = client.messages.create(
        model='claude-sonnet-4-6',
        max_tokens=10000,
        thinking={'type': 'adaptive'},
        messages=messages
    )

    thinking_text = ''
    response_text = ''

    for block in response.content:
        if hasattr(block, 'text') and block.type == 'text' :
            response_text += block.text
        if hasattr(block, 'thinking') and block.type == 'thinking':
            thinking_text += block.thinking

    print('==== Thinking =====')
    print(thinking_text)

    print('\n\n ==== Response ====')
    print(response_text)

if __name__ == '__main__':
    main()