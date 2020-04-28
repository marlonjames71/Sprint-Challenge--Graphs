from room import Room
from player import Player
from world import World

from utils import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


def process_raw_room_graph(room_graph):
    rooms = {}
    for raw_room_id in room_graph:
        room = Room('', '', raw_room_id)
        rooms[raw_room_id] = room
    return rooms


explored_rooms = {}
opposite_cardinals = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
traveled = []


def add_room_to_explored(room):
    if room.id in explored_rooms:
        return
    connected_rooms = {}
    for exit in room.get_exits():
        connected_rooms[exit] = None

    explored_rooms[room.id] = connected_rooms


add_room_to_explored(player.current_room)


def wander_single_room(room):
    add_room_to_explored(room)

    valid_exits = room.get_unexplored_exits(explored_rooms)
    if len(valid_exits) == 0:
        return None

    direction = random.choice(valid_exits)
    next_room = room.get_room_in_direction(direction)
    add_room_to_explored(next_room)
    explored_rooms[room.id][direction] = next_room.id
    opposite_direction = opposite_cardinals[direction]
    explored_rooms[next_room.id][opposite_direction] = room.id
    return next_room


def go_exploring(room):
    path = []
    next_room = room
    while next_room is not None:
        path.append(next_room.id)
        next_room = wander_single_room(next_room)

    return path


def find_nearest_room_with_unexplored_paths(room):
    # return something or nothing depending on what it finds
    pass


go_exploring(player.current_room)


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
