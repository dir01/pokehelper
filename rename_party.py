# -*- coding: utf-8 -*-
from time import sleep
from pogo.pokedex import pokedex
from buddy_walk_distance import get_buddy_walk_distance_by_pokemon_id


def rename_party(session):
    for mon in sorted(session.inventory.party, key=lambda p: p.cp, reverse=True):
        name = pokedex[mon.pokemon_id]
        if mon.nickname:
            continue
        ivs = sum([mon.individual_attack, mon.individual_defense, mon.individual_stamina])
        nickname = '{}A{}D{}S{}{}'.format(
            ivs,
            mon.individual_attack,
            mon.individual_defense,
            mon.individual_stamina,
            get_buddy_walk_distance_by_pokemon_id(mon.pokemon_id)
        )
        print name, mon.cp, nickname
        sleep(5)
        print session.nicknamePokemon(mon, nickname)
