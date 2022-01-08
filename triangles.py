#Método recebe as medidas dos 3 lados de um triângulo e o classifica entre:
#Triângulo Isósceles, Triângulo Escaleno, Triâmgulo Equilátero ou Triângulo não Existe.
def classifica_triangulo (tamanhoLado1, tamanholado2, tamanholado3):
    if(tamanhoLado1 <= 0 or tamanholado2 <= 0 or tamanholado3 <= 0):
        return "Triângulo não Existe"
    if(tamanhoLado1 + tamanholado2 <= tamanholado3 or tamanholado2 + tamanholado3 <= tamanhoLado1 or tamanhoLado1 + tamanholado3 <= tamanholado2):
        return "Triângulo não Existe"
    if(tamanhoLado1 != tamanholado2 and tamanholado2 != tamanholado3 and tamanhoLado1 != tamanholado3):
        return "Triângulo Escaleno"
    if(tamanholado3 == tamanholado2 and tamanholado2 == tamanhoLado1):
        return "Triângulo Equilátero"
    return "Triângulo Isósceles"

def calcula_area (tamanhoLado1, tamanholado2, tamanholado3):
    if(classifica_triangulo(tamanhoLado1, tamanholado2, tamanholado3) == "Triângulo não Existe"):
        return "Triângulo não Existe"
    s = (tamanhoLado1 + tamanholado2 + tamanholado3) / 2
    area = (s*(s-tamanhoLado1)*(s-tamanholado2)*(s-tamanholado3)) ** 0.5
    return round(area,2)
