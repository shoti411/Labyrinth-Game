Pair: crookt-Dsap5131 \
Commit: [b747e6faa39a793d792b3b73fc957da001391113](https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/tree/b747e6faa39a793d792b3b73fc957da001391113) \
Self-eval: https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/7734f8a5c5b107f59945e10a01c6ec495442475b/3/self-3.md \
Score: 66/85 \
Grader: Eshwari Bhide

`Self Eval`: 20/20 points

`state.PP`: 31/45 

- Signatures and purpose statements of the following: 
  - [5/5pt] rotate the spare tile by some number of degrees
  - [5/5pt] shift a row/column and insert the spare tile
  - [3/5pt] move the avatar of the currently active player to a designated spot
    - Method not present, but acknowledged on self-eval so 60% credit
  - [3/5pt] check whether the active player's move has returned its avatar home
    - Method not present, but acknowledged on self-eval so 60% credit
    - Yes, the spec did say "goal", but Matthias also wanted you to also check "home" as it is more significant in that it finishes the game (I double checked with him on this). See Matthias if you have more questions.
  - [5/5pt] kick out the currently active player

- inspect the unit tests for "shift a row/column and insert the spare tile"
  - [10/10pt] test a row and a column insertion
  - [0/10pt] how does a (the) unit test(s) confirm that a player (or several) move along
    - To get the points for this, you had to test 1. sliding in 2 directions 2. A player moving 3. A player not moving 4. A player sliding off the board

`player.md`: 15/20

- [5/5pt] A player must have a `take turn` function/method; it may have more. 

A player must _know_ about:

- [5/5pt] its home,
- [5/5pt] its current goal assignment,
- [5/5pt] its current location

- -5 points if there is no specification of when/how the player receives all the data it receives
