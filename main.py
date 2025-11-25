import pandas as pd
import requests as rq

url = "https://www.codewars.com/api/v1/users/"
group = 'python_2'
results = f"groups/{group}.csv"

all_data = []

try:
    users = pd.read_csv(results)['username'].tolist()   

    for user in users:
        response = rq.get(f'{url}{user}')
        if response.status_code == 200:
            data = response.json()
            all_data.append({
                "username": data.get("username"),
                # "fullname": data.get("name", "No name"),
                # "honor": data.get("honor", 0),
                # "rank_name": data.get("ranks", {}).get("overall", {}).get("name", "Unknown"),
                "totalCompleted": data.get("codeChallenges", {}).get("totalCompleted", 0)
            })

except Exception as xatolik:
    print('xatolik:', xatolik)

if all_data:
    df = pd.DataFrame(all_data)
    df.sort_values(by="totalCompleted",ascending=False,inplace=True)
    df.to_csv(f'{group}_all.csv', index=False)
    print(df)
