# Tamagotchi LLM

A virtual pet application with Together AI's Llama-3-70B conversation capabilities.

## Features

- Virtual pet with hunger, happiness, and energy attributes
- Command-line interface for interaction
- Together AI API integration for conversations
- State persistence between sessions

## Installation

1. Clone this repository
2. Get a free API key from [Together AI](https://www.together.ai)
3. Create a `.env` file in the project root with:
   ```bash
   TOGETHER_API_KEY=your_api_key_here
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the application:
   ```bash
   python -m tamagotchi_llm.main_phi3
   ```

## Usage

After starting the application:
1. Name your pet
2. Interact using commands:
   - `feed`: Increase pet's hunger
   - `play`: Increase pet's happiness
   - `talk`: Have a conversation
   - `quit`: Save and exit

## Roadmap

- [ ] Implement state decay over time
- [x] Add LLM integration (Together AI's Llama-3-70B)
- [ ] Implement JSON/SQLite persistence
- [ ] Add graphical interface option
