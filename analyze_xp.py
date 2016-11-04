# -*- coding: utf-8 -*-
from collections import defaultdict
from pogo.pokedex import pokedex

from mass_evolve.candy_calculator import _CandyCalculator


def analyze_xp(session):
    species_counts = defaultdict(int)

    for pokemon in session.inventory.party:
        species_counts[pokemon.pokemon_id] += 1

    for species_id, pokemons_count in species_counts.iteritems():
        candies_count = session.inventory.candies.get(species_id)
        if not candies_count or not pokemons_count:
            continue
        species_name = pokedex[species_id]
        candies_per_evolution = pokedex.evolves[species_id]
        if not candies_per_evolution:
            continue
        advice = _CandyCalculator(
            candies_per_evolution=candies_per_evolution,
            candies_count=candies_count,
            mons_count=pokemons_count
        ).get_advice()
        if not advice.evolved_mons_count:
            continue
        seconds_spent = float(advice.evolved_mons_count) * 20
        minutes_spent = seconds_spent / 60
        time = (
            '{:.1f} MINUTES'.format(minutes_spent)
            if seconds_spent >= 60 else
            '{:.1f} seconds'.format(seconds_spent)
        )
        print "{species_name}: {advice.evolved_mons_count} in {time}".format(**locals())
