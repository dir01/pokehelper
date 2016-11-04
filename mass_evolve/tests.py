# -*- coding: utf-8 -*-
from nose.tools import assert_equal

from mass_evolve.candy_calculator import get_evolution_advice


class TestCandyCalculator:
    def test_more_pokemons_than_candies(self):
        # Test pidgey without transfers
        # Transfer 7 Pidgey before activating your Lucky Egg.
        # You will begin evolving with 18 Pidgey and 200 Candy.
        # You will be able to evolve 18 Pidgey and earn 18,000XP.
        # You will have 0 Pidgeys and 2 Candy left over.
        # It should take approximately 7.2 minutes to evolve them all.
        # This will give you 22.8 minutes to spare.
        result = get_evolution_advice(
            candies_per_evolution=12,
            mons_count=25,
            candies_count=193,
        )
        assert_equal(7, result.transfers)
        assert_equal(18, result.evolved_mons_count)
        assert_equal(200, result.initial_candies_count)
        assert_equal(0, result.left_mons_count)
        assert_equal(2, result.left_candies_count)

    def test_more_candies_than_pokemons(self):
        # Transfer 0 Pidgey before activating your Lucky Egg.
        # You will begin evolving with 9 Pidgey and 665 Candy.
        # You will be able to evolve 9 Pidgey and earn 9,000XP.
        # You will be have transferred 0 Pidgeotto whilst evolving.
        # You will have 0 Pidgeys and 566 Candy left over.
        # It should take approximately 3.2 minutes to evolve them all.
        # This will give you 26.9 minutes to spare.

        result = get_evolution_advice(
            candies_per_evolution=12,
            mons_count=9,
            candies_count=665
        )
        assert_equal(0, result.transfers)
        assert_equal(9, result.evolved_mons_count)
        assert_equal(665, result.initial_candies_count)
        assert_equal(0, result.left_mons_count)
        assert_equal(566, result.left_candies_count)
