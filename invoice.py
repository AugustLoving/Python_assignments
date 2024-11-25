from datetime import datetime

class Invoice:
    def __init__(self, fakturanummer, kund, belopp):
        self.fakturanummer = fakturanummer
        self.kund = kund
        self.belopp = belopp
        self.betalningsstatus = "Obetald"
        self.date = datetime.now()

    def update_payment_status(self, status):
        self.betalningsstatus = status
    
class InvoiceManager():
    def __init__(self):
        self.fakturor = {}

    def skapa_faktura(self, faktura):
        if faktura.fakturanummer in self.fakturor:
            raise ValueError("Fakturanummer finns redan!")
        self.fakturor[faktura.fakturanummer] = faktura
    
    def lista_obetalda_fakturor(self):
        return [faktura for faktura in self.fakturor.values() if faktura.betalningsstatus == "unpaid"]

