class Test:
    testing = 54
    _priv = 4
    def __init__(self):
        print(self._priv)

t = Test()
print(t._priv)