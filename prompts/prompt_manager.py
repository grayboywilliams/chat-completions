def save_prompt(prompt, filename="prompts.txt"):
    with open(filename, "a") as file:
        file.write(prompt + "\n")
