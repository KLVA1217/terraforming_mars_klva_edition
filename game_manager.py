class game_manager:

    def print_current_status(temperature, oxygen, terraforming_rating, ocean_tiles, project_cards, player_hand, player_corporation):
        print("Current Game Status:")
        print("\tTemperature: " + str(temperature) + " C")
        print("\tOxygen: " + str(oxygen) + " %")
        print("\tTerraforming Rating: " + str(terraforming_rating))
        print("\tOcean Tiles: " + str(len(ocean_tiles)))
        # print("\tProject Cards: " + str(len(project_cards)))

        print("Player Status:")
        print("\tNumber of Cards in Player Hand: " + str(len(player_hand)))
        print("\tCorporation: " + player_corporation.name)
        
        print("\n")

    def print_player_cards(player_hand):
        print("Cards in your hand: ")
        for card in player_hand:
            card.print_stats()