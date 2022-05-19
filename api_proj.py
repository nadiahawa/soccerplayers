import requests as r
import os

teams_api = r.get('https://foxes90-prempundit.herokuapp.com/players')
if teams_api.status_code == 200:
    teams_data = teams_api.json()
else:
    print('API call unsuccessful, try again!')



class Player():
    def __init__(self, first_name, injured, position, suspended, team):
        self.first_name = first_name
        self.injured = injured
        self.position = position
        self.suspended = suspended
        self.team = team

class Team():
    def __init__(self):
        self.team_dict = {}
        self.positions_dict = {}



    def add_to_team(self, player_data):
        player_data = r.get('https://foxes90-prempundit.herokuapp.com/players')
        player_data = player_data.json()
        # player_info = Player(player_data['first_name'], player_data['injured'], player_data['position'], player_data['suspended'], player_data['team'])
        self.team_dict[player_info.first_name] = player_info
        print(player_info)



    def positions(self, player_data, player_info):
        player_data = player_data.json()
        player_info = Player(player_data['first_name'], player_data['injured'], player_data['position'], player_data['suspended'], player_data['team'])
        self.player_dict[player_data] = player_info


newplay = Team()

newplay.positions()
