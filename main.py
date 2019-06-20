import tcod
from roguelike.map import Map


def main():
    SCR_WIDTH = 20
    SCR_HEIGHT = 20
    
    tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    tcod.console_init_root(SCR_WIDTH, SCR_HEIGHT, 'My cool console.', order='F')
    tcod.console_set_default_foreground(0, tcod.yellow)
    p_char = '@'
    x_pos, y_pos = 0, 0
    x_pos_prev, y_pos_prev = x_pos, y_pos
    
    lvl_map = Map(SCR_HEIGHT, SCR_WIDTH)
    tcod.console_print(0, 0, 0, ''.join([''.join(s) for s in lvl_map.grid]))
    while not tcod.console_is_window_closed():
        tcod.console_put_char(0, x_pos, y_pos, p_char, tcod.BKGND_NONE)
        tcod.console_flush()
        kp = tcod.console_check_for_keypress()

        if kp.vk == tcod.KEY_ESCAPE:
            return True
        elif kp.vk == tcod.KEY_DOWN:
            if y_pos < SCR_HEIGHT - 1:
                tcod.console_put_char(0, x_pos, y_pos, lvl_map.grid[x_pos_prev][y_pos_prev], tcod.BKGND_NONE)
                y_pos += 1
        elif kp.vk == tcod.KEY_UP:
            if y_pos > 0:
                tcod.console_put_char(0, x_pos, y_pos, lvl_map.grid[x_pos_prev][y_pos_prev], tcod.BKGND_NONE)
                y_pos -= 1
        elif kp.vk == tcod.KEY_RIGHT:
            if x_pos < SCR_WIDTH - 1:
                tcod.console_put_char(0, x_pos, y_pos, lvl_map.grid[x_pos_prev][y_pos_prev], tcod.BKGND_NONE)
                x_pos += 1
        elif kp.vk == tcod.KEY_LEFT:
            if x_pos > 0:
                tcod.console_put_char(0, x_pos, y_pos, lvl_map.grid[x_pos_prev][y_pos_prev], tcod.BKGND_NONE)
                x_pos -= 1
        tcod.console_put_char(0, 0, 25, x_pos, tcod.BKGND_NONE)
        tcod.console_put_char(0, 0, 26, y_pos, tcod.BKGND_NONE)
        if x_pos != x_pos_prev or y_pos != y_pos_prev:
            print(str(x_pos) + ',' + str(y_pos))
            x_pos_prev, y_pos_prev = x_pos, y_pos



if __name__ == '__main__':
    main()