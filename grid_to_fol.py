import random

class FOL:
    def __init__(self, grid):
        # Initialize base variables
        self.quantifiers = ["All", "Some"]
        self.numbers = [str(i) for i in range(0, 10)]
        self.colors = ["red", "blue", "green"]
        self.shapes = ["triangles", "squares", "circles"]
        self.grid = grid
        
        # Color expressions
        self.color_exp = list()
        for color in self.colors:
            exp = (self.quantifiers[0], color)
            self.color_exp.append(exp)
            exp = (self.quantifiers[1], color)
            self.color_exp.append(exp)
            
        # Shape expressions
        self.shape_exp = list()
        for shape in self.shapes:
            exp = (self.quantifiers[0], shape)
            self.shape_exp.append(exp)
            exp = (self.quantifiers[1], shape)
            self.shape_exp.append(exp)
        
        # Number expressions
        self.num_exp = list()
        for num in self.numbers:
            exp = (self.quantifiers[0], num)
            self.num_exp.append(exp)
            exp = (self.quantifiers[1], num)
            self.num_exp.append(exp)
        exp = (self.quantifiers[0], "even")
        self.num_exp.append(exp)
        exp = (self.quantifiers[1], "even")
        self.num_exp.append(exp)
        exp = (self.quantifiers[0], "odd")
        self.num_exp.append(exp)
        exp = (self.quantifiers[1], "odd")
        self.num_exp.append(exp)
        
        # Color-Shape expressions
        self.color_shape_exp = list()
        for shape in self.shapes:
            for color in self.colors:
                exp = (self.quantifiers[0], color, shape)
                self.color_shape_exp.append(exp)
                exp = (self.quantifiers[1], color, shape)
                self.color_shape_exp.append(exp)
        
        # Color-Number expressions
        self.color_num_exp = list()
        for color in self.colors:
            for num in self.numbers:
                exp = (self.quantifiers[0], color, num)
                self.color_num_exp.append(exp)
                exp = (self.quantifiers[1], color, num)
                self.color_num_exp.append(exp)
            exp = (self.quantifiers[0], color, "even")
            self.color_num_exp.append(exp)
            exp = (self.quantifiers[1], color, "even")
            self.color_num_exp.append(exp)
            exp = (self.quantifiers[0], color, "odd")
            self.color_num_exp.append(exp)
            exp = (self.quantifiers[1], color, "odd")
            self.color_num_exp.append(exp)
        
        # Shape-Number expressions
        self.shape_num_exp = list()
        for shape in self.shapes:
            for num in self.numbers:
                exp = (self.quantifiers[0], shape, num)
                self.shape_num_exp.append(exp)
                exp = (self.quantifiers[1], shape, num)
                self.shape_num_exp.append(exp)
            exp = (self.quantifiers[0], shape, "even")
            self.shape_num_exp.append(exp)
            exp = (self.quantifiers[1], shape, "even")
            self.shape_num_exp.append(exp)
            exp = (self.quantifiers[0], shape, "odd")
            self.shape_num_exp.append(exp)
            exp = (self.quantifiers[1], shape, "odd")
            self.shape_num_exp.append(exp)
        
        # Predicates
        self.color_predicates = ["color=red", "color=blue", "color=green"]
        self.num_predicates = ["".join(["num=", str(i)]) for i in self.numbers]
        self.even_odd = ["even=TRUE", "odd=TRUE"]
        self.shape_predicates = ["shape=triangle", "shape=square", "shape=circle"]
        self.location_predicates = ["loc=top2", "loc=top3",         # rows
                                    "loc=right2", "loc=right3",     # columns
                                    "loc=bottom2", "loc=bottom3",   # rows
                                    "loc=left2", "loc=left3"]       # columns
        
        self.color_loc_predicates = list()
        for color in self.color_predicates:
            for location in self.location_predicates:
                predicate = (color, location)
                self.color_loc_predicates.append(predicate)


