class project_card:
        def __init__(self, name, cost, requirement, tag1, tag2, tag3, color, effect, production, capability, action1, action2, action3, active_phase1, active_phase2, active_phase3, active_phase4, active_phase5,ability1, ability2, ability3, victory_points, card_number): 
            self.name = name
            self.cost = cost
            self.requirement = requirement
            self.tag1 = tag1
            self.tag2 = tag2
            self.tag3 = tag3
            self.color = color
            self.effect = effect
            self.production = production
            self.capability = capability
            self.action1 = action1
            self.action2 = action2
            self.action3 = action3
            self.active_phase1 = active_phase1
            self.active_phase2 = active_phase2
            self.active_phase3 = active_phase3
            self.active_phase4 = active_phase4
            self.active_phase5 = active_phase5
            self.ability1 = ability1
            self.ability2 = ability2
            self.ability3 = ability3
            self.victory_points = victory_points
            self.card_number = card_number

        def print_stats(self):
            print("=======================================================================================================")
            print("Name: " + self.name)

            print("\tCost: " + self.cost)
            if(self.requirement != "NONE"):
                print("\tRequirement: " + self.requirement)

            tags_array = []
            if(self.tag1 != "NONE"):    
                tags_array.append(self.tag1)
            if(self.tag2 != "NONE"):
                tags_array.append(self.tag2)
            if(self.tag3 != "NONE"):
                tags_array.append(self.tag3)
            if(tags_array != []):
                tags_string = ", ".join(tags_array)
                print("\tTags: " + tags_string)

            print("\tColor: " + self.color)

            if(self.effect != "NONE"):
                print("\tEffect: " + self.effect)

            if(self.production != "NONE"):
                print("\tProduction: " + self.production)

            if(self.capability != "NONE"):
                print("\tCapability: " + self.capability)  

            if(self.action1 != "NONE"):    
                print("\tAction 1: " + self.action1)
            if(self.action2 != "NONE"):    
                print("\tAction 2: " + self.action2)
            if(self.action3 != "NONE"):    
                print("\tAction 3: " + self.action3)

            active_phases_array = []
            if(self.active_phase1 != "FALSE"):
                active_phases_array.append("I")
            if(self.active_phase2 != "FALSE"):
                active_phases_array.append("II")
            if(self.active_phase3 != "FALSE"):
                active_phases_array.append("III")
            if(self.active_phase4 != "FALSE"):
                active_phases_array.append("IV")
            if(self.active_phase5 != "FALSE"):
                active_phases_array.append("V")
            if(active_phases_array != []):
                active_phases_string = ", ".join(active_phases_array)
                print("\tActive on Phases: " + active_phases_string)

            if(self.ability1 != "NONE"):
                print("\tAbility 1: " + self.ability1)
            if(self.ability2 != "NONE"):
                print("\tAbility 2: " + self.ability2)
            if(self.ability3 != "NONE"):
                print("\tAbility 3: " + self.ability3)

            if(self.victory_points != "NONE"):
                print("\tVictory Points: " + self.victory_points)

            print("\tCard Number: " + self.card_number)

            print("\n")