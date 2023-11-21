import datetime

def log_session(prompt, response, filename="./outputs/prompt_response_log.txt"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    completion = response.choices[0].message.content.strip()
    print("Completion: " + completion + "\n")
    
    log_entry = f"Timestamp: {timestamp}\nPrompt: {prompt}\nResponse: {completion}\n\n"

    with open(filename, "a") as file:
        file.write(log_entry)
    
    update_token_usage(response.usage.total_tokens)

def update_token_usage(new_tokens, token_file="./outputs/tokens.txt"):
    try:
        with open(token_file, "r") as file:
            current_tokens = int(file.read())
    except FileNotFoundError:
        current_tokens = 0

    total_tokens = current_tokens + new_tokens

    with open(token_file, "w") as file:
        file.write(str(total_tokens))

    print(f"Total tokens used: {total_tokens}")