def generate_grid(size):
    """ Generates a grid by creating a size by size matrix using a list.
    
    Args:
        size (int): size of the square grid
    
    Returns:
        list: a matrix of dimensions size by size
    """
    numbers = [str(i) for i in range(0, 10)]    # 0-9
    colors = ["R", "B", "G"]                    # Red, Blue, Green
    shape = ["T", "S", "C"]                     # Triangle, Square, Circle
    grid = list()
    
    for row in range(size):
        # Row to append to grid
        row_items = list()
        for col in range(size):
            # Cell to append to row
            cell = ""
            # Randomly select a number, color, and shape
            cell += numbers[random.randint(0, len(numbers) - 1)]
            cell += colors[random.randint(0, len(colors) - 1)]
            cell += shape[random.randint(0, len(shape) - 1)]
            # Put cell in the row
            row_items.append(cell)
        # Put the row into the grid
        grid.append(row_items)
    
    return grid


def print_grid(grid, size):
    """ Prints a grid to the terminal and writes it to grid.txt
    
    Args:
        grid (list): the grid in list form
        size (int): the size of the grid
    """
    # Writing grid to file
    grid_file = open("grid.txt", mode='w')
    
    # Printing preliminary boundary
    for i in range(size):
        print("+-----", end ="")
        grid_file.write("+-----")
    print("+")
    grid_file.write("+\n")
    
    for i in range(size):
        print("| ", end="")
        grid_file.write("| ")
        
        for j in range(size):
            print(grid[i][j], end=" | ")
            grid_file.write(grid[i][j] + " | ")
        print("")
        grid_file.write("\n")
        
        for j in range(size):
            print("+-----", end ="")
            grid_file.write("+-----")
        print("+")
        grid_file.write("+\n")
    
    grid_file.close()

def eval_color(grid, fol_exp):
    """ Returns list of expressions with valid color predicates
    
    Args:
        grid (list): the grid in list form
        fol_exp (FOL): the FOL expressions object instance
    
    Returns:
        list: valid expressions with color predicates
    """
    exp = list()
    
    # SHAPE EXPRESSIONS
    for shape_exp in fol_exp.shape_exp:
        for i in range(len(fol_exp.color_predicates)):
            all_check = True
            some_check = False
            quantifier = shape_exp[0]
            shape = shape_exp[1]
            if shape == "triangles":
                shape = "T"
            elif shape == "squares":
                shape = "S"
            else:
                shape = "C"
            color = fol_exp.color_predicates[i].split("color=")[1]
            if color == "red":
                color = "R"
            elif color == "blue":
                color = "B"
            else:
                color = "G"

            for row in grid:
                for col in row:
                    if quantifier == "All":
                        if shape == col[2]:
                            if color != col[1]: # Counterexample
                                all_check = False
                                break
                    else:
                        if shape == col[2]:
                            if color == col[1]: # Example
                                some_check = True
                                break
                    
                if not all_check or some_check:
                    break
            
            if all_check and quantifier == "All":
                new_exp = list(shape_exp)
                new_exp.append(fol_exp.color_predicates[i])
                exp.append(tuple(new_exp))
            elif some_check and quantifier == "Some":
                new_exp = list(shape_exp)
                new_exp.append(fol_exp.color_predicates[i])
                exp.append(tuple(new_exp))
    
    # NUMBER EXPRESSIONS
    for num_exp in fol_exp.num_exp:
        for i in range(len(fol_exp.color_predicates)):
            all_check = True
            some_check = False
            quantifier = num_exp[0]
            num = num_exp[1]
            color = fol_exp.color_predicates[i].split("color=")[1]
            if color == "red":
                color = "R"
            elif color == "blue":
                color = "B"
            else:
                color = "G"

            for row in grid:
                for col in row:
                    if quantifier == "All":
                        if num == col[0]:
                            if color != col[1]: # Counterexample
                                all_check = False
                                break
                        elif num == "even" and int(col[0]) % 2 == 0:
                            if color != col[1]:
                                all_check = False
                                break
                        elif num == "odd" and int(col[0]) % 2 == 1:
                            if color != col[1]:
                                all_check = False
                                break
                    else:
                        if num == col[0]:
                            if color == col[1]: # Example
                                some_check = True
                                break
                        elif num == "even" and int(col[0]) % 2 == 0:
                            if color == col[1]:
                                some_check = True
                                break
                        elif num == "odd" and int(col[0]) % 2 == 1:
                            if color == col[1]:
                                some_check = True
                                break
                    
                if not all_check or some_check:
                    break
            
            if all_check and quantifier == "All":
                new_exp = list(num_exp)
                new_exp.append(fol_exp.color_predicates[i])
                exp.append(tuple(new_exp))
            elif some_check and quantifier == "Some":
                new_exp = list(num_exp)
                new_exp.append(fol_exp.color_predicates[i])
                exp.append(tuple(new_exp))
    
    # SHAPE-NUMBER EXPRESSIONS
    for shape_num_exp in fol_exp.shape_num_exp:
        for i in range(len(fol_exp.color_predicates)):
            all_check = True
            some_check = False
            quantifier = shape_num_exp[0]
            shape = shape_num_exp[1]
            if shape == "triangles":
                shape = "T"
            elif shape == "squares":
                shape = "S"
            else:
                shape = "C"
            num = shape_num_exp[2]
            color = fol_exp.color_predicates[i].split("color=")[1]
            if color == "red":
                color = "R"
            elif color == "blue":
                color = "B"
            else:
                color = "G"
            
            for row in grid:
                for col in row:
                    if quantifier == "All":
                        if num == col[0] and shape == col[2]:
                            if color != col[1]: # Counterexample
                                all_check = False
                                break
                        elif num == "even" and int(col[0]) % 2 == 0 and shape == col[2]:
                            if color != col[1]:
                                all_check = False
                                break
                        elif num == "odd" and int(col[0]) % 2 == 1 and shape == col[2]:
                            if color != col[1]:
                                all_check = False
                                break
                    else:
                        if num == col[0]:
                            if color == col[1] and shape == col[2]: # Example
                                some_check = True
                                break
                        elif num == "even" and int(col[0]) % 2 == 0 and shape == col[2]:
                            if color == col[1]:
                                some_check = True
                                break
                        elif num == "odd" and int(col[0]) % 2 == 1 and shape == col[2]:
                            if color == col[1]:
                                some_check = True
                                break
                    
                if not all_check or some_check:
                    break
            
            if all_check and quantifier == "All":
                new_exp = list(shape_num_exp)
                new_exp.append(fol_exp.color_predicates[i])
                exp.append(tuple(new_exp))
            elif some_check and quantifier == "Some":
                new_exp = list(shape_num_exp)
                new_exp.append(fol_exp.color_predicates[i])
                exp.append(tuple(new_exp))
    
    return exp


