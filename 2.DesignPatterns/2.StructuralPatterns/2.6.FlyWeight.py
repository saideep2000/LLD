# Problem Statement
# In systems where a large number of fine-grained objects are required, 
# creating individual instances for each can lead to excessive memory consumption and 
# poor performance. Many of these objects often share common intrinsic (state-independent) 
# data, while only a small portion of their state (extrinsic) differs from one instance to 
# another. The problem is how to efficiently manage and reuse these shared intrinsic states
#  to reduce resource usage while still allowing each object to maintain its unique extrinsic properties.

# The Flyweight Design Pattern addresses this problem by separating an object's intrinsic 
# state (which is shared) from its extrinsic state (which is provided by the client). 
# A Flyweight Factory manages a pool of shared flyweight objects, and the client supplies 
# the extrinsic state when using the flyweight.

# Consider a text editor that must render a large document. Each character on the screen 
# can be represented as a flyweight. The intrinsic state might include the character code, 
# font, and size (which are often shared), while the extrinsic state—such as the character's 
# 'position on the screen—is supplied by the client during rendering.

class Character:
    """
    Flyweight object that stores intrinsic state: character, font, and size.
    """
    def __init__(self, char, font, size):
        self.char = char      # intrinsic state: the actual character
        self.font = font      # intrinsic state: font style
        self.size = size      # intrinsic state: font size

    def draw(self, x, y):
        """
        Draw the character on the screen at position (x, y) using its intrinsic state.
        Extrinsic state (position) is passed by the client.
        """
        print(f"Drawing '{self.char}' in {self.font} font of size {self.size} at position ({x}, {y})")


class CharacterFactory:
    """
    Factory that creates and manages flyweight Character objects.
    """
    _characters = {}

    @classmethod
    def get_character(cls, char, font, size):
        key = (char, font, size)
        if key not in cls._characters:
            cls._characters[key] = Character(char, font, size)
        return cls._characters[key]


# Client code using the Flyweight Pattern:
if __name__ == "__main__":
    # Text to render
    text = "HELLO"
    font = "Arial"
    size = 12

    # Positions where each character will be drawn (extrinsic state)
    positions = [(10, 10), (30, 10), (50, 10), (70, 10), (90, 10)]

    # Render each character using the flyweight factory.
    for char, pos in zip(text, positions):
        # Get the flyweight object from the factory.
        flyweight_char = CharacterFactory.get_character(char, font, size)
        # The extrinsic state (position) is passed to the draw method.
        flyweight_char.draw(*pos)

    # Check how many flyweight objects were created.
    print(f"Total flyweight objects created: {len(CharacterFactory._characters)}")


# python3 2.DesignPatterns/2.StructuralPatterns/2.6.FlyWeight.py