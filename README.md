# OpenAI Chat Completion API Test Tool

This repository contains a toy architecture for experimenting with prompts and completions using OpenAI's Chat Completion API.

## Requirements

- `openai` Python package.
- An OpenAI API key set as an environment variable.

## Installation

1. **Install OpenAI Package**
   ```shell
   pip install openai
   ```

2. **Set OpenAI API Key
   ```cmd
   set OPENAI_API_KEY=your_api_key_here
   ```

## Usage

1. **Run main**
   ```shell
   python main.py
   ```

2. **Analyze Results**
   - Session history is recorded in `outputs/prompt_response_log.txt``.
   - Token usage is tracked in `outputs/tokens.txt``.