def eval_num(grid, fol_exp):
    """ Returns list of expressions with valid number predicates
    
    Args:
        grid (list): the grid in list form
        fol_exp (FOL): the FOL expressions object instance
    
    Returns:
        list: valid expressions with number predicates
    """
    exp = list()
    
    # COLOR EXPRESSIONS
    for color_exp in fol_exp.color_exp:
        for i in range(len(fol_exp.num_predicates)):
            all_check = True
            some_check = False
            quantifier = color_exp[0]
            color = color_exp[1]
            if color == "red":
                color = "R"
            elif color == "blue":
                color = "B"
            else:
                color = "G"
            num = fol_exp.num_predicates[i].split("num=")[1]

            for row in grid:
                for col in row:
                    if quantifier == "All":
                        if color == col[1]:
                            if num != col[0]: # Counterexample
                                all_check = False
                                break
                    else:
                        if color == col[1]:
                            if num == col[0]: # Example
                                some_check = True
                                break
                    
                if not all_check or some_check:
                    break
            
            if all_check and quantifier == "All":
                new_exp = list(color_exp)
                new_exp.append(fol_exp.num_predicates[i])
                exp.append(tuple(new_exp))
            elif some_check and quantifier == "Some":
                new_exp = list(color_exp)
                new_exp.append(fol_exp.num_predicates[i])
                exp.append(tuple(new_exp))
        
        # Even-Odd
        for i in range(len(fol_exp.even_odd)):
            all_check = True
            some_check = False
            quantifier = color_exp[0]
            color = color_exp[1]
            if color == "red":
                color = "R"
            elif color == "blue":
                color = "B"
            else:
                color = "G"
            num = fol_exp.even_odd[i]

            for row in grid:
                for col in row:
                    if quantifier == "All":
                        if color == col[1]:
                            if num == "even=TRUE" and int(col[0]) % 2 != 0: # Counterexample
                                all_check = False
                                break
                            elif num == "odd=TRUE" and int(col[0]) % 2 != 1:
                                all_check = False
                                break
                    else:
                        if color == col[1]:
                            if num == "even=TRUE" and int(col[0]) % 2 == 0: # Example
                                some_check = True
                                break
                            elif num == "odd=TRUE" and int(col[0]) % 2 == 1:
                                some_check = True
                                break
                    
                if not all_check or some_check:
                    break
            
            if all_check and quantifier == "All":
                new_exp = list(color_exp)
                new_exp.append(fol_exp.even_odd[i])
                exp.append(tuple(new_exp))
            elif some_check and quantifier == "Some":
                new_exp = list(color_exp)
                new_exp.append(fol_exp.even_odd[i])
                exp.append(tuple(new_exp))
    
    
    # SHAPE EXPRESSIONS
    for shape_exp in fol_exp.shape_exp:
        for i in range(len(fol_exp.num_predicates)):
            all_check = True
            some_check = False
            quantifier = shape_exp[0]
            shape = shape_exp[1]
            if shape == "triangles":
                shape = "T"
            elif shape == "squares":
                shape = "S"
            else:
                shape = "C"
            num = fol_exp.num_predicates[i].split("num=")[1]
            
            for row in grid:
                for col in row:
                    if quantifier == "All":
                        if shape == col[2]:
                            if num != col[0]: # Counterexample
                                all_check = False
                                break
                    else:
                        if shape == col[2]:
                            if num == col[0]: # Example
                                some_check = True
                                break
                    
                if not all_check or some_check:
                    break
            
            if all_check and quantifier == "All":
                new_exp = list(shape_exp)
                new_exp.append(fol_exp.num_predicates[i])
                exp.append(tuple(new_exp))
            elif some_check and quantifier == "Some":
                new_exp = list(shape_exp)
                new_exp.append(fol_exp.num_predicates[i])
                exp.append(tuple(new_exp))
        
        # Even-Odd
        for i in range(len(fol_exp.even_odd)):
            all_check = True
            some_check = False
            quantifier = shape_exp[0]
            shape = shape_exp[1]
            if shape == "triangles":
                shape = "T"
            elif shape == "squares":
                shape = "S"
            else:
                shape = "C"
            num = fol_exp.even_odd[i]

            for row in grid:
                for col in row:
                    if quantifier == "All":
                        if shape == col[2]:
                            if num == "even=TRUE" and int(col[0]) % 2 != 0: # Counterexample
                                all_check = False
                                break
                            elif num == "odd=TRUE" and int(col[0]) % 2 != 1:
                                all_check = False
                                break
                    else:
                        if shape == col[2]:
                            if num == "even=TRUE" and int(col[0]) % 2 == 0: # Example
                                some_check = True
                                break
                            elif num == "odd=TRUE" and int(col[0]) % 2 == 1:
                                some_check = True
                                break
                    
                if not all_check or some_check:
                    break
            
            if all_check and quantifier == "All":
                new_exp = list(shape_exp)
                new_exp.append(fol_exp.even_odd[i])
                exp.append(tuple(new_exp))
            elif some_check and quantifier == "Some":
                new_exp = list(shape_exp)
                new_exp.append(fol_exp.even_odd[i])
                exp.append(tuple(new_exp))
    
    # COLOR-SHAPE EXPRESSIONS
    for color_shape_exp in fol_exp.color_shape_exp:
        for i in range(len(fol_exp.num_predicates)):
            all_check = True
            some_check = False
            quantifier = color_shape_exp[0]
            color = color_shape_exp[1]
            if color == "red":
                color = "R"
            elif color == "blue":
                color = "B"
            else:
                color = "G"
            shape = color_shape_exp[2]
            if shape == "triangles":
                shape = "T"
            elif shape == "squares":
                shape = "S"
            else:
                shape = "C"
            num = fol_exp.num_predicates[i].split("num=")[1]
            
            for row in grid:
                for col in row:
                    if quantifier == "All":
                        if color == col[1] and shape == col[2]:
                            if num != col[0]: # Counterexample
                                all_check = False
                                break
                    else:
                        if color == col[1] and shape == col[2]:
                            if num == col[0]: # Example
                                some_check = True
                                break
                    
                if not all_check or some_check:
                    break
            
            if all_check and quantifier == "All":
                new_exp = list(color_shape_exp)
                new_exp.append(fol_exp.num_predicates[i])
                exp.append(tuple(new_exp))
            elif some_check and quantifier == "Some":
                new_exp = list(color_shape_exp)
                new_exp.append(fol_exp.num_predicates[i])
                exp.append(tuple(new_exp))
        
        for i in range(len(fol_exp.even_odd)):
            all_check = True
            some_check = False
            quantifier = color_shape_exp[0]
            color = color_shape_exp[1]
            if color == "red":
                color = "R"
            elif color == "blue":
                color = "B"
            else:
                color = "G"
            shape = color_shape_exp[2]
            if shape == "triangles":
                shape = "T"
            elif shape == "squares":
                shape = "S"
            else:
                shape = "C"
            num = fol_exp.even_odd[i]

            for row in grid:
                for col in row:
                    if quantifier == "All":
                        if color == col[1] and shape == col[2]:
                            if num == "even=TRUE" and int(col[0]) % 2 != 0: # Counterexample
                                all_check = False
                                break
                            elif num == "odd=TRUE" and int(col[0]) % 2 != 1:
                                all_check = False
                                break
                    else:
                        if color == col[1] and shape == col[2]:
                            if num == "even=TRUE" and int(col[0]) % 2 == 0: # Example
                                some_check = True
                                break
                            elif num == "odd=TRUE" and int(col[0]) % 2 == 1:
                                some_check = True
                                break
                    
                if not all_check or some_check:
                    break
            
            if all_check and quantifier == "All":
                new_exp = list(color_shape_exp)
                new_exp.append(fol_exp.even_odd[i])
                exp.append(tuple(new_exp))
            elif some_check and quantifier == "Some":
                new_exp = list(color_shape_exp)
                new_exp.append(fol_exp.even_odd[i])
                exp.append(tuple(new_exp))
    
    return exp

