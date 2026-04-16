from fastapi import FastAPI
import json
import subprocess

app = FastAPI()

API_KEY = "mysecret123"

# run scraper on startup
try:
    subprocess.run(["python", "scraper.py"])
except Exception as e:
    print("Scraper failed:", e)


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
    return {
        "count": len(load_data()),
        "data": load_data()
    }


@app.get("/match")
def get_match(team: str, api_key: str = None):
    if api_key != API_KEY:
        return {"error": "Unauthorized"}

    result = []
    for match in load_data():
        if team.lower() in match["home_team"].lower() or team.lower() in match["away_team"].lower():
            result.append(match)

    return {
        "count": len(result),
        "matches": result
    }


@app.get("/status")
def status():
    return {
        "service": "Football Odds API",
        "status": "running",
        "total_matches": len(load_data())
    }
