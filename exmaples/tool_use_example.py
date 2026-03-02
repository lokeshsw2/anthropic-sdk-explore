from http.client import responses

import anthropic

@anthropic.beta_tool
def get_weather(location: str, unit: str = 'celsius'):
    """ Get current weather for location

    Args:
        location: City or State, e.g. San Fransisco, CA, Delhi.
        unit: Temperature unit, either "celsius" or "cahrenheit"
    """

    # Your real implementation here
    return f"72°F and sunny in {location}"

client = anthropic.Anthropic()

def main():
    runner = client.beta.messages.tool_runner(
        model='claude-haiku-4-5',
        max_tokens=4096,
        tools=[get_weather],
        messages=[{'role': 'user', 'content': "What's the weather in Paris ?"}]
    )

    for message in runner:
        if message.content[0].type == 'tool_use':
            print(f'==== Tool called: {message.content[0].name} ==== ')
        if message.content[0].type == 'text':
            print(message.content[0].text)


if __name__ == '__main__':
    main()