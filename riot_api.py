import random

def get_match_data(puuid):
    # Dummy data, in real app call Riot API here
    return {
        "map": random.choice(["Bind", "Haven", "Split"]),
        "kdr": round(random.uniform(0.5, 2.0), 2)
    }