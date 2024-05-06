import streamlit as st 

class ContaBancaria():

    # def __init__(self, saldo,nome,idade,cpf) -> None:
    #     self.saldo = saldo
    #     self.dono=Pessoa(nome,idade,cpf)
    #     self.numero=None#atributo
    def __init__(self, saldo,nome) -> None:
        self.saldo = saldo
        self.dono=nome
        self.numero=None#atributo

    def depositar(self,valor):
        self.saldo+=valor
        print("Saldo atualizado")
        return self.saldo

    def sacar(self,valor):
        if self.saldo-valor>0:
            self.saldo-=valor   
            return self.saldo
        else:
            print("Negado")




st.title("Conta Bancária")

st.write("Olá, seja bem-vindo ao banco do povo!")
st.write("Para começar, precisamos de algumas informações")
st.write("Qual o seu nome?")
nome = st.text_input("Digite seu nome")
st.write("Qual o seu saldo?")
saldo = st.number_input("Digite seu saldo")
st.write("Qual a sua idade?")
idade = st.number_input("Digite sua idade")
st.write("Qual o seu CPF?")
cpf = st.number_input("Digite seu CPF")
st.write("Qual o número da sua conta?")
numero = st.number_input("Digite o número da sua conta")
if st.button("Cadastrar"):
    conta = ContaBancaria(saldo,nome)
    st.write("Cadastro realizado com sucesso!")
    st.write("Seu saldo atual é de R$",conta.saldo)
    # st.write("Seu nome é",conta.dono.nome)
    # st.write("Sua idade é",conta.dono.idade)
    # st.write("Seu CPF é",conta.dono.cpf)
    st.write("O número da sua conta é",conta.numero)

st.write("O que deseja fazer agora?")
opcao = st.selectbox("Selecione uma opção",["Depositar","Sacar"])
if opcao == "Depositar":
    valor = st.number_input("Digite o valor a ser depositado")
    if st.button("Depositar"):
        conta.depositar(valor)
        st.write("Depósito realizado com sucesso!")
        st.write("Seu saldo atual é de R$",conta.saldo)
elif opcao == "Sacar":
    valor = st.number_input("Digite o valor a ser sacado")
    if st.button("Sacar"):
        conta.sacar(valor)
        st.write("Saque realizado com sucesso!")
        st.write("Seu saldo atual é de R$",conta.saldo)
        





# class Pessoa():
#     def __init__(self,nome,idade,cpf) -> None:
#         self.nome = nome
#         self.idade = idade
#         self.cpf = cpf

# class Professor(Pessoa):

#     def __init__(self, nome, idade, cpf,materia,salario) -> None:
#         super().__init__(nome, idade, cpf)
#         self.materia = materia
#         self.salario = salario
#         self.conta = None

#     def criar_conta(self,saldo):

#         self.conta = ContaBancaria(saldo,self.nome,self.idade,self.cpf)


    

# p1 = Professor("Marcus",21,"1212321312","programacao","12301230")

# p1.criar_conta(2000)

# p1.conta.depositar(1000)

# print(p1.conta.saldo)