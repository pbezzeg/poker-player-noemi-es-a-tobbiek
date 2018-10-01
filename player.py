from __future__ import print_function
import sys


class Player:
    VERSION = "2.0.2"

    def betRequest(self, game_state):
        position = game_state["in_action"]
        players = game_state["players"]
        community_cards = game_state["community_cards"]

        def check_our_pairs():
            first_card = own_card(0)
            second_card = own_card(1)
            if first_card == second_card:
                print("pair in hand")
                return 100

            for community_card in community_cards:
                if (community_card[0]['rank'] == first_card["rank"]) or (community_card[0]['rank'] == second_card["rank"]):
                    print("pair with desk")
                    return 50

        def own_card(card):
            for player in players:
                if player["id"] == position:
                    cards = player["hole_cards"]
                    return cards[card]

        print("asd" + str(own_card(0)), file=sys.stderr)
        print("asd" + str(own_card(1)), file=sys.stderr)

        print("asd" + str(community_cards), file=sys.stderr)
        print("asd" + community_cards[0]['rank'], file=sys.stderr)

        check_our_pairs()

        return 1

    def showdown(self, game_state):
        pass
