======= TODO =======
* Referee: Catch timeout errors on all API calls (win, takeTurn, setup, proposeBoard). General error checks on all API calls.
* Board: Make board class immutable. Include undo() function, that undoes a previous turn.
* Strategy: Change return type from -1 on pass to False
* Observer: Add support for an Observer type - an abstract class.
* Observer: Abstract out helpers. Clean up a lot of the code (some design flaws).
* Strategy: Abstracting Euclid and Reimann to have a common enumerated_tiles method, that takes in a priority function.
* Referee: __valid_move should return a boolean, not raise errors.
* Board: Finding tile should throw error if the tile isn't on the board, or the extra tile.

* REQUIRED REVISIONS

======= In Progress =======


======= Completed =======
* State: Get current active player's game state information that also includes other player's positions.
    * Commit message: "add other players to player game state"
* State: Fixing the parallel data structure (players and next players)
* State: Active_can_reach_tile, remove redundant searches (as long as one path exists, return true.)
* State: Clean up get_winners() method.
* Strategy: Remove redundant checks to speed up search.
