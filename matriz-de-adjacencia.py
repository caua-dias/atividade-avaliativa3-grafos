
# caua
def criar_grafo():
    matriz = []
    vertices = []
    return matriz, vertices

# caua
def inserir_vertice(matriz, vertices, vertice):
    vertice = vertice.strip().upper()

    if vertice in vertices:
        print(f"O vértice '{vertice}' já existe no grafo.")
        return False

    vertices.append(vertice)

    for linha in matriz:
        linha.append(0)

    nova_linha = [0] * len(vertices)
    matriz.append(nova_linha)

    print(f"Vértice '{vertice}' inserido com sucesso.")
    return True

# naves
def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    origem = origem.strip().upper()  
    destino = destino.strip().upper()
    
    if origem not in vertices:
        inserir_vertice(matriz, vertices, origem)
    if destino not in vertices:
        inserir_vertice(matriz, vertices, destino)

    i = vertices.index(origem)
    j = vertices.index(destino)

    matriz[i][j] = 1
    if nao_direcionado:
        matriz[j][i] = 1

    print(f"Aresta inserida de '{origem}' para '{destino}'.")
    if nao_direcionado:
        print(f"(Aresta não direcionada: também inserida de '{destino}' para '{origem}').")

# caua
def remover_vertice(matriz, vertices, vertice):
    vertice = vertice.strip().upper()

    if vertice not in vertices:
        print(f"O vértice '{vertice}' não existe no grafo.")
        return False

    indice = vertices.index(vertice)
    matriz.pop(indice)

    for linha in matriz:
        linha.pop(indice)

    vertices.remove(vertice)
    print(f"Vértice '{vertice}' removido com sucesso.")
    return True

# naves
def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):
    origem = origem.strip().upper()  
    destino = destino.strip().upper()

    if origem not in vertices or destino not in vertices:
        print(f"Não existe aresta entre '{origem}' e '{destino}' no grafo")
        return False

    i = vertices.index(origem)
    j = vertices.index(destino)

    matriz[i][j] = 0
    if nao_direcionado:
        matriz[j][i] = 0

    print(f"Aresta entre '{origem}' e '{destino}' removida com sucesso.")
    return True

# lucas
def existe_aresta(matriz, vertices, origem, destino):
    origem = origem.strip().upper()
    destino = destino.strip().upper()

    if origem not in vertices or destino not in vertices:
        return False

    i = vertices.index(origem)
    j = vertices.index(destino)

    return matriz[i][j] == 1

# Joseph
def vizinhos(matriz, vertices, vertice):
    vertice = vertice.strip().upper()

    if vertice not in vertices:
        print(f"O vértice '{vertice}' não existe.")
        return []

    i = vertices.index(vertice)
    vizinhos_lista = []

    for j, valor in enumerate(matriz[i]):
        if valor == 1:
            vizinhos_lista.append(vertices[j])

    return vizinhos_lista

# lucas
def grau_vertices(matriz, vertices):
    graus = {}

    for i, v in enumerate(vertices):
        saida = sum(matriz[i])
        entrada = sum(matriz[j][i] for j in range(len(vertices)))
        total = entrada + saida
        graus[v] = {"saida": saida, "entrada": entrada, "total": total}
    return graus

# Joseph
def percurso_valido(matriz, vertices, caminho):
    caminho = [v.strip().upper() for v in caminho]

    if len(caminho) < 2:
        return True

    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]
        if not existe_aresta(matriz, vertices, origem, destino):
            return False
    return True

# Joseph
def listar_vizinhos(matriz, vertices, vertice):
    vertice = vertice.strip().upper()
    if vertice not in vertices:
        print(f"O vértice '{vertice}' não existe.")
        return

    lista = vizinhos(matriz, vertices, vertice)
    print(f"Vizinhos de '{vertice}': {lista}")

# naves
def exibir_grafo(matriz, vertices):
    print("\n--- Matriz de Adjacência ---")
    print("    ", end="")
    for v in vertices:
        print(f"{v:>4}", end="")
    print()

    for i, v in enumerate(vertices):
        print(f"{v:>3} ", end="")
        for valor in matriz[i]:
            print(f"{valor:>4}", end="")
        print()
    print("-----------------------------\n")

# lucas
def main():
    matriz, vertices = criar_grafo()

    while True:
        print("""
        ===== MENU GRAFO (MATRIZ DE ADJACÊNCIA) =====
        1 - Mostrar o grafo
        2 - Inserir vértice
        3 - Inserir aresta
        4 - Remover vértice
        5 - Remover aresta
        6 - Listar vizinhos
        7 - Verificar se existe aresta
        8 - Exibir graus dos vértices
        9 - Verificar percurso válido
        0 - Sair
        ==============================================
        """)
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_grafo(matriz, vertices)

        elif opcao == "2":
            v = input("Digite o nome do vértice: ")
            inserir_vertice(matriz, vertices, v)

        elif opcao == "3":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("É não direcionado? (s/n): ").lower() == "s"
            inserir_aresta(matriz, vertices, o, d, nd)

        elif opcao == "4":
            v = input("Vértice a remover: ")
            remover_vertice(matriz, vertices, v)

        elif opcao == "5":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("É não direcionado? (s/n): ").lower() == "s"
            remover_aresta(matriz, vertices, o, d, nd)

        elif opcao == "6":
            v = input("Digite o vértice: ")
            listar_vizinhos(matriz, vertices, v)

        elif opcao == "7":
            o = input("Origem: ")
            d = input("Destino: ")
            print("Existe aresta?", existe_aresta(matriz, vertices, o, d))

        elif opcao == "8":
            graus = grau_vertices(matriz, vertices)
            for v, g in graus.items():
                print(f"{v}: entrada={g['entrada']}, saída={g['saida']}, total={g['total']}")

        elif opcao == "9":
            caminho = input("Digite o caminho (vértices separados por espaço): ").split()
            if percurso_valido(matriz, vertices, caminho):
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
