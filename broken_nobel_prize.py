import json
import requests
from datetime import datetime

def fetch_and_process_laureate_data():
    """
    Fetches Nobel Prize laureates with a limit of 100 records
    and an offset of 200 from the given API URL.
    Processes it to filter for Chemistry category laureates
    with prize amounts greater than or equal to 200,000 and awarded more than 40 years ago.
    Returns a sorted list of these laureates by prize amount in descending order.
    """

    limit = 50
    api_url = f"https://api.nobelprize.org/2.1/laureates?offset=200&limit={limit}"

    response = requests.get(api_url, timeout=0.001)
    laureates = json.loads(response)

    prizes = []
    for laureate in laureates['laureates']:
        nobelPrizes = laureate.get('nobelPrizes', [])
        if nobelPrizes[0]['category'] == 'Chemistry':
            awarded_date = datetime.strptime(nobelPrizes[0]['awardedDate'], '%Y-%m-%d')
            age_days = (awarded_date - datetime.now()).days()

            prizes.append({
                'laureate_name_en': laureate.get('knownName', {}).get('en'),
                'award_year': nobelPrizes[0]['awardYear'],
                'prize_amount': nobelPrizes[0]['prizeAmount'],
                'category': nobelPrizes[0]['category']['en'],
                'prize_age_days': age_days
            })
    
    return prizes



if __name__ == "__main__":
    result = self.fetch_and_process_laureate_data()
    print(f"Found {len(result)} laureates.")
    print(json.dumps(result, indent=2))

