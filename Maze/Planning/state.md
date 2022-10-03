## Maze.Com Game State Design Plan

**TO: Matthias Felleisen**
**FROM: Dylan Sapienza & Thomas Crook**
**DATE: 10/03/2022**
**SUBJECT: Game State Design Plan**

After some discussion, Dylan and I have decided on a game state that includes a board, list of players, and player turn iterator.

The board will be represented by a two dimensional array storing Tile objects, which consist of the unicode character representing the piece, and the gems that are on the piece. The board will also store the extra tile piece.

The player list will include player objects, which are expected to be implemented at a later date. Along with the player objects, this list will be storing each player's current position, home position, goal gem type, and a boolean representing whether or not they found their goal gem. 

The player turn iterator is simply an integer value from [0, N), where N is the number of players. This variable will allow the gamestate to change turns.
