import tcod
from roguelike.map import Map
from roguelike.space import Space
from roguelike.player import Player
from roguelike.engine import Engine


def main():
    SCR_WIDTH = 20
    SCR_HEIGHT = 21
    
    tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    tcod.console_init_root(SCR_WIDTH, SCR_HEIGHT, 'My cool console.', order='F')
    tcod.console_set_default_foreground(0, tcod.yellow)
    print('Ready to make map.')
    lvl_map = Map(SCR_HEIGHT - 1, SCR_WIDTH)
    print('Ready to make player.')
    player = Player(*lvl_map.get_random_legal_space())
    print('Ready to print map to console.')
    for row in lvl_map.spaces:
        for space in row:
            tcod.console_put_char(0, space.x, space.y, space.terrain, tcod.BKGND_NONE)
    print('Ready to enter main loop.')
    while not tcod.console_is_window_closed():
        # print(f'Player at {player.loc}')
        tcod.console_put_char(0, player.x, player.y, player.symbol, tcod.BKGND_NONE)
        tcod.console_flush()
        kp = tcod.console_check_for_keypress()
        next_x_pos = player.x
        next_y_pos = player.y
        if kp.vk == tcod.KEY_ESCAPE:
            return True
        elif kp.vk == tcod.KEY_DOWN:
                next_y_pos += 1
        elif kp.vk == tcod.KEY_UP:
                next_y_pos -= 1
        elif kp.vk == tcod.KEY_RIGHT:
                next_x_pos += 1
        elif kp.vk == tcod.KEY_LEFT:
                next_x_pos -= 1
        # import pdb; pdb.set_trace()
        if lvl_map.space_is_legal(next_x_pos, next_y_pos):

            # Current position becomes next position
            player.move(next_x_pos, next_y_pos)
            # Print position at bottom of window
            tcod.console_print(0, 0, SCR_HEIGHT - 1, str(player.x).zfill(2) + ',' + str(player.y).zfill(2))
            # Draw terrain in space just vacated
            tcod.console_put_char(0, player.x_prev, player.y_prev, lvl_map.spaces[player.y_prev][player.x_prev].terrain, tcod.BKGND_NONE)
            # Set prev space to current
            player.x_prev, player.y_prev = player.x, player.y
            # show_neigbors(lvl_map, player)

def show_neigbors(lvl_map, player):
    if lvl_map.spaces[player.y][player.x].n:
        print(f'n={lvl_map.spaces[player.y][player.x].n.loc}')
    if lvl_map.spaces[player.y][player.x].e:
        print(f'e={lvl_map.spaces[player.y][player.x].e.loc}')
    if lvl_map.spaces[player.y][player.x].s:
        print(f's={lvl_map.spaces[player.y][player.x].s.loc}')
    if lvl_map.spaces[player.y][player.x].w:
        print(f'w={lvl_map.spaces[player.y][player.x].w.loc}')
    print('=' * 20)


if __name__ == '__main__':
    main()