import mysql.connector as mysql

class DAO:
  def __init__(self) -> None:
    self.server = mysql.connect(
      host = "localhost",
      user = "root",
      password = "aluno99"
    )
    self.c = self.server.cursor()
    
    self.c.execute("CREATE DATABASE IF NOT EXISTS garagem")
    
    self.server = mysql.connect(
      host = "localhost",
      user = "root",
      password = "aluno99",
      database = "garagem"
    )
    self.c = self.server.cursor()
    

  def Execution(self, value):
      return self.c.execute(value)

  def ReturnAllValuesOnTable(self,table):
    self.Execution(f"""SELECT * FROM {table}""")
    return self.c.fetchall()
  
  def ReturnValueNoPaidOn(self, table, Id, idTicket, EstaPago):
    self.Execution(f"SELECT * FROM {table} WHERE {Id} = {idTicket} AND {EstaPago} = 0")
    return self.c.fetchone()
  
  def ReturnValueOnTable(self, table, Id, HoraEntrada, idTicket): 
    self.Execution(f"""SELECT {HoraEntrada} FROM {table} WHERE {Id} = {idTicket}""")
    return self.c.fetchone()

  def Insert(self, table, HoraEntrada, EstaPago, horaAtual):
    self.Execution(f"""INSERT INTO {table} ({HoraEntrada}, {EstaPago}) VALUES ('{horaAtual}', 0)""")
    self.server.commit()
  
  def Update(self,table, EstaPagoCol, ValorTicketCol, calculoValor, IdCol, idTicket, horarioPagamentoCol, horarioPagamento):
    print(f"""UPDATE {table} SET {EstaPagoCol} = 1, {ValorTicketCol} = {calculoValor}, {horarioPagamentoCol} = {horarioPagamento} WHERE {IdCol} = {idTicket}""")
    self.Execution(f"""UPDATE {table} SET {EstaPagoCol} = 1, {ValorTicketCol} = {calculoValor}, {horarioPagamentoCol} = {horarioPagamento} WHERE {IdCol} = {idTicket}""")
    self.server.commit()

