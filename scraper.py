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
            "league": "Premier League",
            "match": "Man United vs Liverpool",
            "home_team": "Man United",
            "away_team": "Liverpool",
            "odds": {
                "home_win": 2.9,
                "draw": 3.2,
                "away_win": 2.4
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
        },
        {
            "league": "La Liga",
            "match": "Real Madrid vs Atletico Madrid",
            "home_team": "Real Madrid",
            "away_team": "Atletico Madrid",
            "odds": {
                "home_win": 2.3,
                "draw": 3.1,
                "away_win": 2.9
            },
            "timestamp": datetime.utcnow().isoformat()
        },
        {
            "league": "Serie A",
            "match": "Juventus vs Inter",
            "home_team": "Juventus",
            "away_team": "Inter",
            "odds": {
                "home_win": 2.6,
                "draw": 3.2,
                "away_win": 2.7
            },
            "timestamp": datetime.utcnow().isoformat()
        },
        {
            "league": "Bundesliga",
            "match": "Bayern vs Dortmund",
            "home_team": "Bayern",
            "away_team": "Dortmund",
            "odds": {
                "home_win": 1.8,
                "draw": 3.6,
                "away_win": 4.1
            },
            "timestamp": datetime.utcnow().isoformat()
        }
    ]

    with open("odds.json", "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    fetch_data()
