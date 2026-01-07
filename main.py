class RoboJogador:
    def __init__(self, nome):
        self.nome = nome
        self.em_campo = False
        self.potencia_chute = 0
        self.limite_max_potencia = 100

    def entrar_em_campo(self):
        if self.em_campo:   #Verifique se ele já está lá dentro. Se não estiver, o código muda o "interruptor" para True
            print(f'O {self.nome} já está pronto!')
        else:
            self.em_campo = True
            self.potencia_chute = 10  # E da o bonus de 10
            print(f'{self.nome} entrou no campo. Potência: {self.potencia_chute}')

    def sair_do_campo(self):
        if not self.em_campo:    # Verifica se o robô já está fora
            print(f'O {self.nome} já está fora!')
        else:
            self.em_campo = False   # Aqui é ver se tiver em campo, saia 'False'
            print(f'{self.nome} saiu do campo.')

    def treinar_chute(self):
        if not self.em_campo:   # Esta linha diz: "Se o robô NÃO esteja no campo, pare tudo, mostre um erro e saia do metodo (o return faz isso)".
            print(f'ERRO: {self.nome} precisa entrar no campo primeiro para treinar.')
            return   # Aqui para e sai do metodo
        if self.potencia_chute < self.limite_max_potencia:    # Verifica se a potência do chute é igual ou menor que '100'
            self.potencia_chute += 5
            print(f'Treinando... Potência atual: {self.potencia_chute}')
        else:
            self.potencia_chute = self.limite_max_potencia
            print('Aviso: Força máxima atingida!')

    def descansar(self):
        if not self.em_campo:
            print(f'ERRO: {self.nome} só descansa em campo.')
            return

        if self.potencia_chute >= 10:   # Se a potência atual foir >= 10
            self.potencia_chute -= 10   # Retira 10 da potência atual
        else:
            self.potencia_chute = 0   # Aqui verifica caso a potência seja < 0 oque nao faz sentido, ele pede pra deixar zerado e evitar allgum bug.
        print(f'Descansando... Potência atual: {self.potencia_chute}')

meu_robo = RoboJogador("")
meu_robo.treinar_chute()
meu_robo.entrar_em_campo()
meu_robo.treinar_chute()
meu_robo.treinar_chute()
meu_robo.descansar()
meu_robo.sair_do_campo()
