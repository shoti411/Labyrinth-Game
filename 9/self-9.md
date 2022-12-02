**If you use GitHub permalinks, make sure your link points to the most recent commit before the milestone deadline.**

## Self-Evaluation Form for Milestone 9

Indicate below each bullet which file/unit takes care of each task.

Getting the new scoring function right is a nicely isolated design
task, ideally suited for an inspection that tells us whether you
(re)learned the basic lessons from Fundamentals I, II, and III. 

This piece of functionality must perform the following four tasks:

- find the player(s) that has(have) visited the highest number of goals
- compute their distances to the home tile
- pick those with the shortest distance as winners
- subtract the winners from the still-active players to determine the losers

The scoring function per se should compose these functions,
with the exception of the last, which can be accomplised with built-ins. 

1. Point to the scoring method plus the three key auxiliaries in your code. 
This whole function comprises of the methods to compute the winners.
https://github.khoury.northeastern.edu/CS4500-F22/egoless-bears/blob/2304576b3e453e7ea7b5d27cb23cbd2bea5e8acf/Maze/Common/state.py#L221-L240
The function to compute their distances to their goal tile is listed here:
https://github.khoury.northeastern.edu/CS4500-F22/egoless-bears/blob/2304576b3e453e7ea7b5d27cb23cbd2bea5e8acf/Maze/Common/state.py#L242-L254

3. Point to the unit tests of these four functions.

We did not have enough time to create unit tests for these 4 functions.

The ideal feedback for each of these three points is a GitHub
perma-link to the range of lines in a specific file or a collection of
files.

A lesser alternative is to specify paths to files and, if files are
longer than a laptop screen, positions within files are appropriate
responses.

You may wish to add a sentence that explains how you think the
specified code snippets answer the request.

If you did *not* realize these pieces of functionality, say so.

