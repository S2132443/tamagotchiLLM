"""Main module for Tamagotchi LLM application using Together AI's Llama-3-70B."""
from .state import PetState
import requests
import os

class TamagotchiLlama3:
    """Virtual pet with Llama-3-70B conversation capabilities."""
    
    def __init__(self, name: str):
        """Initialize a new Tamagotchi with Together AI's Llama-3-70B.
        
        Args:
            name: Name for the virtual pet
        """
        self.state = PetState(name)
        self.api_key = os.getenv("TOGETHER_API_KEY")
        if not self.api_key:
            print("Warning: TOGETHER_API_KEY environment variable not set!")

    def update_state(self):
        """Update pet's state based on time and interactions."""
        self.state.update()

    def feed(self):
        """Increase hunger level."""
        self.state.feed()

    def play(self):
        """Increase happiness level."""
        self.state.play()

    def talk(self, message: str) -> str:
        """Have a conversation with the pet using Together AI's Llama-3-70B."""
        if not self.api_key:
            return "API key not configured!"
            
        prompt = (
            f"You are {self.state.name}, a virtual pet with these traits:\n"
            "- Acts like a real animal companion\n"
            "- Responds with simple, 1-2 sentence answers\n"
            "- Shows emotions through text\n"
            f"- Current state: Hunger:{self.state.hunger}/100, Happiness:{self.state.happiness}/100\n"
            f"User says: {message}\n"
            f"{self.state.name} responds:"
        )

        try:
            response = requests.post(
                "https://api.together.xyz/inference",
                json={
                    "model": "meta-llama/Llama-3-70b-chat-hf",
                    "prompt": prompt,
                    "max_tokens": 50,
                    "temperature": 0.7,
                    "stop": ["\n", "User:"]
                },
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                }
            ).json()
            
            if "output" in response:
                return response["output"]["choices"][0]["text"].strip()
            return "Sorry, I couldn't generate a response."
        except Exception as e:
            return f"API error: {str(e)}"

    def save_state(self):
        """Save current state to persistent storage."""
        pass

    def load_state(self):
        """Load state from persistent storage."""
        pass


def main():
    """Main CLI interface for Llama-3 Tamagotchi."""
    print("Welcome to Tamagotchi LLM (Llama-3 version)!")
    
    pet_name = input("\nWhat would you like to name your pet? ")
    pet = TamagotchiLlama3(pet_name)
    
    while pet.state.is_alive:
        status = pet.state.get_status()
        print(f"\n{status['name']}'s Status:")
        print(f"Hunger: {status['hunger']}/100")
        print(f"Happiness: {status['happiness']}/100")
        print(f"Energy: {status['energy']}/100")
        
        action = input("\nWhat would you like to do? (feed/play/talk/quit): ").lower()
        
        if action == "quit":
            pet.save_state()
            break
        elif action == "feed":
            pet.feed()
        elif action == "play":
            pet.play()
        elif action == "talk":
            message = input("What would you like to say? ")
            response = pet.talk(message)
            print(f"{pet.state.name} says: {response}")
        else:
            print("Invalid action. Please try again.")
        
        pet.update_state()


if __name__ == "__main__":
    main()
