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
    exp = list()

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
        shape = shape_num_exp[1]
        num = shape_num_exp[2]

        if num in {"even", "odd"}:
            continue

        shape = shape[0].upper()

        for i in range(len(fol_exp.color_loc_predicates)):
            color = fol_exp.color_loc_predicates[i][0].split("color=")[1]
            direction = fol_exp.color_loc_predicates[i][1].split("loc=")[1]
            color = color[0].upper()

            if "top" in direction or "left" in direction:
                start = 0
                end = int(direction[-1])
                direction_type = direction[:-1]
                reverse = False
            else:
                start = len(grid[0]) - 1
                end = start - int(direction[-1])
                direction_type = direction[:-1]
                reverse = True

            all_check = True

            def check_cell(i, j):
                cell = grid[i][j] if direction_type in {"top", "bottom"} else grid[j][i]
                return str(cell[0]) == num and cell[2] == shape

            def color_match(i, j):
                cell = grid[i][j] if direction_type in {"top", "bottom"} else grid[j][i]
                return cell[1] == color

            # If within bound, then must match color
            index = start
            while (index <= end if not reverse else index >= end):
                for j in range(len(grid[0])):
                    if check_cell(index, j):
                        if not color_match(index, j):
                            all_check = False
                            break
                if not all_check:
                    break
                index = index + 1 if not reverse else index - 1

            # If out of bounds, then must not match shape+num
            while (index < len(grid) if direction_type in {"top", "bottom"} else index < len(grid[0])) if not reverse else index >= 0:
                for j in range(len(grid[0])):
                    if check_cell(index, j):
                        all_check = False
                        break
                if not all_check:
                    break
                index = index + 1 if not reverse else index - 1

            if all_check:
                new_exp = list(shape_num_exp)
                new_exp.append(fol_exp.color_loc_predicates[i])
                exp.append(tuple(new_exp))

    return exp

def medium2(grid, fol_exp):
    exp = list()

    for shape_num_exp in fol_exp.shape_num_exp:
        shape = shape_num_exp[1]
        num = shape_num_exp[2]

        if num not in {"even", "odd"}:
            continue

        shape = shape[0].upper()

        for i in range(len(fol_exp.color_loc_predicates)):
            color = fol_exp.color_loc_predicates[i][0].split("color=")[1]
            direction = fol_exp.color_loc_predicates[i][1].split("loc=")[1]
            color = color[0].upper()

            # Direction setup
            if "top" in direction or "left" in direction:
                start = 0
                end = int(direction[-1])
                direction_type = direction[:-1]
                reverse = False
            else:
                start = len(grid[0]) - 1
                end = start - int(direction[-1])
                direction_type = direction[:-1]
                reverse = True

            all_check = True

            def matches_parity_and_shape(i, j):
                cell = grid[i][j] if direction_type in {"top", "bottom"} else grid[j][i]
                val = int(cell[0])
                return (val % 2 == 0 if num == "even" else val % 2 == 1) and cell[2] == shape

            def color_match(i, j):
                cell = grid[i][j] if direction_type in {"top", "bottom"} else grid[j][i]
                return cell[1] == color

            # Check inside bounded region
            index = start
            while (index <= end if not reverse else index >= end):
                for j in range(len(grid[0])):
                    if matches_parity_and_shape(index, j) and not color_match(index, j):
                        all_check = False
                        break
                if not all_check:
                    break
                index = index + 1 if not reverse else index - 1

            # Check outside region for violations
            while (index < len(grid) if direction_type in {"top", "bottom"} else index < len(grid[0])) if not reverse else index >= 0:
                for j in range(len(grid[0])):
                    if matches_parity_and_shape(index, j):
                        all_check = False
                        break
                if not all_check:
                    break
                index = index + 1 if not reverse else index - 1

            if all_check:
                new_exp = list(shape_num_exp)
                new_exp.append(fol_exp.color_loc_predicates[i])
                exp.append(tuple(new_exp))

    return exp

