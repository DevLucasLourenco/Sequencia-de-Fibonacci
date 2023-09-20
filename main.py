class SequenciaFibonacci():
    '''
    n_sequencia: Quantidade de sequencias que serão apresentadas
    '''

    def __init__(self, n_sequencia: int):
        self.quantidade = int(n_sequencia)
        self.matriz = [0, 1, 1]
        
        if self.quantidade >= 3:
            self.sequencia()  

        elif self.quantidade == 2:
            self.matriz = [0, 1]

        else:
            self.matriz = [0]
        
        print(self.apresentacao())            


    def sequencia(self):         
        for i in range(self.quantidade - 2):
            self.matriz.append(self.matriz[-1] + self.matriz[-2])
                
                
    def apresentacao(self) -> str:
        tratamento = ('  —>  '.join([str(item) for item in self.matriz]))
        return tratamento
        
        
        
if __name__ == '__main__':
    instancia = SequenciaFibonacci(13)
