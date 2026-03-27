class TypedAttribute:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type.__name__}, got {type(value).__name__}")
        instance.__dict__[self.name] = value

class Profile:
    age = TypedAttribute('age', int)

# Example Usage:
# p = Profile()
# p.age = 25    # Works fine
# p.age = "25"  # Raises TypeError