def medium3(grid, fol_exp):
    exp = list()

    for shape_num_exp in fol_exp.min_max_exp:
        shape = shape_num_exp[1]
        raw_val = shape_num_exp[2]

        min_bool = raw_val.startswith("min=")
        val = int(raw_val.split("=")[1])

        shape = shape[0].upper()

        for i in range(len(fol_exp.color_loc_predicates)):
            color = fol_exp.color_loc_predicates[i][0].split("color=")[1][0].upper()
            direction = fol_exp.color_loc_predicates[i][1].split("loc=")[1]

            if "top" in direction or "left" in direction:
                index = 0
                limit = int(direction[-1])
                direction_type = direction[:-1]
                reverse = False
            else:
                index = len(grid[0]) - 1
                limit = index - int(direction[-1])
                direction_type = direction[:-1]
                reverse = True

            all_check = True

            def value_check(cell_val):
                return int(cell_val) >= val if min_bool else int(cell_val) <= val

            def is_matching_cell(i, j):
                cell = grid[i][j] if direction_type in {"top", "bottom"} else grid[j][i]
                return value_check(cell[0]) and cell[2] == shape

            def color_is_correct(i, j):
                cell = grid[i][j] if direction_type in {"top", "bottom"} else grid[j][i]
                return cell[1] == color

            # Check in-bounds region for implication condition
            while (index <= limit if not reverse else index >= limit):
                for j in range(len(grid[0])):
                    if is_matching_cell(index, j) and not color_is_correct(index, j):
                        all_check = False
                        break
                if not all_check:
                    break
                index = index + 1 if not reverse else index - 1

            # Check out of bounds for violations
            while (index < len(grid) if direction_type in {"top", "bottom"} else index < len(grid[0])) if not reverse else index >= 0:
                for j in range(len(grid[0])):
                    if is_matching_cell(index, j):
                        all_check = False
                        break
                if not all_check:
                    break
                index = index + 1 if not reverse else index - 1

            if all_check:
                new_exp = list(shape_num_exp)
                new_exp.append(fol_exp.color_loc_predicates[i])
                exp.append(tuple(new_exp))

    return exp

def hard1(grid, fol_exp):
    exp = list()

    for shape_color_exp in fol_exp.shape_color_exp:
        for predicate in fol_exp.hard_one:
            shape1 = shape_color_exp[1]
            color1 = shape_color_exp[2]
            shape2 = predicate[0]
            min_val = int(predicate[1].split("min=")[1])
            all_check = True

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

    print(exp)
    return exp

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

def hard4(grid, fol_exp):
    exp = list()

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
    """ Generates expressions given a grid
    
    Args:
        grid (list): the nxn list representation of the grid
    
    Returns:
        list: a 3-element list comprised of the easy, medium, and hard expressions
    """
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

def validate_expression(element, index):
    """ Helper function for check_expression() to validate an expression
    
    Args:
        element (str): 1 part of the expression (i.e., 'min=4')
        index (int): a counter to keep track of where you are within the entire expression
    
    Returns:
        bool: a boolean representing whether the element of the expression is valid
    """
    spatial_relations = {"RightOf", "LeftOf", "Above", "Below"}

    if index == 0:
        return element == "All"
    elif index == 1:
        return element in [
            "triangles", "squares", "circles",
            "red", "blue", "green",
            *map(str, range(10)), "even", "odd"
        ]
    elif index == 2:
        return element in [
            *map(str, range(10)),
            "even", "odd",
            *["min=" + str(i) for i in range(10)],
            *["max=" + str(i) for i in range(10)],
            "red", "blue", "green"
        ]
    elif index == 3:
        if isinstance(element, str):
            return False
        elif isinstance(element, tuple):
            if len(element) == 2:
                color, loc = element
                valid_colors = ["color=red", "color=blue", "color=green"]
                valid_locs = [
                    "loc=top2", "loc=top3", "loc=bottom2", "loc=bottom3",
                    "loc=left2", "loc=left3", "loc=right2", "loc=right3"
                ]
                return color in valid_colors and loc in valid_locs
            elif len(element) == 3:
                shape, constraint, direction = element
                valid_shapes = ["triangles", "squares", "circles"]
                valid_constraints = [
                    "min=" + str(i) for i in range(10)
                ] + ["max=" + str(i) for i in range(10)]
                return shape in valid_shapes and constraint in valid_constraints and direction in spatial_relations
    return True


