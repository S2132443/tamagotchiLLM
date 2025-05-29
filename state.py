"""Module for managing Tamagotchi state and attributes."""

class PetState:
    """Handles the virtual pet's state and attributes."""
    
    def __init__(self, name: str):
        """Initialize pet state with default values.
        
        Args:
            name: Name of the pet
        """
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.is_alive = True

    def update(self):
        """Update pet state based on time passing."""
        self.hunger = max(0, min(100, self.hunger - 5))
        self.happiness = max(0, min(100, self.happiness - 3))
        self.energy = max(0, min(100, self.energy - 2))
        
        # Check if pet has died from neglect
        if self.hunger <= 0 or self.happiness <= 0 or self.energy <= 0:
            self.is_alive = False

    def feed(self, amount: int = 15):
        """Increase pet's hunger level.
        
        Args:
            amount: How much to increase hunger by (default 15)
        """
        self.hunger = min(100, self.hunger + amount)

    def play(self, amount: int = 10):
        """Increase pet's happiness level.
        
        Args:
            amount: How much to increase happiness by (default 10)
        """
        self.happiness = min(100, self.happiness + amount)
        # Playing also consumes energy
        self.energy = max(0, self.energy - 5)

    def sleep(self, amount: int = 20):
        """Increase pet's energy level.
        
        Args:
            amount: How much to increase energy by (default 20)
        """
        self.energy = min(100, self.energy + amount)

    def get_status(self) -> dict:
        """Return current pet state as a dictionary.
        
        Returns:
            Dictionary containing all state attributes
        """
        return {
            'name': self.name,
            'hunger': self.hunger,
            'happiness': self.happiness,
            'energy': self.energy,
            'is_alive': self.is_alive
        }
