# Tamagotchi LLM

A virtual pet application with Large Language Model (LLM) conversation capabilities.

## Features

- Virtual pet with hunger, happiness, and energy attributes
- Command-line interface for interaction
- Local LLM integration for conversations
- State persistence between sessions

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
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
- [x] Add LLM integration (Phi-3-mini)
- [ ] Implement JSON/SQLite persistence
- [ ] Add graphical interface option
