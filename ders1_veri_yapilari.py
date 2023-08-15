# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:28:48 2020

@author: m.acilar
"""
# =============================================================================
# LIST
# TUPLE
# DICTIONARY
# SET
# =============================================================================
#list :  1) index'e göre sıralı erişimi, index her zaman 0 baslar
#        2) İçeriğini değiştirebiliyorum
#        3) İçerisinde farklı tiplerde veri tutabiliyorum
#Nasıl tanımlanır? [] veya list() fonksiyonunu kullanarak

fiyat=[50,55,45,18,'merhaba']
len(fiyat)
karma=[5,3,6,'m']
type(karma)
karma2=[22,16,karma]
len(karma2)
print(karma[2])
# karma'nın ilk 3 elemanını ekrana yazdıralım
#yani 0. index'den 3'e kadar olanı
karma[0:3] # 0. index dahil, 3. index dahil degil
print(karma[0:3])
print(karma[:3])
print(karma[2:]) # 2. indexden baslayıp sona kadar
# fiyat listesinde 55 ve 45 yazdırın
print(fiyat[1:3]) #1. indexi yaz, 3. index yazmiyor
#karma2'nin içindeki 'm' elemanını yazdırmak istiyorum
print(karma2[2][3])
fiyat2=[23,52,60]
fiyat_tum=fiyat+fiyat2
del fiyat #listeyi silmek için kullanıyorum, kullanılmayan listeler hafıza bosuna yer işgal etmesin diye kullanırım bu komutu
#karma2 listesinin içindeki 'm' stringini 'merhaba' yapmak istiyorum
karma2[2][3]="merhaba"# bu kod satırını çalıştırınca, karma2'nin içindeki karma listesindeki 'm' stringide değişir
# fiyat_tum listesinin icindeki 23 ve 52 değerlerini, sırası ile 40 ve 100 yapalım
# yani 23->40 , 52->100 yazılacak
fiyat_tum[4:6]=40,100
# listeye yeni eleman ekleme
fiyat2=fiyat2+[70]
#listeden eleman silme
#Ornek: fiyat 2'de 23 silelim
del fiyat2[0]
# Liste için kullanılan fonksiyonlar
#append : mevcut listenin sonuna, arguman olarak aldığı degeri ekler
fiyat2.append(12)
fiyat2.remove(70) # arguman olarak, silmek istediğim degeri direkt veriyorum. Index'ini vermiyorum
# insert ve pop komutları
fiyat2.insert(1,15) # fiyat2'nin 1. indexine 15 sayısını eklemek için
fiyat2.pop(2) # fiyat2'nin 2. indexinde bulunan değeri siler
fiyat2.pop(5) # 5. elemanı olmadığı için hata verecek :" pop index out of range"
#sort: listeleri sıralar.
fiyat_tum.sort()
fiyat2.clear() # listenin eleman sayısını sıfırlıyor
fiyat_tum.count(40) # arguman olarak aldıgı degerin, listede kaç tane oldugunu sayar

# =============================================================================
# # Tuple : Birbirinden farklı eleman tutabilir, 
#           indexleme vardır, 
#           DEGİSTİRİLEMEZLER
#           olusturma () kullanarak olusturabilirim
# =============================================================================
# olusturma () kullanarak olusturabilirim
t=("Merhaba",1,15)
#indexleme işlemlerinde herzaman [] kullanılyorum
t(2) # hatalı index erişimi : "'tuple' object is not callable"
t[2] # doğru index erişimi
t[2]=30 # hata verir. cunku tuple değiştirilemez : TypeError: 'tuple' object does not support item assignment
t2=("bilgisayar",) # tek elemanlı tuple tanımlarken sonuna virgul koymayı unutmuyoruz !!
# =============================================================================
# # Dictionary : Birbirinden farkli eleman tutabilir, 
#                değiştirilebilir 
#                ancak index kavramı yok, 
#                 yani indexe göre sırasızdır.
#                key-value mantıgı ile çalışır
#                tanımlarken {} parantez kullanılır
# =============================================================================
# tanımlarken {} parantez kullanılır
sozluk={"ock":"OCAK","sbt":"SUBAT","mrt":"MART","gun":30}
sozluk["sbt"]
sozluk["mrt"]="MART1"
sozluk[0] # hata verir, indexleme yok: "KeyError: 0"
sozluk2={"ock":["OCAK",31], "sbt":["SUBAT",28],"mrt":["MART",31]}
sozluk2["sbt"][1]
# yeni eleman ekleme
sozluk["nsn"]="NISAN"
#key değerleri sabit veri yapıları olarak atanmalıdır. orneğin liste tipinde bir key olamaz ama tuple tipinde olabilir
t=("tuple",1)
sozluk[t]="Haziran"

# =============================================================================
# # SET : Sırasızdır yani index yok sozluk gibi, 
#         içindeki değerler eşsizdir, 
          #değiştirilebilir, 
          #farklı tipleri barındırabilir.
# #       yani içindeki veriler unique'dir. 
#         Performas için kullanımı tercih edilir
# # set olusturma
# =============================================================================
lst=[1,"a",123,"a"]
s=set(lst)
s
