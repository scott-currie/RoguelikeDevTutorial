import tcod
from roguelike.map import Map
from roguelike.space import Space
from roguelike.player import Player
from roguelike.engine import Engine


def main():
    SCR_WIDTH = 20
    SCR_HEIGHT = 21

    tcod.console_set_custom_font(
        'arial10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    tcod.console_init_root(SCR_WIDTH, SCR_HEIGHT,
                           'My cool console.', order="C")
    tcod.console_set_default_foreground(0, tcod.yellow)
    print('Ready to make map.')
    lvl_map = Map(SCR_HEIGHT - 1, SCR_WIDTH)
    print('Ready to make player.')
    player = Player(*lvl_map.get_random_legal_space())
    print('Ready to print map to console.')
    # Print map to console
    for row in lvl_map.spaces:
        for space in row:
            tcod.console_put_char(0, space.col, space.row,
                                  space.terrain, tcod.BKGND_NONE)
    print('Ready to enter main loop.')
    # Enter main loop
    while not tcod.console_is_window_closed():
        tcod.console_put_char(0, player.col, player.row,
                              player.symbol, tcod.BKGND_NONE)
        kp = tcod.console_check_for_keypress()
        if kp.vk == tcod.KEY_ESCAPE:
            return True
        elif kp.vk == tcod.KEY_DOWN:
            player.row_next += 1
        elif kp.vk == tcod.KEY_UP:
            player.row_next -= 1
        elif kp.vk == tcod.KEY_RIGHT:
            player.col_next += 1
        elif kp.vk == tcod.KEY_LEFT:
            player.col_next -= 1
        # Do player move if next position dfferent than current
        if player.col_next != player.col or player.row_next != player.row:
            if lvl_map.space_is_legal(player.col_next, player.row_next):
                # Current position becomes next position
                player.move(player.row_next, player.col_next)
                # Print position at bottom of window
                tcod.console_print(
                    0, 0, SCR_HEIGHT - 1, 'row=' + str(player.row).zfill(2) + ',col=' + str(player.row).zfill(2))
                # show_neigbors(lvl_map, player)
                # Draw terrain in space just vacated
                tcod.console_put_char(0, player.col_prev, player.row_prev,
                                      lvl_map.spaces[player.row_prev][player.col_prev].terrain, tcod.BKGND_NONE)
                # Set prev space to current
                player.col_prev, player.row_prev = player.col, player.row
                # Set next space to current
                player.col_next, player.row_next = player.col, player.row
            else:
                print(f'Can\'t go to {player.row_next, player.col_next}')
        tcod.console_flush()


if __name__ == '__main__':
    main()
