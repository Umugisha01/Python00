class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def describe(self):
        return f"Pizza with {', '.join(self.ingredients)}"
    
    @classmethod
    def margherita(cls):
        return cls(["tomato", "mozzarella", "basil"])
    
    @classmethod
    def pepperoni(cls):
        return cls(["tomato", "mozzarella", "pepperoni"])

    @staticmethod
    def calculate_area(diameter):
        import math
        return math.pi * (diameter /2) ** 2
    
margherita = Pizza.margherita()
print(margherita.describe())
area = Pizza.calculate_area(22)
print(f'Area: {area:.2f}')
    
