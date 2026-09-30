from __future__ import annotations
from datetime import date


# Implemente sua classe Medicamento aqui
class Medicamento:
    def __init__(self, nome:str, lote:str, validade:date, quantidade:int, valor:float):
        self._nome = nome
        self._lote = lote
        self._validade = validade
        self._quantidade = quantidade
        self._valor = valor

        """"Implemente um método de classe (@classmethod) chamado de_registro(), que receba
        uma única string no formato "nome;lote;validade;quantidade;valor" (com a validade em formato
        ISO, "AAAA-MM-DD") e retorne uma instância de Medicamento já construída a partir desses
        dados. 
        
        Implemente também um método estático (@staticmethod) chamado
        dias_para_vencer(), que receba uma data de validade (date) e devolva, como int, a
        quantidade de dias entre a data atual (date.today()) e essa validade, sem depender de
        nenhuma instância da classe."""

    @staticmethod
    def dias_para_vencer (validade:date) -> int:
        dias = validade - date.today()
        return dias.days

    @classmethod
    def de_registro (cls, registro:str) -> Medicamento:
        nome,lote,validade,quantidade,valor = registro.split(';')
        validade = date.fromisoformat(validade)
        return cls (nome, lote, validade, int(quantidade), float(valor))
    
    def __str__(self) -> str:
        return f"Nome: {self._nome}, Lote: {self._lote}, Validade: {self._validade}, Quantidade: {self._quantidade}, Valor: {self._valor}"

'''medicamento = Medicamento.de_registro('dipirona;5555555;2026-10-26;6;35.2')
print(medicamento)'''
print(Medicamento.dias_para_vencer(date(2026,10,26)))

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