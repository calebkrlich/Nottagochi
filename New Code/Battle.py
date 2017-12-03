from Character import Character
class Battle:
    _turn = None
    _fighterOne = None
    _fighterTwo = None

    def __init__(self, fighterOne, fighterTwo):
        self._fighterOne = fighterOne
        self._fighterTwo = fighterTwo

    def fighterMove(self,move):
        if(move == "ATTACK"):
            if(self._fighterTwo.getDefencePower() > self._fighterOne.getAttackPower()):
                self._fighterTwo.setHealth((self._fighterTwo.getDefencePower() - (self._fighterOne.getAttackPower() / 2)))
                print("Attack was not very effective!")
            else:
                self._fighterTwo.setHealth((self._fighterTwo.getDefencePower() - self._fighterOne.getAttackPower()))
                print("Attack was super effective!")

        if(move == "TEST"):
            print(self._fighterOne.getAttackPower())
