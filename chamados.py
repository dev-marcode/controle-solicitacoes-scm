# chamados.py
# Registro simples de chamados abertos pelo time de operações

chamados = []


def abrir_chamado(titulo, solicitante):
    chamado = {
        'id': len(chamados) + 1,
        'titulo': titulo,
        'solicitante': solicitante,
        'status': 'aberto',
    }
    chamados.append(chamado)
    return chamado


def listar_chamados():
    for c in chamados:
        print('#' + str(c['id']), c['titulo'], '-', c['solicitante'], '-', c['status'])


if __name__ == '__main__':
    abrir_chamado('Erro no relatório diário', 'Operações')
    abrir_chamado('Novo campo no cadastro', 'Operações')
    listar_chamados()