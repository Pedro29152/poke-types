from typing import overload
from .PokemonTypes import Types

class MatchupList:
    def __init__(self, defaultValues = 1, matchupList: list = None):
        if matchupList:
            if not isinstance(matchupList, list):
                raise TypeError('matchupList argument must be a list')
            max = Types.max() + 1
            if not len(matchupList) == max:
                raise ValueError('the list must have the exact size of {0}, not {1}'.format(max, len(matchupList)))

            self._typeMatch = matchupList
        else:
            self._typeMatch = [defaultValues for i in range(Types.max() + 1)]

    def getList(self):
        return self._typeMatch.copy()

    def __getStr(self):
        ret = []

        for t in Types:
            ret.append('{0}: {1}'.format(t.name, self._typeMatch[t.value]))

        return '[' + (', '.join(ret)) + ']'

    #def __add__(self, o):

    def __mul__(self, o):
        if not isinstance(o, MatchupList):
            raise TypeError('unsupported operand type(s) for *: \'{0}\' and \'{1}\''.format(type(self).__name__, type(o).__name__))

        ret = MatchupList()
        for i, value in enumerate(self._typeMatch):
            ret[i] = value * o[i]
        return ret

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [self[i] for i in key.indices(len(self))]
        
        if isinstance(key, int):
            return self._typeMatch[key]

        raise TypeError('matchup list indices must be integers or slices')

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError('matchup list indices must be integer')

        if not (isinstance(value, int) or isinstance(value, float)):
            raise TypeError('matchup list values must be integers or floats')
        
        self._typeMatch[key] = value

    def __str__(self):
        return self.__getStr()

    def __repr__(self):
        return self.__getStr() 
