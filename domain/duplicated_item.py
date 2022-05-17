class DuplicatedItem:
    name = None
    possible_matches = None

    def __init__(self, name, possible_matches):
        self.name = name
        self.possible_matches = possible_matches

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name
