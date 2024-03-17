class Game:
    def __init__(self, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if len(title) == 0:
            raise ValueError("Title must have at least 1 character")
        self._title = title

    @property
    def title(self):
        return self._title

    def results(self):
        return [result for result in Result.all_results if result.game == self]

    def players(self):
        return list({result.player for result in self.results()})

    def average_score(self, player):
        player_results = [result.score for result in Result.all_results if
                          result.player == player and result.game == self]
        return sum(player_results) / len(player_results) if player_results else 0


class Player:
    def __init__(self, username):
        if not isinstance(username, str):
            raise ValueError("Username must be a string")
        if not (2 <= len(username) <= 16):
            raise ValueError("Username must be between 2 and 16 characters long")
        self._username = username

    @property
    def username(self):
        return self._username

    def results(self):
        return [result for result in Result.all_results if result.player == self]

    def games_played(self):
        return list({result.game for result in self.results()})

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return sum(1 for result in self.results() if result.game == game)

    @classmethod
    def highest_scored(cls, game):
        players = {result.player for result in Result.all_results if result.game == game}
        if not players:
            return None
        return max(players, key=lambda player: game.average_score(player))


class Result:
    all_results = []

    def __init__(self, player, game, score):
        if not isinstance(score, int):
            raise ValueError("Score must be an integer")
        if not (1 <= score <= 5000):
            raise ValueError("Score must be between 1 and 5000")
        self._player = player
        self._game = game
        self._score = score
        Result.all_results.append(self)

    @property
    def score(self):
        return self._score

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game

