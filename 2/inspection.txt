Pair: crookt-Dsap5131 \
Commit: [cab0268dfb4e07b08a9648f4efba5a7e6f59f93b](https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/tree/cab0268dfb4e07b08a9648f4efba5a7e6f59f93b) \
Self-eval: https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/cab0268dfb4e07b08a9648f4efba5a7e6f59f93b/2/self-2.md \
Score: 36/80 \
Grader: Alexis Hooks \

PROGRAMMING TASK:

Note: self evaluation was not turned in on time so the assignment will be graded on a 60% scale
- **[-24]** : no self eval

**[30/40]** Having an operation that determines the reachable tiles from some spot

  **[-10]** : is there a data def. for "coordinates" (places to go to)? 
    
   - your code doesnt tell me much about how the coordinates work. Where is (0,0) located? top-left? top-right? center? Be very specific, and this clarification as an interpretation in your data definition
              
  **[+10]** : is there a signature/purpose statement? 
            
  **[+10]** : is it clear how the method/function checks for cycles? 
  
  **[+10]** : is there at least one unit test with a non-empty expected result
  
  <hr>
  
  
**[20/30]** an operation for sliding a row or column in a direction

  **[+10]** : signature and purpose statement
            
  **[-10]** : the method should check that row/column has even index
  -I couldn't find any functionality that validates the row/column is moveable. The spec states "The key complication is that every other row and column can slide in either direction."
  
  **[+10]** : unit tests: at least one for rows and one for columns
  
  <hr>


**[10/10]** an operation for inserting the spare tile

  **[+5]** method for inserting spare tile
  
  **[+5]** for clarity on what happens to the tile that's pushed out
  
  <hr>
  
DESIGN TASK (ungraded):
- Ref needs to know the player color
- Ref needs to keep track of the last action that was performed
- For future design tasks include high level function/method names/signatures for the functionality you plan to implement
