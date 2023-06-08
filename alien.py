from user import User


class Alien:
    def __init__(self, level: int, hp: int):
        self.level = level
        self.hp = hp
        self.alien_position = ()

    def set_alien_position(self, position: tuple):
        self.alien_position = position
        return position

    def attack_user(self, user: User):
        damage = self.level * 10
        user.hp -= damage

        if user.hp <= 0:
            user.hp = 0
            print(f'{user.username} został pokonany przez obcego')
        else:
            print(f'{user.username} został zaatakowany przez obcego i stracił {damage} punktów żcyia')