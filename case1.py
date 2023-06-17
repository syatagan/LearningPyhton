    #PYTHON PRACTICES
##########33
2
############
text = "deneme test,merhaba."
print(text.upper())
print(text.replace(","," "))
print(text.replace(".", " "))
text = text.replace("."," ")
text = text.replace(",", " ")
text.split() ## metinleri böler dilediğin seperatöre göre varsayılan özel karakterlere göre


#################
3
#########
lst= []
lst=["D","A","T","A","S","C","I","E","N","C","E"]
len(lst)
print(lst[0])
print(lst[10])
print(lst[0:4])
lst.pop(8)
print(lst)
lst.insert(8,"N")  #APPEND SONA EKLERKEN INSERT ISTENILEN INDEXE EKLEME YAPAR.
print(lst)

##############
# gorev 4
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


##########3333
# görev 5
#############

l=[2,13,18,93,22]

def f_ayir(xlist):
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
even_list, odd_list = f_ayir(l)

##############
gorev 6
############3333333
ogrenciler = ["ALİ","Veli", "Ayşe" , "Talat" , "Zeynep" ,"Ece"]

for xi, xogrenci in enumerate(ogrenciler,1):
    if xi < 4:
        print(f"Mühendislik Fak {xi}. öğrenci : {xogrenci}")
    else:
        xderece = xi-3
        print(f"Tıp Fak {xderece}. öğrenci : {xogrenci}")

##############
gorev 7
#############
ders_kodu=["cmp1005","psy1001","huk299","swn78"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

xtoplu = list(zip(ders_kodu,kredi,kontenjan))
for xders,xkredi,xkon in xtoplu:
    print(f"Kredisi {xkredi} olan {xders} kodlu dersin kontenjanı {xkon} kişidir.")

#########
gorev 8
###########3
kume1=set(["data","pyhton"])
kume2=set(["data","func","qcut","lambda","pyhton","miuul"])

if kume1.issuperset(kume2):
    print(kume1.intersection(kume2))
else:
    print(kume2.difference(kume1))

#### comprehensions
######## gorev1
import seaborn as sns
df = sns.load_dataset("car_crashes")
## kontrol ettim öncelikle
for xcol in df.columns:
    print(df[xcol].dtype)
["NUM_" + xcol.upper()  if df[xcol].dtype != "object" else xcol.upper() for xcol in df.columns]


######## gorev2
import seaborn as sns
df = sns.load_dataset("car_crashes")
print(df.columns)
[xcol.upper() + "_FLAG" if "no" not in xcol else xcol.upper() for xcol in df.columns]

######## gorev3
og_list=["abbrev","no_previous"]
import seaborn as sns
df = sns.load_dataset("car_crashes")

num_cols= [xcol for xcol in df.columns if xcol not in og_list]
df[num_cols].head()
