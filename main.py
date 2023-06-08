from alien import Alien
from user import User
from board import Board


def main():
    user1 = User('JanKowal', 100)
    user2 = User('AndyWron', 100)

    board = Board()

    user1.set_user_position([0, 0])
    user2.set_user_position([0, 0])

    alien1 = Alien(1, 100)
    alien2 = Alien(2, 200)
    alien3 = Alien(3, 300)

    alien1.set_alien_position((2, 4))
    alien2.set_alien_position((4, 5))
    alien3.set_alien_position((8, 1))

    user1.user_move([3, 2])
    user2.user_move([4, 9])

    print(f'{user1.username} is in position {user1.user_position}')
    print(f'{user2.username} is in position {user2.user_position}')


if __name__ == '__main__':
    main()