def check_expressions(test_expression, expressions):
    """ The function responsible for checking if test_expression is in the set of generated expressions
    
    Args:
        test_expression (list): a valid expression to test against the set of expressions which is verified with validate_expression()
        expressions (list): the list of all expressions generated by generate_expressions()
    
    Returns:
        bool: a boolean representing whether the expression is part of the set of generated expressions
    """
    if len(test_expression) < 3:
        raise ValueError("Test expression does not meet minimum number of elements")
    if len(test_expression) > 4:
        raise ValueError("Test expression exceeds maximum expression size")
    if test_expression[0] != "All":
        raise ValueError("Test expression must begin with \"All\"")

    for idx, element in enumerate(test_expression):
        if not validate_expression(element, idx):
            raise ValueError(f"Invalid element at position {idx}: {element}")

    # Normalize number strings like '9' to match the types used in expressions
    normalized = list()
    for val in test_expression:
        if isinstance(val, str) and val.isdigit():
            normalized.append(str(int(val)))
        else:
            normalized.append(val)
    
    # Check for membership
    for difficulty in expressions:
        for subset in difficulty:
            if tuple(normalized) in subset:
                return True
    return False

def run_test():
    # Robustly test easy
    print("\n ===== EASY TEMPLATE ROBUSTNESS TEST =====")
    test_grid = [
        ['1GC', '1GC', '1GC', '1GC', '1GC'],
        ['1GC', '1GC', '1GC', '1GC', '1GC'],
        ['1GC', '1GC', '1GC', '1GC', '1GC'],
        ['1GC', '1GC', '1GC', '1GC', '1GC'],
        ['1GC', '1GC', '1GC', '1GC', '1GC']
    ]
    test_expressions = [
        (['Some', 'Apples', 'Are', 'Green'], False),
        (['All'], False),
        (['All', 'green', '3', ('color=green', 'loc=right2'), 'color=red', 'min=4', 'RightOf'], False),
        (['All', '1', 'shape=circle'], True),
        (['All', '1', 'color=green'], True),
        (['All', 'circles', 'color=green'], True),
        (['All', 'circles', 'num=1'], True),
        (['All', 'green', 'shape=circle'], True),
        (['All', 'green', 'num=1'], False),
        (['All', 'green', 'num=2'], False),
        (['All', 'squares', 'num=6'], True),
        (['All', 'odd', 'shape=circle'], True),
        (['All', 'triangles', '2', ('color=red', 'loc=left2')], True),
        (['All', 'circles', '1', ('color=green', 'loc=top3')], False)
    ]
    expressions = generate_expressions(test_grid)
    
    test_no = 1
    for test in test_expressions:
        print(f"Test #{test_no}: ", end="")
        try:
            if check_expressions(test[0], expressions) == test[1]:
                print("✅ PASSED!")
            else:
                print("❌ FAILED!")
        except ValueError:
            print("✅ PASSED!")
        test_no += 1
    
    # Robustly test medium
    print("\n ===== MEDIUM TEMPLATE ROBUSTNESS TEST =====")
    test_grid = [
        ['8RT', '7RT', '6RT', '5RT', '4RT'],
        ['8RT', '7RT', '6RT', '5RT', '4RT'],
        ['2GS', '2GS', '2GS', '2GS', '2GS'],
        ['1BC', '1BC', '1BC', '1BC', '1BC'],
        ['9BS', '9BS', '9BS', '9BS', '9BS'],
    ]
    test_expressions = [
        (['All', 'squares', '2', ('color=green', 'loc=top3')], True),
        (['All', 'triangles', '6', ('color=red', 'loc=top3')], True),
        (['All', 'circles', '1', ('color=blue', 'loc=bottom2')], True),
        (['All', 'squares', 'even', ('color=green', 'loc=top3')], True),
        (['All', 'circles', 'odd', ('color=blue', 'loc=bottom2')], True),
        (['All', 'triangles', 'min=6', ('color=red', 'loc=top2')], True),
        (['All', 'squares', 'max=2', ('color=green', 'loc=top3')], True),
        (['All', 'circles', 'even', ('color=green', 'loc=bottom3')], True),
        (['All', 'squares', 'odd', ('color=green', 'loc=top3')], False),
    ]
    expressions = generate_expressions(test_grid)
    
    test_no = 1
    for test in test_expressions:
        print(f"Test #{test_no}: ", end="")
        if check_expressions(test[0], expressions) == test[1]:
            print("✅ PASSED!")
        else:
            print("❌ FAILED!")
        test_no += 1
    
    test_grid = [
        ['1RC', '2RC', '3RC', '4RC', '5RC'],
        ['6RC', '7RC', '8RC', '9RC', '0RC'],
        ['1RC', '2RC', '3RC', '4RC', '5RC'],
        ['6RC', '7RC', '8RC', '9RC', '0RC'],
        ['1RC', '2RC', '3RC', '4RC', '5RC'],
    ]
    test_expressions = [
        (['All', 'circles', '5', ('color=green', 'loc=top2')], False),
        (['All', 'circles', 'even', ('color=green', 'loc=bottom3')], False),
        (['All', 'circles', 'odd', ('color=blue', 'loc=top3')], False),
        (['All', 'circles', 'min=8', ('color=blue', 'loc=top2')], False),
        (['All', 'circles', 'max=2', ('color=green', 'loc=bottom3')], False),
    ]
    expressions = generate_expressions(test_grid)
    for test in test_expressions:
        print(f"Test #{test_no}: ", end="")
        if check_expressions(test[0], expressions) == test[1]:
            print("✅ PASSED!")
        else:
            print("❌ FAILED!")
        test_no += 1
    
    # Robustly test hard
    print("\n ===== HARD TEMPLATE ROBUSTNESS TEST =====")
    test_grid = [
        ['9RC', '1GC', '2GC', '3GC', '4GC'],
        ['8RT', '0GT', '2GT', '4GT', '6GT'],
        ['7RS', '1GS', '3GS', '5GS', '7GS'],
        ['6RS', '2GS', '4GS', '6GS', '8GS'],
        ['5RC', '3GC', '5GC', '7GC', '9GC']
    ]
    test_expressions = [
        (['All', 'triangles', 'green', ('triangles', 'min=2', 'RightOf')], False),
        (['All', 'triangles', 'green', ('triangles', 'max=9', 'LeftOf')], True),
        (['All', 'squares', 'green', ('squares', 'min=1', 'Above')], False),
        (['All', 'squares', 'green', ('squares', 'max=8', 'Below')], False),
        (['All', 'circles', 'blue', ('triangles', 'min=9', 'RightOf')], True),
        (['All', 'squares', 'blue', ('circles', 'max=4', 'Below')], True),
        (['All', 'triangles', 'red', ('circles', 'max=0', 'LeftOf')], False),
        (['All', 'squares', 'green', ('squares', 'min=9', 'Above')], False),
        (['All', 'circles', 'red', ('triangles', 'min=9', 'RightOf')], False),
        (['All', 'triangles', 'red', ('circles', 'max=5', 'LeftOf')], False),
        (['All', 'circles', 'green', ('squares', 'min=9', 'Below')], False),
        (['All', 'squares', 'green', ('triangles', 'max=1', 'Above')], False)
    ]
    expressions = generate_expressions(test_grid)
    
    test_no = 1
    for test in test_expressions:
        print(f"Test #{test_no}: ", end="")
        result = check_expressions(test[0], expressions)
        if result == test[1]:
            print("✅ PASSED!")
        else:
            print("❌ FAILED!")
        test_no += 1


if __name__ == "__main__":
    # Driver
    size = int(input("Enter size of grid: "))
    grid = generate_grid(size)
    print_grid(grid, size=5)
    expressions = generate_expressions(grid)
    write_expressions(expressions)
    
    # TEST
    yes_run_test = str(input("Do you want to run tests (y/n)? "))
    if yes_run_test.lower() == 'y':
        run_test()
