"""Main module for Tamagotchi LLM application using Phi-3-mini."""
from .state import PetState
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class TamagotchiPhi3:
    """Virtual pet with Phi-3-mini conversation capabilities."""
    
    def __init__(self, name: str):
        """Initialize a new Tamagotchi with Phi-3-mini.
        
        Args:
            name: Name for the virtual pet
        """
        self.state = PetState(name)
        try:
            self.tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-3-mini-4k-instruct")
            self.model = AutoModelForCausalLM.from_pretrained(
                "microsoft/phi-3-mini-4k-instruct",
                torch_dtype="auto",
                device_map="auto"
            )
            print("Phi-3-mini LLM loaded successfully!")
        except Exception as e:
            print(f"Error loading Phi-3: {str(e)}")
            self.model = None

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
        """Have a conversation with the pet using Phi-3-mini."""
        if not self.model:
            return "LLM not available!"
            
        prompt = (
            f"<|system|>\n"
            f"You are {self.state.name}, a virtual pet with these traits:\n"
            "- Acts like a real animal companion\n"
            "- Responds with simple, 1-2 sentence answers\n"
            "- Shows emotions through text\n"
            f"- Current state: Hunger:{self.state.hunger}/100, Happiness:{self.state.happiness}/100\n"
            "<|user|>\n"
            f"{message}\n"
            "<|assistant|>\n"
            f"{self.state.name}:"
        )

        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.model.device)
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=50,
            temperature=0.7,
            do_sample=True
        )
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response.split(f"{self.state.name}:")[-1].strip()

    def save_state(self):
        """Save current state to persistent storage."""
        pass

    def load_state(self):
        """Load state from persistent storage."""
        pass


def main():
    """Main CLI interface for Phi-3 Tamagotchi."""
    print("Welcome to Tamagotchi LLM (Phi-3 version)!")
    
    pet_name = input("\nWhat would you like to name your pet? ")
    pet = TamagotchiPhi3(pet_name)
    
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
