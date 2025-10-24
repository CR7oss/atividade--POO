# Criar matriz 5x8 (5 fileiras, 8 assentos)
cinema = [[0 for a in range(8)] for f in range(5)]

# Função para reservar
def reservar(fileira, assento):
    cinema[fileira-1][assento-1] = 1

# Função para cancelar
def cancelar(fileira, assento):
    cinema[fileira-1][assento-1] = 0

# Função para mostrar mapa
def mostrar():
    for f in cinema:
        print(f)

# Reservas
reservar(1, 3)
reservar(2, 5)
reservar(4, 7)

# Cancelamento
cancelar(2, 5)

# Mostrar mapa final
print("\nMapa final dos assentos:")
mostrar()
