import sys
import requests
from player import Player
from constants import API_URLS

FPL_URL = "https://fantasy.premierleague.com/api/"
PLAYERS_INFO_SUBURL = "elements/"


def get_base_json(url, item_id=None, append=None, auth=False):
    """
    Gets the data from the Fantasy Premier League API
    target: string to follow base url
    item_id: id for player, team etc.
    Authentication required for certain endpoints.
    """
    if item_id:
        url += '{}'.format(item_id)
    if append:
        url += '/{}'.format(append)
    response = requests.get(url)
    try:
        return response.json()
    except Exception:
        sys.exit("Game is being updated")


def get_players():
    players = []
    for item in get_url(API_URLS["players"]):
        players.append(Player(item))
    return players

players = get_players()
