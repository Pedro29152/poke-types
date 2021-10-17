from enum import IntEnum

class Types(IntEnum):
    #region Types
    Normal =    0
    Fighting =  1
    Flying =    2
    Poison =    3
    Ground =    4
    Rock =      5
    Bug =       6
    Ghost =     7
    Steel =     8
    Fire =      9
    Water =     10
    Grass =     11
    Electric =  12
    Psychic =   13
    Ice =       14
    Dragon =    15
    Dark =      16
    Fairy =     17
    #endregion
    
    def max():
        maior = None
        for t in Types:
            if maior == None:
                maior = t
                continue
            
            if t.value > maior.value:
                maior = t
        
        return maior
