import inputs
import time
listas = []


def verificar_situaçao(media):
    if media >= 7:
        situaçao = "aprovado"
        
    elif media >= 5 and num1 <= 6.9:
        situaçao = "de recuperação"
        
    elif media < 5:
        situaçao = "reprovado"

    return situaçao



def cadastro_de_aluno():
    nome_do_aluno = inputs.input_str("Digite o nome do aluno: ")
    idade = inputs.input_int("-Digite a idade do aluno: ")
    genero = inputs.input_str("-Digite o genero do aluno: ")
    nota1 = inputs.input_int("-Digite a nota do aluno: ")
    nota2 = inputs.input_int("-Digite a nota do aluno: ")
    nota3 = inputs.input_int("-Digite a nota do aluno: ")
    media = calcular_mediafinal(nota1,nota2,nota3)
    situaçao = verificar_situaçao(media)
    livro = {
        "Nome do aluno":nome_do_aluno,
        "Idade do estudante":idade,
        "Genero do estudante":genero,
        "Media do estudante":media,
        "situação do estudante":situaçao,
    }
    print("")
    listas.append(livro)
    
    
def exibir_relatorio():
    for ordem1 in listas:
        for chave, valor in ordem1.items():
            print(f' {chave}:  {valor}')
        print("")


## return mediafinal
    

def situaçao_dos_estudantes():
    for livro in listas:
        print(f"{listas['livro']}")
            
            
def calcular_mediafinal(nota1,nota2,nota3):
    media1 = nota1 + nota2 + nota3
    mediafinal = media1 / 3
    return mediafinal
    print("a media foi: ",mediafinal)
    
    listas["media"] = mediafinal
            
            
            

while True:
    print(".")
    print(".")
    print(".")
    print(".")
    print(".")
    print("        _____MENU_____")
    print("...................................")
    print("Escolha uma das opçoes abaixo ")
    print("1 - Cadastro do estudante ")
    print("2 - Exibir relatorio do estudante")
    print("0 - Sair ")
    print("...................................")
    es = inputs.input_int("Digite a opção desejada: ")

    if es == 0:
        print(".")
        print(".")
        print("                saindo do menu de escolhas")
        time.sleep(1)
        print("                         final.")
        print("---------Muito obrigado por acessar meu aplicativo---------")
        break

    print(".")
    print(".")

    if es == 1:
        cadastro_de_aluno()

    elif es == 2:
        exibir_relatorio()

        