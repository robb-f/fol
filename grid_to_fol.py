import random

class FOL:
    def __init__(self, grid):
        # Initialize base variables
        self.quantifiers = ["All"]
        self.numbers = [str(i) for i in range(0, 10)]
        self.colors = ["red", "blue", "green"]
        self.shapes = ["triangles", "squares", "circles"]
        self.grid = grid
        
        # Easy 2 and 6
        self.color_exp = list()
        for color in self.colors:
            exp = (self.quantifiers[0], color)
            self.color_exp.append(exp)
            
        # Easy 1 and 3 | Medium 1
        self.shape_exp = list()
        for shape in self.shapes:
            exp = (self.quantifiers[0], shape)
            self.shape_exp.append(exp)
        
        # Easy 4 and 5 | Medium 1
        self.num_exp = list()
        for num in self.numbers:
            exp = (self.quantifiers[0], num)
            self.num_exp.append(exp)
        exp = (self.quantifiers[0], "even")
        self.num_exp.append(exp)
        exp = (self.quantifiers[0], "odd")
        self.num_exp.append(exp)
        
        # Medium 1
        self.shape_num_exp = list()
        for shape in self.shapes:
            for num in self.numbers:
                exp = (self.quantifiers[0], shape, num)
                self.shape_num_exp.append(exp)
            exp = (self.quantifiers[0], shape, "even")
            self.shape_num_exp.append(exp)
            exp = (self.quantifiers[0], shape, "odd")
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
                
        # Hard 1, 2, 3, & 4
        self.shape_color_exp = list()
        for shape in self.shapes:
            for color in self.colors:
                exp = (self.quantifiers[0], shape, color)
                self.shape_color_exp.append(exp)
        
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
                
        self.hard_one = list()
        for shape in self.shapes:
            for num in self.numbers:
                min_str = "min=" + num
                right_of = "RightOf"
                exp = (shape, min_str, right_of)
                self.hard_one.append(exp)
                
        self.hard_two = list()
        for shape in self.shapes:
            for num in self.numbers:
                max_str = "max=" + num
                left_of = "LeftOf"
                exp = (shape, max_str, left_of)
                self.hard_two.append(exp)
                
        self.hard_three = list()
        for shape in self.shapes:
            for num in self.numbers:
                min_str = "min=" + num
                above = "Above"
                exp = (shape, min_str, above)
                self.hard_three.append(exp)
                
        self.hard_four = list()
        for shape in self.shapes:
            for num in self.numbers:
                max_str = "max=" + num
                below = "Below"
                exp = (shape, max_str, below)
                self.hard_four.append(exp)

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
        shape = shape_exp[1][0].upper()
        
        for color_pred in fol_exp.color_predicates:
            color = color_pred.split("color=")[1][0].upper()
            
            # Check if all cells with the shape also have the matching color
            all_check = all(
                col[1] == color
                for row in grid
                for col in row
                if col[2] == shape
            )
            
            if all_check:
                new_exp = list(shape_exp)
                new_exp.append(color_pred)
                exp.append(tuple(new_exp))
                
    return exp

def easy2(grid, fol_exp):
    exp = list()

    for color_exp in fol_exp.color_exp:
        color = color_exp[1][0].upper()

        for shape_pred in fol_exp.shape_predicates:
            shape = shape_pred.split("shape=")[1][0].upper()

            all_check = all(
                col[2] == shape
                for row in grid
                for col in row
                if col[1] == color
            )

            if all_check:
                new_exp = list(color_exp)
                new_exp.append(shape_pred)
                exp.append(tuple(new_exp))

    return exp

def easy3(grid, fol_exp):
    exp = list()

    for shape_exp in fol_exp.shape_exp:
        shape = shape_exp[1][0].upper()

        for i in range(len(fol_exp.num_predicates)):
            num = fol_exp.num_predicates[i].split("num=")[1]

            all_check = all(
                str(col[0]) == num
                for row in grid
                for col in row
                if col[2] == shape
            )

            if all_check:
                new_exp = list(shape_exp)
                new_exp.append(fol_exp.num_predicates[i])
                exp.append(tuple(new_exp))

        for i in range(len(fol_exp.even_odd)):
            num = fol_exp.even_odd[i]

            if num == "even=TRUE":
                check = lambda v: v % 2 == 0
            else:
                check = lambda v: v % 2 == 1

            all_check = all(
                check(int(col[0]))
                for row in grid
                for col in row
                if col[2] == shape
            )

            if all_check:
                new_exp = list(shape_exp)
                new_exp.append(fol_exp.even_odd[i])
                exp.append(tuple(new_exp))

    return exp

