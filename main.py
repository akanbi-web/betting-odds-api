from fastapi import FastAPI, HTTPException
import requests
from datetime import datetime, timedelta, timezone

app = FastAPI()

# ================= USERS =================
USERS = {
    "test123": {"limit": 20, "used": 0}
}

# Odds API key
ODDS_API_KEY = "0704b60e5be58e6ac4113c2b7da0cd04"


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
        data = response.json()

        if isinstance(data, dict):
            return []

        return data

    except:
        return []


# ================= AUTH =================
def check_key(api_key):
    user = USERS.get(api_key)

    if not user:
        raise HTTPException(401, "Unauthorized")

    if user["used"] >= user["limit"]:
        raise HTTPException(429, "Limit reached")

    user["used"] += 1
    return user


# ================= ALL MATCHES =================
@app.get("/odds")
def odds(api_key: str):
    user = check_key(api_key)

    data = fetch_odds()

    return {
        "success": True,
        "used": user["used"],
        "limit": user["limit"],
        "count": len(data),
        "data": data
    }


# ================= TODAY =================
@app.get("/today")
def today(api_key: str):
    user = check_key(api_key)

    data = fetch_odds()
    today_date = datetime.now(timezone.utc).date()

    result = []

    for m in data:
        t = m.get("commence_time", "")
        try:
            match_date = datetime.fromisoformat(t.replace("Z", "+00:00")).date()
            if match_date == today_date:
                result.append(m)
        except:
            pass

    return {
        "success": True,
        "used": user["used"],
        "limit": user["limit"],
        "count": len(result),
        "matches": result
    }


# ================= TOMORROW =================
@app.get("/tomorrow")
def tomorrow(api_key: str):
    user = check_key(api_key)

    data = fetch_odds()
    target_date = (datetime.now(timezone.utc) + timedelta(days=1)).date()

    result = []

    for m in data:
        t = m.get("commence_time", "")
        try:
            match_date = datetime.fromisoformat(t.replace("Z", "+00:00")).date()
            if match_date == target_date:
                result.append(m)
        except:
            pass

    return {
        "success": True,
        "used": user["used"],
        "limit": user["limit"],
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
