def registrar_cartao(dados):
      cadastro_cartao = input("\n\nCartao: ")
      if cadastro_cartao in dados:
          print("ERRO! Ja existe um cartao com esse nome")
          return
      cadastro_senha = input("\n\nSenha: ")
      print("Cadatro realizado com sucesso!")
      dados[cadastro_cartao] = cadastro_senha

dados_login_e_senha = {}
answer = input("Você é um novo usuário? Responda 'Sim' ou 'Não': ")

if answer == "Sim" or answer == "sim": 
    print("Vamos nos cadatrar!")
    registrar_cartao(dados_login_e_senha)

usuario = input("Entre com seu cartao: ")
senha = input("Informe a senha: ")
if usuario in dados_login_e_senha:
    if dados_login_e_senha[usuario] == senha:
        print("Login efetuado")
    else:
        print("Senha incorreta")
else:
    print("Nao existe nenhum cadastro com esse nome de usuario")