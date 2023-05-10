#Calculadora que converte um valor de milhas terrestres e náuticas para quilômetros
km = int(input("Digite os kilômetros: "))
print(f"{km} km equivalem a {1.60934 * km} milhas terrestres e {1.852 * km} milhas náuticas")