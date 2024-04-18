import openai

client = openai.OpenAI(api_key="key here")

# Non-streaming:
print("----- standard request -----")
completion = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        },
    ],
)
print(completion.choices[0].message.content)

