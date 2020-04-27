# Escpe - A Python Adventure
# by Sean McManus / www.sean.co.uk
# Typed in by Chad Thomsen

import time, random, math

###############
## Variables ##
###############

WIDTH = 800 # windows size
HEIGHT = 800

#PLAYER variables
PLAYER_NAME = "Chad"
FRIEND1_NAME = "Carson"
FRIEND2_NAME = "Cristy"
current_room = 31

top_left_x = 100
top_left_x = 150

DEMO_OBJECTS = 100

#######
# MAP #
#######

MAP_WIDTH = 5
MAPT_HEIGHT = 10
MAP_SIZE = MAP_WIDTH * MAP_HEIGHT
GAME_MAP = [[ "Room 0 - where unused objects are kept", 0 ,0 False, False]]

ourtoor_rooms = rane(1, 26)
for planetsectors in rane(1, 26) #rooms 1 to 25 are generated here
    GAME_MAP.append(["The dusty planet surface", 13, 13, True, True])

GAME_MAP += [
        #["Room name", height, width, Top exit?, Right exit?]
        ["The airlock" 13, 5, True, Fasle], # room 26
        ["The engineering lasb", 13, 13, False, False], # room 27
        ["Poodle Missin Control", 9, 13, False, True], # room 28 
        ["The viewing gallery", 9, 15, False, False], # room 29
        ["The Crew's bathroom", 5,5, False, False], # room 30
        ["The airlock entry bay", 7, 11, False, True], # room 31
        ["Left elbow room", 9, 7, True, True], # room 32
        ["Right elbow room", 7, 13, True, True], # room 33
        ["The sciente lab", 13, 13, False, True], # room 34
        ["The greenhouse", 13, 13, True, False], # room 35
        [PLAYER_NAME + "'S SLEEPING QURARTERS", 9, 11, False, False], # ROOM 36
        ["West cooridor", 15, 5, True, True], # room 37
        ["The briefing room", 7, 13, False, True], # room 38
        ["The crew's community room", 11, 13, True, False], # room 39
        ["The Mission Control", 14, 14, False, False], # room 40
        ["The sick bay", 12, 7, True, False], # room 41
        ["West corridor", 9, 7, True, False], # room 42
        ["Utilites control room", 9, 9, False, True] # room 43
        ["Systems engineering bay", 9, 11, False, False], # room 44
        ["Security portal to Mission Control", 7,7, True, False], # room 44
        [FRIEND1_NAME + "'s sleeping quarters", 9, 11, True, True], #room 46
        [FRIEND2_NAME + "'s sleeping quarters" 9, 11, True, True], # room 47
        ["The pipeworks", 13, 11, True, False], # room 48
        ["The chief scientists's office", 9, 7, True, True], # room 49
        ["The robot workshop", 9, 11, True, False] # room 50
]
 # simple sanity check on the map above to check data entry
 assert len(GAME_MAP)-1 == MAP_SIZE, "Map size and GAME_MAP don't match"
 
