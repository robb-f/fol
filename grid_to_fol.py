import random

class FOL:
    def __init__(self, grid):
        self.quantifiers = ["All", "Some"]
        self.numbers = [str(i) for i in range(0, 10)]
        self.colors = ["red", "blue", "green"]
        self.shapes = ["triangles", "squares", "circles"]
        self.grid = grid
        
        self.color_shape_exp = list()
        
        for shape in self.shapes:
            for color in self.colors:
                color = color + " " + shape
                exp = (self.quantifiers[0], color)
                self.color_shape_exp.append(exp)
                exp = (self.quantifiers[1], color)
                self.color_shape_exp.append(exp)
        
        self.color_exp = list()
        for color in self.colors:
            color += " shapes"
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
            # TO-DO
            self.num_exp.append(1)
            
    def color_checker(self, grid):
        # run algorithm against grid and self.color_exp
        # returns all members in self.color_exp which are valid in grid

def generate_grid(size):
    """ Generates a grid by creating a size by size matrix using a list.
    
    Args:
        size (int): size of the square grid
    
    Returns:
        list: a matrix of dimensions size by size
    """
    numbers = [str(i) for i in range(0, 10)]     # 0-9
    colors = ["R", "B", "G"]                # Red, Blue, Green
    shape = ["T", "S", "C"]                 # Triangle, Square, Circle
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

def generate_expressions(grid):
    print("=*=*=*=*= generate_expressions =*=*=*=*=")
    fol_exp = FOL(grid)
    print("List of color_shape expressions:")
    print(fol_exp.color_shape_exp)
    print("List of color expressions:")
    print(fol_exp.color_exp)
    print("List of shape expressions:")
    print(fol_exp.shape_exp)

if __name__ == "__main__":
    size = int(input("Enter size of grid: "))
    grid = generate_grid(size)
    print_grid(grid, size)
    generate_expressions(grid)