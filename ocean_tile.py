class ocean_tile:

        def __init__(self, id, cards, plants, mega_credits): 
            self.id = id 
            self.cards = cards
            self.plants = plants
            self.mega_credits = mega_credits

        def print_stats(self):
            print("=======================================================================================================")
            print("Ocean Tile Number " + self.id)

            if (int(self.cards) > 0):
                 print("\tCards to give: " + self.cards)

            if (int(self.plants) > 0):
                 print("\tPlants to give: " + self.plants)

            if (int(self.mega_credits) > 0):
                 print("\tMega Credits to give: " + self.mega_credits)