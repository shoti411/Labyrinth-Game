Pair: crookt-Dsap5131 \
Commit: [fac5a435dbe41ca16397a40b650e3be101850acc](https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/tree/fac5a435dbe41ca16397a40b650e3be101850acc) \
Self-eval: https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/3aec8e58530c852e18574dcf18111f4a9702262f/4/self-4.md \
Score: 95/110  \
Grader: Varsha Ramesh

Linked to post-deadline commit 3cbefd8ea2406443f5fcc8bae474cc0775b71bd8 from 10-21 11:29 AM

### Self-Eval

- [10/10] helpful and accurate self-eval

Have not cut marks this time for submitting self-eval links to commits from _after_ the miletsone, but in the future, we will.

### Programming -[65/100]

- [20/20] a data definition for the return value of a call to strategy
  - Is `-1` an appropriate way of representing passing a turn?
- [10/15] - good name, signature/types, and purpose statement for the top-level function that *composes* generating a sequence of spots to move to and searching.
  - Why do you have two top-level methods (`slide_and_insert`, `move`)?
  - Method names do not reflect what the methods actually do.
- [10/15] - good name, signature/types, and purpose statement for generating the sequence of alternative goals
  - incorrect purpose statement for `get_enumerated_tiles` in `Riemann`.
- [15/15] - good name, signature/types, and purpose statement for searching rows then columns.
- [10/15] - good name, signature/types, and purpose statement for some function/method that validates the location of the avatar after slide/insert is not the target and the current target is reachable.
  - [+5] nice job factoring this out into a separate method.
  - [+5] for handling the edge case of making sure the target is reachable even if the the player slides off the board after slide/insert
  - Purpose statement should mention `check_move` is called after insertion and rotation.
  - You do not have a method that checks if the goal tile is different from the avatar's location after slide/insert.
  - Your Strategy does not prevent the player from undoing the previous action.
- [10/10] - for unit test that produces an action to move the player
- [10/10] - for unit test that forces player to pass on turn


### Design Task (Ungraded)
- Havent considered the fact that there could be cheating in the game.
- You have not thought about the referee when the player decides to pass a turn.
- When does the game end? Where is winning or losing?
