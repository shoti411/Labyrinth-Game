Pair: sly-mice \
Commit: [d64ecca1f6cbc3b3bfd81cfc0e4553494a867347](https://github.khoury.northeastern.edu/CS4500-F22/sly-mice/tree/d64ecca1f6cbc3b3bfd81cfc0e4553494a867347) \
Self-eval: https://github.khoury.northeastern.edu/CS4500-F22/sly-mice/blob/f65b1faa30b6769a55281619f912690f9ba3c281/7/self-7.md \
Score: 137/205 \
Grader: Mike Delmonaco

## git log inspection (70pts)

Good job transferring your commit history!

WARNING: You should not commit pycache files! https://github.com/github/gitignore/blob/main/Python.gitignore

It adds a lot of noise to your commits and wastes space in your repository. It should be easy to find what has been changed in a commit. That's one of the main uses of git.

Forming good git habits is very important for your career.

## Tech debt downpayment (60 pts)

-50 Commit messages are all unclear, except for your first completed todo item. Your commit message should describe the change made, and each commit should be focused on a single task. Your 10 tasks were completed in just 3 commits, mostly in 2. If you want to figure out when a change was made, would it be easy to do this with your git commit messages?

Each commit should be focused on a single task. Each commit message should briefly describe the changes made, and you may elaborate further in the extended description of a commit message.

It is important to keep you commit history clean and clear. In the industry, other people will need to look at changes you've made and review them. If you give them one big commit that said "this week's changes", you will be making your reviewers' jobs more difficult, and they might even reject your changes outright for this reason. Also, if someone wants to see when a change was made, it'll be very difficult to figure that out if the history is unclear. You also might want to undo a change or edit a change (rebasing). This is common while addressing feedback in a code review. This is much more difficult on a messy history than a clean one.

## Required revision (40 pts code, 20pts self-eval)

-10 No test for non-square board

Good job being clear, honest, and explicit in your self eval. You get partial credit for honesty.

-4 (partial credit for honesty) No unit test that validates that a board is suitabile for the given number of players 

-4 (partial credit for honesty) No unit that that rejects a board as too small for the given number of players 

## Design (15 pts)

"The initial construction of our board and state included this case, so a lot of the framework is already in place"

This sentence is confusing. Use clearer wording.

