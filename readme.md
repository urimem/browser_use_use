# Browser Use Testing Automation

A Python-based automation tool for browser testing and web interaction using LangChain and OpenAI's GPT models.

## Description

This project provides a framework for automated browser testing and web interaction using AI-powered agents. It leverages LangChain and OpenAI's GPT models to perform intelligent web testing and interaction tasks.

## Features

- Automated browser testing using AI agents
- Integration with OpenAI's GPT models via LangChain
- Environment variable management with python-dotenv
- Asynchronous operation support

## Prerequisites

- Python 3.7+
- OpenAI API key
- pip (Python package manager)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd browser_use_use
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Connect to Chrome browser - Using Chrome DevTools Protocol (CDP)

To test this locally, follow these steps:
1. Find the chrome executable file.
2. On mac by default, the chrome is in `/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=$(mktemp -d -t 'chrome-remote')`
3. Add the following argument to the shortcut:
   `--remote-debugging-port=9222`
4. Open a web browser and navigate to `http://localhost:9222/json/version` to verify that the Remote Debugging Protocol (CDP) is running.
5. Launch this test.

## Usage

1. Modify the `task` variable in `main.py` to specify your testing requirements
2. Run the script:
```bash
python main.py
```
The script will use an AI agent to perform the specified testing tasks on the target website.

See examples for Testing and QA tasks/prompts here:
https://github.com/browser-use/awesome-prompts?tab=readme-ov-file#testing-and-qa-prompts 


## Dependencies

- browser-use: Browser automation library
- langchain_openai: OpenAI integration for LangChain
- asyncio: Asynchronous I/O support
- python-dotenv: Environment variable management

## License

[Add your license information here]
