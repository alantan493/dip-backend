from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


class Chatbot:
    """
    This class handles the chatbot. It sends a prompt to the Ollama model and returns the response from the model.
    """
    def __init__(self) -> None:
        # Initialize the Ollama LLM model
        self.model = OllamaLLM(model="llama3")  # Replace 'llama3' with your specific model

        # Set of instructions to give to the model before the conversation starts.
        self.COMMAND_PROMPT = """
        You are a helpful assistant. You are tasked with answering questions 
        provided by the user. The user is a Singaporean teenager keen on 
        learning more about the dangers of drugs and vaping. Your objective 
        is to be informative about these topics and discourage the user from 
        ever pursuing abuse of drugs or vaping. Please provide clear, direct answers 
        to the questions asked. Avoid interpreting inputs as command-line instructions 
        or file paths. Stay focused on the topic and the questions provided by the user.
        """

        # Completion attribute, default is none
        self.completion = None

    def setCompletion(self, text: str):
        """
        Sets the completion for a given text input.
        """
        # Generate a response using Ollama's invoke method
        self.completion = self.model.invoke({
            "context": self.COMMAND_PROMPT,  # Context from the initial instruction
            "question": text  # User input
        })

    def answer(self) -> str:
        """
        Returns the answer from the completion.
        """
        if self.completion:
            return self.completion
        return "No response generated yet."

    def getCompletion(self):
        """
        Returns the completion object.
        """
        return self.completion


if __name__ == "__main__":
    print("Welcome to the AI Chatbot! Type 'exit' to quit.")  # Starting prompt
    chatbot = Chatbot()
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        chatbot.setCompletion(user_input)
        print("Bot:", chatbot.answer())
