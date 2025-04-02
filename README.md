# FOL Learner - Grid to FOL API

Basic API to generate a list of all valid FOL expressions given a grid.

The main function in this file currently demonstrates how the functions work.

Valid expressions are generated and written to a file `expressions.txt`, which
will reside in the same directory as the git repo.

Currently in the works:
- Alter template algorithms to account for different display sizes and increase
increase flexibility
- `check_expression()`: A function that would take a single FOL statement as
input, and returns a boolean that represents whether the expression is valid
for the grid 
- Revamping code so that it is spread out across multiple files (ideally,
categorized by difficulty level)
- Write documentation for how to use critical functions

## Usage
Just make sure you have python3 installed. Clone the repository, and run

    python3 grid_to_fol.py

We plan for the grid to be 5x5, so when asked for the size of the grid, you
should input 5, otherwise the code for the medium and hard templates will throw 
exceptions.
