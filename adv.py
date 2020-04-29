from room import Room
from player import Player
from world import World

from utils import Queue

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

explored_rooms = {}
opposite_cardinals = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}


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


def find_nearest_room_with_unexplored_paths(room_id):
    visited = set()
    queue = Queue()
    queue.enqueue([room_id])

    while queue.size() > 0:
        path = queue.dequeue()
        recent_room_id = path[-1]

        if recent_room_id in visited:
            continue

        visited.add(recent_room_id)
        recent_room = world.get_room_with_id(recent_room_id)
        unexplored_exits = recent_room.get_unexplored_exits(explored_rooms)
        if len(unexplored_exits) > 0:
            return path[1:]

        all_exits = recent_room.get_exits()
        for exit in all_exits:
            next_room = recent_room.get_room_in_direction(exit)
            path_copy = path.copy()
            path_copy.append(next_room.id)
            queue.enqueue(path_copy)

    return None


def convert_abs_to_rel(path):
    prev_id = None
    directions = []
    for id in path:
        if prev_id is None:
            prev_id = id
            continue
        prev_room = world.get_room_with_id(prev_id)
        direction = prev_room.direction_for_room(id)
        directions.append(direction)
        prev_id = id

    return directions


def travel_the_world(start_room):
    traveled = []
    room = start_room
    while len(explored_rooms) < len(room_graph):
        path = go_exploring(room)
        return_path = find_nearest_room_with_unexplored_paths(path[-1])
        if return_path is not None:
            room = world.get_room_with_id(return_path[-1])
            path.extend(return_path[:-1])
        traveled.extend(path)

    return traveled


traveled = travel_the_world(player.current_room)
traversal_path = convert_abs_to_rel(traveled)

# ===-==----------------------------------------------------------

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
