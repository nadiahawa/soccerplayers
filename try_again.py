import requests as r
import os

teams_api = r.get('https://foxes90-prempundit.herokuapp.com/players')
if teams_api.status_code == 200:
    teams_data = teams_api.json()
else:
    print('API call unsuccessful, try again!')

print(type(teams_api))

def play_creation(self):
    for i in range(len(self.teams_data)):
        player_fname = self.teams_data['Players'][i]['first_name']
        player_injury = self.teams_data['Players'][i]['injured']
        player_lname = self.teams_data['Players'][i]['last_name']
        player_position = self.teams_data['Players'][i]['position']
        playerstatus = self.teams_data['Players'][i]['suspended']
        player_team = self.teams_data['Players'][i]['team']

# how do i create a class then make these all attributes to be pulled out 


class Player():
    def __init__(self, fname, injured, lname, position, suspended, team):
         self.fname = fname
         self.injured = injured
         self.lname = lname
         self.position = position
         self.suspended = suspended
         self.team = team
    
    
    def add_to_team(self):
        if player_team == 
        player_team = teams_data['Players'][0]['team']
        print(player_team)

class Main:
    def team_make(self):
        self.team = {}
        x  = set()


# def status_check(playerstatus):
#     count = 0
#     if playerstatus == False:
#         count += 1
#         print(count)
#     else:
#         print('player is suspended, cant play!')   

# status_check(teams_data['Players'][27]['suspended'])


class Player():
    def __init__(self, first_name, injured, position, suspended, team):
        self.first_name = first_name
        self.injured = injured
        self.position = position
        self.suspended = suspended
        self.team = team

class Teams():
    def __init__(self):
        self.team_dict = {}

    def pre_add(self):

