from bs4 import BeautifulSoup
from Team import Team
import requests
from datetime import date


def is_current_date(comp_date):
    # todays_date = datetime.today().strftime('%Y-%m-%d')
    # todays_date = str(date.today())
    #test date
    todays_date = '2019-09-01'
    date_only = comp_date.split('T')[0]
    if todays_date == date_only:
        return True
    else:
        return False

def is_sooners(game_name):
    if "Oklahoma Sooners" in game_name:
        return True
    else:
        return False

def find_game_id():
    site_url = 'http://site.api.espn.com/apis/site/v2/sports/football/college-football/scoreboard?groups=80&limit=900'
    ou_game_id = 0
    # test_game = '401019470'
    response = requests.get(site_url, timeout=5)
    content = response.json()
    games = content['events']
    for game in games:
        if is_current_date(game['date']) and is_sooners(game['name']):
            ou_game_id = game['id']
    return ou_game_id

def query_game_details(game_id):
    ou_site = "http://site.api.espn.com/apis/site/v2/sports/football/college-football/summary?event=" + game_id
    response = requests.get(ou_site, timeout=5)
    game_data = response.json()
    teams = game_data['header']['competitions'][0]['competitors']
    team1 = Team(teams[0])
    team2 = Team(teams[1])
    return team1, team2

def output_data(details):
    t1 = details[0]
    t2 = details[1]
    print(t1.abbreviation, ":", t1.score)
    print(t2.abbreviation, ":", t2.score)


if __name__ == '__main__':
    game_id = find_game_id()
    if game_id == 0:
        print("No OU game found!")
    else:
        details = query_game_details(game_id)
        output_data(details)
