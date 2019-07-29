import logging
import tcod
from roguelike.actors import Actors
from roguelike.map import Map
from roguelike.space import Space
from roguelike.player import Player
from roguelike.monster import Monster
import time


SCR_WIDTH = 20
SCR_HEIGHT = 21
PLAYER_MAX_HP = 20
PLAYER_ATK = 2
MONSTER_MAX_HP = 20
MONSTER_ATK = 1

def main():
    logging.basicConfig(level=logging.DEBUG)
    tcod.console_set_custom_font(
        'arial10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    tcod.console_init_root(SCR_WIDTH, SCR_HEIGHT,
                           'My cool console.', order="C")
    tcod.console_set_default_foreground(0, tcod.yellow)
    logging.debug('Ready to make map.')
    lvl_map = Map(SCR_HEIGHT - 1, SCR_WIDTH)
    logging.debug('Ready to make player.')
    player = Player(*lvl_map.get_random_legal_space(), PLAYER_ATK, PLAYER_MAX_HP)
    monster = Monster(*lvl_map.get_random_legal_space(), MONSTER_ATK, MONSTER_MAX_HP)
    actors = Actors()
    actors.player = player
    actors.queue = [player, monster]
    logging.debug('Ready to render map to console.')
    lvl_map.render()
    logging.debug('Ready to enter main loop.')
    next_actor = True
    # Enter main loop
    while not tcod.console_is_window_closed():
        # Pump events for keypress
        kp = tcod.console_check_for_keypress()
        if kp.vk == tcod.KEY_ESCAPE:
            return True
        # Get next actor from the queue if we're ready
        if next_actor:
            actor = actors.queue.pop()
            next_actor = False
        # Update the actor
        actor.update(kp, lvl_map, actors)
        # logging.debug(f'{actor} acted = {actor.acted}')
        if actor.acted:
            # logging.debug(f'{actor} has acted.')
            next_actor = True
            # Put old actor back in the queue
            actors.queue.insert(0, actor)
        # Update the player position
        update_position_display(player)
        tcod.console_flush()


def update_position_display(player):
    '''Print player position on last line of the console.'''
    tcod.console_set_default_foreground(0, tcod.green)
    tcod.console_print(
        0, 0, SCR_HEIGHT - 1, 'x=' + str(player.col).zfill(2) + ',y=' + str(SCR_HEIGHT - 1 - player.row).zfill(2))


if __name__ == '__main__':
    main()
