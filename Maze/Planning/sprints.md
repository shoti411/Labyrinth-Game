## Splitting "Labyrinth" into 3 Sprints

**TO: Matthias Felleisen** </br>
**FROM: Dylan Sapienza & Thomas Crook**</br>
**DATE: 09/26/2022**</br>
**SUBJECT: Proposal for Labyrinth Sprints**</br>

In order to split the implementation of Labyrinth into three 16-hour sprints, we have decided on a very specific approach. Our first sprint will focus on the creation of the player-referee interface, the player logic, as well as unit testing to wrap up our sprint. In sprint 2 we will complete the referee logic and a basic observer. Finally, for sprint 3,  we will complete the remote-player communication and the final implementation of the observer. Unit testing and integration testing will be ran at the end of every sprint, to catch any bugs that need to be prioritized before moving on to the next sprint.

The player-referee interface is the foundational step in our interpretation of the specifications, as both the player and referee models will be built using it's documentation as a guide. Sprint 1 prioritizes this interface to ensure we can limit future errors. Once our working design of this interface is complete, we will move on to the player logic. 

Sprint 2 tackles the referee logic after the completion of the player logic. The project specifications state that the referee controls the players; therefore, in order to adequately test the referee logic, player needs to have a full working implementation. We will end sprint 2 with a basic observer so we can visualize our project so far, and potentially catch bugs.

The final sprint will prioritize the remote-player communication and the final view. The functionality in this sprint all requires the previous work to be finished and tested carefully,  as they both require a functioning Labyrinth backend in order to be implemented. Therefore, we've selected these tasks to be implemented last.
