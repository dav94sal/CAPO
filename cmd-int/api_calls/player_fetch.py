import requests


def get_all_players():
    url = "http://localhost:5000/api/players/all"

    response = requests.get(url)
    # print(response)

    if response.status_code < 400:
        return response.json()
    else:
        print(f"Error: {response.status_code}")


def add_player(player):
    url = "http://localhost:5000/api/players/new"

    # print("Frontend player: ", player)
    response = requests.post(url, json=player)
    # print("Frontend response: ", response)

    if response.status_code < 400:
        print("Player created successfully.")
    else:
        print(f"Error: {response.status_code}")

    return response.json()
