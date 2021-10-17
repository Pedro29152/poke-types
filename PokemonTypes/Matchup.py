from .PokemonTypes import Types
from .MatchupList import MatchupList

class Matchup:
    def __init__(self, type: Types, defenceMultipliers: MatchupList, attackMultipliers: MatchupList = None):
        self.Type = type
        self.Defence = defenceMultipliers
        self.Attack = attackMultipliers

    def __add__(self, mtch):
        if isinstance(mtch, str):
            return self.__str__() + mtch.__str__()
        if not isinstance(mtch, Matchup):
            raise TypeError('unsupported operand type(s) for *: \'{0}\' and \'{1}\''.format(type(self).__name__, type(Matchup).__name__))

        if isinstance(self.Type, list):
            stype = self.Type
        else:
            stype = [self.Type]
        if isinstance(mtch, list):
            mtype = mtch.Type
        else:
            mtype = [mtch.Type]

        atk = self.Attack * mtch.Attack
        dfn = self.Defence * mtch.Defence

        ret = Matchup(stype + mtype, dfn, atk)
        return ret

    def __str__(self):
        return '{0} - Attack: {1}, Defence: {2}'.format((', '.join(t.name for t in self.Type) if isinstance(self.Type, list) else self.Type.name), self.Attack, self.Defence)

    def __repr__(self):
        return '{' + (', '.join(self.Type.name) if isinstance(self.Type, list) else self.Type.name) + ' type matchups}'
