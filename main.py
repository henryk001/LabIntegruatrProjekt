import hashlib
import datetime

class Blloku:
    def __init__(self, hash_i_meparemshem, te_dhena, kohe_krijimi, veshtiresia=4):
        self.hash_i_meparemshem = hash_i_meparemshem  # Hash-i i bllokut te meparshem
        self.te_dhena = te_dhena  # Informacioni i ruajtur ne bllok
        self.kohe_krijimi = kohe_krijimi  # Timestamp kur krijohet blloku
        self.nonce = 0  # Variabel qe ndryshon per te gjetur hash-in e sakte
        self.veshtiresia = veshtiresia  # Sa shifra "0" duhet te filloje hash-i
        self.hash = self.procesi_punes()

    @staticmethod
    def krijo_bllokun_gjenez():
        return Blloku("0", "Blloku i Pare", datetime.datetime.now())

    def llogarit_hashin(self):
        permbajtja = (str(self.hash_i_meparemshem) + str(self.te_dhena) +
                      str(self.kohe_krijimi) + str(self.nonce)).encode()
        return hashlib.sha256(permbajtja).hexdigest()

    def procesi_punes(self):
        target = "0" * self.veshtiresia  # Krijon nje varg qe fillon me numrin e duhur te "0"
        while True:
            self.hash = self.llogarit_hashin()
            if self.hash.startswith(target):
                break
            self.nonce += 1  # Rrit nonce derisa te gjejme nje hash te sakte
        return self.hash

class ZinxhiriBllokut:
    def __init__(self, zinxhiri=None, veshtiresia=4):
        self.veshtiresia = veshtiresia  # Veshtiresia e Proof of Work
        if zinxhiri is None or len(zinxhiri) == 0:
            self.zinxhiri = [Blloku.krijo_bllokun_gjenez()]
        else:
            self.zinxhiri = zinxhiri

    def shto_bllok(self, te_dhena):
        blloku_fundit = self.zinxhiri[-1]  # Merr bllokun e fundit ne zinxhir
        bllok_i_ri = Blloku(blloku_fundit.hash, te_dhena, datetime.datetime.now(), self.veshtiresia)
        self.zinxhiri.append(bllok_i_ri)

    def verifiko_zinxhirin(self):
        for i in range(1, len(self.zinxhiri)):
            blloku_tanish = self.zinxhiri[i]
            blloku_meparshme = self.zinxhiri[i - 1]

            if blloku_tanish.hash != blloku_tanish.llogarit_hashin():
                print(f"Blloku {i} eshte i manipuluar!")
                return False

            if blloku_tanish.hash_i_meparemshem != blloku_meparshme.hash:
                print(f"Blloku {i} ka hash te meparshem te pavlefshem!")
                return False

            if not blloku_tanish.hash.startswith("0" * self.veshtiresia):
                print(f"Blloku {i} nuk ploteson Proof of Work!")
                return False

        print("Zinxhiri i bllokut eshte i vlefshem!")
        return True


zinxhiri_mjekesor = ZinxhiriBllokut(veshtiresia=4)

zinxhiri_mjekesor.shto_bllok("Pacient: Ana M., Diagnoza: Astma, Doktor: Dr. Basha, Data: 2025-02-13")
zinxhiri_mjekesor.shto_bllok("Pacient: Edi K., Diagnoza: Hipertension, Doktor: Dr. Lila, Data: 2025-02-12")
zinxhiri_mjekesor.shto_bllok("Pacient: Sara T., Diagnoza: Grip, Doktor: Dr. Hoxha, Data: 2025-02-10")

zinxhiri_mjekesor.verifiko_zinxhirin()
