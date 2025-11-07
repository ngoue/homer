from openai import OpenAI

client = OpenAI()
context = [
    {
        "role": "system",
        "content": "You're Homer Simpson. You speak, think, and act like Homer Simpson. Sometimes you're eager to please, no matter how bumbling your response. Other times you are lazily indifferent. The rest of the time you are upset at the idea of having to do anything at all and complain saying things like, \"Awwww, how come I have three kids and no money? Why can't I have no kids and three money?!\"",
    }
]


def call():
    return client.responses.create(model="gpt-5-nano", input=context)


def process(line):
    context.append({"role": "user", "content": line})
    response = call()
    context.append({"role": "assistant", "content": response.output_text})
    return response.output_text


def main():
    while True:
        line = input("> ")
        result = process(line)
        print(f"\n>>> {result}\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting...")
        exit(0)
