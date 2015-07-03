import libtcodpy as libtcod
from floor import Floor
from object import Object

#############################################
# Definitions
#############################################

# Actual size of the window
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

# Size of the map
MAP_WIDTH = 80
MAP_HEIGHT = 45

PLAYER_INDEX = 0

#############################################
# Handle Keys
#############################################

def handle_keys(player, map):
    global playerx, playery

    key = libtcod.console_wait_for_keypress(True)  #turn-based

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

    elif key.vk == libtcod.KEY_ESCAPE:
        return True  #exit game

    #movement keys
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        player.move(map, 0, -1)

    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        player.move(map, 0, 1)

    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        player.move(map, -1, 0)

    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        player.move(map, 1, 0)

#############################################
# Create the Map
#############################################
def make_map():
    global map

    # fill map with "unblocked" tiles
    map = [[ Floor(False)
        for y in range(MAP_HEIGHT) ]
            for x in range(MAP_WIDTH) ]

    # TEST CREATE PILLARS
    map[30][22].blocked = True
    map[30][22].block_sight = True
    map[50][22].blocked = True
    map[50][22].block_sight = True

#############################################
# Rendering Function
#############################################
def render_all(con):
    global color_light_wall
    global color_light_ground

    # Go through all the tiles and set their background color
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            wall = map[x][y].block_sight
            if wall:
                libtcod.console_set_char_background(con, x, y, color_dark_wall, libtcod.BKGND_SET )
            else:
                libtcod.console_set_char_background(con, x, y, color_dark_ground, libtcod.BKGND_SET )

    # Draw all objects
    for object in objects:
        object.draw(con)
    # Overlay the con over root
    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
#############################################
# Initialization & Main Loop
#############################################

libtcod.console_set_custom_font('./fonts/arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'roguey', False)
con = libtcod.console_new(SCREEN_WIDTH,SCREEN_HEIGHT)

# Initialize the player
player = Object(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, '@', libtcod.white)

# Initialize an NPC
npc = Object(SCREEN_WIDTH/2 - 5, SCREEN_HEIGHT/2, '@', libtcod.yellow)

# The list of all objects in the game
objects = [player, npc]

# Define the color of the wall and ground when they are hidden
color_dark_wall = libtcod.Color(0, 0, 100)
color_dark_ground = libtcod.Color(50, 50, 150)

# Make the map
make_map()

# The main iteration of the game.
while not libtcod.console_is_window_closed():

    # Write the the created console
    libtcod.console_set_default_foreground(con, libtcod.white)

    # Draw the objects
    render_all(con)

    # Display the contents of the console to the screen
    libtcod.console_flush()

    # Clear the objects so we don't have the same character printed again and again.
    for object in objects:
        object.clear(con)

    #Handle keys and exit game if needed
    exit = handle_keys(objects[0], map)
    if exit:
        break
