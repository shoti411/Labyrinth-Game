## Self-Evaluation Form for Milestone 3

Indicate below each bullet which file/unit takes care of each task:

1. rotate the spare tile by some number of degrees
https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/b747e6faa39a793d792b3b73fc957da001391113/Maze/Common/state.py#L55-L62
https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/b747e6faa39a793d792b3b73fc957da001391113/Maze/Common/tile.py#L48-L61

2. shift a row/column and insert the spare tile
   - plus its unit tests
   - In State
   - https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/b747e6faa39a793d792b3b73fc957da001391113/Maze/Common/state.py#L97-L128
   - In Board
   - https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/b747e6faa39a793d792b3b73fc957da001391113/Maze/Common/board.py#L64-L158
   - Tests
   - https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/b747e6faa39a793d792b3b73fc957da001391113/Maze/Common/Tests/test_board.py#L34-L172
   - https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/b747e6faa39a793d792b3b73fc957da001391113/Maze/Common/Tests/test_state.py#L71-L116
   
3. move the avatar of the currently active player to a designated spot
   - After re-reading the spec we realized we have misread that requirement. We just checked that the current players location was at a goal state. But did not make anything to make them move. We will add player movement during 4. 

4. check whether the active player's move has returned its avatar home
   - Spec milestone 3 does not include checking if a player has returned home and thus we did not check for this.

5. kick out the currently active player
   - https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/b747e6faa39a793d792b3b73fc957da001391113/Maze/Common/state.py#L88-L95

The ideal feedback for each of these points is a GitHub
perma-link to the range of lines in a specific file or a collection of
files.

A lesser alternative is to specify paths to files and, if files are
longer than a laptop screen, positions within files are appropriate
responses.

You may wish to add a sentence that explains how you think the
specified code snippets answer the request.

If you did *not* realize these pieces of functionality, say so.

