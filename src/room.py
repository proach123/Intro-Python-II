# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, subtext, items):
        self.name = name
        self.subtext = subtext
        self.items = []

    def __str__(self):
        return f"{self.name}"

    def print_description(self):
        return f"{self.subtext}"

    def print_items(self):
        return f"{self.items}"

