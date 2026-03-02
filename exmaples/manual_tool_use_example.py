import anthropic

client = anthropic.Anthropic()

def get_weather(location: str, unit: str = 'celsius'):
    """ Get current weather for location

    Args:
        location: City or State, e.g. San Fransisco, CA, Delhi.
        unit: Temperature unit, either "celsius" or "cahrenheit"
    """

    # Your real implementation here
    return f"72°F and sunny in {location}"

tools = [
    {
        'name': 'get_weather',
        'description': 'Get Weather for location',
        'input_schema': {
            'type': 'object',
            'properties': {
                'location': {
                    'type': 'string',
                }
            },
            'required': ['location']
        }
    }
]

def main():
    messages = [{'role': 'user', 'content': 'whats the weather in paris ?'}]

    while True:
        response = client.messages.create(
            model='claude-haiku-4-5',
            max_tokens=4096,
            tools=tools,
            messages=messages
        )

        messages.append({'role': 'assistant', 'content': response.content})

        # claude is done
        if response.stop_reason == 'end_turn':
            response_text = '\n'.join(block.text for block in response.content if hasattr(block, 'text'))
            print(response_text)
            break

        # claude wants to use a tool
        if response.stop_reason == 'tool_use':
            print('Executing tool')
            tool_call = next(block for block in response.content if block.type == 'tool_use')
            if tool_call.name == 'get_weather':
                result = get_weather(tool_call.input.get('location'))

            messages.append({
                'role': 'user',
                'content': [{
                    'type': 'tool_result',
                    'tool_use_id': tool_call.id,
                    'content': result
                }]
            })

if __name__ == '__main__':
    main()