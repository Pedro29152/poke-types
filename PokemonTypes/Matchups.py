from .PokemonTypes import Types
from .Matchup import Matchup
from .MatchupList import MatchupList

ZERO = 0
HALF = 1/2
DOUBLE = 2

def baseMatchup(matchupsList = None):
    ret = MatchupList()

    if matchupsList:
        for item in matchupsList:
            ret[item['type']] = item['multiplier']
    
    return ret
    
class Matchups:
    #region TypeMatchups

    #NORMAL
    normalAttack = [
        {'type': Types.Ghost, 'multiplier': ZERO},
        {'type': Types.Steel, 'multiplier': HALF},
        {'type': Types.Rock, 'multiplier': HALF}
    ]
    normalDefence = [
        {'type': Types.Ghost, 'multiplier': ZERO},
        {'type': Types.Fighting, 'multiplier': DOUBLE}
    ]

    #FIGHTING
    fightingAttack = [
        {'type': Types.Normal, 'multiplier': DOUBLE},
        {'type': Types.Flying, 'multiplier': HALF},
        {'type': Types.Poison, 'multiplier': HALF},
        {'type': Types.Rock, 'multiplier': DOUBLE},
        {'type': Types.Bug, 'multiplier': HALF},
        {'type': Types.Ghost, 'multiplier': ZERO},
        {'type': Types.Steel, 'multiplier': DOUBLE},
        {'type': Types.Psychic, 'multiplier': HALF},
        {'type': Types.Ice, 'multiplier': DOUBLE},
        {'type': Types.Dark, 'multiplier': DOUBLE},
        {'type': Types.Fairy, 'multiplier': HALF}
    ]
    fightingDefence = [
        {'type': Types.Flying, 'multiplier': DOUBLE},
        {'type': Types.Rock, 'multiplier': HALF},
        {'type': Types.Bug, 'multiplier': HALF},
        {'type': Types.Psychic, 'multiplier': DOUBLE},
        {'type': Types.Dark, 'multiplier': HALF},
        {'type': Types.Fairy, 'multiplier': DOUBLE}
    ]

    #FLYING
    flyingAttack = [
        {'type': Types.Fighting, 'multiplier': DOUBLE},
        {'type': Types.Rock, 'multiplier': HALF},
        {'type': Types.Bug, 'multiplier': DOUBLE},
        {'type': Types.Steel, 'multiplier': HALF},
        {'type': Types.Grass, 'multiplier': DOUBLE},
        {'type': Types.Electric, 'multiplier': HALF}
    ]
    flyingDefence = [
        {'type': Types.Fighting, 'multiplier': HALF},
        {'type': Types.Ground, 'multiplier': ZERO},
        {'type': Types.Rock, 'multiplier': DOUBLE},
        {'type': Types.Bug, 'multiplier': HALF},
        {'type': Types.Grass, 'multiplier': HALF},
        {'type': Types.Electric, 'multiplier': DOUBLE},
        {'type': Types.Ice, 'multiplier': DOUBLE}
    ]

    #POISON
    poisonAttack = [
        {'type': Types.Poison, 'multiplier': HALF},
        {'type': Types.Ground, 'multiplier': HALF},
        {'type': Types.Rock, 'multiplier': HALF},
        {'type': Types.Ghost, 'multiplier': HALF},
        {'type': Types.Steel, 'multiplier': ZERO},
        {'type': Types.Grass, 'multiplier': DOUBLE},
        {'type': Types.Fairy, 'multiplier': DOUBLE},
    ]
    poisonDefence = [
        {'type': Types.Fighting, 'multiplier': HALF},
        {'type': Types.Poison, 'multiplier': HALF},
        {'type': Types.Ground, 'multiplier': DOUBLE},
        {'type': Types.Bug, 'multiplier': HALF},
        {'type': Types.Grass, 'multiplier': HALF},
        {'type': Types.Psychic, 'multiplier': DOUBLE},
        {'type': Types.Fairy, 'multiplier': HALF},
    ]

    #GROUND
    groundAttack = [
        {'type': Types.Flying, 'multiplier': ZERO},
        {'type': Types.Poison, 'multiplier': DOUBLE},
        {'type': Types.Rock, 'multiplier': DOUBLE},
        {'type': Types.Bug, 'multiplier': HALF},
        {'type': Types.Steel, 'multiplier': DOUBLE},
        {'type': Types.Fire, 'multiplier': DOUBLE},
        {'type': Types.Grass, 'multiplier': HALF},
        {'type': Types.Electric, 'multiplier': DOUBLE}
    ]
    groundDefence = [
        {'type': Types.Poison, 'multiplier': HALF},
        {'type': Types.Rock, 'multiplier': HALF},
        {'type': Types.Water, 'multiplier': DOUBLE},
        {'type': Types.Grass, 'multiplier': DOUBLE},
        {'type': Types.Electric, 'multiplier': ZERO},
        {'type': Types.Ice, 'multiplier': DOUBLE}
    ]

    #ROCK
    rockAttack = [
        {'type': Types.Fighting, 'multiplier': HALF},
        {'type': Types.Flying, 'multiplier': DOUBLE},
        {'type': Types.Ground, 'multiplier': HALF},
        {'type': Types.Bug, 'multiplier': DOUBLE},
        {'type': Types.Steel, 'multiplier': HALF},
        {'type': Types.Fire, 'multiplier': DOUBLE},
        {'type': Types.Ice, 'multiplier': DOUBLE}
    ]
    rockDefence = [
        {'type': Types.Normal, 'multiplier': HALF},
        {'type': Types.Fighting, 'multiplier': DOUBLE},
        {'type': Types.Flying, 'multiplier': HALF},
        {'type': Types.Poison, 'multiplier': HALF},
        {'type': Types.Ground, 'multiplier': DOUBLE},
        {'type': Types.Steel, 'multiplier': DOUBLE},
        {'type': Types.Fire, 'multiplier': HALF},
        {'type': Types.Water, 'multiplier': DOUBLE},
        {'type': Types.Grass, 'multiplier': DOUBLE}
    ]

    #BUG
    bugAttack = [
        {'type': Types.Fighting, 'multiplier': HALF},
        {'type': Types.Flying, 'multiplier': HALF},
        {'type': Types.Poison, 'multiplier': HALF},
        {'type': Types.Ghost, 'multiplier': HALF},
        {'type': Types.Steel, 'multiplier': HALF},
        {'type': Types.Fire, 'multiplier': HALF},
        {'type': Types.Grass, 'multiplier': DOUBLE},
        {'type': Types.Psychic, 'multiplier': DOUBLE},
        {'type': Types.Dark, 'multiplier': DOUBLE},
        {'type': Types.Fairy, 'multiplier': HALF}
    ]
    bugDefence = [
        {'type': Types.Fighting, 'multiplier': HALF},
        {'type': Types.Flying, 'multiplier': DOUBLE},
        {'type': Types.Ground, 'multiplier': HALF},
        {'type': Types.Rock, 'multiplier': DOUBLE},
        {'type': Types.Fire, 'multiplier': DOUBLE},
        {'type': Types.Grass, 'multiplier': HALF}
    ]

    #GHOST
    ghostAttack = [
        {'type': Types.Normal, 'multiplier': ZERO},
        {'type': Types.Ghost, 'multiplier': DOUBLE},
        {'type': Types.Psychic, 'multiplier': DOUBLE},
        {'type': Types.Dark, 'multiplier': HALF}
    ]
    ghostDefence = [
        {'type': Types.Normal, 'multiplier': ZERO},
        {'type': Types.Fighting, 'multiplier': ZERO},
        {'type': Types.Poison, 'multiplier': HALF},
        {'type': Types.Bug, 'multiplier': HALF},
        {'type': Types.Ghost, 'multiplier': DOUBLE},
        {'type': Types.Dark, 'multiplier': DOUBLE}
    ]

    #STEEL
    steelAttack = [
        {'type': Types.Rock, 'multiplier': DOUBLE},
        {'type': Types.Steel, 'multiplier': HALF},
        {'type': Types.Fire, 'multiplier': HALF},
        {'type': Types.Water, 'multiplier': HALF},
        {'type': Types.Electric, 'multiplier': HALF},
        {'type': Types.Ice, 'multiplier': DOUBLE},
        {'type': Types.Fairy, 'multiplier': DOUBLE}
    ]
    steelDefence = [
        {'type': Types.Normal, 'multiplier': HALF},
        {'type': Types.Fighting, 'multiplier': DOUBLE},
        {'type': Types.Flying, 'multiplier': HALF},
        {'type': Types.Poison, 'multiplier': ZERO},
        {'type': Types.Ground, 'multiplier': DOUBLE},
        {'type': Types.Rock, 'multiplier': HALF},
        {'type': Types.Bug, 'multiplier': HALF},
        {'type': Types.Steel, 'multiplier': HALF},
        {'type': Types.Fire, 'multiplier': DOUBLE},
        {'type': Types.Grass, 'multiplier': HALF},
        {'type': Types.Psychic, 'multiplier': HALF},
        {'type': Types.Ice, 'multiplier': HALF},
        {'type': Types.Dragon, 'multiplier': HALF},
        {'type': Types.Fairy, 'multiplier': HALF},
    ]

    #FIRE
    fireAttack = [
        {'type': Types.Rock, 'multiplier': HALF},
        {'type': Types.Bug, 'multiplier': DOUBLE},
        {'type': Types.Steel, 'multiplier': DOUBLE},
        {'type': Types.Fire, 'multiplier': HALF},
        {'type': Types.Water, 'multiplier': HALF},
        {'type': Types.Grass, 'multiplier': DOUBLE},
        {'type': Types.Ice, 'multiplier': DOUBLE},
        {'type': Types.Dragon, 'multiplier': HALF}
    ]
    fireDefence = [
        {'type': Types.Ground, 'multiplier': DOUBLE},
        {'type': Types.Rock, 'multiplier': DOUBLE},
        {'type': Types.Bug, 'multiplier': HALF},
        {'type': Types.Steel, 'multiplier': HALF},
        {'type': Types.Fire, 'multiplier': HALF},
        {'type': Types.Water, 'multiplier': DOUBLE},
        {'type': Types.Grass, 'multiplier': HALF},
        {'type': Types.Ice, 'multiplier': HALF},
        {'type': Types.Fairy, 'multiplier': HALF}
    ]

    #WATER
    waterAttack = [
        {'type': Types.Ground, 'multiplier': DOUBLE},
        {'type': Types.Rock, 'multiplier': DOUBLE},
        {'type': Types.Fire, 'multiplier': DOUBLE},
        {'type': Types.Water, 'multiplier': HALF},
        {'type': Types.Grass, 'multiplier': HALF},
        {'type': Types.Dragon, 'multiplier': HALF}
    ]
    waterDefence = [
        {'type': Types.Steel, 'multiplier': HALF},
        {'type': Types.Fire, 'multiplier': HALF},
        {'type': Types.Water, 'multiplier': HALF},
        {'type': Types.Grass, 'multiplier': DOUBLE},
        {'type': Types.Electric, 'multiplier': DOUBLE},
        {'type': Types.Ice, 'multiplier': HALF}
    ]

    #GRASS
    grassAttack = [
        {'type': Types.Flying, 'multiplier': HALF},
        {'type': Types.Poison, 'multiplier': HALF},
        {'type': Types.Ground, 'multiplier': DOUBLE},
        {'type': Types.Rock, 'multiplier': DOUBLE},
        {'type': Types.Bug, 'multiplier': HALF},
        {'type': Types.Steel, 'multiplier': HALF},
        {'type': Types.Fire, 'multiplier': HALF},
        {'type': Types.Water, 'multiplier': DOUBLE},
        {'type': Types.Grass, 'multiplier': HALF},
        {'type': Types.Dragon, 'multiplier': HALF}
    ]
    grassDefence = [
        {'type': Types.Flying, 'multiplier': DOUBLE},
        {'type': Types.Poison, 'multiplier': DOUBLE},
        {'type': Types.Ground, 'multiplier': HALF},
        {'type': Types.Bug, 'multiplier': DOUBLE},
        {'type': Types.Fire, 'multiplier': DOUBLE},
        {'type': Types.Water, 'multiplier': HALF},
        {'type': Types.Grass, 'multiplier': HALF},
        {'type': Types.Electric, 'multiplier': HALF},
        {'type': Types.Ice, 'multiplier': DOUBLE}
    ]

    #ELECTRIC
    electricAttack = [
        {'type': Types.Flying, 'multiplier': DOUBLE},
        {'type': Types.Ground, 'multiplier': ZERO},
        {'type': Types.Water, 'multiplier': DOUBLE},
        {'type': Types.Grass, 'multiplier': HALF},
        {'type': Types.Electric, 'multiplier': HALF},
        {'type': Types.Dragon, 'multiplier': HALF}
    ]
    electricDefence = [
        {'type': Types.Flying, 'multiplier': HALF},
        {'type': Types.Ground, 'multiplier': DOUBLE},
        {'type': Types.Steel, 'multiplier': HALF},
        {'type': Types.Electric, 'multiplier': HALF}
    ]

    #PSYCHIC
    psychicAttack = [
        {'type': Types.Fighting, 'multiplier': DOUBLE},
        {'type': Types.Poison, 'multiplier': DOUBLE},
        {'type': Types.Steel, 'multiplier': HALF},
        {'type': Types.Psychic, 'multiplier': HALF},
        {'type': Types.Dark, 'multiplier': ZERO}
    ]
    psychicDefence = [
        {'type': Types.Fighting, 'multiplier': HALF},
        {'type': Types.Bug, 'multiplier': DOUBLE},
        {'type': Types.Ghost, 'multiplier': DOUBLE},
        {'type': Types.Electric, 'multiplier': HALF},
        {'type': Types.Dark, 'multiplier': DOUBLE}
    ]

    #ICE
    iceAttack = [
        {'type': Types.Flying, 'multiplier': DOUBLE},
        {'type': Types.Ground, 'multiplier': DOUBLE},
        {'type': Types.Steel, 'multiplier': HALF},
        {'type': Types.Fire, 'multiplier': HALF},
        {'type': Types.Water, 'multiplier': HALF},
        {'type': Types.Grass, 'multiplier': DOUBLE},
        {'type': Types.Ice, 'multiplier': HALF},
        {'type': Types.Dragon, 'multiplier': DOUBLE}
    ]
    iceDefence = [
        {'type': Types.Fighting, 'multiplier': DOUBLE},
        {'type': Types.Rock, 'multiplier': DOUBLE},
        {'type': Types.Steel, 'multiplier': DOUBLE},
        {'type': Types.Fire, 'multiplier': DOUBLE},
        {'type': Types.Ice, 'multiplier': HALF}
    ]

    #DRAGON
    dragonAttack = [
        {'type': Types.Steel, 'multiplier': HALF},
        {'type': Types.Dragon, 'multiplier': DOUBLE},
        {'type': Types.Fairy, 'multiplier': ZERO}
    ]
    dragonDefence = [
        {'type': Types.Fire, 'multiplier': HALF},
        {'type': Types.Water, 'multiplier': HALF},
        {'type': Types.Grass, 'multiplier': HALF},
        {'type': Types.Electric, 'multiplier': HALF},
        {'type': Types.Ice, 'multiplier': DOUBLE},
        {'type': Types.Dragon, 'multiplier': DOUBLE},
        {'type': Types.Fairy, 'multiplier': DOUBLE}
    ]

    #DARK
    darkAttack = [
        {'type': Types.Fighting, 'multiplier': HALF},
        {'type': Types.Ghost, 'multiplier': DOUBLE},
        {'type': Types.Psychic, 'multiplier': DOUBLE},
        {'type': Types.Dark, 'multiplier': HALF},
        {'type': Types.Fairy, 'multiplier': HALF}
    ]
    darkDefence = [
        {'type': Types.Fighting, 'multiplier': DOUBLE},
        {'type': Types.Bug, 'multiplier': DOUBLE},
        {'type': Types.Ghost, 'multiplier': HALF},
        {'type': Types.Psychic, 'multiplier': ZERO},
        {'type': Types.Dark, 'multiplier': HALF},
        {'type': Types.Fairy, 'multiplier': DOUBLE}
    ]

    #FAIRY
    fairyAttack = [
        {'type': Types.Fighting, 'multiplier': DOUBLE},
        {'type': Types.Poison, 'multiplier': HALF},
        {'type': Types.Steel, 'multiplier': HALF},
        {'type': Types.Fire, 'multiplier': HALF},
        {'type': Types.Dragon, 'multiplier': DOUBLE},
        {'type': Types.Dark, 'multiplier': DOUBLE}
    ]
    fairyDefence = [
        {'type': Types.Fighting, 'multiplier': HALF},
        {'type': Types.Poison, 'multiplier': DOUBLE},
        {'type': Types.Bug, 'multiplier': HALF},
        {'type': Types.Steel, 'multiplier': DOUBLE},
        {'type': Types.Dragon, 'multiplier': ZERO},
        {'type': Types.Dark, 'multiplier': HALF}
    ]

    #endregion

    def getMatchups(self):
        ret = (Types.max() + 1) * [None]

        ret[Types.Normal.value] = Matchup(
            Types.Normal,
            baseMatchup(self.normalDefence),
            baseMatchup(self.normalAttack)
        )
        ret[Types.Fighting.value] = Matchup(
            Types.Fighting,
            baseMatchup(self.fightingDefence),
            baseMatchup(self.fightingAttack)
        )
        ret[Types.Flying.value] = Matchup(
            Types.Flying,
            baseMatchup(self.flyingDefence),
            baseMatchup(self.flyingAttack)
        )
        ret[Types.Poison.value] = Matchup(
            Types.Poison,
            baseMatchup(self.poisonDefence),
            baseMatchup(self.poisonAttack)
        )
        ret[Types.Ground.value] = Matchup(
            Types.Ground,
            baseMatchup(self.groundDefence),
            baseMatchup(self.groundAttack)
        )
        ret[Types.Rock.value] = Matchup(
            Types.Rock,
            baseMatchup(self.rockDefence),
            baseMatchup(self.rockAttack)
        )
        ret[Types.Bug.value] = Matchup(
            Types.Bug,
            baseMatchup(self.bugDefence),
            baseMatchup(self.bugAttack)
        )
        ret[Types.Ghost.value] = Matchup(
            Types.Ghost,
            baseMatchup(self.ghostDefence),
            baseMatchup(self.ghostAttack)
        )
        ret[Types.Steel.value] = Matchup(
            Types.Steel,
            baseMatchup(self.steelDefence),
            baseMatchup(self.steelAttack)
        )
        ret[Types.Fire.value] = Matchup(
            Types.Fire,
            baseMatchup(self.fireDefence),
            baseMatchup(self.fireAttack)
        )
        ret[Types.Water.value] = Matchup(
            Types.Water,
            baseMatchup(self.waterDefence),
            baseMatchup(self.waterAttack)
        )
        ret[Types.Grass.value] = Matchup(
            Types.Grass,
            baseMatchup(self.grassDefence),
            baseMatchup(self.grassAttack)
        )
        ret[Types.Electric.value] = Matchup(
            Types.Electric,
            baseMatchup(self.electricDefence),
            baseMatchup(self.electricAttack)
        )
        ret[Types.Psychic.value] = Matchup(
            Types.Psychic,
            baseMatchup(self.psychicDefence),
            baseMatchup(self.psychicAttack)
        )
        ret[Types.Ice.value] = Matchup(
            Types.Ice,
            baseMatchup(self.iceDefence),
            baseMatchup(self.iceAttack)
        )
        ret[Types.Dragon.value] = Matchup(
            Types.Dragon,
            baseMatchup(self.dragonDefence),
            baseMatchup(self.dragonAttack)
        )
        ret[Types.Dark.value] = Matchup(
            Types.Dark,
            baseMatchup(self.darkDefence),
            baseMatchup(self.darkAttack)
        )
        ret[Types.Fairy.value] = Matchup(
            Types.Fairy,
            baseMatchup(self.fairyDefence),
            baseMatchup(self.fairyAttack)
        )

        return ret

    def getMatchupsObj(self):
        ret = (Types.max() + 1) * [None]

        ret[Types.Normal.value] = Matchup(Types.Normal, self.normalDefence, self.normalAttack)
        ret[Types.Fighting.value] = Matchup(Types.Fighting, self.fightingDefence, self.fightingAttack)
        ret[Types.Flying.value] = Matchup(Types.Flying, self.flyingDefence, self.flyingAttack)
        ret[Types.Poison.value] = Matchup(Types.Poison, self.poisonDefence, self.poisonAttack)
        ret[Types.Ground.value] = Matchup(Types.Ground, self.groundDefence, self.groundAttack)
        ret[Types.Rock.value] = Matchup(Types.Rock, self.rockDefence, self.rockAttack)
        ret[Types.Bug.value] = Matchup(Types.Bug, self.bugDefence, self.bugAttack)
        ret[Types.Ghost.value] = Matchup(Types.Ghost, self.ghostDefence, self.ghostAttack)
        ret[Types.Steel.value] = Matchup(Types.Steel, self.steelDefence, self.steelAttack)
        ret[Types.Fire.value] = Matchup(Types.Fire, self.fireDefence, self.fireAttack)
        ret[Types.Water.value] = Matchup(Types.Water, self.waterDefence, self.waterAttack)
        ret[Types.Grass.value] = Matchup(Types.Grass, self.grassDefence, self.grassAttack)
        ret[Types.Electric.value] = Matchup(Types.Electric, self.electricDefence, self.electricAttack)
        ret[Types.Psychic.value] = Matchup(Types.Psychic, self.psychicDefence, self.psychicAttack)
        ret[Types.Ice.value] = Matchup(Types.Ice, self.iceAttack, self.iceDefence )
        ret[Types.Dragon.value] = Matchup(Types.Dragon, self.dragonDefence, self.dragonAttack)
        ret[Types.Dark.value] = Matchup(Types.Dark, self.darkDefence, self.darkAttack)
        ret[Types.Fairy.value] = Matchup(Types.Fairy, self.fairyDefence, self.fairyAttack)

        return ret
