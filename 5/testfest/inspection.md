Pair: crookt-Dsap5131 \
Commit: [f0f99f9982fa58e0aec241bf124b2761183e9daa](https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/tree/f0f99f9982fa58e0aec241bf124b2761183e9daa) \
Self-eval: https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/00c1b1a1802e3defad03dff95eec156fe571f730/5/self-5.md \
Score: 125/160 \
Grader: Rajat Keshri

Self-eval - [20/20]

player.pp - [50/50]
The _player_ should be something like a 10-line class offering four methods:
- [10/10pt] `name`
- [10/10pt] `propose board`
- [10/10pt] `setting up`
- [10/10pt] `take a turn`
- [10/10pt] `did I win`

referee.pp - [35/40]
The _testing referee_ must perform the following tasks in order and hence must have separate functions:
- [10/10pt] setting up the player with initial information
- [10/10pt] running rounds until the game is over
- [5/10pt] running a round, which must have functionality for
  - checking for "all passes"
    -  No functionality for checking "what happens if all players pass". 
  - checking for a player that returned to its home (winner)
- [10/10pt] score the game

Unit tests - [20/20]
The entire package needs unit tests for running a game:
- [10/10pt] a unit test for the referee function that returns a unique winner
- [10/10pt] a unit test for the scoring function that returns several winners

---------------------------------------------------------------------

Design.md - [0/30]
- [0/10pt] rotates the tile before insertion
- [0/10pt] selects a row or column to be shifted and in which direction
- [0/10pt] selects the next place for the player's avatar

\<free text\>
