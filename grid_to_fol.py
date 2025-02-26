import random

class FOL:
    def __init__(self, grid):
        # Initialize base variables
        self.quantifiers = ["All", "Some"]
        self.numbers = [str(i) for i in range(0, 10)]
        self.colors = ["red", "blue", "green"]
        self.shapes = ["triangles", "squares", "circles"]
        self.grid = grid
        
        # Easy 2 and 6
        self.color_exp = list()
        for color in self.colors:
            exp = (self.quantifiers[0], color)
            self.color_exp.append(exp)
            # TO-DO: remove this and remove if quantifier != "All" check
            exp = (self.quantifiers[1], color)
            self.color_exp.append(exp)
            
        # Easy 1 and 3 | Medium 1
        self.shape_exp = list()
        for shape in self.shapes:
            exp = (self.quantifiers[0], shape)
            self.shape_exp.append(exp)
            # TO-DO: remove this and remove if quantifier != "All" check
            exp = (self.quantifiers[1], shape)
            self.shape_exp.append(exp)
        
        # Easy 4 and 5 | Medium 1
        self.num_exp = list()
        for num in self.numbers:
            exp = (self.quantifiers[0], num)
            self.num_exp.append(exp)
            # TO-DO: remove this and remove if quantifier != "All" check
            exp = (self.quantifiers[1], num)
            self.num_exp.append(exp)
        exp = (self.quantifiers[0], "even")
        self.num_exp.append(exp)
        # TO-DO: remove this and remove if quantifier != "All" check
        exp = (self.quantifiers[1], "even")
        self.num_exp.append(exp)
        exp = (self.quantifiers[0], "odd")
        self.num_exp.append(exp)
        # TO-DO: remove this and remove if quantifier != "All" check
        exp = (self.quantifiers[1], "odd")
        self.num_exp.append(exp)
        
        # Medium 1
        self.shape_num_exp = list()
        for shape in self.shapes:
            for num in self.numbers:
                exp = (self.quantifiers[0], shape, num)
                self.shape_num_exp.append(exp)
                # TO-DO: remove this and remove if quantifier != "All" check
                exp = (self.quantifiers[1], shape, num)
                self.shape_num_exp.append(exp)
            exp = (self.quantifiers[0], shape, "even")
            self.shape_num_exp.append(exp)
            # TO-DO: remove this and remove if quantifier != "All" check
            exp = (self.quantifiers[1], shape, "even")
            self.shape_num_exp.append(exp)
            exp = (self.quantifiers[0], shape, "odd")
            self.shape_num_exp.append(exp)
            # TO-DO: remove this and remove if quantifier != "All" check
            exp = (self.quantifiers[1], shape, "odd")
            self.shape_num_exp.append(exp)
        
        # Medium 3
        self.min_max_exp = list()
        for shape in self.shapes:
            for num in self.numbers:
                min_str = "min=" + num
                max_str = "max=" + num
                exp = (self.quantifiers[0], shape, min_str)
                self.min_max_exp.append(exp)
                exp = (self.quantifiers[0], shape, max_str)
                self.min_max_exp.append(exp)
                # TO-DO: remove this and remove if quantifier != "All" check
                exp = (self.quantifiers[1], shape, min_str)
                self.min_max_exp.append(exp)
                # TO-DO: remove this and remove if quantifier != "All" check
                exp = (self.quantifiers[1], shape, max_str)
                self.min_max_exp.append(exp)
        
        # All Predicates
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

def easy1(grid, fol_exp):
    exp = list()
    
    for shape_exp in fol_exp.shape_exp:
        for i in range(len(fol_exp.color_predicates)):
            quantifier = shape_exp[0]
            if quantifier != "All":
                continue
            
            all_check = True
            shape = shape_exp[1]
            color = fol_exp.color_predicates[i].split("color=")[1]
            
            if shape == "triangles":
                shape = "T"
            elif shape == "squares":
                shape = "S"
            else:
                shape = "C"
            
            if color == "red":
                color = "R"
            elif color == "blue":
                color = "B"
            else:
                color = "G"
            
            for row in grid:
                for col in row:
                    if shape == col[2]:
                        if color != col[1]: # Counterexample
                            all_check = False
                            break
                    
                if not all_check:
                    break
            
            if all_check:
                new_exp = list(shape_exp)
                new_exp.append(fol_exp.color_predicates[i])
                exp.append(tuple(new_exp))
                
    return exp

