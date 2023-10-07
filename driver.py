from setup_manager import *
from game_manager import *

#Setup initial values

setup_instance = setup_manager.standard_setup()

temperature = setup_instance[0]
oxygen = setup_instance[1]
terraforming_rating = setup_instance[2]
ocean_tiles = setup_instance[3]
project_cards = setup_instance[4]
player_hand = setup_instance[5]

game_manager.print_current_status(temperature, oxygen, terraforming_rating, ocean_tiles, project_cards, player_hand)

game_manager.print_player_cards(player_hand)