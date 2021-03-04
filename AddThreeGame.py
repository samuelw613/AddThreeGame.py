#Samuel Weintraub
#3/3/2021
#Project 9: creates game where two players pick numbers from 1 to 9 to add up to 15

class AddThreeGame:
    """Represents a number game for two players, each player can pick 3 distinct numbers from 1 to 9"""
    def __init__(self):
        """Creates a number game object with private"""
        self._first_list = []
        self._second_list = []
        self._first_player = 0
        self._second_player = 0
        self._player = self._first_player or self._second_player
        self._input_number = []
        self._current_state = "UNFINISHED," "FIRST_WON", "SECOND_WON", "DRAW"

    def get_current_state(self):
        """Returns current state"""
        return self._current_state

    def make_move(self, player, number):
        """Eliminates possibility of input higher than 9"""
        if number not in range(1, 10) or number in self._input_number:
            return False

        count = 0
        count += 1

        self._input_number.append(number)
        self._player[self._player].append(number)

        if len(self._player[self._player]) >= 3:
            given_player = self._player[self._player]
            for i in range(0, len(given_player) - 2):
                for j in range(i + 1, len(given_player) - 1):
                    for k in range(j + 1, len(given_player)):
                        if (given_player[i] + given_player[j] + given_player[k]) == 15:
                            self._current_state = player
                            return True

        if len(self._input_number) == 9:
            self._current_state = "Draw"

            return False


game = AddThreeGame()
game.make_move("first", 2)
game.make_move("second", 5)
result = game.make_move("first", 7)
state = game.get_current_state()
