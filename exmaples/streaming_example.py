import anthropic

client = anthropic.Anthropic()

def main():

    messages = [{'role': 'user', 'content': 'Write a story ?'}]

    with client.messages.stream(
        model='claude-haiku-4-5',
        max_tokens=100,
        messages=messages
    ) as stream:
        for text in stream.text_stream:
            print(text, end='', flush=True)

    final_response = stream.get_final_message()
    print()
    print(f'Tokens [Input: {final_response.usage.input_tokens} | Output: {final_response.usage.output_tokens}]')

if __name__ == '__main__':
    main()