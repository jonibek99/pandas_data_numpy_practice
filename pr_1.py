import pandas as pd
import requests as rq

users = ['jonibek_99',  'shamsiyev', 'zopirov','HUSANBOI001','Sanjar1218','Jaloliddin_n1']
all_data = []
for user in users:
    url = f"https://www.codewars.com/api/v1/users/{user}"
    response = rq.get(url)
    try:
        if response.status_code == 200:
            data = response.json()
            if "username" in data:
                all_data.append({
                    "username": data.get("username"),
                     "fullname": data.get("name", "No name"),
                     "honor": data.get("honor", 0),
                    "rank_name": data.get("ranks", {}).get("overall", {}).get("name", "Unknown"),
                    "totalCompleted": data.get("codeChallenges", {}).get("totalCompleted")})
        else:
            print(f"⚠️ {user} topilmadi yoki API xato: {data}")
    except Exception as user:
        print(f"❌ {user} uchun API xato: {response.status_code}")

if all_data:
    df = pd.DataFrame(all_data)
    a=df.sort_values(by="totalCompleted",ascending=True)
    #df=df.iloc[::-1]
    a.to_csv("codewars_users.csv", index=False)
    print(a)
else:
    print("Hech bir foydalanuvchi topilmadi!")

