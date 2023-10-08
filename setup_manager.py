from ocean_tile import *
from project_card import *
import random
from corporation_card import *

class setup_manager:

    def standard_setup():
        #Initial Values
        temperature = -30
        oxygen = 0
        terraforming_rating = 5

        #Set up ocean tiles
        ocean_tiles = []

        file_to_read = "ocean_tiles.txt"
        f = open(file_to_read, "r")
        lines = f.readlines()

        for line in lines:
            line_split = line.split(":")

            name = line_split[0].strip()
            value = line_split[1].strip()

            if(name == "id"):
                ocean_tile_id_current = value.strip()

            elif(name == "effect1"):
                ocean_tile_effect1_current = value.strip()                

            elif(name == "effect2"):
                ocean_tile_effect2_current = value.strip()
                ocean_tiles.append(ocean_tile(ocean_tile_id_current,ocean_tile_effect1_current,ocean_tile_effect2_current))

        #Set up project cards
        project_cards = []

        file_to_read = "project_cards.txt"
        f = open(file_to_read, "r")
        lines = f.readlines()

        for line in lines:
            line_split = line.split(":")

            name = line_split[0].strip()
            value = line_split[1].strip()

            if(name == "name"):
                project_card_name_current = value.strip()         

            elif(name == "cost"):
                project_card_cost_current = value.strip()

            elif(name == "requirement"):
                project_card_requirement_current = value.strip()

            elif(name == "tag1"):
                project_card_tag1_current = value.strip()

            elif(name == "tag2"):
                project_card_tag2_current = value.strip()

            elif(name == "tag3"):
                project_card_tag3_current = value.strip()

            elif(name == "color"):
                project_card_color_current = value.strip()

            elif(name == "effect"):
                project_card_effect_current = value.strip()

            elif(name == "production"):
                project_card_production_current = value.strip()

            elif(name == "capability"):
                project_card_capability_current = value.strip()

            elif(name == "action1"):
                project_card_action1_current = value.strip()

            elif(name == "action2"):
                project_card_action2_current = value.strip()

            elif(name == "action3"):
                project_card_action3_current = value.strip()

            elif(name == "active_phase1"):
                project_card_active_phase1_current = value.strip()

            elif(name == "active_phase2"):
                project_card_active_phase2_current = value.strip()

            elif(name == "active_phase3"):
                project_card_active_phase3_current = value.strip()

            elif(name == "active_phase4"):
                project_card_active_phase4_current = value.strip()

            elif(name == "active_phase5"):
                project_card_active_phase5_current = value.strip()

            elif(name == "ability1"):
                project_card_ability1_current = value.strip()

            elif(name == "ability2"):
                project_card_ability2_current = value.strip()

            elif(name == "ability3"):
                project_card_ability3_current = value.strip()

            elif(name == "victory_points"):
                project_card_victory_points_current = value.strip()

            elif(name == "card_number" and value != "XX"):
                project_card_card_number_current = value.strip()
                project_cards.append(project_card(project_card_name_current, project_card_cost_current, project_card_requirement_current, project_card_tag1_current, project_card_tag2_current, project_card_tag3_current, project_card_color_current, project_card_effect_current, project_card_production_current, project_card_capability_current, project_card_action1_current, project_card_action2_current, project_card_action3_current, project_card_active_phase1_current, project_card_active_phase2_current, project_card_active_phase3_current, project_card_active_phase4_current, project_card_active_phase5_current, project_card_ability1_current, project_card_ability2_current, project_card_ability3_current, project_card_victory_points_current, project_card_card_number_current))

        # Set up player hand
        player_hand = []
        for int in range(8):
            number_of_project_cards = len(project_cards) - 1

            random_number = random.randint(0, number_of_project_cards)

            player_hand.append(project_cards[random_number])
            project_cards.remove(project_cards[random_number])

        # Set up corporations
        corporation_cards = []

        file_to_read = "coporation_cards.txt"
        f = open(file_to_read, "r")
        lines = f.readlines()

        for line in lines:
            line_split = line.split(":")

            name = line_split[0].strip()
            value = line_split[1].strip()

            # name, tag1, tag2, mc, production, capability, cards, effect, action, card_number

            if(name == "name"):
                corporation_card_name_current = value.strip()         

            elif(name == "tag1"):
                corporation_card_tag1_current = value.strip()

            elif(name == "tag2"):
                corporation_card_tag2_current = value.strip()

            elif(name == "mc"):
                corporation_card_mc_current = value.strip()

            elif(name == "production"):
                corporation_card_production_current = value.strip()

            elif(name == "capability"):
                corporation_card_capability_current = value.strip()

            elif(name == "cards"):
                corporation_card_cards_current = value.strip()

            elif(name == "effect"):
                corporation_card_effect_current = value.strip()

            elif(name == "action"):
                corporation_card_action_current = value.strip()

            elif(name == "card_number" and value != "XX"):
                corporation_card_card_number_current = value.strip()
                corporation_cards.append(corporation_card(corporation_card_name_current, corporation_card_tag1_current, corporation_card_tag2_current, corporation_card_mc_current, corporation_card_production_current, corporation_card_capability_current, corporation_card_cards_current, corporation_card_effect_current, corporation_card_action_current, corporation_card_card_number_current))

        # Set up player corporation
        corporation_cards_player_options = []
        for int in range(2):
            number_of_corporation_cards = len(corporation_cards) - 1

            random_number = random.randint(0, number_of_corporation_cards)

            corporation_cards_player_options.append(corporation_cards[random_number])
            corporation_cards.remove(corporation_cards[random_number])        

        for card in corporation_cards_player_options:
            card.print_stats()

        # print("Select one corporation card from the above, enter the card number to select it and continue on.")

        player_corporation_choice = input("Select one corporation card from the above, enter the card number to select it and continue on.\n")

        for card in corporation_cards_player_options:
            if card.card_number == player_corporation_choice:
                player_corporation = card

        return [temperature, oxygen, terraforming_rating, ocean_tiles, project_cards, player_hand, player_corporation]