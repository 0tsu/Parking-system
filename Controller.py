from DAO import DAO
from Model import Model
from datetime import datetime, timedelta

class Controller:
    def __init__(self):
        self.dao = DAO()
        self.model = Model(self.dao)
        
    def FazerTicket(self):
        self.dao.Insert(self.model.table, self.model.HoraEntrada, self.model.EstaPago, datetime.now())
        
    def CalculoTicket(self, idTicket, horaPagamanto):
        value = self.dao.ReturnValueOnTable(self.model.table, self.model.Id, self.model.HoraEntrada, idTicket)
        if not(value):
            return "Erro no retorno"
        horaEntrada = value[0]
        diferenca = horaPagamanto - horaEntrada

        qtn = diferenca/timedelta(minutes=1)/30
        intQtn = int(qtn)
        if intQtn < 1:
            return 3.50
        return (intQtn + 1) * 5 if qtn > intQtn + 0.5 else intQtn * 5
    
    def PagarTicket(self, idTicket):
        value = self.dao.ReturnValueNoPaidOn(self.model.table, self.model.Id, idTicket, self.model.EstaPago)
        if value:
            horaSaida = datetime.now()
            self.dao.Update(self.model.table, self.model.EstaPago, self.model.ValorTicket, self.CalculoTicket(idTicket, horaSaida), self.model.Id, idTicket, self.model.HorarioPagamento, horaSaida)
            return "Pagamento efetuado com sucesso"
        return "Esse ticket ja esta pago ou o id não existe"
    
    def ParseToJson(self, callback):
        valueJson = []
        for i in callback:
            if i[2] == 0:
                valueJson.append({
                    "Id":i[0],
                    "HoraEntrada":i[1],
                    "EstaPago": "Não esta pago"
                })  
                continue
            valueJson.append({
                "Id":i[0],
                "HoraEntrada":i[1],
                "EstaPago": "Esta pago",
                "ValorTicket":i[3],
                "HorarioPagamento":i[4]
            })
        return valueJson
    
    def VizualizarTicketsPagos(self):
        return list(filter(lambda x: (x["EstaPago"] == "Esta pago"), self.VizualizarTickets()))
    
    def VizualizarTicketsNaoPagos(self):
        return list(filter(lambda x: (x["EstaPago"] == "Não esta pago"), self.VizualizarTickets()))

    def VizualizarTickets(self):
        return self.ParseToJson(self.dao.ReturnAllValuesOnTable(self.model.table))