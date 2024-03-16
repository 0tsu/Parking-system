from Controller import Controller

class View:
    def __init__(self):
        self.controller = Controller()
        
    def ViewValues(self, callback):
        for i in callback():
            print("------------------------------------------")
            for k,v in i.items():
                print(f"{k} - {v}")
            print("------------------------------------------")

    def Menu(self):
        print("Sistema de estacionamento")
        print("Escolha suas Opções")
        print("1 - Criar um ticket")        
        print("2 - Vizualizar tickets")        
        print("3 - pagar um ticket")        
        print("4 - Sair")
        opc = int(input("Digite sua opção: "))
        match opc:
            case 1:
                self.controller.FazerTicket()

            case 2:
                self.ViewTicketOptions()

            case 3:
                self.ViewValues(self.controller.VizualizarTicketsNaoPagos)
                idTicket = int(input("Qual desses tickets vc deseja pagar (selecione de acordo com o Id): "))
                print(self.controller.PagarTicket(idTicket))
            case 4:
                return False
            
        return True

    def ViewTicketOptions(self):
        print("Qual das formas você deseja mostrar")
        print("1 - Apenas as pagas")
        print("2 - Apenas as não pagas")
        print("3 - Tanto Pagas quanto não Pagas")
        print("4 - Sair")
        opc = int(input("Digite sua opção: "))
        match opc:
            case 1:
                self.ViewValues(self.controller.VizualizarTicketsPagos)
            
            case 2:
                self.ViewValues(self.controller.VizualizarTicketsNaoPagos)
            
            case 3:
                self.ViewValues(self.controller.VizualizarTickets)
            
            case 4:
                print("👍")

