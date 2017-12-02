from Character import Character
from Battle import Battle

test = Character(2,3,4,5)
test2 = Character(3,2,5,6)

fightTest = Battle(test, test2)

fightTest.fighterOneMove('ATTACK')
