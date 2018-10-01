from __future__ import print_function
import sys


class Player:
    VERSION = "4"

    def betRequest(self, game_state):
        position = game_state["in_action"]
        players = game_state["players"]
        community_cards = game_state["community_cards"]
        our_money = 0
        for player in players:
            if player["id"] == position:
                our_money = player["stack"]

        def raise_money(perc):
            return game_state["current_buy_in"] + (our_money - game_state["current_buy_in"])/100*perc

        def check_our_pairs():
            first_card = own_card(0)
            second_card = own_card(1)
            if first_card == second_card:
                print("pair in hand", file=sys.stderr)

                return raise_money(50)

            for community_card in community_cards:
                if (community_card['rank'] == first_card["rank"]) or (community_card['rank'] == second_card["rank"]):
                    print("pair with desk", file=sys.stderr)
                    return raise_money(20)



        def own_card(card):
            for player in players:
                if player["id"] == position:
                    cards = player["hole_cards"]
                    return cards[card]

        print("asd" + str(own_card(0)), file=sys.stderr)
        print("asd" + str(own_card(1)), file=sys.stderr)


        if check_our_pairs() > 49:
            return check_our_pairs()
        return 0

    def showdown(self, game_state):
        pass

