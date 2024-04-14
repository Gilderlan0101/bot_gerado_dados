import telebot
import os
import random
import string

LOGIN = "CHAVE API"
# opcional 
ARQUIVOS = 'pasta'
# Iniciando o bot
bot = telebot.TeleBot(LOGIN)

# Criando um função geradora de cpf
# Decorator --> Sempre deve esta preesente quando for cria uma def que faça algo. 
@bot.message_handler(commands=['gera_cpf'])
def gerador_cpf(mensagem):
    
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0,9))
        resultado_digito_1 = 0
        contador_regressivo_1 = 10
        
    for digito_1 in nove_digitos:
        resultado_digito_1 += int(digito_1) * contador_regressivo_1
        contador_regressivo_1 -= 1
            
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 >= 9 else 0
    
    
    dez_digito = str(nove_digitos) + str(digito_1)
    contador_regressivo_2 = 11
    resultado_digito_2 = 0
    
    for digito_2 in dez_digito:
        resultado_digito_2 += int(digito_2) * contador_regressivo_2
        contador_regressivo_2 -= 1
        
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 >= 9 else 0
    
    gerador_cpf = f'{nove_digitos}{digito_1}{digito_2}'
    
    bot.send_message(mensagem.from_user.id, f' CPf Gerado com sucesso {gerador_cpf} ✅')


# Decorator --> Sempre deve esta preesente quando for cria uma def que faça algo.    
@bot.message_handler(commands=['gera_numero'])
def telefone(mensagem):
    
    def gera_numero():
        numero = '+55'
        
    # gerando codigo postal com dois digitos
        ddd = random.randint(11,75)
        numero += str(ddd) + ' '
        for _ in range(4):
            numero += str(random.randint(0,9))
        numero += '-'
            
        for _ in range(4):
            numero += str(random.randint(0,9))
            
        return numero
        
    numero = gera_numero()
    bot.send_message(mensagem.from_user.id, f'Numero gerado com Sucesso 📞 {numero}')
        
# Funçao geradora de senha
@bot.message_handler(commands=['gera_senha'])
def gera_senha(mensagem):
        # 2 variavel que aceita dois modulos
    def senha(size=11, char=string.ascii_uppercase + string.digits):
        # juntando a string e o digitos com numeros
        senha = ''.join(random.choice(char)for _ in range(size))
        return senha
    
    pwd = senha()
    bot.send_message(mensagem.from_user.id, f'Senha Gerada Com Sucesso! 🔑 {pwd}')
        

def gera_tudo(cpf, tel, pwd):
    mensagem = 'Dados Gerados Com Sucesso'
    if mensagem.strip():  # Verifica se a mensagem não está vazia
        return mensagem
    else:
        return 'Nenhuma informação disponível no momento.'
# Funçao que vai gerar todos os dados
@bot.message_handler(commands=['gera_tudo'])
def dados(mensagem):
    cpf = gerador_cpf(mensagem)
    tel = telefone(mensagem)
    pwd = gera_senha(mensagem)
    
    todos_os_dados = gera_tudo(cpf,tel,pwd)

    bot.send_message(mensagem.from_user.id, todos_os_dados)

# Mensagen padrõa
@bot.message_handler(func=lambda mensagem: mensagem.text == 'chat')
def login(mensagem):
# editer como deseja 
    defaut = '''Ola seja bem vindo. (Escolha uma opção)
    /gera_cpf
    /gera_numero
    /gera_senha
    /gera_tudo'''
    
    bot.send_message(mensagem.from_user.id, defaut)


# Faz o bot fica online == ativar bot
bot.polling()
