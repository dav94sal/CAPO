import requests


def get_rounds(match_id):
    url = f"http://localhost:5000/api/rounds/{match_id}"

    response = requests.get(url)

    if response.status_code < 400:
        # print("Match created successfully.")
        return response.json()
    else:
        print(f"Error: {response.status_code}")

    return response


def new_round(round):
    url = "http://localhost:5000/api/rounds/new"

    response = requests.post(url, json=round)

    if response.status_code < 400:
        # print("Match created successfully.")
        return response.json()
    else:
        print(f"Error: {response.status_code}")

    return response
