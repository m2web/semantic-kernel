import asyncio
import os
import logging
from dotenv import load_dotenv

from semantic_kernel import Kernel
from semantic_kernel.utils.logging import setup_logging
from semantic_kernel.functions import kernel_function
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.chat_completion_client_base import ChatCompletionClientBase
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.functions.kernel_arguments import KernelArguments

from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.open_ai_prompt_execution_settings import (
    OpenAIChatPromptExecutionSettings,
)

# Load environment variables from .env file
load_dotenv()

async def main():
    # Initialize the kernel
    kernel = Kernel()

    # Add OpenAI chat completion
    chat_completion = OpenAIChatCompletion(
        ai_model_id=os.getenv("OPENAI_MODEL_ID", "gpt-4"),
        api_key=os.getenv("OPENAI_API_KEY"),
    )
    kernel.add_service(chat_completion)

    # Set the logging level for  semantic_kernel.kernel to DEBUG.
    setup_logging()
    logging.getLogger("kernel").setLevel(logging.DEBUG)

    # Add a plugin (the LightsPlugin class is defined below)
    kernel.add_plugin(
        LightsPlugin(),
        plugin_name="Lights",
    )

    # Enable planning
    execution_settings = OpenAIChatPromptExecutionSettings()
    execution_settings.function_choice_behavior = FunctionChoiceBehavior.Auto()

    # Create a history of the conversation
    history = ChatHistory()

    # Initiate a back-and-forth chat
    userInput = None
    while True:
        # Collect user input
        userInput = input("User > ")

        # Terminate the loop if the user says "exit"
        if userInput == "exit":
            break

        # Add user input to the history
        history.add_user_message(userInput)

        # Get the response from the AI
        result = await chat_completion.get_chat_message_content(
            chat_history=history,
            settings=execution_settings,
            kernel=kernel,
        )

        # Print the results
        print("Assistant > " + str(result))

        # Add the message from the agent to the chat history
        history.add_message(result)

class LightsPlugin:
    """A sample plugin for controlling lights."""
    def __init__(self):
        self.lights = [
            {"id": 1, "name": "Table Lamp", "is_on": False},
            {"id": 2, "name": "Porch light", "is_on": False},
            {"id": 3, "name": "Chandelier", "is_on": False},
        ]

    @kernel_function(
        name="get_lights",
        description="Gets a list of lights and their current state",
    )
    def get_lights(self) -> list[dict]:
        """Returns the list of lights and their states."""
        return self.lights

    @kernel_function(
        name="change_state",
        description="Changes the state of a light",
    )
    def change_state(self, id: int, is_on: bool) -> dict:
        """Changes the state of a light and returns the updated light object."""
        for light in self.lights:
            if light["id"] == id:
                light["is_on"] = is_on
                return light
        return None

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