def easy2(grid, fol_exp):
    exp = list()
    
    for color_exp in fol_exp.color_exp:
        for i in range(len(fol_exp.color_predicates)):
            quantifier = color_exp[0]
            if quantifier != "All":
                continue
            
            all_check = True
            color = color_exp[1]
            shape = fol_exp.shape_predicates[i].split("shape=")[1]
            
            if color == "red":
                color = "R"
            elif color == "blue":
                color = "B"
            else:
                color = "G"
            
            if shape == "triangle":
                shape = "T"
            elif shape == "square":
                shape = "S"
            else:
                shape = "C"

            for row in grid:
                for col in row:
                    if color == col[1]:
                        if shape != col[2]: # Counterexample
                            all_check = False
                            break
                    
                if not all_check:
                    break
            
            if all_check:
                new_exp = list(color_exp)
                new_exp.append(fol_exp.shape_predicates[i])
                exp.append(tuple(new_exp))
                
    return exp

def easy3(grid, fol_exp):
    exp = list()
    
    for shape_exp in fol_exp.shape_exp:
        for i in range(len(fol_exp.num_predicates)):
            quantifier = shape_exp[0]
            if quantifier != "All":
                continue
            
            all_check = True
            shape = shape_exp[1]
            num = fol_exp.num_predicates[i].split("num=")[1]
            
            if shape == "triangles":
                shape = "T"
            elif shape == "squares":
                shape = "S"
            else:
                shape = "C"
            
            for row in grid:
                for col in row:
                    if shape == col[2]:
                        if num != col[0]: # Counterexample
                            all_check = False
                            break
                    
                if not all_check:
                    break
            
            if all_check:
                new_exp = list(shape_exp)
                new_exp.append(fol_exp.num_predicates[i])
                exp.append(tuple(new_exp))
        
        # Even-Odd
        for i in range(len(fol_exp.even_odd)):
            quantifier = shape_exp[0]
            if quantifier != "All":
                continue
            
            all_check = True
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
                    if shape == col[2]:
                        if num == "even=TRUE" and int(col[0]) % 2 != 0: # Counterexample
                            all_check = False
                            break
                        elif num == "odd=TRUE" and int(col[0]) % 2 != 1:
                            all_check = False
                            break
                    
                if not all_check:
                    break
            
            if all_check:
                new_exp = list(shape_exp)
                new_exp.append(fol_exp.even_odd[i])
                exp.append(tuple(new_exp))
                
    return exp
    
def easy4(grid, fol_exp):
    exp = list()
    
    for num_exp in fol_exp.num_exp:
        for i in range(len(fol_exp.color_predicates)):
            quantifier = num_exp[0]
            if quantifier != "All":
                continue
            
            all_check = True
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
                    
                if not all_check:
                    break
            
            if all_check:
                new_exp = list(num_exp)
                new_exp.append(fol_exp.shape_predicates[i])
                exp.append(tuple(new_exp))
                
    return exp

def easy5(grid, fol_exp):
    exp = list()
    
    for num_exp in fol_exp.num_exp:
        for i in range(len(fol_exp.color_predicates)):
            quantifier = num_exp[0]
            if quantifier != "All":
                continue
            
            all_check = True
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
                    
                if not all_check:
                    break
            
            if all_check:
                new_exp = list(num_exp)
                new_exp.append(fol_exp.color_predicates[i])
                exp.append(tuple(new_exp))
                
    return exp
    
