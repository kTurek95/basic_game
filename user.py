class User:
    def __init__(self, username: str, hp: int):
        self.username = username
        self.hp = hp
        self.level = 0
        self.kills = 0
        self.user_position = []

    def count_kills(self):
        return self.kills + 1

    def upgrade_level(self):
        if 0 < self.kills < 5:
            self.level = 1
        elif 5 < self.kills < 10:
            self.level = 2
        else:
            self.level = 3

        return self.level

    def set_user_position(self, position: list):
        self.user_position = position
        return position

    def user_move(self, distance: list):
        self.user_position[0] += distance[0]
        self.user_position[1] += distance[1]
        return self.user_position
