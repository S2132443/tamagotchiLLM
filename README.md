# Tamagotchi LLM

A virtual pet application with Together AI's Llama-3-70B conversation capabilities and emotional states.

## Features

- Virtual pet with hunger, happiness, and energy attributes
- Emotional state system:
  - **Hunger**: Starving (<25%), Hungry (<50%), Neutral (>50%), Bloated (>80%)
  - **Happiness**: Sad (<25%), Neutral, Happy (>50%), Extremely Happy (>80%)
  - **Energy**: Sleepy (<10%), Energetic
- State-influenced responses from pet
- Command-line interface for interaction
- Together AI API integration for conversations

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
   - `feed`: Increase pet's hunger (careful not to overfeed!)
   - `play`: Increase pet's happiness (consumes energy)
   - `talk`: Have a conversation (responses match pet's state)
   - `sleep`: Fully restore pet's energy
   - `quit`: Save and exit

## Roadmap

- [x] Implement state decay over time
- [x] Add LLM integration (Together AI's Llama-3-70B)
- [x] Implement emotional state system
- [ ] Implement JSON/SQLite persistence
- [ ] Add graphical interface option
