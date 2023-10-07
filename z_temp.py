project_card_stats_array = ["name", "cost", "requirement", "tag1", "tag2", "tag3", "color", "effect", "production", "capability", "action1", "action2", "action3", "active_phase1", "active_phase2", "ability1", "ability2", "ability3", "victory_points", "card_number"]
string_large = ""

for stat in project_card_stats_array:
    print("if(self."+stat+ " != \"NONE\"):" )