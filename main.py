import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

class Player:
    """
    The Player class represents the base player in the game.
    This class defines the methods for making a move and learning from previous moves.
    """
    def __init__(self):
        """
        Initialize the Player with an empty list to store learned moves.
        """
        self.learned_moves = []


    def move(self):
        """
        Return the player's move. This method needs to be implemented by subclasses.
        """
        return 'rock'


    def learn(self, my_move, their_move):
        """Add the player's move and the opponent's move to the learned moves list."""
        self.learned_moves.append((my_move, their_move))


class RandomPlayer(Player):
    """
    The RandomPlayer class represents a player that makes random moves.
    """

    def move(self):
        """
        Return a random move from the moves list.
        """
        index = random.randrange(0, 3)
        return moves[index]


class HumanPlayer(Player):
    """
    The HumanPlayer class represents a human player that can input moves via the console.
    """
    def move(self):
        """
        Prompt the user to input their move and return the valid move in lowercase.
        """
        while True:
            move = input("Rock, paper, scissors? > ")
            if move.lower() in ['rock', 'paper', 'scissors']:
                return move.lower()


class ReflectPlayer(RandomPlayer):
    """
    The ReflectPlayer class represents a player that reflects the opponent's last move.
    """
    def move(self, round):
        """
        Return the opponent's last move if available, otherwise make a random move.
        """
        if len(self.learned_moves) > 0:
            return self.learned_moves[round - 1][1]
        else:
            return super().move()


class CyclePlayer(ReflectPlayer):
    """
    The CyclePlayer class represents a player
    that cycles through moves based on the opponent's last move.
    """
    def move(self, round):
        """
        Return the next move in the cycle based on the opponent's last move,
        otherwise make a random move.
        """
        if len(self.learned_moves) > 0:
            if self.learned_moves[round - 1][0] == moves[0]:
                return moves[2]
            elif self.learned_moves[round - 1][0] == moves[1]:
                return moves[0]
            else:
                return moves[1]
        else:
            return super().move(round)


def beats(one, two):
    """
    Return True if 'one' beats 'two', False otherwise.
    """
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def check_equal(one, two):
    """
    Return True if 'one' equals 'two', False otherwise.
    """
    return one == two


class Game:
    """
    The Game class represents the Rock, Paper, Scissors game.
    It manages the game flow and scorekeeping.
    """
    def __init__(self, p1, p2):
        """
        Initialize the game with two players and their initial scores.
        """
        self.p1 = p1
        self.p2 = p2
        self.count1 = 0
        self.count2 = 0


    def check_win(self):
        """
        Print the winner of the game based on the scores.
        """
        if self.count1 > self.count2:
            print("** PLAYER ONE WINS **")
        else:
            print("** PLAYER TWO WINS **")


    def score(self, move1, move2):
        """
        Update the scores based on the moves made and print the result of the round.
        """
        if check_equal(move1, move2):
             print("** TIE **")
        elif beats(move1, move2):
            self.count1 += 1
            self.check_win()
        else:
            self.count2 += 1
            self.check_win()


    def play_round(self, round):
        """
        Play a single round of the game, including moves, scoring, and learning.
        """
        move1 = self.p1.move()
        move2 = self.p2.move(round)
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.score(move1, move2)
        print(f"Score: Player One {self.count1}, Player Two {self.count2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        """
        Play the full game, consisting of multiple rounds, and print the final result.
        """
        print("Game start!")
        for round in range(5):
            print(f"Round {round}:")
            self.play_round(round)
        print("Game over!")
        self.check_win()

if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()