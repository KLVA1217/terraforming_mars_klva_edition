class planet:
    def __init__(self, name, temperature, oxygen, number_of_ocean_tiles):
        self.name = name
        self.temperature = temperature
        self.oxygen = oxygen
        self.number_of_ocean_tiles = number_of_ocean_tiles
        self.ocean_tiles = []

    def print_stats(self):
        print("=======================================================================================================")
        print(self.name + ": ")
        print("\tTemperature: " + str(self.temperature) + " C")
        print("\tOxygen: " + str(self.oxygen) + " %")
        print("\tOcean Tiles: " + str(self.number_of_ocean_tiles))

    def print_status(self):
        print("=======================================================================================================")
        print("Current " + self.name + " Status:")
        print("\tTemperature: " + str(self.temperature) + " C")
        print("\tOxygen: " + str(self.oxygen) + " %")
        print("\tOcean Tiles: " + str(len(self.ocean_tiles)))

    def add_ocean_tiles(self, ocean_tiles):
        self.ocean_tiles = ocean_tiles