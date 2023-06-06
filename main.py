class User:
    def __init__(self, username: str, hp: int):
        self.username = username
        self.hp = hp
        self.level = 0
        self.kills = 0

    def count_kills(self):
        return self.kills + 1

    def upgrade_level(self):
        if 0 < self.kills < 5:
            self.level = 1
        elif 5 < self.kills < 10:
            self.level = 2
        else:
            self.level = 3


class Alien:
    def __init__(self, level: int, hp: int):
        self.level = level
        self.hp = hp


class Board:
    def __init__(self, size: int, x_position: int, y_position: int):
        self.size = size

    def alien_position(self):
        pass

    def user_position(self):
        pass


alien = Alien(5, 100)
user = User('Kacperinho', 100)

