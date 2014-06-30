import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *


from WorldCup import *

class MainWindow(QMainWindow):

	""" This is the class for the main window of the world cup python statistics api"""

	def __init__(self):

		super().__init__()

		self.resize(400,400)

		self.setWindowTitle("PyCup Statistics")

		#attributes

		# instantiate the world cup class
		self.wc = WorldCup()

		
	
		#create the stacked layout

		self.stacked_layout = QStackedLayout()
		
		#call to layouts
		self.create_initial_layout()
		self.upcoming_games_layout()
		self.current_games_layout()
		self.previous_games_layout()


	
		
		self.widget = QWidget()

		self.widget.setLayout(self.stacked_layout)

        #set the central widget

		self.setCentralWidget(self.widget)		

	
	#switch back to the initial layout home page

	def back_button_switch(self):
		
		self.stacked_layout.setCurrentIndex(0)
	

	
	def current_games_switch(self):

		self.stacked_layout.setCurrentIndex(2)
	
	def upcoming_games_switch(self):
		
		self.stacked_layout.setCurrentIndex(1)

	def previous_games_switch(self):
		
		self.stacked_layout.setCurrentIndex(3)

	def match_stats_layout(self, match_id):


		#vertical layout
	
		stats = self.wc.getMatchStats(match_id)
		
		team1 = self.wc.getTeam(stats['homeTeamId'])
		team2 = self.wc.getTeam(stats['awayTeamId'])

		match_title = team1['name'] + 'VS' + team2['name']
		self.gameTitle = QLabel(match_title)
		self.mainVerticalLayout = QVBoxLayout()
		
		#titleWidget
		#get the current games	

		self.matchStatsData = self.wc.getMatchStats(match_id)
		self.mainVerticalLayout.addWidget(self.gameTitle)

		self.matchStatsWidget = QWidget()
		self.matchStatsWidget.setLayout(self.mainVerticalLayout)
		
		#add the widget to the stacked layout

		#has the stack index of ============ 1

		self.stacked_layout.addWidget(self.matchStatsWidget)


		#button connections
		
		self.backPushButton.clicked.connect(self.back_button_switch)
		
		


	def create_initial_layout(self):
		#vertical layout

		self.initialVerticalLayout = QVBoxLayout()
		

		#buttons 
		self.upcomingGamesPushButton = QPushButton("Upcoming Games")
		self.currentGamesPushButton = QPushButton("Current Games")
		self.previousGamesPushButton = QPushButton("Previous Games")


		self.initialVerticalLayout.addWidget(self.previousGamesPushButton)
		self.initialVerticalLayout.addWidget(self.currentGamesPushButton)
		self.initialVerticalLayout.addWidget(self.upcomingGamesPushButton)
		
		#new widget
		self.initialWidget = QWidget()
		self.initialWidget.setLayout(self.initialVerticalLayout)

		self.setCentralWidget(self.initialWidget)
		
		#add the widget to the stacked layout

		#has the stack index of ========= 0

		self.stacked_layout.addWidget(self.initialWidget)


		#button connections for initiallayout 
		
		self.upcomingGamesPushButton.clicked.connect(self.upcoming_games_switch)
		self.currentGamesPushButton.clicked.connect(self.current_games_switch)
		self.previousGamesPushButton.clicked.connect(self.previous_games_switch)
	def previous_games_layout(self):


		#vertical layout
	

		self.mainVerticalLayout = QVBoxLayout()
		
		#titleWidget

		self.titleLayout = QHBoxLayout()
		self.titleLabel = QLabel("Previous Games")
		self.backPushButton = QPushButton("Back")
		spacer = QSpacerItem(60,40,QSizePolicy.Minimum,QSizePolicy.Expanding)
		
		self.titleLabel.setStyleSheet("font-size: 18pt; font-family: Courier;")
		#self.titleLabel.setStyleSheet("text-align: center;")
		
		self.titleLayout.addWidget(self.backPushButton)
		self.titleLayout.addItem(spacer)
		self.titleLayout.addWidget(self.titleLabel)
		
		self.titleWidget = QWidget()
		self.titleWidget.setLayout(self.titleLayout)

		self.mainVerticalLayout.addWidget(self.titleWidget)
		
		#get the current games	

		self.previousGames = self.wc.getPreviousGames()

		for game in self.previousGames[-5:-1]:
			
			#create horizontal layout for each game

			self.hLayout = QHBoxLayout()

			#QWidgets components


			self.homeTeam = self.wc.getTeam(game["homeTeamId"])
			self.awayTeam = self.wc.getTeam(game["awayTeamId"])


			#labels and buttons
			
			self.homeTeamLabel = QLabel(self.homeTeam["name"])
			self.homeTeamLabel.setStyleSheet("qproperty-alignment: AlignCenter;")
			self.awayTeamLabel = QLabel(self.awayTeam["name"])
			self.awayTeamLabel.setStyleSheet("qproperty-alignment: AlignCenter;")
			self.vsLabel = QLabel("VS")
			self.vsLabel.setStyleSheet("qproperty-alignment: AlignCenter;")
			self.viewGameButton = QPushButton("Stats")
			spacer = QSpacerItem(60,40,QSizePolicy.Minimum,QSizePolicy.Expanding)


			#add QLabels to the horizontal layout
			
			self.hLayout.addWidget(self.homeTeamLabel)
			self.hLayout.addWidget(self.vsLabel)
			self.hLayout.addWidget(self.awayTeamLabel)
			self.hLayout.addItem(spacer)
			self.hLayout.addWidget(self.viewGameButton)
			
			

			#new QWidget

			self.matchWidget = QWidget()
			self.matchWidget.setLayout(self.hLayout)


			
			self.mainVerticalLayout.addWidget(self.matchWidget)
		

		#main Widget

		self.previousGamesWidget = QWidget()
		self.previousGamesWidget.setLayout(self.mainVerticalLayout)
		
		#add the widget to the stacked layout

		#has the stack index of ============ 1

		self.stacked_layout.addWidget(self.previousGamesWidget)


		#button connections
		
		self.backPushButton.clicked.connect(self.back_button_switch)

	def current_games_layout(self):


		#vertical layout
	

		self.mainVerticalLayout = QVBoxLayout()
		
		#titleWidget

		self.titleLayout = QHBoxLayout()
		self.titleLabel = QLabel("Current Games")
		self.backPushButton = QPushButton("Back")
		spacer = QSpacerItem(60,40,QSizePolicy.Minimum,QSizePolicy.Expanding)
		
		self.titleLabel.setStyleSheet("font-size: 18pt; font-family: Courier;")
		#self.titleLabel.setStyleSheet("text-align: center;")
		
		self.titleLayout.addWidget(self.backPushButton)
		self.titleLayout.addItem(spacer)
		self.titleLayout.addWidget(self.titleLabel)
		
		self.titleWidget = QWidget()
		self.titleWidget.setLayout(self.titleLayout)

		self.mainVerticalLayout.addWidget(self.titleWidget)
		
		#get the current games	

		self.currentGames = self.wc.getCurrentGames()

		for game in self.currentGames:
			
			#create horizontal layout for each game

			self.hLayout = QHBoxLayout()

			#QWidgets components


			self.homeTeam = self.wc.getTeam(game["homeTeamId"])
			self.awayTeam = self.wc.getTeam(game["awayTeamId"])


			#labels and buttons
			
			self.homeTeamLabel = QLabel(self.homeTeam["name"])
			self.homeTeamLabel.setStyleSheet("qproperty-alignment: AlignCenter;")
			self.awayTeamLabel = QLabel(self.awayTeam["name"])
			self.awayTeamLabel.setStyleSheet("qproperty-alignment: AlignCenter;")
			self.vsLabel = QLabel("VS")
			self.vsLabel.setStyleSheet("qproperty-alignment: AlignCenter;")
			self.viewGameButton = QPushButton("Stats")
			spacer = QSpacerItem(60,40,QSizePolicy.Minimum,QSizePolicy.Expanding)


			#add QLabels to the horizontal layout
			
			self.hLayout.addWidget(self.homeTeamLabel)
			self.hLayout.addWidget(self.vsLabel)
			self.hLayout.addWidget(self.awayTeamLabel)
			self.hLayout.addItem(spacer)
			self.hLayout.addWidget(self.viewGameButton)
			
			

			#new QWidget

			self.matchWidget = QWidget()
			self.matchWidget.setLayout(self.hLayout)


			
			self.mainVerticalLayout.addWidget(self.matchWidget)
		

		#main Widget

		self.currentGamesWidget = QWidget()
		self.currentGamesWidget.setLayout(self.mainVerticalLayout)
		
		#add the widget to the stacked layout

		#has the stack index of ============ 2

		self.stacked_layout.addWidget(self.currentGamesWidget)


		#button connections
		
		self.backPushButton.clicked.connect(self.back_button_switch)
	
	def upcoming_games_layout(self):


		#vertical layout
	

		self.mainVerticalLayout = QVBoxLayout()
		
		#titleWidget

		self.titleLayout = QHBoxLayout()
		self.titleLabel = QLabel("Upcoming Games")
		self.backPushButton = QPushButton("Back")
		spacer = QSpacerItem(60,40,QSizePolicy.Minimum,QSizePolicy.Expanding)
		
		self.titleLabel.setStyleSheet("font-size: 18pt; font-family: Courier;")
		#self.titleLabel.setStyleSheet("text-align: center;")
		
		self.titleLayout.addWidget(self.backPushButton)
		self.titleLayout.addItem(spacer)
		self.titleLayout.addWidget(self.titleLabel)
		
		self.titleWidget = QWidget()
		self.titleWidget.setLayout(self.titleLayout)

		self.mainVerticalLayout.addWidget(self.titleWidget)
		
		#get the current games	

		self.upcomingGames = self.wc.getUpcomingGames()

		for game in self.upcomingGames:
			
			#create horizontal layout for each game

			self.hLayout = QHBoxLayout()

			#QWidgets components


			self.homeTeam = self.wc.getTeam(game["homeTeamId"])
			self.awayTeam = self.wc.getTeam(game["awayTeamId"])


			#labels and buttons
			
			self.homeTeamLabel = QLabel(self.homeTeam["name"])
			self.homeTeamLabel.setStyleSheet("qproperty-alignment: AlignCenter;")
			self.awayTeamLabel = QLabel(self.awayTeam["name"])
			self.awayTeamLabel.setStyleSheet("qproperty-alignment: AlignCenter;")
			self.vsLabel = QLabel("VS")
			self.vsLabel.setStyleSheet("qproperty-alignment: AlignCenter;")
			self.viewGameButton = QPushButton("Stats")
			spacer = QSpacerItem(60,40,QSizePolicy.Minimum,QSizePolicy.Expanding)


			#add QLabels to the horizontal layout
			
			self.hLayout.addWidget(self.homeTeamLabel)
			self.hLayout.addWidget(self.vsLabel)
			self.hLayout.addWidget(self.awayTeamLabel)
			self.hLayout.addItem(spacer)
			self.hLayout.addWidget(self.viewGameButton)
			
			

			#new QWidget

			self.matchWidget = QWidget()
			self.matchWidget.setLayout(self.hLayout)


			
			self.mainVerticalLayout.addWidget(self.matchWidget)
		

		#main Widget

		self.upcomingGamesWidget = QWidget()
		self.upcomingGamesWidget.setLayout(self.mainVerticalLayout)
		
		#add the widget to the stacked layout

		#has the stack index of ============ 1

		self.stacked_layout.addWidget(self.upcomingGamesWidget)


		#button connections
		
		self.backPushButton.clicked.connect(self.back_button_switch)

if __name__ == "__main__":

	app = QApplication(sys.argv)
	window = MainWindow()
	window.show()	
	window.raise_()
	app.exec_()
	
