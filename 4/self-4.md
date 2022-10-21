**If you use GitHub permalinks, make sure your links points to the most recent commit before the milestone deadline.**

## Self-Evaluation Form for Milestone 4

The milestone asks for a function that performs six identifiable
separate tasks. We are looking for four of them and will overlook that
some of you may have written deep loop nests (which are in all
likelihood difficult to understand for anyone who is to maintain this
code.)

Indicate below each bullet which file/unit takes care of each task:

1. the "top-level" function/method, which composes tasks 2 and 3 

https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/fac5a435dbe41ca16397a40b650e3be101850acc/Maze/Common/strategy.py#L83-L114

2. a method that `generates` the sequence of spots the player may wish to move to

https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/fac5a435dbe41ca16397a40b650e3be101850acc/Maze/Common/strategy.py#L55-L66

https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/fac5a435dbe41ca16397a40b650e3be101850acc/Maze/Common/riemann.py#L12-L38

https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/fac5a435dbe41ca16397a40b650e3be101850acc/Maze/Common/euclid.py#L14-L43

3. a method that `searches` rows,  columns, etcetc. 

https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/3cbefd8ea2406443f5fcc8bae474cc0775b71bd8/Maze/Common/strategy.py#L116-L174

4. a method that ensure that the location of the avatar _after_ the
   insertion and rotation is a good one and makes the target reachable
   
   https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/3cbefd8ea2406443f5fcc8bae474cc0775b71bd8/Maze/Common/strategy.py#L77-L80
   
*   The 'move' is performed after the slide_and_insert, and verifies in line 80 by calling 'check_move' whether that move can occur.

ALSO point to

- the data def. for what the strategy returns

https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/3cbefd8ea2406443f5fcc8bae474cc0775b71bd8/Maze/Common/strategy.py#L18-L24

https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/3cbefd8ea2406443f5fcc8bae474cc0775b71bd8/Maze/Common/strategy.py#L40-L42

- unit tests for the strategy

FOR EUCLID:
https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/3cbefd8ea2406443f5fcc8bae474cc0775b71bd8/Maze/Common/Tests/test_euclid.py#L16-L107

FOR RIEMANN:
https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/3cbefd8ea2406443f5fcc8bae474cc0775b71bd8/Maze/Common/Tests/test_riemann.py#L16-L107


The ideal feedback for each of these points is a GitHub
perma-link to the range of lines in a specific file or a collection of
files.

A lesser alternative is to specify paths to files and, if files are
longer than a laptop screen, positions within files are appropriate
responses.

You may wish to add a sentence that explains how you think the
specified code snippets answer the request.

If you did *not* realize these pieces of functionality or realized
them differently, say so and explain yourself.


