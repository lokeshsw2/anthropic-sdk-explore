import anthropic

client = anthropic.Anthropic()


def log_cache_usage(response):
    usage = response.usage
    cache_write = getattr(usage, "cache_creation_input_tokens", 0) or 0
    cache_read = getattr(usage, "cache_read_input_tokens", 0) or 0

    if cache_write > 0:
        print(f'CACHE MISS - wrote {cache_write} tokens to cache')
    elif cache_read > 0:
        print(f'CACHE HIT - read {cache_read} tokens from cache (90% savings!)')
    else:
        print(f'NO CACHE - all {usage.input_tokens} tokens charged at full price')


# A large system prompt (1,024+ tokens)
big_system_prompt = """You are an expert mathematician and professor.
  You specialize in probability theory, statistics, linear algebra,
  calculus, and discrete mathematics.

  Here is your complete reference textbook on probability:

  """ + """
  Probability is the branch of mathematics concerning numerical
  descriptions of how likely an event is to occur. The probability
  of an event is a number between 0 and 1, where 0 indicates
  impossibility and 1 indicates certainty. The higher the probability
  of an event, the more likely it is that the event will occur.
  A simple example is the tossing of a fair coin. Since the coin
  is fair, the two outcomes are both equally probable. The probability
  of heads equals the probability of tails. Since no other outcomes
  are possible, the probability of either heads or tails is 1/2.
  """ * 20  # Repeat to make it 1,024+ tokens


def main():
    # --- Call 1: Cache WRITE ---
    response1 = client.messages.create(
        model='claude-haiku-4-5',
        max_tokens=256,
        cache_control={'type': 'ephemeral'},
        system=big_system_prompt,
        messages=[{'role': 'user', 'content': 'Explain probability in simple terms?'}]
    )

    print('==== Call 1 ====')
    print(response1.content[0].text[:200])
    print('\n==== Caching Info ====')
    log_cache_usage(response1)

    # --- Call 2: Cache READ (run within 5 minutes) ---
    response2 = client.messages.create(
        model='claude-haiku-4-5',
        max_tokens=256,
        cache_control={'type': 'ephemeral'},
        system=big_system_prompt,
        messages=[{'role': 'user', 'content': 'What is Bayes theorem?'}]
    )

    print('\n\n==== Call 2 ====')
    print(response2.content[0].text[:200])
    print('\n==== Caching Info ====')
    log_cache_usage(response2)  # Should show CACHE HIT!


if __name__ == '__main__':
    main()
