num1 = int(input("Digite quantos graus esta: "))
num2 = int(input("Digite quanto esta a humidade do ar: "))
estaçao = input("estamos no inverno ou do verao: ")


def verificar_verao_ou_inverno():
   
    if estaçao == "inverno":
        if num1 >= 20 and num1 <= 22:
            print("A qualidade do ar esta adequada para o inverno.")
            if num2 >= 40 and num2 <= 55:
                print("A humidade do ar esta adequada para o inverno.")
            else:
                print("A humidade do ar nao esta adequada para o inverno.")
        else:
            print("A qualidade do ar não esta adequada para o inverno.")
            

            
            
            
    if estaçao == "verao":
        if num1 >= 23 and num1 <= 26:
            print("A qualidade do ar esta adequada para o verão.")
            if num2 >= 56 and num2 <= 65:
                print("A humidade do ar esta adequada para o verão.")
            else:
                print("A humidade do ar nao esta adequada para o verão.")
        else:
            print("A qualidade do ar não esta adequada para o verão.")
            
        
verificar_verao_ou_inverno()
