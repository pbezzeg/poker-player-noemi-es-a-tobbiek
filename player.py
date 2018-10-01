from __future__ import print_function
import sys


class Player:
    VERSION = "1.1.7"

    def betRequest(self, game_state):

        def owncard():
            position = game_state["in_action"]
            players = game_state["players"]
            for player in players:
                if player["id"] == position:
                    return player["hole_cards"]

        print >>sys.stderr, "teszt20"
    def showdown(self, game_state):
        pass

