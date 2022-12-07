Pair: egoless-bears \
Commit: [2304576b3e453e7ea7b5d27cb23cbd2bea5e8acf](https://github.khoury.northeastern.edu/CS4500-F22/egoless-bears/tree/2304576b3e453e7ea7b5d27cb23cbd2bea5e8acf) \
Self-eval: https://github.khoury.northeastern.edu/CS4500-F22/egoless-bears/blob/19198efd76d0a56f1493ac9475de1e84571bfaa1/9/self-9.md \
Score: 64/100  \
Grader: Varsha Ramesh

## Program Inspection

- [20/20] for an accurate and helpful self evaluation. 

The top-level scoring function must perform the following tasks:

- find the player(s) that has(have) visited the highest number of goals
- compute their distances to the home tile
- pick those with the shortest distance as winners
- subtract the winners from the still-active players to determine the losers


The first three tasks should be separated out as methods/functions:
1. Find player(s) that has(have) visited the highest number of goals.
2. Compute player distances to next goal.
3. Find player(s) with shortest distance to next goal.

_Points_

- [20/40] Each of these functions should have a good name or a purpose statement.
  - [10/10] Top-level scoring method 
  - [0/10] Find players that have visited the highest number of goals - Did not separate it out to a different function.
  - [10/10] Find players with shortest distance to next goal 
  - [0/10] For computing player distances to next goal - Did not separate it out to a different function.

- [24/40] These functions should have unit tests
  - [12/20] for unit tests for scoring
  - [6/10] for a unit test that covers no players in the game at the time or scoring OR purpose statements / data interpretations indicate the state comes with at least one active player
  - [6/10] for a unit test that covers scoring a game where multiple players have the same number of goals
  - Given partial credits for all of the above (60%) as you have mentioned you have not done it.