def eval_shape(grid, fol_exp):
    """ Returns list of expressions with valid shape predicates
    
    Args:
        grid (list): the grid in list form
        fol_exp (FOL): the FOL expressions object instance
    
    Returns:
        list: valid expressions with shape predicates
    """
    exp = list()
    
    # COLOR EXPRESSIONS
    for color_exp in fol_exp.color_exp:
        for i in range(len(fol_exp.color_predicates)):
            all_check = True
            some_check = False
            quantifier = color_exp[0]
            color = color_exp[1]
            if color == "red":
                color = "R"
            elif color == "blue":
                color = "B"
            else:
                color = "G"
            shape = fol_exp.shape_predicates[i].split("shape=")[1]
            if shape == "triangle":
                shape = "T"
            elif shape == "square":
                shape = "S"
            else:
                shape = "C"

            for row in grid:
                for col in row:
                    if quantifier == "All":
                        if color == col[1]:
                            if shape != col[2]: # Counterexample
                                all_check = False
                                break
                    else:
                        if color == col[1]:
                            if shape == col[2]: # Example
                                some_check = True
                                break
                    
                if not all_check or some_check:
                    break
            
            if all_check and quantifier == "All":
                new_exp = list(color_exp)
                new_exp.append(fol_exp.shape_predicates[i])
                exp.append(tuple(new_exp))
            elif some_check and quantifier == "Some":
                new_exp = list(color_exp)
                new_exp.append(fol_exp.shape_predicates[i])
                exp.append(tuple(new_exp))
    
    # NUMBER EXPRESSIONS
    for num_exp in fol_exp.num_exp:
        for i in range(len(fol_exp.color_predicates)):
            all_check = True
            some_check = False
            quantifier = num_exp[0]
            num = num_exp[1]
            shape = fol_exp.shape_predicates[i].split("shape=")[1]
            if shape == "triangle":
                shape = "T"
            elif shape == "square":
                shape = "S"
            else:
                shape = "C"

            for row in grid:
                for col in row:
                    if quantifier == "All":
                        if num == col[0]:
                            if shape != col[2]: # Counterexample
                                all_check = False
                                break
                        elif num == "even" and int(col[0]) % 2 == 0:
                            if shape != col[2]:
                                all_check = False
                                break
                        elif num == "odd" and int(col[0]) % 2 == 1:
                            if shape != col[2]:
                                all_check = False
                                break
                    else:
                        if num == col[0]:
                            if shape == col[2]: # Example
                                some_check = True
                                break
                        elif num == "even" and int(col[0]) % 2 == 0:
                            if shape == col[2]:
                                some_check = True
                                break
                        elif num == "odd" and int(col[0]) % 2 == 1:
                            if shape == col[2]:
                                some_check = True
                                break
                    
                if not all_check or some_check:
                    break
            
            if all_check and quantifier == "All":
                new_exp = list(num_exp)
                new_exp.append(fol_exp.shape_predicates[i])
                exp.append(tuple(new_exp))
            elif some_check and quantifier == "Some":
                new_exp = list(num_exp)
                new_exp.append(fol_exp.shape_predicates[i])
                exp.append(tuple(new_exp))
    
    # COLOR-NUMBER EXPRESSIONS
    for color_num_exp in fol_exp.color_num_exp:
        for i in range(len(fol_exp.color_predicates)):
            all_check = True
            some_check = False
            quantifier = color_num_exp[0]
            color = color_num_exp[1]
            if color == "red":
                color = "R"
            elif color == "blue":
                color = "B"
            else:
                color = "G"
            num = color_num_exp[2]
            shape = fol_exp.shape_predicates[i].split("shape=")[1]
            if shape == "triangle":
                shape = "T"
            elif shape == "square":
                shape = "S"
            else:
                shape = "C"            
            
            for row in grid:
                for col in row:
                    if quantifier == "All":
                        if num == col[0] and color == col[1]:
                            if shape != col[2]: # Counterexample
                                all_check = False
                                break
                        elif num == "even" and int(col[0]) % 2 == 0 and color == col[1]:
                            if shape != col[2]:
                                all_check = False
                                break
                        elif num == "odd" and int(col[0]) % 2 == 1 and color == col[1]:
                            if shape != col[2]:
                                all_check = False
                                break
                    else:
                        if num == col[0]:
                            if color == col[1] and shape == col[2]: # Example
                                some_check = True
                                break
                        elif num == "even" and int(col[0]) % 2 == 0 and color == col[1]:
                            if shape == col[2]:
                                some_check = True
                                break
                        elif num == "odd" and int(col[0]) % 2 == 1 and color == col[1]:
                            if shape == col[2]:
                                some_check = True
                                break
                    
                if not all_check or some_check:
                    break
            
            if all_check and quantifier == "All":
                new_exp = list(color_num_exp)
                new_exp.append(fol_exp.shape_predicates[i])
                exp.append(tuple(new_exp))
            elif some_check and quantifier == "Some":
                new_exp = list(color_num_exp)
                new_exp.append(fol_exp.shape_predicates[i])
                exp.append(tuple(new_exp))
    
    return exp

