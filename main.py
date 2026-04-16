from fastapi import FastAPI

app = FastAPI()

API_KEY = "mysecret123"

odds_data = [
    {
        "league": "Premier League",
        "home": "Chelsea",
        "away": "Man City",
        "odds": {
            "home_win": 3.5,
            "draw": 3.2,
            "away_win": 2.1
        }
    },
    {
        "league": "La Liga",
        "home": "Real Madrid",
        "away": "Barcelona",
        "odds": {
            "home_win": 2.4,
            "draw": 3.1,
            "away_win": 2.8
        }
    }
]

@app.get("/")
def home():
    return {"message": "Betting Odds API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/odds")
def get_odds(api_key: str = None):
    if api_key != API_KEY:
        return {"error": "Unauthorized"}
    return odds_data
    @app.get("/match")
def get_match(team: str, api_key: str = None):
    if api_key != API_KEY:
        return {"error": "Unauthorized"}
    
    result = []
    for match in odds_data:
        if team.lower() in match["home"].lower() or team.lower() in match["away"].lower():
            result.append(match)
    
    return result

@app.get("/status")
def status():
    return {
        "service": "Betting Odds API",
        "status": "running",
        "matches": len(odds_data)
    }
