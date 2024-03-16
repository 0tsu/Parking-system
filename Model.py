from DAO import DAO

class Model:
  def __init__(self,dao) -> None:
    self.dao = dao
    self.table = "Estacionamento"
    
    self.Id = "Id"
    self.HoraEntrada = "HoraEntrada"
    self.EstaPago = "EstaPago"
    self.ValorTicket = "ValorTicket"
    self.HorarioPagamento = "HorarioPagamento" 
    
    self.dao.Execution(f"""CREATE TABLE IF NOT EXISTS {self.table}(
                  {self.Id} INTEGER PRIMARY KEY AUTO_INCREMENT,
                  {self.HoraEntrada} DATETIME NOT NULL,
                  {self.EstaPago} BIT NOT NULL,
                  {self.HorarioPagamento} DATETIME,
                  {self.ValorTicket} FLOAT
                  );""")