import openai, json
import bob  # Assuming this module holds your API key securely

with open("api/1000_words.json", "r") as f:
    words = json.load(f)


def get_gpt_response(messages):
    """Sends messages to the GPT API and returns the streamed response."""
    client = openai.OpenAI(api_key=bob.conan)
    response_stream = client.chat.completions.create(
        model="gpt-4-turbo",  # Or another suitable model
        messages=messages,
        stream=True
    )
    return response_stream

def chat_loop():
    conversation_history = []  # Store the conversation for context

    while True:
        user_input = input("You: ")
        conversation_history.append({"role": "user", "content": user_input})

        response_stream = get_gpt_response(conversation_history)

        full_response = ""  # To accumulate the full GPT response
        for chunk in response_stream:
            chunk_message = chunk.choices[0]
            if chunk_message.finish_reason is None:
                full_response += chunk_message.delta.content or ""  # Accumulate response
        print("GPT:", full_response)  # Print the full response once it's complete

        # Append GPT's response to the conversation history for context
        conversation_history.append({"role": "assistant", "content": full_response})


if __name__ == "__main__":
    chat_loop()
