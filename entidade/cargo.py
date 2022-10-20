
class Cargo():
    def __init__(self, cargo: str):
        self.__cargo = cargo

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo: str):
        self.__cargo = cargo
