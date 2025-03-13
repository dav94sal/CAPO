import requests


def get_tourny_num():
    url = "http://localhost:5000/api/matches/last_tournament"

    response = requests.get(url)

    if response.status_code < 400:
        return response.json()["tournament_num"] + 1
    else:
        return None


def new_match(match):
    url = "http://localhost:5000/api/matches/new"

    response = requests.post(url, json=match)

    if response.status_code < 400:
        # print("Match created successfully.")
        pass
    else:
        print(f"Error: {response.status_code}")

    return response
