class corporation_card:
    def __init__(self, name, tag1, tag2, mc, production, capability, cards, effect, action, card_number):
        self.name = name
        self.tag1 = tag1
        self.tag2 = tag2
        self.mc = mc
        self.production = production
        self.capability = capability
        self.cards = cards
        self.effect = effect
        self.action = action
        self.card_number = card_number

    def print_stats(self):
        print("Name: " + self.name)

        tags_array = []
        if(self.tag1 != "NONE"):    
            tags_array.append(self.tag1)
        if(self.tag2 != "NONE"):
            tags_array.append(self.tag2)
        if(tags_array != []):
            tags_string = ", ".join(tags_array)
            print("\tTags: " + tags_string)

        print("\tStarting MC: " + self.mc)

        if(self.production != "NONE"):
            print("\tProduction: " + self.production)

        if(self.capability != "NONE"):
            print("\tCapability: " + self.capability)  
        
        if(self.cards != "NONE"):
            print("\tDraws the following amount of cards: " + self.cards)

        if(self.effect != "NONE"):
            print("\tEffect: " + self.effect)

        if(self.action != "NONE"):
            print("\tAction: " + self.action)

        print("\tCard Number: " + self.card_number)

        print("\n")