def eval_color_loc(grid, fol_exp):
    """ Returns list of expressions with valid color-location predicates
    
    Args:
        grid (list): the grid in list form
        fol_exp (FOL): the FOL expressions object instance
    
    Returns:
        list: valid expressions with shape predicates
    """
    exp = list()
    #debug = open("debug.txt", mode='w')
    
    # SHAPE-NUMBER EXPRESSIONS
    for shape_num_exp in fol_exp.shape_num_exp:
        for i in range(len(fol_exp.color_loc_predicates)):
            all_check = True
            some_check = False
            quantifier = shape_num_exp[0]
            shape = shape_num_exp[1]
            if shape == "triangles":
                shape = "T"
            elif shape == "squares":
                shape = "S"
            else:
                shape = "C"
            num = shape_num_exp[2]
            color = fol_exp.color_loc_predicates[i][0].split("color=")[1]
            if color == "red":
                color = "R"
            elif color == "blue":
                color = "B"
            else:
                color = "G"
            direction = fol_exp.color_loc_predicates[i][1].split("loc=")[1]
            index = 0
            limit = 0
            if direction == "top2" or direction == "top3" or direction == "left2" or direction == "left3":
                index = 0
            elif direction == "bottom2" or direction == "bottom3" or direction == "right2" or direction == "right3":
                index = len(grid[0])
            limit = int(direction[len(direction) - 1])
            direction = direction[:len(direction) - 1]
            
            # Check row by row, until you reach the limit
            if direction == "top":
                # Check for the validity of the color clause
                while index < limit:
                    for j in range(len(grid[0])):
                        if quantifier == "All":
                            if num == grid[index][j][0] and shape == grid[index][j][2]:
                                if color != grid[index][j][1]: # counterexample
                                    #print("failed on", quantifier, shape, num, color, direction, str(limit), end=", ")
                                    #print(grid[index][j], "at", index)
                                    all_check = False
                                    break
                            elif num == "even" and int(grid[index][j][0]) % 2 == 0 and shape == grid[index][j][2]:
                                if color != grid[index][j][1]:
                                    #print("failed on", quantifier, shape, num, color, direction, str(limit), end=", ")
                                    #print(grid[index][j], "at", index)
                                    all_check = False
                                    break
                            elif num == "odd" and int(grid[index][j][0]) % 2 == 1 and shape == grid[index][j][2]:
                                if color != grid[index][j][1]:
                                    #print("failed on", quantifier, shape, num, color, direction, str(limit), end=", ")
                                    #print(grid[index][j], "at", index)
                                    all_check = False
                                    break
                        else:
                            if num == grid[index][j][0]:
                                if color == grid[index][j][1] and shape == grid[index][j][2]: # Example
                                    some_check = True
                                    break
                            elif num == "even" and int(grid[index][j][0]) % 2 == 0 and shape == grid[index][j][2]:
                                if color == grid[index][j][1]:
                                    some_check = True
                                    break
                            elif num == "odd" and int(grid[index][j][0]) % 2 == 1 and shape == grid[index][j][2]:
                                if color == grid[index][j][1]:
                                    some_check = True
                                    break
                        
                    if not all_check or some_check:
                        break
                    
                    index += 1
                
                #debug.write("===== ")
                #debug.write(quantifier)
                #debug.write(" ")
                #debug.write(shape)
                #debug.write(" ")
                #debug.write(num)
                #debug.write(" ")
                #debug.write(color)
                #debug.write(" ")
                #debug.write(direction)
                #debug.write(" ")
                #debug.write(str(limit))
                #debug.write(" ")
                #debug.write(" =====\n")
                
                # Check validity of location clause
                # Here, if we are out of bounds, but we reach a cell with a number and shape match, we immediately break
                while index < len(grid[0]):
                    for j in range(len(grid[0])):
                        if some_check:
                            break
                        
                        #debug.write("index = ")
                        #debug.write(str(index))
                        #debug.write("\n")
                        #debug.write(grid[index][j])
                        #debug.write("\n")
                        if quantifier == "All":
                            if num == grid[index][j][0] and shape == grid[index][j][2]:
                                #print("round 2 failed on", quantifier, shape, num, color, direction, str(limit), end=", ")
                                #print(grid[index][j], "at", index)
                                all_check = False
                                break
                            elif num == "even" and int(grid[index][j][0]) % 2 == 0 and shape == grid[index][j][2]:
                                #print("round 2 failed on", quantifier, shape, num, color, direction, str(limit), end=", ")
                                #print(grid[index][j], "at", index)
                                all_check = False
                                break
                            elif num == "odd" and int(grid[index][j][0]) % 2 == 1 and shape == grid[index][j][2]:
                                #print("round 2 failed on", quantifier, shape, num, color, direction, str(limit), end=", ")
                                #print(grid[index][j], "at", index)
                                all_check = False
                                break
                    index += 1
            elif direction == "bottom":
                # TO-DO
                # Backwards algorithm to "top"
                # Start at len(grid[0]) and work your way backwards towards len(grid[0]) - limit
                all_check = False
            elif direction == "left":
                # TO-DO
                # Similar algorithm to "top"
                all_check = False
                """
                for j in range(len(grid[0])):
                    while index < limit:
                        if quantifier == "All":
                            if num == grid[j][index][0] and shape == grid[j][index][2]:
                                if color != grid[j][index][1]: # counterexample
                                    all_check = False
                                    break
                            elif num == "even" and int(grid[j][index][0]) % 2 == 0 and shape == grid[j][index][2]:
                                if color != grid[j][index][1]:
                                    all_check = False
                                    break
                            elif num == "odd" and int(grid[j][index][0]) % 2 == 1 and shape == grid[j][index][2]:
                                if color != grid[j][index][1]:
                                    all_check = False
                                    break
                        else:
                            if num == grid[j][index][0]:
                                if color == grid[j][index][1] and shape == grid[j][index][2]: # Example
                                    some_check = True
                                    break
                            elif num == "even" and int(grid[j][index][0]) % 2 == 0 and shape == grid[j][index][2]:
                                if color == grid[j][index][1]:
                                    some_check = True
                                    break
                            elif num == "odd" and int(grid[j][index][0]) % 2 == 1 and shape == grid[j][index][2]:
                                if color == grid[j][index][1]:
                                    some_check = True
                                    break
                        
                        index += 1
                        
                        if not all_check or some_check:
                            break
                """
            elif direction == "right":
                # TO-DO
                # Similar algorithm to bottom
                all_check = False
            
            if all_check and quantifier == "All":
                #print("appending", quantifier, shape, num, color, direction, str(limit))
                new_exp = list(shape_num_exp)
                new_exp.append(fol_exp.color_loc_predicates[i])
                exp.append(tuple(new_exp))
            elif some_check and quantifier == "Some":
                #print("appending", quantifier, shape, num, color, direction, str(limit))
                new_exp = list(shape_num_exp)
                new_exp.append(fol_exp.color_loc_predicates[i])
                exp.append(tuple(new_exp))
                
    return exp

