# -*- coding: utf-8 -*-
from collections import namedtuple


def get_evolution_advice(candies_per_evolution, mons_count, candies_count):
    """ :rtype:EvolutionAdvice """
    return _CandyCalculator(candies_per_evolution, mons_count, candies_count).get_advice()


class _CandyCalculator(object):
    def __init__(self, candies_per_evolution, mons_count, candies_count):
        self.candies_per_evolution = candies_per_evolution
        self.mons_count = mons_count
        self.initial_mons_count = mons_count
        self.candies_count = candies_count

        self.initial_candies_count = self.candies_count
        self.evolved_count = 0
        self.transferred_count = 0

    def get_advice(self):
        """ :rtype:EvolutionAdvice """
        while self.is_enough_mons() and self.is_enough_candy():
            self.evolve()
            self.transfer()
        return EvolutionAdvice(
            transfers=self.transferred_count,
            initial_mons_count=self.initial_mons_count - self.transferred_count,
            initial_candies_count=self.initial_candies_count + self.transferred_count,
            evolved_mons_count=self.evolved_count,
            left_mons_count=self.mons_count,
            left_candies_count=self.candies_count,
        )

    def is_enough_mons(self):
        return self.mons_count > 0

    def is_enough_candy(self):
        return self.candies_count >= self.candies_per_evolution

    def evolve(self):
        if not self.mons_count or self.candies_count < self.candies_per_evolution:
            return 0
        potential_evolves_count = self.candies_count / self.candies_per_evolution
        evolved_count = min([self.mons_count, potential_evolves_count])
        self.candies_count -= evolved_count * self.candies_per_evolution
        self.candies_count += evolved_count
        self.mons_count -= evolved_count
        self.evolved_count += evolved_count
        evolved_count += self.evolve()
        return evolved_count

    def transfer(self):
        if self.mons_count <= 1:
            return
        if (self.mons_count - 1 + self.candies_count) >= self.candies_per_evolution:
            to_transfer = self.mons_count - 1
            self.mons_count -= to_transfer
            self.candies_count += to_transfer
            self.transferred_count += to_transfer


EvolutionAdvice = namedtuple(
    'EvolutionAdvise',
    'transfers '
    'initial_mons_count '
    'initial_candies_count '
    'evolved_mons_count '
    'left_mons_count '
    'left_candies_count '
)
