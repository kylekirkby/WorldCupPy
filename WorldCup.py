import urllib.request, json

class WorldCup:

	""" This is a python3 class which interfaces with kimono world cup 2014 api. Can generate stats and predict games"""

	def __init__(self):
		
		self.upcoming_games = []
		self.api_key = "m9LfDNzM0ONCcbXFmRtSNGghMsRq9OvQ"

	def getMatchStats(self, match_id):

		response = urllib.request.urlopen("http://worldcup.kimonolabs.com/api/matches?sort=status&fields=homeScore,awayScore,currentGameMinute,startTime,status,venue,group,awayTeamId,homeTeamId,id,type&apikey={0}".format(self.api_key))

		content = response.read()

		data = json.loads(content.decode('utf8'))

		match_stats = []

		for each in data:
			each = dict(each)
			if each['id'] == match_id:
				match_stats.append(each)

		return match_stats


	def getMatchTeamStats(self,match_id):
		
		response = urllib.request.urlopen("http://worldcup.kimonolabs.com/api/matches?sort=status&fields=homeScore,awayScore,currentGameMinute,startTime,status,venue,group,awayTeamId,homeTeamId,id,type&apikey={0}".format(self.api_key))

		content = response.read()

		data = json.loads(content.decode('utf8'))

		match_stats = []

		for each in data:
			each = dict(each)
			if each['id'] == match_id:
				homeTeamId = each['homeTeamId']
				awayTeamId = each['awayTeamId']

		match_stats.append(self.getTeam(homeTeamId))
		match_stats.append(self.getTeam(awayTeamId))

		return match_stats
		
	def getUpcomingGames(self):

		response = urllib.request.urlopen("http://worldcup.kimonolabs.com/api/matches?sort=status&fields=homeScore,awayScore,currentGameMinute,startTime,status,venue,group,awayTeamId,homeTeamId,id,type&apikey={0}".format(self.api_key))

		content = response.read()

		data = json.loads(content.decode('utf8'))

		game_list = []

		for each in data:
			each = dict(each)
			if each['status'] == 'Pre-game':
				game_list.append(each)


		return game_list
			
	def getCurrentGames(self):

		response = urllib.request.urlopen("http://worldcup.kimonolabs.com/api/matches?sort=status&fields=homeScore,awayScore,currentGameMinute,startTime,status,venue,group,awayTeamId,homeTeamId,id,type&apikey={0}".format(self.api_key))

		content = response.read()

		data = json.loads(content.decode('utf8'))

		game_list = []

		for each in data:
			each = dict(each)
			if each['status'] == 'In-progress':
				game_list.append(each)

		return game_list



	def getPreviousGames(self):

		response = urllib.request.urlopen("http://worldcup.kimonolabs.com/api/matches?sort=status&fields=homeScore,awayScore,currentGameMinute,startTime,status,venue,group,awayTeamId,homeTeamId,id,type&apikey={0}".format(self.api_key))

		content = response.read()

		data = json.loads(content.decode('utf8'))

		game_list = []

		for each in data:
			each = dict(each)
			if each['status'] == 'Final':
				game_list.append(each)


		return game_list
			


	def getTeam(self, teamId):

		response = urllib.request.urlopen("http://worldcup.kimonolabs.com/api/teams/{0}?apikey={1}".format(teamId,self.api_key))

		content = response.read()

		data = json.loads(content.decode('utf8'))

		return data



if __name__ == "__main__":


	wc = WorldCup()

	games = wc.getGames()
	
	print(games)
	

		
		
