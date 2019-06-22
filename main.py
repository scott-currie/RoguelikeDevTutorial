import tcod
from roguelike.map.map import Map


def main():
    SCR_WIDTH = 20
    SCR_HEIGHT = 21
    
    tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    tcod.console_init_root(SCR_WIDTH, SCR_HEIGHT, 'My cool console.', order='F')
    tcod.console_set_default_foreground(0, tcod.yellow)
    
    lvl_map = Map(SCR_HEIGHT - 1, SCR_WIDTH)
    
    p_char = '@'
    for y, row in enumerate(lvl_map.terrain):
        for x, col in enumerate(row):
            if col == '.':
                x_pos, y_pos = x, y
                break
    x_pos_prev, y_pos_prev = -1, -1
    

    tcod.console_print(0, 0, 0, ''.join([''.join(s) + '\n' for s in lvl_map.terrain]))
    while not tcod.console_is_window_closed():
        tcod.console_put_char(0, x_pos, y_pos, p_char, tcod.BKGND_NONE)
        tcod.console_flush()
        kp = tcod.console_check_for_keypress()
        next_x_pos = x_pos
        next_y_pos = y_pos
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
        if lvl_map.space_is_legal(next_x_pos, next_y_pos):
            # Current position becomes next position
            x_pos, y_pos = next_x_pos, next_y_pos
            # Print position at bottom of window
            tcod.console_print(0, 0, SCR_HEIGHT - 1, str(x_pos).zfill(2) + ',' + str(y_pos).zfill(2))
            # Draw terrain in space just left
            tcod.console_put_char(0, x_pos_prev, y_pos_prev, lvl_map.terrain[y_pos_prev][x_pos_prev], tcod.BKGND_NONE)
            # Set prev space to current
            x_pos_prev, y_pos_prev = x_pos, y_pos



if __name__ == '__main__':
    main()