def easy6(grid, fol_exp):
    exp = list()
    
    for color_exp in fol_exp.color_exp:
        for i in range(len(fol_exp.num_predicates)):
            quantifier = color_exp[0]
            if quantifier != "All":
                continue
            
            all_check = True
            color = color_exp[1]
            num = fol_exp.num_predicates[i].split("num=")[1]
            if color == "red":
                color = "R"
            elif color == "blue":
                color = "B"
            else:
                color = "G"

            for row in grid:
                for col in row:
                    if color == col[1]:
                        if num != col[0]: # Counterexample
                            all_check = False
                            break
                    
                if not all_check:
                    break
            
            if all_check:
                new_exp = list(color_exp)
                new_exp.append(fol_exp.num_predicates[i])
                exp.append(tuple(new_exp))
        
        # Even-Odd
        for i in range(len(fol_exp.even_odd)):
            quantifier = color_exp[0]
            if quantifier != "All":
                continue
            
            all_check = True
            color = color_exp[1]
            num = fol_exp.even_odd[i]
            
            if color == "red":
                color = "R"
            elif color == "blue":
                color = "B"
            else:
                color = "G"

            for row in grid:
                for col in row:
                    if color == col[1]:
                        if num == "even=TRUE" and int(col[0]) % 2 != 0: # Counterexample
                            all_check = False
                            break
                        elif num == "odd=TRUE" and int(col[0]) % 2 != 1:
                            all_check = False
                            break
                    
                if not all_check:
                    break
            
            if all_check:
                new_exp = list(color_exp)
                new_exp.append(fol_exp.even_odd[i])
                exp.append(tuple(new_exp))
    
    return exp

def medium1(grid, fol_exp):
    exp = list()
    
    for shape_num_exp in fol_exp.shape_num_exp:
        for i in range(len(fol_exp.color_loc_predicates)):
            quantifier = shape_num_exp[0]
            if quantifier != "All":
                continue
            
            all_check = True
            shape = shape_num_exp[1]
            num = shape_num_exp[2]
            color = fol_exp.color_loc_predicates[i][0].split("color=")[1]
            direction = fol_exp.color_loc_predicates[i][1].split("loc=")[1]
            index = 0
            limit = 0
            
            if shape == "triangles":
                shape = "T"
            elif shape == "squares":
                shape = "S"
            else:
                shape = "C"
            if num == "even" or num == "odd":
                continue
            
            if color == "red":
                color = "R"
            elif color == "blue":
                color = "B"
            else:
                color = "G"
                
            if direction == "top2" or direction == "top3" or direction == "left2" or direction == "left3":
                index = 0
                limit = int(direction[len(direction) - 1])
            elif direction == "bottom2" or direction == "bottom3" or direction == "right2" or direction == "right3":
                index = len(grid[0]) - 1
                limit = index - int(direction[len(direction) - 1])
            direction = direction[:len(direction) - 1]
            
            # Check row by row, until you reach the limit
            if direction == "top":
                # Check for the validity of the color clause
                while index < limit:
                    for j in range(len(grid[0])):
                        if num == grid[index][j][0] and shape == grid[index][j][2]:
                            if color != grid[index][j][1]: # counterexample
                                all_check = False
                                break
                        
                    if not all_check:
                        break
                    
                    index += 1
                
                # Check validity of location clause
                # Here, if we are out of bounds, but we reach a cell with a number and shape match, we immediately break
                while index < len(grid[0]):
                    for j in range(len(grid[0])):
                        if num == grid[index][j][0] and shape == grid[index][j][2]:
                            all_check = False
                            break
                    index += 1
            elif direction == "bottom":
                # Backwards algorithm to "top"
                # Start at len(grid[0]) and work your way backwards towards len(grid[0]) - limit
                # Check for the validity of the color clause
                while index > limit:
                    for j in range(len(grid[0])):
                        if num == grid[index][j][0] and shape == grid[index][j][2]:
                            if color != grid[index][j][1]: # counterexample
                                all_check = False
                                break
                        
                    if not all_check:
                        all_check = True
                        break
                    
                    index -= 1
                
                # Check validity of location clause
                # Here, if we are out of bounds, but we reach a cell with a number and shape match, we immediately break
                while index >= 0:
                    if not all_check:
                        break
                    for j in range(len(grid[0])):
                        if num == grid[index][j][0] and shape == grid[index][j][2]:
                            all_check = False
                            break
                    index -= 1
            elif direction == "left":
                # Similar algorithm to "top"
                # Check for the validity of the color clause
                while index < limit:    
                    for j in range(len(grid[0])):
                        if num == grid[j][index][0] and shape == grid[j][index][2]:
                            if color != grid[j][index][1]: # counterexample
                                all_check = False
                                break
                                
                    index += 1
                        
                    if not all_check:
                        break
                
                # Check validity of location clause
                # Here, if we are out of bounds, but we reach a cell with a number and shape match, we immediately break
                while index < len(grid[0]):
                    for j in range(len(grid[0])):
                        if num == grid[j][index][0] and shape == grid[j][index][2]:
                            all_check = False
                            break
                        
                    index += 1
            elif direction == "right":
                # Similar algorithm to bottom and left
                while index > limit:    
                    for j in range(len(grid[0])):
                        if num == grid[j][index][0] and shape == grid[j][index][2]:
                            if color != grid[j][index][1]: # counterexample
                                all_check = False
                                break
                                
                    index -= 1
                        
                    if not all_check:
                        break
                
                # Check validity of location clause
                # Here, if we are out of bounds, but we reach a cell with a number and shape match, we immediately break
                while index >= 0:
                    for j in range(len(grid[0])):
                        if num == grid[j][index][0] and shape == grid[j][index][2]:
                            all_check = False
                            break
                        
                    index -= 1
            
            if all_check:
                new_exp = list(shape_num_exp)
                new_exp.append(fol_exp.color_loc_predicates[i])
                exp.append(tuple(new_exp))
                
    return exp

