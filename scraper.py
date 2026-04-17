import json
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def fetch_data():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.sportybet.com/ng/sport/football")

    time.sleep(5)

    matches = []

    rows = driver.find_elements(By.CSS_SELECTOR, ".match-row")

    for row in rows[:20]:  # limit for stability
        try:
            home = row.find_element(By.CSS_SELECTOR, ".home-team").text
            away = row.find_element(By.CSS_SELECTOR, ".away-team").text
            odds = row.find_elements(By.CSS_SELECTOR, ".odd")

            matches.append({
                "league": "Football",
                "match": f"{home} vs {away}",
                "home_team": home,
                "away_team": away,
                "odds": {
                    "home_win": odds[0].text,
                    "draw": odds[1].text,
                    "away_win": odds[2].text
                },
                "timestamp": datetime.utcnow().isoformat()
            })
        except:
            continue

    driver.quit()

    with open("odds.json", "w") as f:
        json.dump(matches, f)

if __name__ == "__main__":
    fetch_data()
