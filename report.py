

def show_report(values:list, draw:list):
    """Gera HTML com resultados

    Args:
        values (list): Aposta e conferência
        draw (list): Resultado do sorteio
    """
    draw = str(draw).replace("[", "").replace("]", "")
    print(header(draw))
    for line in values:
        game = str(line[0]).replace("[", "").replace("]", "")
        hits = str(line[1]).replace("[", "").replace("]", "")
        print(f"<tr><td>{game}</td><td>{hits}</td></tr>")
    print(footer())


def header(draw:str):
    """ Imprime o Header"""

    value1 = """<html>
    <head>
        <style>
        table, th, td {
          border: 1px solid black;
        }
        table.center {
          margin-left: auto;
          margin-right: auto;
        }
        </style>
    </head>
    <body>
        <h1>Jogos e seus resultados</h1>"""

    value2 = f"<p>Valores sorteados: {draw}  </p>"
    value3 = """
        <table style="align-content:center">
            <tr><th>Aposta</th><th>Dezenas Acertadas</th></tr>"""


    return value1 + value2 + value3

def footer():
    """
    Imprime o FOOTER
    """
    value = """</table></body></html>"""
    return value
