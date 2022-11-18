**If you use GitHub permalinks, make sure your link points to the most recent commit before the milestone deadline.**

## Self-Evaluation Form for Milestone 8

Indicate below each bullet which file/unit takes care of each task.

For `Maze/Remote/player`,

- explain how it implements the exact same interface as `Maze/Player/player`

In our code base, there is an "interface" (it's python, so it's not really an interface) called PlayerAPI. The default player is a LocalPlayerAPI,
and for this milestone all we had to do was implement our remote player as a RemotePlayerAPI.

https://github.khoury.northeastern.edu/CS4500-F22/sly-mice/blob/3e3056401111cdcac1efef7565fa2dd3c84e86d3/Maze/Players/player.py#L15-L27

- explain how it receives the TCP connection that enables it to communicate with a client

The server takes all of the TCP sockets that get connected, delegate them to a RemotePlayerAPI, which will then send any functions through the socket.

https://github.khoury.northeastern.edu/CS4500-F22/sly-mice/blob/3e3056401111cdcac1efef7565fa2dd3c84e86d3/Maze/Server/server.py#L46-L58

- point to unit tests that check whether it writes JSON to a mock output device

We were unable to create enough unit tests during this milestone due to time constraints.

For `Maze/Remote/referee`,

- explain how it implements the same interface as `Maze/Referee/referee`

Our remote referee doesn't implement the same interface as a normal referee. Our remote referee simply parses incoming messages from the player proxy, and translates it in order to tell the local player what function should be run (with the parsed arguments).

- explain how it receives the TCP connection that enables it to communicate with a server

The client connects the sockets to a server, then creates a LocalPlayerAPI and a RefereeProxy. The RefereeProxy stores one player and the socket connection. All of our connections then get their own thread, and are told to start listening indefinitely for messages. 

https://github.khoury.northeastern.edu/CS4500-F22/sly-mice/blob/3e3056401111cdcac1efef7565fa2dd3c84e86d3/Maze/Client/client.py#L19-L32

- point to unit tests that check whether it reads JSON from a mock input device

We were unable to create enough unit tests during this milestone due to time constraints.

For `Maze/Client/client`, explain what happens when the client is started _before_ the server is up and running:

- does it wait until the server is up (best solution)

No, our client doesn't wait until the server is up.

- does it shut down gracefully (acceptable now, but switch to the first option for 9)

If the game is finished, the RefereeProxy sets 'is_running' to False - this allows the client to know that this player has either been kicked, errored, or the server shut down. Once all players are done running, the client stops. 

https://github.khoury.northeastern.edu/CS4500-F22/sly-mice/blob/3e3056401111cdcac1efef7565fa2dd3c84e86d3/Maze/Client/client.py#L34-L37

https://github.khoury.northeastern.edu/CS4500-F22/sly-mice/blob/3e3056401111cdcac1efef7565fa2dd3c84e86d3/Maze/Remote/referee.py#L25-L43

There is a case that we have figured out a solution for, but is not included in our commit due to time restraints. If the player is kicked from the game, it will often throw a "RecursionError" as it keeps listening for messages. A simple try-catch and exit() of the thread solved this problem, but it is not included in our current commit.


For `Maze/Server/server`, explain how the code implements the two waiting periods:

- is it baked in? (unacceptable after Milestone 7)
- parameterized by a constant (correct).

Our waiting periods are parameterized by a constant within the server class.

https://github.khoury.northeastern.edu/CS4500-F22/sly-mice/blob/3e3056401111cdcac1efef7565fa2dd3c84e86d3/Maze/Server/server.py#L15-L26

The ideal feedback for each of these three points is a GitHub
perma-link to the range of lines in a specific file or a collection of
files.

A lesser alternative is to specify paths to files and, if files are
longer than a laptop screen, positions within files are appropriate
responses.

You may wish to add a sentence that explains how you think the
specified code snippets answer the request.

If you did *not* realize these pieces of functionality, say so.