def easy4(grid, fol_exp):
    exp = list()

    for num_exp in fol_exp.num_exp:
        num = num_exp[1]

        for i in range(len(fol_exp.color_predicates)):
            shape = fol_exp.shape_predicates[i].split("shape=")[1]
            shape = shape[0].upper()

            if num in {"even", "odd"}:
                check = (lambda v: v % 2 == 0) if num == "even" else (lambda v: v % 2 == 1)
                all_check = all(
                    col[2] == shape
                    for row in grid
                    for col in row
                    if check(int(col[0]))
                )
            else:
                all_check = all(
                    col[2] == shape
                    for row in grid
                    for col in row
                    if str(col[0]) == num
                )

            if all_check:
                new_exp = list(num_exp)
                new_exp.append(fol_exp.shape_predicates[i])
                exp.append(tuple(new_exp))

    return exp

def easy5(grid, fol_exp):
    exp = list()

    for num_exp in fol_exp.num_exp:
        num = num_exp[1]

        for i in range(len(fol_exp.color_predicates)):
            color = fol_exp.color_predicates[i].split("color=")[1]
            color = color[0].upper()

            if num in {"even", "odd"}:
                check = (lambda v: v % 2 == 0) if num == "even" else (lambda v: v % 2 == 1)
                all_check = all(
                    col[1] == color
                    for row in grid
                    for col in row
                    if check(int(col[0]))
                )
            else:
                all_check = all(
                    col[1] == color
                    for row in grid
                    for col in row
                    if str(col[0]) == num
                )

            if all_check:
                new_exp = list(num_exp)
                new_exp.append(fol_exp.color_predicates[i])
                exp.append(tuple(new_exp))

    return exp

def easy6(grid, fol_exp):
    exp = []

    for color_exp in fol_exp.color_exp:
        color = color_exp[1][0].upper()

        for i in range(len(fol_exp.num_predicates)):
            num = fol_exp.num_predicates[i].split("num=")[1]

            all_check = all(
                str(col[0]) == num
                for row in grid
                for col in row
                if col[1] == color
            )

            if all_check:
                new_exp = list(color_exp)
                new_exp.append(fol_exp.num_predicates[i])
                exp.append(tuple(new_exp))

        for i in range(len(fol_exp.even_odd)):
            num = fol_exp.even_odd[i]
            check = (lambda v: v % 2 == 0) if num == "even=TRUE" else (lambda v: v % 2 == 1)

            all_check = all(
                check(int(col[0]))
                for row in grid
                for col in row
                if col[1] == color
            )

            if all_check:
                new_exp = list(color_exp)
                new_exp.append(fol_exp.even_odd[i])
                exp.append(tuple(new_exp))

    return exp

def medium1(grid, fol_exp):
    exp = list()
    
    for shape_num_exp in fol_exp.shape_num_exp:
        for i in range(len(fol_exp.color_loc_predicates)):
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

# Vx shape(x) ^ color(x) ==> 3y shape(y) ^ value(y) > min_val ^ right_of(y, x)
def hard1(grid, fol_exp):
    exp = list()

    for shape_color_exp in fol_exp.shape_color_exp:
        for predicate in fol_exp.hard_one:
            shape1 = shape_color_exp[1]
            color1 = shape_color_exp[2]
            shape2 = predicate[0]
            min_val = int(predicate[1].split("min=")[1])
            all_check = True

            # Normalize shapes and colors ("triangles" → "T", etc.)
            shape1 = shape1[0].upper()
            shape2 = shape2[0].upper()
            color1 = color1[0].upper()

            # Check T -> F == skip if any matching x is in the last column
            last_col_index = len(grid[0]) - 1
            if any(row[last_col_index][1] == color1 and row[last_col_index][2] == shape1 for row in grid):
                continue

            for row in grid:
                for i in range(len(row) - 1):
                    x = row[i]
                    y = row[i + 1]
                    if x[1] == color1 and x[2] == shape1:
                        if not (y[2] == shape2 and int(y[0]) >= min_val):
                            all_check = False
                            break
                if not all_check:
                    break

            if all_check:
                new_exp = list(shape_color_exp)
                new_exp.append(predicate)
                exp.append(tuple(new_exp))

    return exp


# Vx shape(x) ^ color(x) ==> 3y shape(y) ^ value(y) < max_val ^ left_of(y, x)
def hard2(grid, fol_exp):
    exp = list()

    for shape_color_exp in fol_exp.shape_color_exp:
        for predicate in fol_exp.hard_two:
            shape1 = shape_color_exp[1]
            color1 = shape_color_exp[2]
            shape2 = predicate[0]
            max_val = int(predicate[1].split("max=")[1])
            all_check = True

            shape1 = shape1[0].upper()
            shape2 = shape2[0].upper()
            color1 = color1[0].upper()

            # Check T -> F == skip if any matching x is in the first column
            if any(row[0][1] == color1 and row[0][2] == shape1 for row in grid):
                continue

            for row in grid:
                for i in range(1, len(row)):
                    x = row[i]
                    y = row[i - 1]

                    if x[1] == color1 and x[2] == shape1:
                        if y[2] != shape2 or int(y[0]) >= max_val:
                            all_check = False
                            break
                if not all_check:
                    break

            if all_check:
                new_exp = list(shape_color_exp)
                new_exp.append(predicate)
                exp.append(tuple(new_exp))

    return exp

