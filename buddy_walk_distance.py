# -*- coding: utf-8 -*-
from pogo.pokedex import pokedex


def get_buddy_walk_distance_by_pokemon_id(pokemon_id):
    return BUDDY_POKEMON_TO_KILOMETERS_MAP[pokemon_id]


BUDDY_POKEMON_TO_KILOMETERS_MAP = {
    pokedex.BULBASAUR: 3,
    pokedex.IVYSAUR: 3,
    pokedex.VENUSAUR: 3,
    pokedex.CHARMANDER: 3,
    pokedex.CHARMELEON: 3,
    pokedex.CHARIZARD: 3,
    pokedex.SQUIRTLE: 3,
    pokedex.WARTORTLE: 3,
    pokedex.BLASTOISE: 3,
    pokedex.CATERPIE: 1,
    pokedex.METAPOD: 1,
    pokedex.BUTTERFREE: 1,
    pokedex.WEEDLE: 1,
    pokedex.KAKUNA: 1,
    pokedex.BEEDRILL: 1,
    pokedex.PIDGEY: 1,
    pokedex.PIDGEOTTO: 1,
    pokedex.PIDGEOT: 1,
    pokedex.RATTATA: 1,
    pokedex.RATICATE: 1,
    pokedex.SPEAROW: 1,
    pokedex.FEAROW: 1,
    pokedex.EKANS: 3,
    pokedex.ARBOK: 3,
    pokedex.PIKACHU: 1,
    pokedex.RAICHU: 1,
    pokedex.SANDSHREW: 3,
    pokedex.SANDSLASH: 3,
    pokedex.NIDORAN_FEMALE: 3,
    pokedex.NIDORINA: 3,
    pokedex.NIDOQUEEN: 3,
    pokedex.NIDORAN_MALE: 3,
    pokedex.NIDORINO: 3,
    pokedex.NIDOKING: 3,
    pokedex.CLEFAIRY: 1,
    pokedex.CLEFABLE: 1,
    pokedex.VULPIX: 3,
    pokedex.NINETALES: 3,
    pokedex.JIGGLYPUFF: 1,
    pokedex.WIGGLYTUFF: 1,
    pokedex.ZUBAT: 1,
    pokedex.GOLBAT: 1,
    pokedex.ODDISH: 3,
    pokedex.GLOOM: 3,
    pokedex.VILEPLUME: 3,
    pokedex.PARAS: 3,
    pokedex.PARASECT: 3,
    pokedex.VENONAT: 3,
    pokedex.VENOMOTH: 3,
    pokedex.DIGLETT: 3,
    pokedex.DUGTRIO: 3,
    pokedex.MEOWTH: 3,
    pokedex.PERSIAN: 3,
    pokedex.PSYDUCK: 3,
    pokedex.GOLDUCK: 3,
    pokedex.MANKEY: 3,
    pokedex.PRIMEAPE: 3,
    pokedex.GROWLITHE: 3,
    pokedex.ARCANINE: 3,
    pokedex.POLIWAG: 3,
    pokedex.POLIWHIRL: 3,
    pokedex.POLIWRATH: 3,
    pokedex.ABRA: 3,
    pokedex.KADABRA: 3,
    pokedex.ALAKAZAM: 3,
    pokedex.MACHOP: 3,
    pokedex.MACHOKE: 3,
    pokedex.MACHAMP: 3,
    pokedex.BELLSPROUT: 3,
    pokedex.WEEPINBELL: 3,
    pokedex.VICTREEBEL: 3,
    pokedex.TENTACOOL: 3,
    pokedex.TENTACRUEL: 3,
    pokedex.GEODUDE: 1,
    pokedex.GRAVELER: 1,
    pokedex.GOLEM: 1,
    pokedex.PONYTA: 3,
    pokedex.RAPIDASH: 3,
    pokedex.SLOWPOKE: 3,
    pokedex.SLOWBRO: 3,
    pokedex.MAGNEMITE: 3,
    pokedex.MAGNETON: 3,
    pokedex.FARFETCHD: 3,
    pokedex.DODUO: 3,
    pokedex.DODRIO: 3,
    pokedex.SEEL: 3,
    pokedex.DEWGONG: 3,
    pokedex.GRIMER: 3,
    pokedex.MUK: 3,
    pokedex.SHELLDER: 3,
    pokedex.CLOYSTER: 3,
    pokedex.GASTLY: 3,
    pokedex.HAUNTER: 3,
    pokedex.GENGAR: 3,
    pokedex.ONIX: 5,
    pokedex.DROWZEE: 3,
    pokedex.HYPNO: 3,
    pokedex.KRABBY: 3,
    pokedex.KINGLER: 3,
    pokedex.VOLTORB: 3,
    pokedex.ELECTRODE: 3,
    pokedex.EXEGGCUTE: 3,
    pokedex.EXEGGUTOR: 3,
    pokedex.CUBONE: 3,
    pokedex.MAROWAK: 3,
    pokedex.HITMONLEE: 5,
    pokedex.HITMONCHAN: 5,
    pokedex.LICKITUNG: 3,
    pokedex.KOFFING: 3,
    pokedex.WEEZING: 3,
    pokedex.RHYHORN: 3,
    pokedex.RHYDON: 3,
    pokedex.CHANSEY: 5,
    pokedex.TANGELA: 3,
    pokedex.KANGASKHAN: 3,
    pokedex.HORSEA: 3,
    pokedex.SEADRA: 3,
    pokedex.GOLDEEN: 3,
    pokedex.SEAKING: 3,
    pokedex.STARYU: 3,
    pokedex.STARMIE: 3,
    pokedex.MR_MIME: 5,
    pokedex.SCYTHER: 5,
    pokedex.JYNX: 5,
    pokedex.ELECTABUZZ: 5,
    pokedex.MAGMAR: 5,
    pokedex.PINSIR: 5,
    pokedex.TAUROS: 3,
    pokedex.MAGIKARP: 1,
    pokedex.GYARADOS: 1,
    pokedex.LAPRAS: 5,
    pokedex.DITTO: 3,
    pokedex.EEVEE: 5,
    pokedex.VAPOREON: 5,
    pokedex.JOLTEON: 5,
    pokedex.FLAREON: 5,
    pokedex.PORYGON: 3,
    pokedex.OMANYTE: 5,
    pokedex.OMASTAR: 5,
    pokedex.KABUTO: 5,
    pokedex.KABUTOPS: 5,
    pokedex.AERODACTYL: 5,
    pokedex.SNORLAX: 5,
    pokedex.ARTICUNO: 5,
    pokedex.ZAPDOS: 5,
    pokedex.MOLTRES: 5,
    pokedex.DRATINI: 5,
    pokedex.DRAGONAIR: 5,
    pokedex.DRAGONITE: 5,
    pokedex.MEWTWO: 5,
    pokedex.MEW: 5,
}