def write_to_file(expression_file, count, expressions):
    """ Helper function for write_expressions()
    
    Args:
        expression_file (file): the expression file to write to
        count (int): 0 is color, 1 is number, 2 is shape predicates,
                     3 is color-location predicates
        expressions (list): the full list of valid expressions
    """
    for exp in expressions:
        splitter = ""
        
        if len(exp) == 3:
            expression_file.write("  - " + exp[0] + " " 
                                  + exp[1] + " are ")
            if count == 0:
                splitter = exp[2].split("color=")[1] + "\n"
            elif count == 1:
                if exp[2] == "even=TRUE":
                    splitter = "even\n"
                elif exp[2] == "odd=TRUE":
                    splitter = "odd\n"
                else:
                    splitter = exp[2].split("num=")[1] + "\n"
            elif count == 2:
                splitter = exp[2].split("shape=")[1] + "s\n"
            
            expression_file.write(splitter)
        else:
            expression_file.write("  - " + exp[0] + " " 
                                  + exp[1] + " " + exp[2] + " are ")
            if count == 0:
                splitter = exp[3].split("color=")[1] + "\n"
            elif count == 1:
                if exp[3] == "even=TRUE":
                    splitter = "even\n"
                elif exp[3] == "odd=TRUE":
                    splitter = "odd\n"
                else:
                    splitter = exp[3].split("num=")[1] + "\n"
            elif count == 2:
                splitter = exp[3].split("shape=")[1] + "s\n"
            elif count == 3:
                expression_file.write(exp[3][0].split("color=")[1] + " and ")
                temp = exp[3][1].split("loc=")[1]
                splitter = "located in the " + temp[:len(temp) - 1] + " " + temp[len(temp) - 1] + " rows of the grid\n"
            
            expression_file.write(splitter)

