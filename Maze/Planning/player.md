## Maze.Com Player Design Plan

**TO: Matthias Felleisen**</br>
**FROM: Dylan Sapienza & Thomas Crook**</br>
**DATE: 10/11/2022**</br>
**SUBJECT: Player Design Plan**</br>

For our player data representation, we have decided that a player must know the following information about the game state: their goal tile, their home tile, their position (x, y) on the board, the board itself, the spare tile, and the other players' locations. 

The goal tile, home tile, player position, and opponent positions will be represented by (int, int) tuples, with some nuance between them. The goal tile and home tile both can be off of the board (as the spare tile), in this case they will be represented by (-1, -1). The opponent positions will be an array of (int, int) tuples, where length is number of players minus one. The player position is simply a standard (int, int) tuple.

The board object is a matrix of connectors; examples are under the specifications for milestone 3. 

The spare tile is represented by a connector string.

The player interface will include: recv_state(), interpret_state(), reachable_tiles(), evaluate_move(), and send_move().

The function recv_state() will receive any incoming data, ensure it's well-formed, then call interpret_state(). Interpret_state() will then convert the data into a readable object, then convert it to useful Player data.

The function reachable_tiles() will find which positions this player object can reach based on it's current position, with any possible tile rotations and shifts.

Evaluate_move() will determine which of the possible reachable_tiles() is the best decision the player can make on this turn. Turns will likely be scored on some metric (messing up other players, reaching our goal, etc.) and then the best move will be selected.

Send_move() will send the best move determined by evaluate_move() to the referee, as a well-formed json object.


