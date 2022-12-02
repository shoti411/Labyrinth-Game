## Revisions

**TO: Matthias Felleisen** </br>
**FROM: Luke Po and Shaun Gentilin**</br>
**DATE: 12/01/2022**</br>
**SUBJECT:Revisions**</br>

The following changes were made to the referee to accomodate the change in the specification for players having multiple goals:

The referee was changed to contain a list of possible goals for the given state given to it.

When running the game, the referee must initialize the player goals within the newly created parameter of the list of possible goals, so the function __initialize_goals was created in order to initialize the list of possible goals so different goals could be given to players at the start of the game.

The function __initialize_players was modified in order to use the initialized list of possible goals (from __initialize_goals) and create the player_states to create the game_state.

The function __do_move was modifed as well, such that it checks if the goal is reached, and if it is, it assigns another goal in the list. This change was necessary due to having the list of goals in the referee, but the game_state calling setup on players when they reach their current goal tiles.

The following changes were made to the state to accomodate the change in the specification for players having multiple goals:

The function move_active_player was modified to return whether a player is on its goal. It previously assigned the player's goal as the home automatically, and we needed to be able to assign a new, different goal as well instead of just the player's home.

The function assign_new_goal was created to allow the referee to assign new goals to the player.

The function is_game_over was modified to no longer check whether a player has simply reached their goal, but also checking whether there were no more alternative goals for the referee to assign.

The following changes were made to the player_state to accomodate the change in the specification for players having multiple goals:

replaced field of has_reached_goal with num_goals_reached and the method 
    reached_goal to just add 1 to the number of goals reached

created get_num_goals_reached function
