## Code Re-Design

**TO: Matthias Felleisen** </br>
**FROM: Shaun Gentilin & Thomas Crook**</br>
**DATE: 11/07/2022**</br>
**SUBJECT:Code Re-Design**</br>

The first proposed change, the addition of blank tiles, is ranked as a 1. Within the tile class, we would have to make minimal changes - adding an empty string as an acceptable string, and setting it's rotation to always return an empty string. Outside of the tile class, however, the player's get assigned goal and home tiles, which we'd need to ensure were not blank spaces (as they are unreachable). 

The second proposed change, the addition of moveable goal tiles, is ranked as a 2. The initial construction of our board and state included this case, so a lot of the framework is already in place. There will likely have to be changes in the strategy, as it allows the goal tile to be off the board and therefore "unreachable" from the player's current position. We would need to add functionality that if the extra tile was the current player's goal, then we should check if it can become reachable through shifts and inserts.

The third proposed change, the addition of several goals being pursued sequentially, is ranked as a 4. The state and referee would need added functionality to account for whether or not a player has reached every goal, in order. Our current implementation only updates a "has_reached_goal" value when their coordinate is equal to their goal tile's coordinate. Some refactoring would have to be completed in order to change goals once one is reached, multiple checks if their goals are valid, and a restructuring of the "check_winners" function that calculates which player is in the lead.