def medium2(grid, fol_exp):
    exp = list()
    
    for shape_num_exp in fol_exp.shape_num_exp:
        for i in range(len(fol_exp.color_loc_predicates)):
            quantifier = shape_num_exp[0]
            if quantifier != "All":
                continue
            
            all_check = True
            shape = shape_num_exp[1]
            num = shape_num_exp[2]
            color = fol_exp.color_loc_predicates[i][0].split("color=")[1]
            direction = fol_exp.color_loc_predicates[i][1].split("loc=")[1]
            index = 0
            limit = 0
            
            if shape == "triangles":
                shape = "T"
            elif shape == "squares":
                shape = "S"
            else:
                shape = "C"
            
            if num != "even" and num != "odd":
                continue
            
            if color == "red":
                color = "R"
            elif color == "blue":
                color = "B"
            else:
                color = "G"
            
            if direction == "top2" or direction == "top3" or direction == "left2" or direction == "left3":
                index = 0
                limit = int(direction[len(direction) - 1])
            elif direction == "bottom2" or direction == "bottom3" or direction == "right2" or direction == "right3":
                index = len(grid[0]) - 1
                limit = index - int(direction[len(direction) - 1])
            direction = direction[:len(direction) - 1]
            
            # Check row by row, until you reach the limit
            if direction == "top":
                # Check for the validity of the color clause
                while index < limit:
                    for j in range(len(grid[0])):
                        if num == "even" and int(grid[index][j][0]) % 2 == 0 and shape == grid[index][j][2]:
                            if color != grid[index][j][1]:
                                all_check = False
                                break
                        elif num == "odd" and int(grid[index][j][0]) % 2 == 1 and shape == grid[index][j][2]:
                            if color != grid[index][j][1]:
                                all_check = False
                                break
                        
                    if not all_check:
                        break
                    
                    index += 1
                
                # Check validity of location clause
                # Here, if we are out of bounds, but we reach a cell with a number and shape match, we immediately break
                while index < len(grid[0]):
                    for j in range(len(grid[0])):
                        if num == "even" and int(grid[index][j][0]) % 2 == 0 and shape == grid[index][j][2]:
                            all_check = False
                            break
                        elif num == "odd" and int(grid[index][j][0]) % 2 == 1 and shape == grid[index][j][2]:
                            all_check = False
                            break
                        
                    index += 1
            elif direction == "bottom":
                # Backwards algorithm to "top"
                # Start at len(grid[0]) and work your way backwards towards len(grid[0]) - limit
                # Check for the validity of the color clause
                while index > limit:
                    for j in range(len(grid[0])):
                        if num == "even" and int(grid[index][j][0]) % 2 == 0 and shape == grid[index][j][2]:
                            if color != grid[index][j][1]:
                                all_check = False
                                break
                        elif num == "odd" and int(grid[index][j][0]) % 2 == 1 and shape == grid[index][j][2]:
                            if color != grid[index][j][1]:
                                all_check = False
                                break
                        
                    if not all_check:
                        all_check = True
                        break
                    
                    index -= 1
                
                # Check validity of location clause
                # Here, if we are out of bounds, but we reach a cell with a number and shape match, we immediately break
                while index >= 0:
                    if not all_check:
                        break
                    for j in range(len(grid[0])):
                        if num == "even" and int(grid[index][j][0]) % 2 == 0 and shape == grid[index][j][2]:
                            all_check = False
                            break
                        elif num == "odd" and int(grid[index][j][0]) % 2 == 1 and shape == grid[index][j][2]:
                            all_check = False
                            break
                    index -= 1
            elif direction == "left":
                # Similar algorithm to "top"
                # Check for the validity of the color clause
                while index < limit:    
                    for j in range(len(grid[0])):
                        if num == "even" and int(grid[j][index][0]) % 2 == 0 and shape == grid[j][index][2]:
                            if color != grid[j][index][1]:
                                all_check = False
                                break
                        elif num == "odd" and int(grid[j][index][0]) % 2 == 1 and shape == grid[j][index][2]:
                            if color != grid[j][index][1]:
                                all_check = False
                                break
                                
                    index += 1
                        
                    if not all_check:
                        break
                
                # Check validity of location clause
                # Here, if we are out of bounds, but we reach a cell with a number and shape match, we immediately break
                while index < len(grid[0]):
                    for j in range(len(grid[0])):
                        if num == "even" and int(grid[j][index][0]) % 2 == 0 and shape == grid[j][index][2]:
                            all_check = False
                            break
                        elif num == "odd" and int(grid[j][index][0]) % 2 == 1 and shape == grid[j][index][2]:
                            all_check = False
                            break
                        
                    index += 1
            elif direction == "right":
                # Similar algorithm to bottom and left
                while index > limit:    
                    for j in range(len(grid[0])):
                        if num == "even" and int(grid[j][index][0]) % 2 == 0 and shape == grid[j][index][2]:
                            if color != grid[j][index][1]:
                                all_check = False
                                break
                        elif num == "odd" and int(grid[j][index][0]) % 2 == 1 and shape == grid[j][index][2]:
                            if color != grid[j][index][1]:
                                all_check = False
                                break
                                
                    index -= 1
                        
                    if not all_check:
                        break
                
                # Check validity of location clause
                # Here, if we are out of bounds, but we reach a cell with a number and shape match, we immediately break
                while index >= 0:
                    for j in range(len(grid[0])):
                        if num == "even" and int(grid[j][index][0]) % 2 == 0 and shape == grid[j][index][2]:
                            all_check = False
                            break
                        elif num == "odd" and int(grid[j][index][0]) % 2 == 1 and shape == grid[j][index][2]:
                            all_check = False
                            break
                        
                    index -= 1
            
            if all_check:
                new_exp = list(shape_num_exp)
                new_exp.append(fol_exp.color_loc_predicates[i])
                exp.append(tuple(new_exp))
                
    return exp

