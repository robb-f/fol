# FOL Learner - Grid to FOL API

Basic API to generate a list of all valid FOL expressions given a grid.

The user has the ability to set the grid size, though 5 has been used for testing.

The main function in this file currently demonstrates how the functions work.

Valid expressions are generated and written to a file `expressions.txt`, which
will reside in the same directory as the git repo.

## Usage
Just make sure you have python3 installed. Clone the repository, and run

    python3 grid_to_fol.py

We plan for the grid to be 5x5, so when asked for the size of the grid, you
should input 5, otherwise the code for the medium and hard templates will throw 
exceptions.

## Important API Functions

### generate_expressions()
This is what is called to generate all the expressions. All you need is the
list representation of the grid and a three-item list is returned. The items are
- Easy expressions
- Medium expressions
- Hard expressions

Within these elements, we have a subset of *n* elements, which is the number
of templates available in that difficulty. Thus, the function returns the list
roughly of the form:
    
    def generate_expressions():
        # Algorithmic work to generate the expressions
        return [ 
            [ [ easy1 ], [ easy2 ], ..., [ easy6 ] ],     # easy
            [ [ medium1 ], [ medium2 ], [ medium3 ] ],    # medium
            [ [ hard1 ], [ hard2 ], [ hard3 ], [hard 4] ] # hard
        ]

However, when you call this function, you should set it to 1 variable, as such:

    grid = [ """ The list version of the grid """ ]
    generated_expressions = generate_expressions(grid)

### check_expressions()
This function should be called only after `generate_expressions()` is called
and set to a variable, as described above. The usage is as follows:

    # Generate all FOL expressions
    grid = [ """ List representation of the grid """ ]
    generated_expressions = generate_expressions(grid)
    
    # Test to see if test_expression is part of generated_expressions
    test_expression = [ """ Described below """ ]
    is_member = check_expressions(test_expression, generated_expressions)
    
    if (is_member):
        print("test_expression is a generated expression!")
    else:
        print("test_expression is not a generated expression.")

The 3 difficulties have different formats, so you need to make sure that
`test_expression` is formatted correctly, otherwise you will be thrown a
`ValueError` by the program or the function will return `False`.

**Basic Rules**:
- The first element of `test_expression` MUST be `'All'`.
- `len(test_expression) == 3 or len(test_expression) == 4`
    - Reasoning for this becomes clear in the next subsection

**Difficulty Templates**
- Easy
    - 3 colors `('red', 'blue', 'green')`
    - 3 shapes `('circles', 'triangles', 'squares')`
    - 12 "numbers" `(0-9 as strings, 'even', 'odd')`.
    - The format is going to be all the different permutations of `['All', X, Y]`, where X and Y are any 2 of these 3 categories.
    - The Y section (predicate) is formatted as:
        - `['color=red', 'color=blue', 'color=green']`
        - `['shape=circle', 'shape=triangle', 'shape=square']`
        - `['num=0', 'num=1', ..., 'num=9', 'even=TRUE', 'odd=TRUE']`
    - Here are a few examples:
        - `['All', 'red', 'shape=circle']`
        - `['All', 'blue', 'shape=triangle']`
        - `['All', '8', 'shape=circle']`
        - `['All', 'even', 'shape=square']`
        - `['All', 'circles', 'color=green']`
        - `['All', 'triangles', 'even=TRUE']`
        - `['All', 'squares', 'num=9']`
- Medium
    - The general format here is `['All', shape, number, ('color=X', 'loc=Y')]`.
    - The `shape` and `number` field are the same as Easy. Thus, you would replace these with `red`, `blue`, `8`, `odd`, and so forth.
    - The 4th element is a tuple. Here are the following accepted values:
        - `['color=red', 'color=blue', 'color=green']` for the 1st element
        - `['loc=top2', 'loc=top3', 'loc=right2', 'loc=right3', 'loc=bottom2', 'loc=bottom3', 'loc=left2', 'loc=left3]` for the 2nd element
    - Here are a few examples:
        - `['All', 'circles', '0', ('color=red', 'loc=right2')]`
        - `['All', 'trianges', 'even', ('color=blue', 'loc=left3')]`
        - `['All', 'squares', '5', ('color=green', 'loc=bottom2')]`
- Hard
    - The general format is `['All', shape(x), color(x), (shape(y), min(y) OR max(y), direction)]`.
    - Here, we deal with 2 cells - `x` and `y`. The `shape()` and `color()` clauses are the same as before. 
    - The `min(y)` refers to `min=some_value` which is required by hard templates 1 and 3. `max(y)` refers to `max=some_value` which is required by templates 2 and 4.
    - **NOTE: Due to min applying to templates 1 & 3 and max applying to templates 2 & 4, min(y) can ONLY be assigned to locations 'RightOf' and 'Above', and max(y) can ONLY be assigned to locations 'LeftOf' and 'Below'.** If you mix min/max with the wrong location, `check_expressions()` will always return `False`.
    - The `direction` refers to the directions `['RightOf', 'LeftOf', 'Above', and 'Below']`.
    - Here are a few examples:
        - `['All', 'triangles', 'red', ('squares', 'min=0', 'RightOf')]`
        - `['All', 'squares', 'green', ('triangles', 'max=0', 'LeftOf')]`
        - `['All', 'circles', 'blue', ('squares', 'min=0', 'Above')]`
        - `['All', 'squares', 'red', ('triangles', 'max=0', 'Below')]`
        - Note how `min` clauses are used only with `RightOf` and `Above`, whereas `max` clauses are used only with `LeftOf` and `Below`.