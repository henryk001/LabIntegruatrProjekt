# **README - Implementimi i Blockchain për Menaxhimin e Pronave**

## **Si të ekzekutoni kodin?**
1. Sigurohuni që keni të instaluar **Python 3** në sistemin tuaj.
2. Ruani kodin në një skedar me emrin **main.py**.
3. Hapni terminalin dhe navigoni te direktoria ku ndodhet skedari.
4. Ekzekutoni komandën:
   ```bash
   python main.py
   ```
5. Do të shfaqet zinxhiri i bllokut dhe verifikimi i tij në terminal.

---

## **Bibliografia e Përdorur**
- Nakamoto, S. (2008). *Bitcoin: A Peer-to-Peer Electronic Cash System*.
- Antonopoulos, A. (2017). *Mastering Bitcoin*.
- Narayanan, A., Bonneau, J., Felten, E. (2016). *Bitcoin and Cryptocurrency Technologies*.

---

## **Raporti mbi Blockchain**
### **Çfarë është Blockchain?**
Blockchain është një teknologji e shpërndarë e regjistrave (DLT) që siguron ruajtjen e të dhënave në mënyrë të sigurt dhe të pandryshueshme.

### **Avantazhet e Blockchain:**
✅ **Siguria dhe pandryshueshmëria** – Të dhënat janë të mbrojtura me kriptografi dhe nuk mund të manipulohen.
✅ **Transparenca** – Çdo transaksion është i verifikueshëm nga të gjithë pjesëmarrësit.
✅ **Decentralizimi** – Eliminon nevojën për një autoritet qendror.
✅ **Përmirësimi i efikasitetit** – Automatizimi i proceseve dhe ulja e kostove administrative.

### **Potenciali i Blockchain**
Blockchain ka aplikime të ndryshme, duke përfshirë financat, logjistikën, menaxhimin e identitetit, regjistrat qeveritarë dhe sektorin e pasurive të paluajtshme.

---

## **Skenari i Përdorimit: Menaxhimi i Pronave**
Në këtë projekt, blockchain përdoret për të ruajtur regjistrat e pronave në mënyrë të sigurt. Çdo bllok përfaqëson një transaksion prone që përmban:
- **Identitetin e pronarit** (p.sh., Emri i koduar ose një ID)
- **Vendndodhjen dhe detajet e pronës**
- **Historikun e blerjeve/shitjeve**
- **Datën e transaksionit**

### **Shembull i Implementimit të Një Blloku**
1. **Krijimi i një blloku të ri:**
   ```python
   bllok = Blloku("hash_i_meparemshem", "Prone: Apartament, Vendndodhje: Tirane, Shites: E. Kola, Bleres: A. Hoxha", datetime.datetime.now())
   ```
2. **Llogaritja e hash-it të bllokut:**
   ```python
   hash_blloku = hashlib.sha256(bllok.te_dhena.encode()).hexdigest()
   ```
3. **Shtimi në zinxhirin e bllokut:**
   ```python
   zinxhiri_pronave.shto_bllok("Prone: Apartament, Vendndodhje: Tirane, Shites: E. Kola, Bleres: A. Hoxha, Data: 2025-02-13")
   ```
4. **Verifikimi i zinxhirit:**
   ```python
   zinxhiri_pronave.verifiko_zinxhirin()
   ```

---
Ky projekt demonstron përdorimin e blockchain për të ruajtur regjistrat e pronave me siguri dhe pa mundësi manipulimi. 🚀