# caua
def criar_grafo():
    return {}

# caua
def inserir_vertice(grafo, vertice):
    vertice = vertice.strip().upper()
    if vertice in grafo:
        return False
    grafo[vertice] = []
    return True

# naves
def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    origem = origem.strip().upper()
    destino = destino.strip().upper()

    if origem not in grafo:
        inserir_vertice(grafo, origem)
    if destino not in grafo:
        inserir_vertice(grafo, destino)

    if destino in grafo[origem]:
        return False
    
    grafo[origem].append(destino)

    if nao_direcionado and origem not in grafo[destino]:
        grafo[destino].append(origem)

    return True

# Joseph
def vizinhos(grafo, vertice):
    vertice = vertice.strip().upper()

    if vertice in grafo:
        return grafo[vertice]
    else:
        return []

# Joseph
def listar_vizinhos(grafo, vertice):
    vertice = vertice.strip().upper()

    if vertice in grafo:
        print(f"Vizinhos de {vertice}: {grafo[vertice]}")
    else:
        print(f"O vértice '{vertice}' não existe no grafo.")

# naves
def exibir_grafo(grafo):
    print("\n--- Grafo (Lista de Adjacência) ---")
    for vertice in sorted(grafo.keys()):
        print(f"{vertice} -> {grafo[vertice]}")
    print("----------------------------------\n")

# naves
def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    origem = origem.strip().upper()
    destino = destino.strip().upper()

    if origem not in grafo or destino not in grafo:
        return False
    
    removido = False

    if destino in grafo[origem]:
        while destino in grafo[origem]:
            grafo[origem].remove(destino)
        removido = True

    if nao_direcionado and origem in grafo[destino]:
        while origem in grafo[destino]:
            grafo[destino].remove(origem)
        removido = True

    return removido

# caua
def remover_vertice(grafo, vertice, nao_direcionado=True):
    vertice = vertice.strip().upper()

    if vertice not in grafo:
        return False

    for v, vizinhos in list(grafo.items()):
        if vertice in vizinhos:
            while vertice in vizinhos:
                vizinhos.remove(vertice)
    del grafo[vertice]
    return True 

# lucas
def existe_aresta(grafo, origem, destino):
    if origem in grafo and destino in grafo[origem]:
        return True
    return False

# lucas
def grau_vertices(grafo):
    graus = {}
    for vertice in grafo:
        graus[vertice] = {"out": 0, "in": 0, "total": 0}

    for u in grafo:
        graus[u]["out"] = len(grafo[u])
        for v in grafo:
            if u in grafo[v]:
                graus[u]["in"] += 1

    for v in graus:
        graus[v]["total"] = graus[v]["out"] + graus[v]["in"]

    return graus

# Joseph
def percurso_valido(grafo, caminho):
    caminho = [v.strip().upper() for v in caminho]

    if len(caminho) < 2:
        return True

    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]
        if not existe_aresta(grafo, origem, destino):
            return False
    return True

# lucas
def main():
    grafo = criar_grafo()

    while True:
        print("""
        ===== MENU GRAFO =====
        1 - Mostrar o Grafo
        2 - Inserir vértice
        3 - Inserir aresta
        4 - Remover vértice
        5 - Remover aresta
        6 - Listar vizinhos
        7 - Verificar se existe aresta
        8 - Exibir graus dos vértices
        9 - Verificar percurso válido
        0 - Sair
        ======================
        """)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_grafo(grafo)

        elif opcao == "2":
            v = input("Digite o nome do vértice: ")
            inserir = inserir_vertice(grafo, v)
            if inserir:
                print(f"Vértice '{v.upper()}' inserido com sucesso.")
            else:
                print(f"{v.upper()} já existe, operação não realizada. ")

        elif opcao == "3":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("É não direcionado? (s/n): ").lower() == "s"
            inserir = inserir_aresta(grafo, o, d, nd)
            if inserir:
                print(f"Aresta ({o.upper()} -> {d.upper()}) inserida com sucesso.")
            else:
                print(f"Aresta ({o.upper()} -> {d.upper()}) já existe, operação não realizada.")

        elif opcao == "4":
            v = input("Vértice a remover: ")
            removido_sucesso = remover_vertice(grafo, v)
    
            if removido_sucesso:
                print(f"Vértice '{v.upper()}' removido com sucesso.")
            else:
                print(f"Vértice '{v.upper()}' não existe. Operação não realizada.")

        elif opcao == "5":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("É não direcionado? (s/n): ").lower() == "s"
            removido_sucesso = remover_aresta(grafo, o, d, nd)
    
            if removido_sucesso:
                print(f"Aresta ({o.upper()} -> {d.upper()}) removida com sucesso.")
            else:
                print(f"A aresta ({o.upper()} -> {d.upper()}) não existe ou vértices inválidos.")

        elif opcao == "6":
            v = input("Digite o vértice: ")
            listar_vizinhos(grafo, v)

        elif opcao == "7":
            o = input("Origem: ")
            d = input("Destino: ")
            print("Existe aresta?" , existe_aresta(grafo, o, d))

        elif opcao == "8":
            graus = grau_vertices(grafo)
            for v, g in graus.items():
                print(f"{v}: in={g['in']}, out={g['out']}, total={g['total']}")

        elif opcao == "9":
            caminho = input("Digite o caminho (vértices separados por espaço): ").split()
            if percurso_valido(grafo, caminho):
                print("O percurso é válido.")
            else:
                print("O percurso é inválido.")

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
