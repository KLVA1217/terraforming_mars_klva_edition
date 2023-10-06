from ocean_tile import *

###FUNCTIONS######FUNCTIONS######FUNCTIONS######FUNCTIONS######FUNCTIONS######FUNCTIONS######FUNCTIONS######FUNCTIONS######FUNCTIONS######FUNCTIONS######FUNCTIONS###

def print_current_status():
    print("Current Status:")
    print("\tTemperature: " + str(temperature) + " C")
    print("\tOxygen: " + str(oxygen) + " %")
    print("\tTerraforming Rating: " + str(terraforming_rating))
    print("\tOcean Tiles: " + str(len(ocean_tiles)))

###FUNCTIONS######FUNCTIONS######FUNCTIONS######FUNCTIONS######FUNCTIONS######FUNCTIONS######FUNCTIONS######FUNCTIONS######FUNCTIONS######FUNCTIONS######FUNCTIONS###

#Setup initial values
temperature = -30
oxygen = 0
terraforming_rating = 5

#Setup ocean tiles
ocean_tiles = []

file_to_read = "ocean_tiles.txt"
f = open(file_to_read, "r")
lines = f.readlines()

for line in lines:
    # print(line, end="")

    line_split = line.split(",")

    if(line_split[0] != "id"):
        ocean_tile_id_current = line_split[0]
        ocean_tile_effect1_current = line_split[1]
        ocean_tile_effect2_current = line_split[2]

        ocean_tile_effects_current = [ocean_tile_effect1_current, ocean_tile_effect2_current]

        ocean_tiles.append(ocean_tile(ocean_tile_id_current,ocean_tile_effects_current))

print("\n")

print_current_status()