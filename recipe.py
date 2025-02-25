import logging

# Configure logging to a file
logging.basicConfig(filename='recipe.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class Recipe:
    def __init__(self, name, ingredients, instructions):
        """Initialize the recipe with a name, list of ingredients, and preparation instructions."""
        self.name = name
        self.ingredients = ingredients  # List of ingredients
        self.instructions = instructions  # List of preparation steps
        self._index = 0  # For iteration

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self.ingredients):
            self._index = 0
            raise StopIteration
        value = self.ingredients[self._index]
        self._index += 1
        return value

    def __getitem__(self, index):
        try:
            self.ingredients[index]
        except Exception as e:
            logging.error(f"Index out of range, error={e}")
            return None
        return self.ingredients[index]

    def __str__(self):
        """Return a string representation of the recipe."""
        ingredients_list = "\n".join(f"- {ing}" for ing in self.ingredients)
        instructions_list = "\n".join(f"{i+1}. {step}" for i, step in enumerate(self.instructions))
        return f"📌 Recipe: {self.name}\n\n🛒 Ingredients:\n{ingredients_list}\n\n👨‍🍳 Instructions:\n{instructions_list}"