def medium3(grid, fol_exp):
    exp = list()
    
    for shape_num_exp in fol_exp.min_max_exp:
        for i in range(len(fol_exp.color_loc_predicates)):
            quantifier = shape_num_exp[0]
            if quantifier != "All":
                continue
            
            all_check = True
            min_bool = True
            shape = shape_num_exp[1]
            num = shape_num_exp[2]
            color = fol_exp.color_loc_predicates[i][0].split("color=")[1]
            direction = fol_exp.color_loc_predicates[i][1].split("loc=")[1]
            index = 0
            limit = 0
            
            if shape == "triangles":
                shape = "T"
            elif shape == "squares":
                shape = "S"
            else:
                shape = "C"
            
            if num[:4] == "min=":
                num = num.split("min=")[1]
            else:
                min_bool = False
                num = num.split("max=")[1]
            
            if color == "red":
                color = "R"
            elif color == "blue":
                color = "B"
            else:
                color = "G"
            
            if direction == "top2" or direction == "top3" or direction == "left2" or direction == "left3":
                index = 0
                limit = int(direction[len(direction) - 1])
            elif direction == "bottom2" or direction == "bottom3" or direction == "right2" or direction == "right3":
                index = len(grid[0]) - 1
                limit = index - int(direction[len(direction) - 1])
            direction = direction[:len(direction) - 1]
            
            # Check row by row, until you reach the limit
            if direction == "top":
                # Check for the validity of the color clause
                while index < limit:
                    for j in range(len(grid[0])):
                        if min_bool:
                            if grid[index][j][0] >= num and shape == grid[index][j][2]:
                                if color != grid[index][j][1]: # counterexample
                                    all_check = False
                                    break
                        else:
                            if grid[index][j][0] <= num and shape == grid[index][j][2]:
                                if color != grid[index][j][1]: # counterexample
                                    all_check = False
                                    break
                        
                    if not all_check:
                        break
                    
                    index += 1
                
                # Check validity of location clause
                # Here, if we are out of bounds, but we reach a cell with a number and shape match, we immediately break
                while index < len(grid[0]):
                    for j in range(len(grid[0])):
                        if min_bool:
                            if grid[index][j][0] >= num and shape == grid[index][j][2]:
                                all_check = False
                                break
                        else:
                            if grid[index][j][0] <= num and shape == grid[index][j][2]:
                                all_check = False
                                break
                            
                    index += 1
            elif direction == "bottom":
                # Backwards algorithm to "top"
                # Start at len(grid[0]) and work your way backwards towards len(grid[0]) - limit
                # Check for the validity of the color clause
                while index > limit:
                    for j in range(len(grid[0])):
                        if min_bool:
                            if grid[index][j][0] >= num and shape == grid[index][j][2]:
                                if color != grid[index][j][1]: # counterexample
                                    all_check = False
                                    break
                        else:
                            if grid[index][j][0] <= num and shape == grid[index][j][2]:
                                if color != grid[index][j][1]: # counterexample
                                    all_check = False
                                    break
                        
                    if not all_check:
                        all_check = True
                        break
                    
                    index -= 1
                
                # Check validity of location clause
                # Here, if we are out of bounds, but we reach a cell with a number and shape match, we immediately break
                while index >= 0:
                    if not all_check:
                        break
                    
                    for j in range(len(grid[0])):
                        if min_bool:
                            if grid[index][j][0] >= num and shape == grid[index][j][2]:
                                all_check = False
                                break
                        else:
                            if grid[index][j][0] <= num and shape == grid[index][j][2]:
                                all_check = False
                                break
                    
                    index -= 1
            elif direction == "left":
                # Similar algorithm to "top"
                # Check for the validity of the color clause
                while index < limit:    
                    for j in range(len(grid[0])):
                        if min_bool:
                            if grid[j][index][0] >= num and shape == grid[j][index][2]:
                                if color != grid[j][index][1]: # counterexample
                                    all_check = False
                                    break
                        else:
                            if grid[j][index][0] <= num and shape == grid[j][index][2]:
                                if color != grid[j][index][1]: # counterexample
                                    all_check = False
                                    break
                                
                    index += 1
                        
                    if not all_check:
                        break
                
                # Check validity of location clause
                # Here, if we are out of bounds, but we reach a cell with a number and shape match, we immediately break
                while index < len(grid[0]):
                    for j in range(len(grid[0])):
                        if min_bool:
                            if grid[j][index][0] >= num and shape == grid[j][index][2]:
                                all_check = False
                                break
                        else:
                            if grid[j][index][0] <= num and shape == grid[j][index][2]:
                                all_check = False
                                break
                        
                    index += 1
            elif direction == "right":
                # Similar algorithm to bottom and left
                while index > limit:    
                    for j in range(len(grid[0])):
                        if min_bool:
                            if grid[j][index][0] >= num and shape == grid[j][index][2]:
                                if color != grid[j][index][1]: # counterexample
                                    all_check = False
                                    break
                        else:
                            if grid[j][index][0] <= num and shape == grid[j][index][2]:
                                if color != grid[j][index][1]: # counterexample
                                    all_check = False
                                    break
                                
                    index -= 1
                        
                    if not all_check:
                        break
                
                # Check validity of location clause
                # Here, if we are out of bounds, but we reach a cell with a number and shape match, we immediately break
                while index >= 0:
                    for j in range(len(grid[0])):
                        if min_bool:
                            if grid[j][index][0] >= num and shape == grid[j][index][2]:
                                all_check = False
                                break
                        else:
                            if grid[j][index][0] <= num and shape == grid[j][index][2]:
                                all_check = False
                                break
                        
                    index -= 1
            
            if all_check:
                new_exp = list(shape_num_exp)
                new_exp.append(fol_exp.color_loc_predicates[i])
                exp.append(tuple(new_exp))
                
    return exp
    
