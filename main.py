import tcod
from roguelike.map import Map
from roguelike.space import Space
from roguelike.player import Player
# from roguelike.engine import Engine

SCR_WIDTH = 20
SCR_HEIGHT = 21


def main():
    tcod.console_set_custom_font(
        'arial10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    tcod.console_init_root(SCR_WIDTH, SCR_HEIGHT,
                           'My cool console.', order="C")
    tcod.console_set_default_foreground(0, tcod.yellow)
    print('Ready to make map.')
    lvl_map = Map(SCR_HEIGHT - 1, SCR_WIDTH)
    print('Ready to make player.')
    player = Player(*lvl_map.get_random_legal_space())
    actors = [player]
    print('Ready to render map to console.')
    lvl_map.render()
    print('Ready to enter main loop.')
    # Enter main loop
    while not tcod.console_is_window_closed():
        # Pump events for keypress
        kp = tcod.console_check_for_keypress()
        if kp.vk == tcod.KEY_ESCAPE:
            return True
        # Get next actor in queue
        actor = actors.pop()
        # Move the actors
        actor.move(lvl_map, kp=kp)
        # Render the actors
        actor.render()


        actors.insert(0, actor)

        # Update the actor position
        update_position_display(player)
        tcod.console_flush()


def update_position_display(player):
    '''Print player position on last line of the console.'''
    tcod.console_set_default_foreground(0, tcod.green)
    tcod.console_print(
        0, 0, SCR_HEIGHT - 1, 'x=' + str(player.col).zfill(2) + ',y=' + str(SCR_HEIGHT - 1 - player.row).zfill(2))


if __name__ == '__main__':
    main()
