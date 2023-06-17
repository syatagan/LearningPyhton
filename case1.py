##### MIUUUL DATA SCIENCE BOOTCAMP CASE 1 

#PYTHON PRACTICES
##########33
Görev 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
kelime kelime ayırınız
############
text = "deneme test,merhaba.NASILSIN,IYI GIDIYOR."
print(text.upper())
print(text.replace(","," "))
print(text.replace(".", " "))
text = text.upper()
text = text.replace("."," ")
text = text.replace(",", " ")
text.split() ## metinleri böler dilediğin seperatöre göre varsayılan özel karakterlere göre


#################
Görev 3: Verilen listeye aşağıdaki adımları uygulayınız.
lst=["D","A","T","A","S","C","I","E","N","C","E"]
Adım 1: Verilen listenin eleman sayısına bakınız.
Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
Adım 4: Sekizinci indeksteki elemanı siliniz.
Adım 5: Yeni bir eleman ekleyiniz.
Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

#########
lst=["D","A","T","A","S","C","I","E","N","C","E"]
len(lst)
print(lst[0])
print(lst[10])
new_list = lst[0:4]
print(new_list)
lst.pop(8)
print(lst)
lst.insert(8,"N")  #APPEND SONA EKLERKEN INSERT ISTENILEN INDEXE EKLEME YAPAR.
print(lst)

##############
Görev 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
Adım 1: Key değerlerine erişiniz.
Adım 2: Value'lara erişiniz.
Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
Adım 5: Antonio'yu dictionary'den siliniz
##############
dict= {'Chr' : ["America", 18],
       "Daisy" : ["England",12] ,
       "Antonia" : ["Spain" , 22],
       "Dante" : ["Italy" , 25]
}
dict.keys()
dict.values()
dict["Daisy"][1] = 13
print(dict["Daisy"])
dict.update({"Ahmet": ["Turkey",24]}) # ilgili key varsa günnceller, yoksa ekler.
dict.pop("Antonia")  ## keye bakarak silme işlemi yapar.
print(dict)


##########
Görev 5: Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri
return eden fonksiyon yazınız
#############

def f_ayi(xlist):
    xelist = []
    xolist = []
    for xnumber in xlist:
        if xnumber % 2 == 0:
            #çift sayı
            xelist.append(xnumber)
        else:
            xolist.append(xnumber)
    return xelist,xolist


##call
test_list=[2,13,18,93,22]
even_list, odd_list = f_ayir(test_list)

##############

Görev 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de
tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

############

ogrenciler = ["ALİ","Veli", "Ayşe" , "Talat" , "Zeynep" ,"Ece"]

for xi, xogrenci in enumerate(ogrenciler,1):
    if xi < 4:
        print(f"Mühendislik Fak {xi}. öğrenci : {xogrenci}")
    else:
        xderece = xi-3
        print(f"Tıp Fak {xderece}. öğrenci : {xogrenci}")

##############

Gorev 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer
almaktadır. Zip kullanarak ders bilgilerini bastırınız.

#############

ders_kodu=["cmp1005","psy1001","huk299","swn78"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

xtoplu = list(zip(ders_kodu,kredi,kontenjan))
#1.yol
for xders,xkredi,xkon in xtoplu:
    print(f"Kredisi {xkredi} olan {xders} kodlu dersin kontenjanı {xkon} kişidir.")
#2.yol
for xl in xtoplu:
    xders,xkredi,xkon=xl
    print(f"Kredisi {xkredi} olan {xders} kodlu dersin kontenjanı {xkon} kişidir.")


#########
Görev 8: Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını
eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###########

kume1=set(["data","pyhton"])
kume2=set(["data","func","qcut","lambda","pyhton","miuul"])

if kume1.issuperset(kume2):
    print(kume1.intersection(kume2))
else:
    print(kume2.difference(kume1))


#### comprehensions
#########
Görev 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük
harfe çeviriniz ve başına NUM ekleyiniz,
#########

import seaborn as sns
df = sns.load_dataset("car_crashes")
## kontrol ettim öncelikle
for xcol in df.columns:
    print(df[xcol].dtype)
["NUM_" + xcol.upper()  if df[xcol].dtype != "object" else xcol.upper() for xcol in df.columns]


########
Görev 2: List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan
değişkenlerin isimlerinin sonuna "FLAG" yazınız.
########

import seaborn as sns
df = sns.load_dataset("car_crashes")
print(df.columns)
[xcol.upper() + "_FLAG" if "no" not in xcol else xcol.upper() for xcol in df.columns]

########
Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan
değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz
#########

og_list=["abbrev","no_previous"]
import seaborn as sns
df = sns.load_dataset("car_crashes")

num_cols= [xcol for xcol in df.columns if xcol not in og_list]
df[num_cols].head()