# Vx shape(x) ^ color(x) ==> 3y shape(y) ^ value(y) >= min_val ^ above(y, x)
def hard3(grid, fol_exp):
    exp = list()

    for shape_color_exp in fol_exp.shape_color_exp:
        for predicate in fol_exp.hard_three:
            shape1 = shape_color_exp[1]
            color1 = shape_color_exp[2]
            shape2 = predicate[0]
            min_val = int(predicate[1].split("min=")[1])
            all_check = True

            shape1 = shape1[0].upper()
            shape2 = shape2[0].upper()
            color1 = color1[0].upper()

            # Check T -> F == if any matching x is in the first row, skip this case
            if any(cell[1] == color1 and cell[2] == shape1 for cell in grid[0]):
                continue

            for row_idx in range(1, len(grid)):
                for col in range(len(grid[0])):
                    x = grid[row_idx][col]
                    y = grid[row_idx - 1][col]

                    if x[1] == color1 and x[2] == shape1:
                        if not (y[2] == shape2 and int(y[0]) >= min_val):
                            all_check = False
                            break
                if not all_check:
                    break

            if all_check:
                new_exp = list(shape_color_exp)
                new_exp.append(predicate)
                exp.append(tuple(new_exp))

    return exp

# Vx shape(x) ^ color(x) ==> 3y shape(y) ^ value(y) < min_val ^ below(y, x)
def hard4(grid, fol_exp):
    exp = []

    for shape_color_exp in fol_exp.shape_color_exp:
        for predicate in fol_exp.hard_four:
            shape1 = shape_color_exp[1]
            color1 = shape_color_exp[2]
            shape2 = predicate[0]
            max_val = int(predicate[1].split("max=")[1])
            all_check = True

            shape1 = shape1[0].upper()
            shape2 = shape2[0].upper()
            color1 = color1[0].upper()

            # Check T -> F == if any x is in the last row, skip
            if any(cell[1] == color1 and cell[2] == shape1 for cell in grid[-1]):
                continue

            for row_idx in range(len(grid) - 1):
                for col in range(len(grid[0])):
                    x = grid[row_idx][col]
                    y = grid[row_idx + 1][col]

                    if x[1] == color1 and x[2] == shape1:
                        if not (y[2] == shape2 and int(y[0]) < max_val):
                            all_check = False
                            break
                if not all_check:
                    break

            if all_check:
                new_exp = list(shape_color_exp)
                new_exp.append(predicate)
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
        if count == 1:
            template_print += "MEDIUM TEMPLATE " + str(template_no) + "\n"
        if count == 2:
            template_print += "HARD TEMPLATE " + str(template_no) + "\n"
        
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
            else:
                expression_file.write("  - For all " 
                                      + exp[2] + " " + exp[1] + ", there exists a ")
                
                predicate = exp[3]
                shape = predicate[0]
                direction = predicate[2]
                val = predicate[1].split("min=")[1] if direction == "RightOf" or direction == "Above" else predicate[1].split("max=")[1]
                
                if direction == "RightOf":
                    direction = " directly to the right of it"
                
                    # Value(y) > min_value
                    expression_file.write(shape + " with min value " 
                                          + val + direction + "\n")
                elif direction == "LeftOf":
                    direction = " directly to the left of it"
                
                    expression_file.write(shape + " with max value " 
                                          + val + direction + "\n")
                elif direction == "Above":
                    direction = " directly above it"
                
                    expression_file.write(shape + " with min value of at least " 
                                          + val + direction + "\n")
                elif direction == "Below":
                    direction = " directly below it"
                
                    expression_file.write(shape + " with max value " 
                                          + val + direction + "\n")

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
    
    # Hard Templates
    hard_expressions = list()
    exp_hard1 = hard1(grid, fol_exp)
    exp_hard2 = hard2(grid, fol_exp)
    exp_hard3 = hard3(grid, fol_exp)
    exp_hard4 = hard4(grid, fol_exp)
    hard_expressions.append(exp_hard1)
    hard_expressions.append(exp_hard2)
    hard_expressions.append(exp_hard3)
    hard_expressions.append(exp_hard4)
    
    return easy_expressions, medium_expressions, hard_expressions


if __name__ == "__main__":
    size = int(input("Enter size of grid: "))
    grid = generate_grid(size)
    print_grid(grid, size)
    expressions = generate_expressions(grid)
    write_expressions(expressions)
