* Referee: Catch timeout errors on all API calls (win, takeTurn, setup, proposeBoard). General error checks on all API calls.
* Board: Make board class immutable. Include undo() function, that undoes a previous turn.
* State: Fixing the parallel data structure (players and next players)
* State: Get current active player's game state information that also includes other player's positions.
* State: Active_can_reach_tile, remove redundant searches (as long as one path exists, return true.)
* Strategy: Remove redundant checks to speed up search.
* Observer: Add support for an Observer type - an abstract class.
* Observer: Abstract out helpers. Clean up a lot of the code (some design flaws).
* Strategy: Abstracting Euclid and Reimann to have a common enumerated_tiles method, that takes in a priority function.
* Referee: __valid_move should return a boolean, not raise errors.
* Board: Finding tile should throw error if the tile isn't on the board, or the extra tile.

hello