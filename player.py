from __future__ import print_function
import sys


class Player:
    VERSION = "4.1"

    def betRequest(self, game_state):
        position = game_state["in_action"]
        players = game_state["players"]
        community_cards = game_state["community_cards"]
        our_money = 0
        for player in players:
            if player["id"] == position:
                our_money = player["stack"]


        def ranksystem():
            number = 0
            card1=owncard(0)
            card2=owncard(1)

            if card1["rank"] == "A":
                number += 13
            elif card1["rank"] == "K":
                number += 12
            elif card1["rank"] == "Q":
                number += 11
            elif card1["rank"] == "J":
                number += 10
            elif card1["rank"] == "10":
                number += 9
            elif card1["rank"] == "9":
                number += 8
            elif card1["rank"] == "8":
                number += 7
            elif card1["rank"] == "7":
                number += 6
            elif card1["rank"] == "6":
                number += 5
            elif card1["rank"] == "5":
                number += 4
            elif card1["rank"] == "4":
                number += 3
            elif card1["rank"] == "3":
                number += 2
            elif card1["rank"] == "2":
                number += 1

            if card2["rank"] == "A":
                number += 13
            elif card2["rank"] == "K":
                number += 12
            elif card2["rank"] == "Q":
                number += 11
            elif card2["rank"] == "J":
                number += 10
            elif card2["rank"] == "10":
                number += 9
            elif card2["rank"] == "9":
                number += 8
            elif card2["rank"] == "8":
                number += 7
            elif card2["rank"] == "7":
                number += 6
            elif card2["rank"] == "6":
                number += 5
            elif card2["rank"] == "5":
                number += 4
            elif card2["rank"] == "4":
                number += 3
            elif card2["rank"] == "3":
                number += 2
            elif card2["rank"] == "2":
                number += 1

            if card2["rank"] == card1["rank"]:
                number += 4

            if number >= 25:
                return 1
            elif number >= 23:
                return 2
            elif number >= 18:
                return 3
            elif number >= 15:
                return 4
            else:
                return 5


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


        if check_our_pairs() > 0:
            return check_our_pairs()

        if ranksystem() == 1:
            return raise_money(60)
        elif ranksystem() == 2:
            return raise_money(40)
        elif ranksystem() == 3:
            return raise_money(10)
        else:
            return 0

    def showdown(self, game_state):
        pass

