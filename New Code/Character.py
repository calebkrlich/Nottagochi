class Character:
    _name = ""
    _health = None
    _attackPower = None
    _defencePower = None
    _speed = None

    def __init__(self,health,attack,defence,speed):
        self._health = health
        self._attackPower = attack
        self._defencePower = defence
        self._speed = speed

    def getName(self):
        return self._name

    def getHealth(self):
        return self._health

    def setHealth(self,health):
        self._health = health

    def getAttackPower(self):
        return self._attackPower

    def getDefencePower(self):
        return self._defencePower

    def getSpeed(self):
        return self._speed
