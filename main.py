from PokemonTypes.Matchup import Matchup
from PokemonTypes.PokemonTypes import Types
from PokemonTypes.Matchups import Matchups
from PokemonTypes.MatchupList import MatchupList

def getTypeStrWknCount():
    matchups = Matchups().getMatchups()
    strengths = MatchupList(0)
    weaknesses = MatchupList(0)

    for t in Types:
        matchup = matchups[t.value]
        s = 0
        w = 0

        for atk in matchup.Attack:
            if atk > 1:
                s += 1
        for defence in matchup.Defence:
            if defence > 1:
                w += 1

        strengths[t.value] = s
        weaknesses[t.value] = w

    return {'strengths': strengths, 'weaknesses': weaknesses}

if __name__ == '__main__':
    matchups = Matchups().getMatchups()
    print()
    print(matchups)
    print()

    aggragateMatchup = matchups[Types.Flying.value] + matchups[Types.Fire.value]
    print()
    print(aggragateMatchup)
    print()
    
    strong = getTypeStrWknCount()
    print()
    print(strong)
    print()
