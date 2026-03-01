import anthropic

client = anthropic.Anthropic() #reads anthropic api key from env


def main():

    print("Hello from anthropic-sdk-demo!")

    response = client.messages.create(
        model='claude-haiku-4-5',
        max_tokens=20,
        messages=[{'role': 'user', 'content': 'What is capital of France ?'}])

    print(response.content[0].text)

    print(f'[ Input {response.usage.input_tokens} | Output {response.usage.output_tokens} ]')


if __name__ == "__main__":
    main()
