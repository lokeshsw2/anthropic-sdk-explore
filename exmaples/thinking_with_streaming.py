import anthropic

client = anthropic.Anthropic()

def main():

    with client.messages.stream(
        model='claude-sonnet-4-6',
        max_tokens=4000,
        thinking={'type': 'adaptive'},
        messages=[{'role': 'user', 'content': 'solve this - 127 ^ 3'}]
    ) as stream:
        for event in stream:
            if event.type == 'content_block_start':
                if event.content_block.type == 'thinking':
                    print("\n--- THINKING ---")
                elif event.content_block.type == 'text':
                    print("\n--- ANSWER ---")
            elif event.type == 'content_block_delta':
                if event.delta.type == 'thinking_delta':
                    print(event.delta.thinking, end="", flush=True)
                if event.delta.type == 'text_delta':
                    print(event.delta.text, end="", flush=True)


if __name__ == '__main__':
    main()