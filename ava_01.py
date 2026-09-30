from __future__ import annotations
from datetime import date

# Erros ------------

class QuantidadeInvalidaError(Exception):
    def __init__(self):
        super().__init__("Quantidade solicitada não pode ser menor ou igual a zero, nem maior que a quantidade disponível")

class MedicamentoVencidoError(Exception):
    def __init__(self):
        super().__init__("Medicamento está vencido")

# Classes ----------

class Medicamento:
    def __init__(self, nome:str, lote:str, validade:str, quantidade:int, valor:float) -> None:
        # Lembra de ajeitar  o type hint da validade
        self._nome = nome
        self._lote = lote
        self._validade = validade
        self.quantidade = quantidade
        self.valor = valor
    
    @property
    def quantidade(self) -> int:
        return self._quantidade

    @property
    def valor(self) -> int:
        return self._valor  

    @quantidade.setter
    def quantidade(self, quant:int) -> None:
        if quant < 0:
            raise ValueError("A quantidade do medicamento não pode ser negativa")
        self._quantidade = quant

    @valor.setter
    def valor(self, valor:int) -> None:
        if valor > 0:
            self._valor = valor
        else:
            raise ValueError("Valor do medicamento deve ser maior que zero")

    def __str__(self) -> str:
        return f"{self._nome} | Lote: {self._lote} | Quantidade: {self._quantidade} | Validade: {self._validade}"

    def __repr__(self) -> str:
        return f"Medicamento(nome={self._nome}, lote={self._lote}, quantidade={self._quantidade}, validade={self._validade})"

    def __eq__(self, outro) -> bool:
        if isinstance(outro, Medicamento):
            if self._nome == outro._nome and self._lote == outro._lote:
                return True
        return False

    def __lt__(self, outro) -> bool:
        return self._validade < outro._validade
        
    def dispensar(self, quantidade:int) -> None:
        if quantidade > self._quantidade or quantidade <= 0:
            raise QuantidadeInvalidaError
            
        #  validar a validade ------

        self.quantidade = self._quantidade - quantidade

    def repor(self, quantidade:int):
        self.quantidade = quantidade

try:
    med = Medicamento("Ibuprofeno", "BGDGS", "15 DIAS", 55, 7)
    med2 = Medicamento("Ibuprofeno", "BGDG", "14 DIAS", 55, 7)
    print(med)
    print([med])
    print(med == med2)

    med.repor()
except Exception as error:
    print(error)

# if __name__ == "__main__":
# m1 = Medicamento("Dipirona 500mg", "L2026A", date(2026, 12, 31), 100, 12.50)
# m2 = Medicamento.de_registro("Amoxicilina 500mg;L2026B;2026-10-15;40;18.90")
# print(f"Dados de m1: {m1}") # ex.: Dipirona 500mg (L2026A) - 100 un. - val. 31/12/2026
# print(f"Dados de m2: {m2}") # ex.: Amoxicilina 500mg (L2026B) - 40 un. - val. 15/10/2026
# print(f"Dias para vencer de m2: {Medicamento.dias_para_vencer(m2.validade)}")
# print("Dispensando 20 medicamentos de m1")
# m1.dispensar(20)
# print(f"Quantidade de m1: {m1.quantidade}")
# try:
# m2.dispensar(999)
# except QuantidadeInvalidaError as erro:
# print(f"Erro esperado: {erro}")

# vencido = Medicamento("Soro Fisiológico", "L2025X", date(2025, 1, 10), 10, 5.0)
# try:
# vencido.dispensar(1)
# except MedicamentoVencidoError as erro:
# print(f"Erro esperado: {erro}")

# outro = Medicamento("Dipirona 500mg", "L2026A", date(2026, 1, 1), 0, 1.0)
# print(f"m1 é igual a outro? {m1 == outro}")

# estoque = [m1, m2, vencido, outro]
# print("Exibindo lista ordenada por data (mais antigos primeiro): ")
# for lote in sorted(estoque):
# print(lote)

# try:
# m1.quantidade = -5
# except ValueError as erro:
# print(f"Erro esperado: {erro}")