def write_expressions(expressions):
    """ Writes expressions to expressions.txt
    
    Args:
        expressions (list): a list of expressions
    """
    expression_file = open("expressions.txt", mode='w')
    
    expression_file.write("\t\t\t\t\t=*=*=*=*= GENERATE EXPRESSIONS =*=*=*=*=\n\n")
    count = 0
    
    for exp in expressions:
        
        if count == 0:
            expression_file.write("COLOR PREDICATES\n")
        elif count == 1:
            expression_file.write("NUMBER PREDICATES\n")
        elif count == 2:
            expression_file.write("SHAPE PREDICATES\n")
        elif count == 3:
            expression_file.write("COLOR-LOCATION PREDICATES\n")
            
        write_to_file(expression_file, count, exp)
        
        expression_file.write("\n")
        count += 1
    
    expression_file.close()

def generate_expressions(grid):
    fol_exp = FOL(grid)
    expressions = list()
    
    exp1 = eval_color(grid, fol_exp)
    exp2 = eval_num(grid, fol_exp)
    exp3 = eval_shape(grid, fol_exp)
    exp4 = eval_color_loc(grid, fol_exp)
    
    expressions.append(exp1)
    expressions.append(exp2)
    expressions.append(exp3)
    expressions.append(exp4)
    
    return expressions


if __name__ == "__main__":
    size = int(input("Enter size of grid: "))
    grid = generate_grid(size)
    print_grid(grid, size)
    expressions = generate_expressions(grid)
    write_expressions(expressions)