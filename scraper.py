import json
from datetime import datetime

def fetch_data():
    data = [
        {
            "league": "Premier League",
            "match": "Chelsea vs Arsenal",
            "home_team": "Chelsea",
            "away_team": "Arsenal",
            "odds": {
                "home_win": 2.8,
                "draw": 3.1,
                "away_win": 2.5
            },
            "timestamp": datetime.utcnow().isoformat()
        },
        {
            "league": "La Liga",
            "match": "Barcelona vs Sevilla",
            "home_team": "Barcelona",
            "away_team": "Sevilla",
            "odds": {
                "home_win": 1.9,
                "draw": 3.4,
                "away_win": 4.0
            },
            "timestamp": datetime.utcnow().isoformat()
        }
    ]

    with open("odds.json", "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    fetch_data()
