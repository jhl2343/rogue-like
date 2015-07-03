import libtcodpy as libtcod
from object import Object

#############################################
# Definitions
#############################################

# Actual size of the window
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

PLAYER_INDEX = 0

#############################################
# Handle Keys
#############################################

def handle_keys():
    global playerx, playery

    key = libtcod.console_wait_for_keypress(True)  #turn-based

    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

    elif key.vk == libtcod.KEY_ESCAPE:
        return True  #exit game

    #movement keys
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        objects[PLAYER_INDEX].y -= 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        objects[PLAYER_INDEX].y += 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        objects[PLAYER_INDEX].x -= 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        objects[PLAYER_INDEX].x += 1


#############################################
# Initialization & Main Loop
#############################################

libtcod.console_set_custom_font('./fonts/arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'roguey', False)
con = libtcod.console_new(SCREEN_WIDTH,SCREEN_HEIGHT)

# Initialize the player
player = Object(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, '@', libtcod.white)
npc = Object(SCREEN_WIDTH/2 - 5, SCREEN_HEIGHT/2, '@', libtcod.yellow)

# The list of all objects in the game
objects = [player, npc]


# The main iteration of the game.
while not libtcod.console_is_window_closed():

    # Write the the created console
    libtcod.console_set_default_foreground(con, libtcod.white)

    # Draw the objects
    for object in objects:
        object.draw(con)

    # Overlay the con over root
    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)

    # Display the contents of the console to the screen
    libtcod.console_flush()

    # Clear the objects so we don't have the same character printed again and again.
    for object in objects:
        object.clear(con)

    #Handle keys and exit game if needed
    exit = handle_keys()
    if exit:
        break
