class Test:
    def __init__(self):
        self.value = 5

    @property
    def test_attr(self):
        return self.value

    def test_self(self, value):
        arg = value ** 2
        return arg
