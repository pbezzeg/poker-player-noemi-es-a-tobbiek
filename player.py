from __future__ import print_function
import sys


class Player:
    VERSION = "1.2.1"

    def betRequest(self, game_state):
        position = game_state["in_action"]
        players = game_state["players"]

        def check_our_pairs():
            pass

        def own_card():
            for player in players:
                if player["id"] == position:
                    return player["name"]

        print("asd" + str(own_card()), file=sys.stderr)

        return 1
    
    def showdown(self, game_state):
        pass

