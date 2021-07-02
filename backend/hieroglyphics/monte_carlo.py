# The shape of the maze.  Each character
# represents a different type of object
#   % - Wall
#   . - Food
#   o - Capsule
#   G - Ghost
#   P - Chomp
# Other characters are ignored


the_layout = [
  "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%",    
  "%.....%.................%.....%",
  "%o%%%.%.%%%.%%%%%%%.%%%.%.%%%o%",
  "%.%.....%......%......%.....%.%",
  "%...%%%.%.%%%%.%.%%%%.%.%%%...%",
  "%%%.%...%.%.........%.%...%.%%%",
  "%...%.%%%.%.%%% %%%.%.%%%.%...%",
  "%.%%%.......%GG GG%.......%%%.%",
  "%...%.%%%.%.%%%%%%%.%.%%%.%...%",
  "%%%.%...%.%.........%.%...%.%%%",
  "%...%%%.%.%%%%.%.%%%%.%.%%%...%",
  "%.%.....%......%......%.....%.%",
  "%o%%%.%.%%%.%%%%%%%.%%%.%.%%%o%",
  "%.....%........P........%.....%",
  "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"]

# what
class Immovable:
    def is_a_wall(self):
        return False
# what
class Nothing(Immovable):
    pass
# -(no window)-(play)-[]-(speed)-
class Maze:
    def __init__(self):
        self.have_window = False
        self.game_over = False
        self.set_layout(the_layout)
        set_speed(20)
    # -(layout)-l{}-(l*la)-l{-()->
    def set_layout(self, layout):
        height = len(layout)                   
        width = len(layout[0])                
        self.make_window(width, height)
        self.make_map(width, height)         
        max_y = height - 1
        # 
        for x in range( width ):     
            for y in range(height):
                char = layout[max_y - y][x]   
                self.make_object((x, y), char) 

    def make_window(self, width, height):
        grid_width = (width -1) * GRID_SIZE
        grid_height = (height - 1) * GRID_SIZE
        screen_width = 2 * MARGIN + grid_width
        screen_height = 2 *  MARGIN + grid_height
        begin_graphics(screen_width, screen_height,"Chomp",BACKGROUND_COLOR)

    def to_screen(self, point):
        (x,y) = point
        x = x * GRID_SIZE + MARGIN
        y = y * GRID_SIZE + MARGIN
        return(x,y)

    def make_map(self, width, height):
        self.width = width
        self.height = height
        self.map = []
        for y in range(width):
            new_row = []
            for x in range(width):
                new_row.append(Nothing())
            self.map.append(new_row)

    def make_object(self,point,charactor):
        (x,y) = point
        if charactor == "%":
            self.map[y][x] = Wall(self,point)

    def finished(self):
        return self.game_over

    def play(self):
        update_when('next_tick')

    def done(self):
        end_graphics()
        self.map = []

    def object_at(self,point):
        (x,y) = point
        if y < 0 or y >= self.height:
            return Nothing()
        if x < 0 or x >= self.width:
            return Nothing()
        return self.map[y][x]




class Wall(Immovable):
    def __init__(self, maze, point):
        self.place = point                          # Store our position
        self.screen_point = maze.to_screen(point)
        self.maze = maze                            # Keep hold of Maze
        self.draw()

    def draw(self):
        (screen_x, screen_y) = self.screen_point
        dot_size = GRID_SIZE * 0.2
        Circle(self.screen_point, dot_size,   
                color = WALL_COLOR, filled = 1)
        (x, y) = self.place
        neighbors = [ (x+1, y), (x-1, y)]
        for neighbor in neighbors:
            self.check_neighbor(neighbor)

    def check_neighbor(self,neighbor):
        maze = self.maze
        object = maze.object_at(neighbor)

        if object.is_a_wall():
            here = self.screen_point
            there = maze.to_screen(neighbor)
            Line(here, there, color = WALL_COLOR,thickness = 2)

    def is_a_wall(self):
        return True

the_maze = Maze()

while not the_maze.finished():
    the_maze.play()
    the_maze.done()