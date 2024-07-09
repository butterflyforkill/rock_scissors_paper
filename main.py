import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.learned_moves = [] 


    def move(self):
        return 'rock'


    def learn(self, my_move, their_move):
        self.learned_moves.append((my_move, their_move)) 


class RandomPlayer(Player):
    def move(self):
        index = random.randrange(0, 3)
        return moves[index]  
    
class HumanPlayer(Player):
    def move(self):
        move = input("Rock, paper, scissors? > ") 
        return move  


class ReflectPlayer(RandomPlayer):
    def move(self, round):
        if len(self.learned_moves) > 0:
            return self.learned_moves[round - 1][1]
        else:
            return super().move()


class CyclePlayer(Player):
    def move(self, round):
        if len(self.learned_moves) > 0:
            if self.learned_moves[round - 1][0] == moves[0]:
                return moves[1]
            elif self.learned_moves[round - 1][0] == moves[1]:
                return moves[0]
            else:
                return moves[2]                
        else:
            return super().move()

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def check_equal(one, two):
    return one == two


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.count1 = 0
        self.count2 = 0


    def check_win(self):
        if self.count1 > self.count2:
            print("** PLAYER ONE WINS **")
        else:
            print("** PLAYER TWO WINS **")
    
    
    def score(self, move1, move2):
        if check_equal(move1, move2):
             print("** TIE **")   
        elif beats(move1, move2):
            self.count1 += 1
            self.check_win()
        else:
            self.count2 += 1
            self.check_win()
    

    def play_round(self, round):
        move1 = self.p1.move()
        move2 = self.p2.move(round)
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.score(move1, move2)
        print(f"Score: Player One {self.count1}, Player Two {self.count2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round(round)
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()