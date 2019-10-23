teams_long = {
    1: "Arsenal",
    2: "Bournemouth",
    3: "Brighton",
    4: "Burnley",
    5: "Cardiff",
    6: "Chelsea",
    7: "Crystal Palace",
    8: "Everton",
    9: "Fulham",
    10: "Huddersfield",
    11: "Leicester",
    12: "Liverpool",
    13: "Man City",
    14: "Man Utd",
    15: "Newcastle",
    16: "Southampton",
    17: "Spurs",
    18: "Watford",
    19: "West Ham",
    20: "Wolves"
}

teams_short = {
    1: "ARS",
    2: "BOU",
    3: "BHA",
    4: "BUR",
    5: "CAR",
    6: "CHE",
    7: "CPL",
    8: "EVE",
    9: "FUL",
    10: "HUD",
    11: "LEI",
    12: "LIV",
    13: "MCI",
    14: "MUN",
    15: "NEW",
    16: "SOU",
    17: "TOT",
    18: "WAT",
    19: "WHU",
    20: "WOL"
}

positions = {
    1: "GK",
    2: "Def",
    3: "Mid",
    4: "For"
}

arrows = {
    "up": {
        "unicode": u"\u25B2",
        "color": "green"
    },
    "down": {
        "unicode": u"\u25BC",
        "color": "red"
    },
    "same": {
        "unicode": u"\u2010",
        "color": "gray"
    },
    "new": {
        "unicode": u"\u2010",
        "color": "gray"
    }
}

chips = {
    "bboost": "Bench Boost",
    "3xc": "Triple Captain",
    "freehit": "Free Hit",
    "wildcard": "Wildcard"
}

API_BASE_URL = "https://fantasy.premierleague.com/api/"

API_URLS = {
    "dynamic": "{}bootstrap-dynamic/".format(API_BASE_URL),
    "fixtures": "{}fixtures/".format(API_BASE_URL),
    "gameweeks": "{}events/".format(API_BASE_URL),
    "gameweek_fixtures": "{}fixtures/?event={{}}".format(API_BASE_URL),
    "gameweek_live": "{}event/{{}}/live".format(API_BASE_URL),
    "league_classic": "{}leagues-classic/{{}}/standings/".format(API_BASE_URL),
    "league_h2h": "{}leagues-h2h/{{}}/standings/".format(API_BASE_URL),
    "league_h2h_fixtures": "{}leagues-h2h-matches/league/{{}}/?{{}}page={{}}".format(API_BASE_URL),
    "players": "{}elements/".format(API_BASE_URL),
    "player": "{}element-summary/{{}}/".format(API_BASE_URL),
    "settings": "{}game-settings/".format(API_BASE_URL),
    "static": "{}bootstrap-static/".format(API_BASE_URL),
    "teams": "{}teams/".format(API_BASE_URL),
    "transfers": "{}transfers/".format(API_BASE_URL),
    "user": "{}entry/{{}}/".format(API_BASE_URL),
    "user_cup": "{}entry/{{}}/cup/".format(API_BASE_URL),
    "user_history": "{}entry/{{}}/history/".format(API_BASE_URL),
    "user_picks": "{}entry/{{}}/event/{{}}/picks/".format(API_BASE_URL),
    "user_team": "{}my-team/{{}}/".format(API_BASE_URL),
    "user_transfers": "{}entry/{{}}/transfers/".format(API_BASE_URL),
    "user_latest_transfers": "{}entry/{{}}/transfers-latest/".format(
        API_BASE_URL),
    "watchlist": "{}watchlist/".format(API_BASE_URL),
    "me": "{}me/".format(API_BASE_URL)
}
