import random
from report import show_report

DOZENS_TOTAL = 60
FIRST_DOZEN = 1
DRAW_DOZENS = 6
DOZENS_ALLOWED = (6, 7, 8, 9, 10)

class Jogo(object):

    def __init__(self, qtd_dezenas:int,  total_jogos:int):
        """Construtor

        Args:
            qtd_dezenas (int): Quantidade de dezenas por jogo
            total_jogos (int): Quantidade de jogos
        """
        self.__qtd_dezenas_set(qtd_dezenas)
        self.__resultado:list(int) = []
        self.__total_jogos_set(total_jogos)
        self.__jogos:list(int) = []


    # SET
    def __qtd_dezenas_set(self, value:int) -> None:
        """Atribui a quantidade de dezenas por jogo

        Args:
            value (int): quantidade de dezenas por jogo

        Raises:
            Exception: [Se estiver fora dos valores definidos levanta um erro]
        """
        if value not in DOZENS_ALLOWED:
            raise Exception("Quantidade de dezenas deve ser 6, 7, 8, 9, 10")
        self.qtd_dezenas = int(value)

    def __total_jogos_set(self, value) -> None:
        self.__total_jogos = int(value)


    # GET
    def dezenas_get(self) -> int:
        return self.__dezenas

    def resultado_get(self) -> list:
        return self.__resultado

    def total_jogos_get(self) -> None:
        return self.total_jogos

    def jogos_get(self) -> list:
        return self.__jogos


    # Private methods
    def __generate_game_array(self) -> list:
        """Cria um array de jogos cujo o tamanho é definido por total de jogos
           e a quantidade de dezenas por jogo é definido por qtd_dezenas

        Returns:
            list: Array de jogos
        """
        result = []
        for i in range(0, self.__total_jogos):
            value = self.__draw(self.qtd_dezenas)
            result.append(value)
        self.__jogos = result

    def __draw(self, qtd_dezenas:int) -> list:
        """Cria um array randomico com tamnho definido em qtd_dezenas

        Args:
            qtd_dezenas (int): Quantidade de dezenas do array

        Returns:
            list: array randomico em ordem crescente
        """
        results = []
        while len(results) < qtd_dezenas:
            number =random.randint(FIRST_DOZEN, DOZENS_TOTAL)
            if number not in results:
                results.append(number)
        return sorted(results)

    # Public Methods

    def draw(self) -> list:
        """Sorteio que define o resultado

        Returns:
            list: Array randomico com comprimento DRAW_DOZENS
        """
        self.__resultado = self.__draw(DRAW_DOZENS)

    def make_bet(self):
        """Gera um array multidimensional com as apostas

        Returns:
            [type]: [description]
        """
        self.__generate_game_array()
        return self.__jogos

    def report_html(self):
        """
        Gera uma saida HTML do resultado
        """
        result = []
        for game in self.__jogos:
            hits = list(set(game) & set(self.__resultado))
            result.append([game, hits])
        show_report(result, self.__resultado)


obj = Jogo(9, 3)
obj.draw()
obj.make_bet()
obj.report_html()