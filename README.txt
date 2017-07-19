This program is a new and improved version of pong-
	Developed using python and pygame

	==== features ======
	- single player mode where you play against AI
	- multiplayer where you can play people on the same computer
		w,s controls left paddle and up, down controls right paddle
	- p pauses the game
	- contains graphical user iterface with event driven key bindings and button style control
	- contains sound effects and music
	- video game style GUI

	===== walk through ===
	- start at main menu and make a selection between singleplayer or multiplayer
	- if single player is selected player will play against AI and first one to seven wins
		- ball starts out at slow pace and speeds up every time it makes contact with paddles
		- depending on where ball hits paddle the trajectory will change
		- there are 5 different places on paddle that will effect trajectory of the ball
		- Player controls up and down direction with w and s keys
	- if multiplayer is selected player will play against another player on the same keyboard, first to seven wins
		- ball starts out at slow pace and speeds up every time it makes contact with paddles
		- depending on where ball hits paddle the trajectory will change
		- there are 5 different places on paddle that will effect trajectory of the ball
		- Player1 controls up and down direction with w and s keys
		- Player2 controls up and down direction with up and down arrow keys
	- After singleplayer or multiplayer game has ended the program goes to end of game screen
		-This screen proclaims the winner and lets you choose from two options
		- selecting main menu will take you to the main menu and start game loop over
		- selecting quit will close the program and window.


