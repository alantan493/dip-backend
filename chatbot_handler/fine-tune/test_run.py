from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the prompt template
template = """
You are a helpful assistant.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

# Initialize the Ollama model
model = OllamaLLM(model="llama3")  # Replace 'llama3' with your specific model name
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to the AI Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Generate the response from the model
        result = chain.invoke({"context": context, "question": user_input})
        print("Bot:", result)

        # Append the conversation history to the context
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()
