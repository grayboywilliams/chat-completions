from api_client.openai_client import OpenAIClient
from prompts.prompt_generator import *
from prompts.prompt_manager import *
from logger.log_handler import *
from responses.response_handler import *
from utils.utilities import *

def main(debug=False):
    print_welcome_message()

    client = OpenAIClient()

    prompt = generate_prompt()
    response = client.send_prompt(prompt, debug=debug)

    handle_response(response)
    log_session(prompt, response)

if __name__ == "__main__":
    main()