def write_to_file(expression_file, count, expressions):
    """ Helper function for write_expressions()
    
    Args:
        expression_file (file): the expression file to write to
        count (int): 0 is easy, 1 is medium, 2 is hard
        expressions (list): the full list of valid expressions
    """
    template_no = 1
    for template in expressions:
        template_print = ""
        if count == 0:
            template_print += "EASY TEMPLATE " + str(template_no) + "\n"
            template_no += 1
        if count == 1:
            template_print += "MEDIUM TEMPLATE " + str(template_no) + "\n"
            template_no += 1
        
        expression_file.write(template_print)
            
        for exp in template:
            splitter = ""
            
            if count == 0:
                expression_file.write("  - " + exp[0] + " " 
                                      + exp[1] + " are ")
                if exp[2] == "even=TRUE":
                    splitter = "even\n"
                elif exp[2] == "odd=TRUE":
                    splitter = "odd\n"
                elif exp[2][:4] == "num=":
                    splitter = exp[2].split("num=")[1] + "\n"
                elif exp[2][:6] == "color=":
                    splitter = exp[2].split("color=")[1] + "\n"
                else:
                    splitter = exp[2].split("shape=")[1] + "s\n"
                
                expression_file.write(splitter)
            elif count == 1:
                expression_file.write("  - " + exp[0] + " " 
                                      + exp[1] + " " + exp[2] + " are ")
                
                predicate = exp[3]
                color = predicate[0].split("color=")[1] + " and "
                temp = exp[3][1].split("loc=")[1]
                location = "located in the " + temp[:len(temp) - 1] + " " + temp[len(temp) - 1] + " rows of the grid\n"
                splitter = color + location
                                
                expression_file.write(splitter)

