**If you use GitHub permalinks, make sure your link points to the most recent commit before the milestone deadline.**

## Self-Evaluation Form for Milestone 7

Indicate below each bullet which file/unit takes care of each task:

The require revision calls for

    - the relaxation of the constraints on the board size
    - a suitability check for the board size vs player number 

1. Which unit tests validate the implementation of the relaxation?

https://github.khoury.northeastern.edu/CS4500-F22/sly-mice/blob/d64ecca1f6cbc3b3bfd81cfc0e4553494a867347/Maze/Common/Tests/test_board.py#L6-L9
    * This test shows that our constructor doesn't fail with a 2x2 board being initialized. Our board class was originally built without a 7x7 restriction.

2. Which unit tests validate the suitability of the board/player combination? 

https://github.khoury.northeastern.edu/CS4500-F22/sly-mice/blob/d64ecca1f6cbc3b3bfd81cfc0e4553494a867347/Maze/Common/Tests/test_state.py#L9-L154
   
   * Apologies for the long permalink. This is our 'test_state' class, that performs a bunch of player-board maneuvers on a 3x3 board.
   * If this question is asking whether or not we check that a board can fit the number of players given (aka a 2x2 board can at maximum hold 1 player with unique non-moveable home tiles), we don't have that implemented yet.

The ideal feedback for each of these three points is a GitHub
perma-link to the range of lines in a specific file or a collection of
files.

A lesser alternative is to specify paths to files and, if files are
longer than a laptop screen, positions within files are appropriate
responses.

You may wish to add a sentence that explains how you think the
specified code snippets answer the request.

If you did *not* realize these pieces of functionality, say so.

