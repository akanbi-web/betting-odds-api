from fastapi import FastAPI, HTTPException
import requests
from datetime import datetime, timedelta, timezone

app = FastAPI()

# your protection key
API_KEY = "mysecret123"

# your real odds API key
ODDS_API_KEY = "0704b60e5be58e6ac4113c2b7da0cd04cz"


@app.get("/")
def home():
    return {"message": "Sellable Odds API running"}


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

    try:
        response = requests.get(url, params=params)
        return response.json()
    except:
        return []


def check_key(api_key):
    if api_key != API_KEY:
        raise HTTPException(401, "Unauthorized")


# ================= ALL ODDS =================
@app.get("/odds")
def odds(api_key: str):
    check_key(api_key)

    data = fetch_odds()

    return {
        "success": True,
        "count": len(data),
        "data": data
    }


# ================= TODAY =================
@app.get("/today")
def today(api_key: str):
    check_key(api_key)

    data = fetch_odds()
    today = datetime.now(timezone.utc).date()

    result = []

    for m in data:
        t = m.get("commence_time", "")
        try:
            if datetime.fromisoformat(t.replace("Z", "+00:00")).date() == today:
                result.append(m)
        except:
            pass

    return {
        "success": True,
        "count": len(result),
        "matches": result
    }


# ================= TOMORROW =================
@app.get("/tomorrow")
def tomorrow(api_key: str):
    check_key(api_key)

    data = fetch_odds()
    target = (datetime.now(timezone.utc) + timedelta(days=1)).date()

    result = []

    for m in data:
        t = m.get("commence_time", "")
        try:
            if datetime.fromisoformat(t.replace("Z", "+00:00")).date() == target:
                result.append(m)
        except:
            pass

    return {
        "success": True,
        "count": len(result),
        "matches": result
    }


# ================= STATUS =================
@app.get("/status")
def status():
    data = fetch_odds()
    return {
        "service": "Odds API",
        "status": "running",
        "total_matches": len(data)
    }
