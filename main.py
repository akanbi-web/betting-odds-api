from fastapi import FastAPI
import requests

app = FastAPI()

API_KEY = "mysecret123"  # your own API protection
ODDS_API_KEY = "0704b60e5be58e6ac4113c2b7da0cd04cz"  # from Odds API


@app.get("/")
def home():
    return {"message": "Real Betting Odds API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


def fetch_odds():
    url = "https://api.the-odds-api.com/v4/sports/soccer/odds/"

    params = {
        "apiKey": ODDS_API_KEY,
        "regions": "eu",
        "markets": "h2h",
        "oddsFormat": "decimal"
    }

    response = requests.get(url, params=params)
    return response.json()


@app.get("/odds")
def get_odds(api_key: str = None):
    if api_key != API_KEY:
        return {"error": "Unauthorized"}

    data = fetch_odds()

    return {
        "success": True,
        "count": len(data),
        "data": data
    }


@app.get("/match")
def get_match(team: str, api_key: str = None):
    if api_key != API_KEY:
        return {"error": "Unauthorized"}

    data = fetch_odds()
    result = []

    for match in data:
        if team.lower() in match["home_team"].lower() or team.lower() in match["away_team"].lower():
            result.append(match)

    return {
        "success": True,
        "count": len(result),
        "matches": result
    }


@app.get("/status")
def status():
    data = fetch_odds()
    return {
        "service": "Real Football Odds API",
        "status": "running",
        "total_matches": len(data)
    }
