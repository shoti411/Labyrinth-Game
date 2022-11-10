======= TODO =======
* Referee: Catch timeout errors on all API calls (win, takeTurn, setup, proposeBoard). General error checks on all API calls.
* Board: Make board class immutable. Include undo() function, that undoes a previous turn.

======= Completed =======
* State: Get current active player's game state information that also includes other player's positions.
    * Commit message: "add other players to player game state"
* State: Fixing the parallel data structure (players and next players)
    * Commit message: TODO ITEMS 11-8-22
* State: Active_can_reach_tile, remove redundant searches (as long as one path exists, return true.)
    * Commit message: TODO ITEMS 11-8-22
* State: Clean up get_winners() method.
    * Commit message: TODO ITEMS 11-8-22
* Strategy: Remove redundant checks to speed up search.
    * Commit message: TODO ITEMS 11-8-22
* Strategy: Change return type from -1 on pass to False
    * Commit message: TODO 11-9-22
* Observer: Add support for an Observer type - an abstract class.
    * Commit message: TODO 11-9-22
* Strategy: Abstracting Euclid and Reimann to have a common enumerated_tiles method, that takes in a priority function.
    * Commit message: TODO 11-9-22
* Observer: Abstract out helpers. Clean up a lot of the code (some design flaws).
    * Commit message: TODO 11-9-22
* Referee: __valid_move should return a boolean, not raise errors.
    * Commit message: TODO 11-10-22