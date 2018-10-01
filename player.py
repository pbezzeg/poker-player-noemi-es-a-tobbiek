from __future__ import print_function
import sys


class Player:
    VERSION = "3.8"

    def betRequest(self, game_state):
        position = game_state["in_action"]
        players = game_state["players"]
        community_cards = game_state["community_cards"]

        def check_our_pairs():
            first_card = own_card(0)
            second_card = own_card(1)
            if first_card == second_card:
                print("pair in hand", file=sys.stderr)
                return 100

            for community_card in community_cards:
                if (community_card['rank'] == first_card["rank"]) or (community_card['rank'] == second_card["rank"]):
                    print("pair with desk", file=sys.stderr)
                    return 50


        def allin():
            our_money = 0
            for player in players:
                if player["id"] == position:
                    our_money = player["stack"]

            for player in players:
                if (our_money < player["stack"]) and game_state["round"] > 0:
                    return 0
                else:
                    return int(our_money)


        def own_card(card):
            for player in players:
                if player["id"] == position:
                    cards = player["hole_cards"]
                    return cards[card]

        print("asd" + str(own_card(0)), file=sys.stderr)
        print("asd" + str(own_card(1)), file=sys.stderr)


        if allin() > 0:
            return allin()

        if check_our_pairs() > 49:
            return check_our_pairs()
        return 1000

    def showdown(self, game_state):
        pass

