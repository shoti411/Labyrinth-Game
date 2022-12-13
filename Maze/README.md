# Labyrinth

This project implements "Labyrinth", a maze game where players compete to reach their goal while navigating the maze.

## Directory Structure

* README.md: This file
* Common/
    * board.py: contains the data representations for the game board and the tiles in the game board
    * state.py: contains the data representations for the game state
    * player_state.py: contains the data representation for an active Player in a game
    * player_game_state.py: contains the data representation for the state of the game which a player would have access to
    * 
* Players/
    * strategy.py: contains the functionality for the strategies
    * riemann.py: The Riemann Strategy implementation
    * euclid.py: The Euclid Strategy implementation
    * player.py: contains a player API implementation
* Referee/
    * referee.py: contains the referee implementation
    * observer.py: contains the observer implementation
* Planning/: contains planning memos and general task items

The UML diagram below depicts the class structure of the code: \


The UML diagram below depicts the pacakge structure of the code: \


## Milestones
Milestone 1:
* Planning memos added

Milestone 2:
* tile.py, board.py, action.py, coordinate.py, directions.py, gems.py added

Milestone 3:
* state.py, player_state.py, player_game_state.py,  added which includes PlayerGameState and State classes
* to run the test harness, then `./xboard`

Milestone 4:
* strategy.py added
* xstate test harness added in 4; to run, type `./xstate`
* Player protocol design added in planning memo.

Milestone 5:
* referee.py and player.py
* xchoice test harness added in 5; to run, type `./xchoice`
* interactive player mechanism design added in Planning/

Milestone 6:
* observer.py added with a test to run and view it in Tests/test_inspect_observer
* xgames and xgames-with-observer test harness added in 6; run `make`, then `./xgames` or `./xgames-with-observer`
* remote design added in Planning/

Milestone 7:
* xbad.py test harness added in 7; to run, type `./xbad`
* Requirements for Changing the rules of the game added to Planning/ in changes.md
* General changes in the code and a priority list of things to change added to Planning/ in todo.md

Milestone 8:



