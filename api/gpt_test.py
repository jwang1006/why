import openai, bob

client = openai.OpenAI(api_key=bob.conan)

stream = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "user", "content": "Say this is a test"},
    ],
    stream=True,  # Add this line
)

for chunk in stream:
    chunk_message = chunk.choices[0] # Get the Choice object
    if chunk_message.finish_reason is None: # Check if the response is still being generated
        print(chunk_message.delta.content or "", end="") # Handle potential None values