def write_expressions(expressions):
    """ Writes expressions to expressions.txt
    
    Args:
        expressions (list): a list of expressions
    """
    expression_file = open("expressions.txt", mode='w')
    
    expression_file.write("\t\t\t\t\t=*=*=*=*= GENERATE EXPRESSIONS =*=*=*=*=\n\n")
    count = 0
    
    for difficulty in expressions:
        if count == 0:
            expression_file.write("* * * EASY TEMPLATES * * *\n\n")
        elif count == 1:
            expression_file.write("* * * MEDIUM TEMPLATES * * *\n\n")
        elif count == 2:
            expression_file.write("* * * HARD TEMPLATES * * *\n\n")
            
        write_to_file(expression_file, count, difficulty)
        
        expression_file.write("\n")
        count += 1
    
    expression_file.close()

def generate_expressions(grid):
    fol_exp = FOL(grid)
    
    # Easy Templates
    easy_expressions = list()
    exp_easy1 = easy1(grid, fol_exp)
    exp_easy2 = easy2(grid, fol_exp)
    exp_easy3 = easy3(grid, fol_exp)
    exp_easy4 = easy4(grid, fol_exp)
    exp_easy5 = easy5(grid, fol_exp)
    exp_easy6 = easy6(grid, fol_exp)
    easy_expressions.append(exp_easy1)
    easy_expressions.append(exp_easy2)
    easy_expressions.append(exp_easy3)
    easy_expressions.append(exp_easy4)
    easy_expressions.append(exp_easy5)
    easy_expressions.append(exp_easy6)
    
    # Medium Templates
    medium_expressions = list()
    exp_med1 = medium1(grid, fol_exp)
    exp_med2 = medium2(grid, fol_exp)
    exp_med3 = medium3(grid, fol_exp)
    medium_expressions.append(exp_med1)
    medium_expressions.append(exp_med2)
    medium_expressions.append(exp_med3)
    
    return easy_expressions, medium_expressions


if __name__ == "__main__":
    size = int(input("Enter size of grid: "))
    grid = generate_grid(size)
    print_grid(grid, size)
    expressions = generate_expressions(grid)
    write_expressions(expressions)