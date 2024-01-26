from abc import ABC, abstractmethod

# Step 1: Defining the Product
class Localizer(ABC):
    """Abstract Product: Represents translations for specific languages."""
    @abstractmethod
    def localize(self, msg):
        """Translate the given message."""
        pass

# Step 2: Creating Concrete Products
class FrenchLocalizer(Localizer):
    """Concrete Product: Represents translations for French."""
    def __init__(self):
        self.translations = {
          "car": "voiture",
          "bike": "bicyclette",
          "cycle": "cyclette"
        }

    def localize(self, msg):
        """Translate the message to French."""
        return self.translations.get(msg, msg)

class SpanishLocalizer(Localizer):
    """Concrete Product: Represents translations for Spanish."""
    def __init__(self):
        self.translations = {
          "car": "coche",
          "bike": "bicicleta",
          "cycle": "ciclo"
        }

    def localize(self, msg):
        """Translate the message to Spanish."""
        return self.translations.get(msg, msg)

class EnglishLocalizer(Localizer):
    """Concrete Product: Represents translations for English."""
    def localize(self, msg):
        """Return the message as is (no translation)."""
        return msg

    
# Step 3: Defining the Creator
class LocalizerFactory(ABC):
    """Abstract Creator: Defines the Factory Method to create localizers."""
    @abstractmethod
    def create_localizer(self):
        """Factory Method: Create a Localizer instance."""
        pass

# Step 4: Implementing Concrete Creators
class FrenchLocalizerFactory(LocalizerFactory):
    """Concrete Creator: Creates FrenchLocalizer instances."""
    def create_localizer(self):
        """Factory Method implementation for creating FrenchLocalizer."""
        return FrenchLocalizer()

class SpanishLocalizerFactory(LocalizerFactory):
    """Concrete Creator: Creates SpanishLocalizer instances."""
    def create_localizer(self):
        """Factory Method implementation for creating SpanishLocalizer."""
        return SpanishLocalizer()

class EnglishLocalizerFactory(LocalizerFactory):
    """Concrete Creator: Creates EnglishLocalizer instances."""
    def create_localizer(self):
        """Factory Method implementation for creating EnglishLocalizer."""
        return EnglishLocalizer()

# Step 5: Utilizing the Factory
if __name__ == "__main__":
    # Create Factory instances for different languages
    f = FrenchLocalizerFactory()
    e = EnglishLocalizerFactory()
    s = SpanishLocalizerFactory()

    message = ["car", "bike", "cycle"]

    for msg in message:
        # Create and use localizers without knowing the concrete classes
        print(f.create_localizer().localize(msg))
        print(e.create_localizer().localize(msg))
        print(s.create_localizer().localize(msg))