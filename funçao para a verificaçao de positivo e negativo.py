num = int(input("Digite um numero para descobrir se é negativoou positivo: "))

def verificar_num():
    if num >= 0:
        return True
        print("numero positivo")
        
    else:
        return False
        print("numero negativo")
    
verificar_num()
