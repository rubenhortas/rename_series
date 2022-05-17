class Match:
    name = None
    match_ratio = None

    def __init__(self, name, match_ratio):
        self.name = name
        self.match_ratio = match_ratio

    def __hash__(self):
        return hash((self.name, self.match_ratio))

    def __eq__(self, other):
        return (self.name, self.match_ratio) == (other.name, self.match_ratio)
