
class Player:
    VERSION = "1.1.4"

    def betRequest(self, game_state):

        def owncard():
            position = game_state["in_action"]
            players = game_state["players"]
            for player in players:
                if player["id"] == position:
                    return player["hole_cards"]
        print "kartyaink" + owncard()
        return 1

    def showdown(self, game_state):
        pass

