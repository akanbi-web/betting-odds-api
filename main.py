from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

API_KEY = "3b232f864b1bb1ad3f56f656870e96357ec1e2ef92227d6f1e62bb561efba871"

# better structured data
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
def get_odds(x_api_key: str = Header(None)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return odds_data
