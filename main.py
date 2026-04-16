from fastapi import FastAPI
import json

app = FastAPI()

API_KEY = "mysecret123"


def load_data():
    try:
        with open("odds.json", "r") as f:
            return json.load(f)
    except:
        return []


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
    return load_data()


@app.get("/match")
def get_match(team: str, api_key: str = None):
    if api_key != API_KEY:
        return {"error": "Unauthorized"}

    result = []
    for match in load_data():
        if team.lower() in match["home_team"].lower() or team.lower() in match["away_team"].lower():
            result.append(match)

    return result


@app.get("/status")
def status():
    return {
        "service": "Football Odds API",
        "status": "running",
        "matches": len(load_data())
    }
