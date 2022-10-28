**If you use GitHub permalinks, make sure your link points to the most recent commit before the milestone deadline.**

## Self-Evaluation Form for Milestone 5

Indicate below each bullet which file/unit takes care of each task:

The player should support five pieces of functionality: 

- `name`
- https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/f0f99f9982fa58e0aec241bf124b2761183e9daa/Maze/Players/player.py#L18-L19
- `propose board` (okay to be `void`)
- https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/f0f99f9982fa58e0aec241bf124b2761183e9daa/Maze/Players/player.py#L21-L27
- `setting up`
- https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/f0f99f9982fa58e0aec241bf124b2761183e9daa/Maze/Players/player.py#L29-L32
- `take a turn`
- https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/f0f99f9982fa58e0aec241bf124b2761183e9daa/Maze/Players/player.py#L34-L36
- `did I win`
- https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/f0f99f9982fa58e0aec241bf124b2761183e9daa/Maze/Players/player.py#L39-L40

Provide links. 

The referee functionality should compose at least four functions:

- setting up the player with initial information
- https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/f0f99f9982fa58e0aec241bf124b2761183e9daa/Maze/Referee/referee.py#L132-L134
- running rounds until termination
- https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/f0f99f9982fa58e0aec241bf124b2761183e9daa/Maze/Referee/referee.py#L136-L151
- running a single round (part of the preceding bullet)
- https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/f0f99f9982fa58e0aec241bf124b2761183e9daa/Maze/Referee/referee.py#L136-L151
- scoring the game
https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/f0f99f9982fa58e0aec241bf124b2761183e9daa/Maze/Referee/referee.py#L136-L151
https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/f0f99f9982fa58e0aec241bf124b2761183e9daa/Maze/Common/state.py#L187-L223

Point to two unit tests for the testing referee:

1. a unit test for the referee function that returns a unique winner
https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/f0f99f9982fa58e0aec241bf124b2761183e9daa/Maze/Common/Tests/test_referee.py#L28-L45
2. a unit test for the scoring function that returns several winners
https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/f0f99f9982fa58e0aec241bf124b2761183e9daa/Maze/Common/Tests/test_referee.py#L48-L67

The ideal feedback for each of these points is a GitHub
perma-link to the range of lines in a specific file or a collection of
files -- in the last git-commit from Thursday evening. 

A lesser alternative is to specify paths to files and, if files are
longer than a laptop screen, positions within files are appropriate
responses.

You may wish to add a sentence that explains how you think the
specified code snippets answer the request.

If you did *not* realize these pieces of functionality, say so.

