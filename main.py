class BankHisob:
    def __init__(self, egasi, balans=0):
        self.egasi = egasi
        self.__balans = balans

    def balansni_kor(self):
        print(f"{self.egasi}ning balansi: {self.__balans} so'm")

    def pul_qosh(self, miqdor):
        if miqdor > 0:
            self.__balans += miqdor
            print(f"{miqdor} so'm qo‘shildi. Yangi balans: {self.__balans} so'm")
        else:
            print("Xatolik: Qo‘shilayotgan summa musbat bo‘lishi kerak.")

hisob1 = BankHisob("Ali", 100000)
hisob1.balansni_kor()    
hisob1.pul_qosh(50000)     
hisob1.balansni_kor()      
