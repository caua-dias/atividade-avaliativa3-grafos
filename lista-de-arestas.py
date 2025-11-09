# caua
def criar_grafo():
    vertices = []
    arestas = []
    return vertices, arestas

# caua
def inserir_vertice(vertices, vertice):
    if vertice not in vertices:
        vertices.append(vertice)
        print(f"Vértice '{vertice}' adicionado.")
    else:
        print(f"Vértice '{vertice}' já existe.")

# naves
def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    origem = origem.strip().upper()  
    destino = destino.strip().upper()

    if origem not in vertices:
        inserir_vertice(vertices, origem)
    if destino not in vertices:
        inserir_vertice(vertices, destino)

    aresta = [origem, destino]
    if aresta not in arestas:
        arestas.append(aresta)
        print(f"Aresta {aresta} adicionada.")
    else:
        print(f"Aresta {aresta} já existe.")

    if nao_direcionado:
        aresta_oposta = [destino, origem]
        if aresta_oposta not in arestas:
            arestas.append(aresta_oposta)
            print(f"Aresta {aresta_oposta} adicionada (não direcionado).")

# naves
def remover_aresta(arestas, origem, destino, nao_direcionado=False):
    origem = origem.strip().upper()  
    destino = destino.strip().upper()

    aresta = [origem, destino]
    if aresta in arestas:
        arestas.remove(aresta)
        print(f"Aresta {aresta} removida.")
    else:
        print(f"Aresta {aresta} não encontrada.")

    if nao_direcionado:
        aresta_oposta = [destino, origem]
        if aresta_oposta in arestas:
            arestas.remove(aresta_oposta)
            print(f"Aresta {aresta_oposta} removida (não direcionado).")

# caua
def remover_vertice(vertices, arestas, vertice):
    vertice = vertice.strip().upper()

    if vertice not in vertices:
        print(f"Vértice '{vertice}' não encontrado.")
        return

    vertices.remove(vertice)
    print(f"Vértice '{vertice}' removido.")

    arestas[:] = [a for a in arestas if vertice not in a]
    print(f"Arestas associadas ao vértice '{vertice}' foram removidas.")

# lucas
def existe_aresta(arestas, origem, destino):
    origem = origem.strip().upper()
    destino = destino.strip().upper()
    
    for a in arestas:
        if a == [origem, destino]:
            return True
    return False

# Joseph
def vizinhos(vertices, arestas, vertice):
    vertice = vertice.strip().upper()
    
    if vertice not in vertices:
        print(f"Vértice '{vertice}' não encontrado.")
        return []

    viz = []
    for a in arestas:
        if a[0] == vertice:
            viz.append(a[1])
    return viz

# lucas
def grau_vertices(vertices, arestas):
    graus = {}

    # Inicializa todos os vértices
    for v in vertices:
        graus[v] = {"entrada": 0, "saida": 0, "total": 0}

    for origem, destino in arestas:
        if origem in graus:
            graus[origem]["saida"] += 1
        if destino in graus:
            graus[destino]["entrada"] += 1

    for v in graus:
        graus[v]["total"] = graus[v]["entrada"] + graus[v]["saida"]

    return graus

# Joseph
def percurso_valido(arestas, caminho):
    caminho = [v.strip().upper() for v in caminho]

    if len(caminho) < 2:
        return True

    for i in range(len(caminho) - 1):
        u = caminho[i]
        v = caminho[i + 1]
        if not existe_aresta(arestas, u, v):
            return False
    return True

# Joseph
def listar_vizinhos(vertices, arestas, vertice):
    vertice = vertice.strip().upper()

    viz = vizinhos(vertices, arestas, vertice)
    if viz:
        print(f"Vizinhos de '{vertice}': {viz}")
    else:
        print(f"O vértice '{vertice}' não possui vizinhos.")

# naves
def exibir_grafo(vertices, arestas):
    print("\n--- Grafo ---")
    print("Vértices:", vertices)
    print("Arestas:")
    for origem, destino in arestas:
        print(f"{origem} -> {destino}")

# lucas
def main():
    vertices, arestas = criar_grafo()

    while True:
        print("\n===== MENU =====")
        print("1 - Exibir Grafo")
        print("2 - Inserir Vértice")
        print("3 - Inserir Aresta")
        print("4 - Remover Vértice")
        print("5 - Remover Aresta")
        print("6 - Listar Vizinhos")
        print("7 - Mostrar Graus dos Vértices")
        print("8 - Verificar Percurso")
        print("0 - Sair")

        opc = input("Escolha uma opção: ")

        if opc == "1":
            exibir_grafo(vertices, arestas)
        elif opc == "2":
            v = input("Digite o nome do vértice: ")
            inserir_vertice(vertices, v)
        elif opc == "3":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("É não direcionado? (s/n): ").lower() == "s"
            inserir_aresta(vertices, arestas, o, d, nd)
        elif opc == "4":
            v = input("Vértice a remover: ")
            remover_vertice(vertices, arestas, v)
        elif opc == "5":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("É não direcionado? (s/n): ").lower() == "s"
            remover_aresta(arestas, o, d, nd)
        elif opc == "6":
            v = input("Vértice: ")
            listar_vizinhos(vertices, arestas, v)
        elif opc == "7":
            graus = grau_vertices(vertices, arestas)
            for v, g in graus.items():
                print(f"{v}: Entrada={g['entrada']}, Saída={g['saida']}, Total={g['total']}")
        elif opc == "8":
            caminho = input("Digite o percurso separado por espaços: ").split()
            valido = percurso_valido(arestas, caminho)
            print("Percurso válido!" if valido else "Percurso inválido.")
        elif opc == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()