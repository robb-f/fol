import random


class FOL:
    def __init__(self, grid):
        self.quantifiers = ["All", "Some"]
        self.numbers = [str(i) for i in range(0, 10)]
        self.colors = ["red", "blue", "green"]
        self.shapes = ["triangles", "squares", "circles"]
        self.grid = grid
        
        self.color_exp = list()
        for color in self.colors:
            exp = (self.quantifiers[0], color)
            self.color_exp.append(exp)
            exp = (self.quantifiers[1], color)
            self.color_exp.append(exp)
            
        self.shape_exp = list()
        for shape in self.shapes:
            exp = (self.quantifiers[0], shape)
            self.shape_exp.append(exp)
            exp = (self.quantifiers[1], shape)
            self.shape_exp.append(exp)
        
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
        
        self.color_shape_exp = list()
        for shape in self.shapes:
            for color in self.colors:
                exp = (self.quantifiers[0], color, shape)
                self.color_shape_exp.append(exp)
                exp = (self.quantifiers[1], color, shape)
                self.color_shape_exp.append(exp)
        
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
        
        self.color_predicates = ["color=red", "color=blue", "color=green"]
        self.num_predicates = ["".join(["num=", str(i)]) for i in self.numbers]
        self.even_odd = ["even=TRUE", "odd=TRUE"]
        self.shape_predicates = ["shape=triangle", "shape=square", "shape=circle"]


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
    """ Prints a grid to the terminal
    
    Args:
        grid (list): the grid in list form
        size (int): the size of the grid
    """
    # Printing preliminary boundary
    for i in range(size):
        print("+-----", end ="")
    print("+")
    
    for i in range(size):
        print("| ", end="")
        
        for j in range(size):
            print(grid[i][j], end=" | ")
        print("")
        
        for j in range(size):
            print("+-----", end ="")
        print("+")


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
                            if color != col[1]:
                                all_check = False
                                break
                    else:
                        if shape == col[2]:
                            if color == col[1]:
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
                            if color != col[1]:
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
                            if color == col[1]:
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
                            if color != col[1]:
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
                            if color == col[1] and shape == col[2]:
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


# # # # # # # # IN PROGRESS # # # # # # # #
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
                            if num != col[0]:
                                all_check = False
                                break
                    else:
                        if color == col[1]:
                            if num == col[0]:
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
                            if num != col[0]:
                                all_check = False
                                break
                    else:
                        if shape == col[2]:
                            if num == col[0]:
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
    '''
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
                            if color != col[1]:
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
                            if color == col[1]:
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
                            if color != col[1]:
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
                            if color == col[1] and shape == col[2]:
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
    '''
    return exp


def generate_expressions(grid):
    fol_exp = FOL(grid)
    expressions = list()
    
    print("=*=*=*=*= generate_expressions =*=*=*=*=")
    exp1 = eval_color(grid, fol_exp)
    print("COLOR PREDICATES")
    print(exp1)
    exp2 = eval_num(grid, fol_exp)
    print("NUMBER PREDICATES")
    print(exp2)
    #exp3 = eval_shape(grid, fol_exp)
    
    expressions.append(exp1)
    #expressions.append(exp2)
    #expressions.append(exp3)
    
    return expressions
    
    #print("List of color expressions:")
    #print(fol_exp.color_exp)
    #print("List of shape expressions:")
    #print(fol_exp.shape_exp)
    #print("List of number expressions:")
    #print(fol_exp.num_exp)
    #print("List of color_shape expressions:")
    #print(fol_exp.color_shape_exp)
    #print("List of color_number expressions:")
    #print(fol_exp.color_num_exp)
    #print("List of shape_number expressions:")
    #print(fol_exp.shape_num_exp)
    
    #print("List of color predicates:")
    #print(fol_exp.color_predicates)
    #print("List of number predicates:")
    #print(fol_exp.num_predicates)
    #print(fol_exp.even_odd)
    #print("List of shape predicates:")
    #print(fol_exp.shape_predicates)


if __name__ == "__main__":
    size = int(input("Enter size of grid: "))
    grid = generate_grid(size)
    print_grid(grid, size)
    generate_expressions(grid)