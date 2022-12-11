"""
İzmirim Kart Sistemi Simüle Ediniz.
- Her kartın bir id numarası, ad soyad bilgisi ve bakiye bilgisi olacak.
- İsim soyisim tanımlama zorunlu olsun.
- Bakiye default olarak 0'dan başlasın.
- 0-999999 arasında random kart numarası olsun. (Kart oluşma durumunda çakışma olmasın)
- Kart Oluşturma ve Seçme işlemleri olsun.
- Kart oluşturma seçilirse isim ve soyisim sorsun ve class'a ait listeye eklesin.
- Kart seçme seçilir ise kartlar listelensin ve seçim yapılsın.
- Kart seçimi yapıldıktan sonra farklı kart seçme desteği olsun.
- Kart seçimi yapıldıktan sonra o kartla ilgili,
- Kart Kullan, Bakiye Yükle, Bakiye Sorgulama, Kart Bilgilerini Yazdırma işlevleri olsun.
"""
import random
import time

class IzmirimKart():

    cards = list()
    price = 7

    def __init__(self,cardNo = None,name = "Tanımlanmadı", surname = "Tanımlanmadı",credit = 0):
        # Eğer değişken başına _ koyulursa private olarak çalışır.
        self._cardNo = self.createRandomCardNo() # private
        self._name = name # private
        self._surname = surname # private
        self._credit = credit # private

    def getCardNo(self):
        return self._cardNo

    def getName(self):
        return self._name

    def getSurname(self):
        return self._surname

    def getCredit(self):
        return self._credit

    def setCardNo(self, value):
        self._cardNo = value

    def setName(self, value):
        self._name = value

    def setSurname(self, value):
        self._surname = value

    def setCredit(self, value):
        self._credit = value

    def __str__(self):
       return "Kart No: {}\tAd Soyad: {}\tBakiye: {}₺".format(self.getCardNo(), self.getName() +" "+self.getSurname(), self.getCredit())

    def createRandomCardNo(self):
        while True:
            randomCardNo = random.randint(1,999999)
            matchCardNo = False

            for i in IzmirimKart.cards:
                if i.getCardNo() == randomCardNo:
                    matchCardNo = True

            if matchCardNo == True:
                #print("Kart numarası aynı geldi")
                continue
            else:
                return randomCardNo

    def useCard(self):
        if self.getCredit() < IzmirimKart.price:
            print("Bakiyeniz yetersiz.")
        else:
            self.setCredit(self.getCredit() - IzmirimKart.price)
            print("Geçiş başarılı! Kesilen tutar: {} Kalan bakiye: {}".format(IzmirimKart.price, self.getCredit()))

def createCard(inputName, inputSurname):
    IzmirimKart.cards.append(IzmirimKart(name = inputName, surname = inputSurname))
    print("Kartınız listeye eklendi.")

cardIndex = None
while True:
    if cardIndex == None:
        print("""
        1- Yeni Kart Oluştur
        2- Kart Seç
        0- Çıkış
        """)
        secim = int(input("İşlem numaranızı tuşlayınız: "))
        if secim == 0:
            print("Çıkış yapıldı.")
            break

        if secim == 1: # Kart Oluşturma
            inputName = input("Adınızı giriniz: ")
            inputSurname = input("Soyadınızı giriniz: ")

            if inputName == "" or inputSurname == "": # Girilmeyen bir veri var mı?
                print("İsim ve soyisim verisi girmediniz.")
                continue
            else:
                createCard(inputName, inputSurname) # Kart Oluşturma Methodu
        elif secim == 2:
            if len(IzmirimKart.cards) <= 0:
                print("Listede hiç kart bulunamadı!")
                continue

            counter = 1
            for i in IzmirimKart.cards:
                print(counter,"-", end=" ")
                print(i)
                counter += 1

            cardIndex = int(input("İşlem yapmak istediğiniz kart numarasını tuşlayın: "))-1
            if cardIndex >= len(IzmirimKart.cards) or cardIndex < 0:
                print("Olmayan bir kart numarası tuşladınız!")
                cardIndex = None
                continue
            else:
                continue

        else:
            print("Hatalı tuşlama yaptıınz!")
            continue
    else:
        card = IzmirimKart.cards[cardIndex]
        print("Hoşgeldiniz,",card.getName(),card.getSurname())
        print("""
        1- Bakiye sorgula
        2- Bakiye yükle
        3- Kart kullan
        4- Kart bilgilerini yazdır
        5- Farklı kart seç
        0- Çıkış
        """)
        secim = int(input("İşlem numaranızı tuşlayınız: "))

        if secim == 0:
            print("Çıkış yapıldı.")
            break

        if secim == 1:
            print("Bakiyenizi sorguluyorum, lütfen bekleyiniz...")
            time.sleep(2)
            print("Kart Bakiyeniz: ",card.getCredit(),"₺")
        elif secim == 2:
            addCredit = int(input("Kaç ₺ yüklensin ?"))
            if (addCredit <= 0 or addCredit == None):
                print("Kredi tutarını geçersiz girdiniz.")
                continue
            else:
                tempCredit = card.getCredit()
                print("Bakiye yüklemesi yapılıyor, lütfen bekleyiniz...")
                time.sleep(1)
                card.setCredit(card.getCredit() + addCredit)
                print("Kartınıza {}₺ yüklendi.\tEski bakiyeniz: {}₺\tYeni bakiyeniz: {}₺ ".format(addCredit, tempCredit,                                                                           card.getCredit()))
        elif secim == 3:
            card.useCard()
        elif secim == 4:
            print(card)
        elif secim == 5:
            cardIndex = None
            del card # Kullanılan nesne silindi.
            continue
        else:
            print("Hatalı işlem tuşladınız!")
            continue