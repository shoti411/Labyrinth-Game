## Player Protocol Design Plan

**TO: Matthias Felleisen**
**FROM: Dylan Sapienza & Thomas Crook**
**DATE: 10/17/2022**
**SUBJECT: Player-Protocol Design Plan**

Our implementation of the Maze.com Labyrinth game will include four unique steps for the players: Join, Pass, Slide_and_Insert,
and Move. 

The 'Join' step of our protocol is responsible for establishing a player-referee connection, such that a referee can account for 
all the players in the game and decide a turn order. The referee collects the player data, including the selected avatar. 

Next, the referee sends the active player the current game state and information about their goal, home, and position. With this information,
the player is expected to return one of two function calls: either a pass, or a slide_and_insert. If the referee receives a pass,
then this steps repeats with the next player. If the referee receives a slide_and_insert, the referee will check if it's valid
and make the move if so. The player is expected to return the column or row data as well as the rotation desired for the 
spare tile. If it's invalid, we will notify the player why their move is invalid and give them the chance to change their move.

Following a slide_and_insert, a player is sent the updated board. This starts the 'Move' step, in which they are expected
to return a reachable position that they want to move to. If the position is invalid for any reason, the referee will send
another move request, with details as to why they couldn't perform their last move.
 


