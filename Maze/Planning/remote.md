## Remote-Proxy Design

**TO: Matthias Felleisen** </br>
**FROM: Dylan Sapienza & Thomas Crook**</br>
**DATE: 10/31/2022**</br>
**SUBJECT:Remote-Proxy Design**</br>

For the start of our remote-proxy design we will have a TCP server that will handle the initial TCP connections of players. During this initial connection players will send over their name and color. Each time a player connects a referee will store their name and color. When a referee decides its time the TCP server will stop allowing new connections and the referee will start setting up the game.

First the referee will call proposeBoard on each player. The following JSON object represents how the information of this call will be sent to each player. {"function": "proposeBoard0", "row": Natural, "column": Natural}. We expect a JSON Board Object to be sent back. This proposeBoard is also how the referee will verify that each player is ready. If a player fails to respond before the referee times them out they will be kicked. An invalid board also results in being kicked. 

Next the referee will initalize the game. This involves making game states, building the board and extra tile, and choosing home and goal tiles. When this is finished the referee will call setup and inform each player of the current state and their goal. The following JSON object represents how this will be formated, {"function": "setup", "state": State, "goal": Coordinate}. 

After the referee has informated each player of their setup it will begin the game. Each turn the referee will call take turn sending the player, {"function": "takeTurn", "state": State}, and expecting a Choice back. If the player takes too long or sends an invalid move they will be kicked. 

When the game is over the referee will call win and inform each player if they won or lost. {"function": "win", "win": Boolean}. They referee will then end the game and the TCP server will disconnect each player.