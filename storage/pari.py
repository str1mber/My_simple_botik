class Pari:
    name: str
    challenger_name: str
    taker_name: str

    def __init__(self, name: str, challenger_name: str) -> None:
        self.challenger_name = challenger_name
        self.name = name

    def set_taker(self, taker_name):
        self.taker_name = taker_name


    def __str__(self) -> str:
        return f"""
        - Название пари: {self.name}
        - Кто заключил: {self.challenger_name}
        - Выполняющий: {self.taker_name}
        """