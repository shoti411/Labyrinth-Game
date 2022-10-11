## Self-Evaluation Form for Milestone 2

Indicate below each bullet which file/unit takes care of each task:

1. point to the functinality for determining reachable tiles 

   - a data representation for "reachable tiles" 
   - its signature and purpose statement
   - its "cycle detection" coding (accumulator)
   - its unit test(s)
   https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/cab0268dfb4e07b08a9648f4efba5a7e6f59f93b/Maze/Common/board.py#L158-L182
   https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/cab0268dfb4e07b08a9648f4efba5a7e6f59f93b/Maze/Common/test_board.py#L155-L227

2. point to the functinality for shifting a row or column 

   - its signature and purpose statement
   - unit tests for rows and columns
   https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/cab0268dfb4e07b08a9648f4efba5a7e6f59f93b/Maze/Common/board.py#L64-L106
   https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/cab0268dfb4e07b08a9648f4efba5a7e6f59f93b/Maze/Common/test_board.py#L36-L89

3. point to the functinality for inserting a tile into the open space

   - its signature and purpose statement
   - unit tests for rows and columns
   We took a slightly different approach for this. Since there is only going to be 1 old tile and 1 open space we do not need the user to tell us where they are inserting the tile. What we did is merge this functionality with shifting row or column. Where our row and column functions take a tile as a parameter. This tile will then be inserting into the blank created by the shift and our shift row and column then return the tile that was knocked off. Thus our inserting tile is part of our shifting row or column. 
   https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/cab0268dfb4e07b08a9648f4efba5a7e6f59f93b/Maze/Common/board.py#L64-L106
   https://github.khoury.northeastern.edu/CS4500-F22/crookt-Dsap5131/blob/cab0268dfb4e07b08a9648f4efba5a7e6f59f93b/Maze/Common/test_board.py#L36-L89

If you combined pieces of functionality or separated them, explain.

If you think the name of a method/function is _totally obvious_,
there is no need for a purpose statement. 

The ideal feedback for each of these points is a GitHub
perma-link to the range of lines in a specific file or a collection of
files.

A lesser alternative is to specify paths to files and, if files are
longer than a laptop screen, positions within files are appropriate
responses.

You may wish to add a sentence that explains how you think the
specified code snippets answer the request.

If you did *not* realize these pieces of functionality, say so.

