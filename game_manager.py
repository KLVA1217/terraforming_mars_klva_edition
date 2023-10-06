class game_manager:

    def print_current_status(temperature, oxygen, terraforming_rating, ocean_tiles):
        print("Current Status:")
        print("\tTemperature: " + str(temperature) + " C")
        print("\tOxygen: " + str(oxygen) + " %")
        print("\tTerraforming Rating: " + str(terraforming_rating))
        print("\tOcean Tiles: " + str(len(ocean_tiles)))