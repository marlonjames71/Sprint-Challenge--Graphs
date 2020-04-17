from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = ['n', 'n', 's', 's', 'w', 'w', 'e', 'e', 'e', 'e', 'w', 'w', 's', 's']

def bfs(starting_room):
    queue = Queue()
    queue.enqueue([starting_room.id])
    pass


def dft(room, visited=None):
    stack = Stack()
    stack.push(room.id)
    
    if visited is None:
        visited = {}
        # Base case: How do we know we're done?
        # We're done when the room has no exits
        
        # Track visited nodes
        visited[room.id] = {}
        
        # Call the function recursively - on rooms not visited
        for exit in room.get_exits():
            if exit not in visited:
                dft(exit, visited)





# current_room
prev_room = None
direction = None
reverse_direction = None

def traverse_map(world, current_room):
    
    
    
    while True:
        directions = player.get_exits()
        player.travel(directions[0])
    
    visited = {}
    path_of_room_ids = queue.dequeue()
    room_id = path_of_room_ids[-1]
    print('Path: ', path_of_room_ids)
    print("Node: ", room_id)
    
oposite_cardinals = { 'n': 's', 'w': 'e', 's': 'n', 'e': 'w' }

# PSEUDO CODE
# init
# get current room
# - room 0
# get the exits o fthe current room
# [n, s, w, e]

current_room = player.current_room
exits = player.current_room.get_exits()

# add current room init to visited
# should look like this -> {0: {n: ?, s: ?, w: ?, e: ?} }

def set_initial_cardinal_directions(room):
    exits = room.get_exits()
    cardinal_directions = {}
    for exit in exits:
        cardinal_directions[exit] = '?'
    return cardinal_directions

visited = {}

visited[current_room.id] = set_initial_cardinal_directions(current_room)

print(visited[current_room.id])

# initialize a stack
# -> 0 (room id) OR... <- This one probably won't work
# -> (direction = None, prev_room = None)
# add room 0 to the stack via Push

stack = Stack()
stack.push(direction=None, prev_room=None)

# start traversal in DFT mode
# room_info = pop -> (direction, previous)
room_info = stack.pop()
# current_room = current_room.id
# previous_room = room_info[1]
# direction = room_info[0]
# get the current room exits from visited

# check if current room isn't visited
# if not, then add to visited
# add to visited
# should look like this -> { current_room: {exits...?} }

# This should fail onthe first iteration because there is no previous room **
# if previous room is not None:
# this is where we update our previous room
# visited[previous_room][direction] = current_room


# This should fail on the first iteration because there is no direction **
# update current_room exits if we have a direction
# if direction is not None:
# visited[current_room][reverse_direction] = previous_room

# Loop over unvisited exits / or maybe all exits
    # move in that direction
    # Update traversal_path -> direction
    # update the stack -> (direction, current_room)
    
# if there are no exits that are unvisited
# enter into bft mode -> This will probably be a helper function


# bft will traverse over our visited graph
    # the destination is a room with a question mark
    # building a path to traverse after finding the destination <~~ ?


# traverse_map(world, player.current_room) ***



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")


