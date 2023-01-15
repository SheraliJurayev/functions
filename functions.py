# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 04:10:42 2023

@author: Sh_Jurayeff
"""

#def salom_ber():
#    """Salom beruvchi funksya"""
#    print("Assalomu Alaykum")
#salom_ber()


#def salom_ber(ism):
#    """ Foydalanuvchi ismini qabul qilib, unga salom beruvchi funksya"""
#     print(salom_ber.__doc__)
#    print(f"Assalomu alaykum hurmatli , {ism.title()}")
#salom_ber("Dima")
#salom_ber("hoshim")    

#def toliq_ism(ism,familiya):
#    print(f"Foydalanuvchi ismi:{ism.title()} \n"
##          f"Foydalanuvchi familiyasi: :{familiya.title()}")
#    
#toliq_ism("Baxa", "tashkenskiy" )
#toliq_ism("Dima", "Buxa")

#def malumot_ber(ism,t_yil):
#    print(f"salom {ism.title()} , siz {2023-t_yil} yoshdasiz ")
#    
#malumot_ber("sherali", 2002)
    
#def kv_kub():
#    n=float(input("Istalgan son kiriting va bu dastur sizga u sobbbing ham vadarati ham kubini chiqarib beradi: "))
#    print(f"{n} ning kvadrati {n**2} ga , kubi esa {n**3} ga teng.")
#kv_kub()
    
#def juft_or_toq():
#    n=float(input("Istalgan son kiriting va bu dastur sizga qanday son kiritganingizni aytadi. "))
#    if n%2==0:
#        print("Juft son kirittingiz")
#    else: print("Toq son kiritdingiz")
#juft_or_toq()
    
#def taqqosla(n,m):
#    if n>m :
#        print(n)
#    elif n<m:
#        print(m)
#    else:
#        print("Sonlar teng")
        
#taqqosla(4, 3)      
#3taqqosla(3, 8)    
#taqqosla(5, 5)  
            
#def daraja(x,y):
#        print(x**y)
#daraja(3, 4)
    
#def daraja(x,y=2):
#        print(x**y)
#daraja(6)    
    

#def bolinish_alomatlari(son):
#    for n in range(2, 11):
#        if not son % n:
#            print(f"{son} {n} ga qoldiqsiz bo'linadi")
#        else:
#            print(f"{son} {n} ga bo'linmaydi" )
#
#
#bolinish_alomatlari(20)
    
#def avto_info(kompaniya,model,rangi,karobka,yili,narhi=None):
#    avto={'kompaniya':kompaniya,
#          'model':model,
#          'rangi':rangi,
#          'karobka':karobka,
#          'yili':yili,
#          'narhi':narhi }    
#    
#    return avto
#avto1=avto_info('GM', "Malibu", "qora", "avtomat",2018)
#avto2=avto_info('GM', "Gentra", "oq", "mexanika",2018,17000)
#avtolar=[avto1,avto2]
#
#print("Onlayn bozordagi mavjud avtomashinalar: ")
#for avto in avtolar:
#    if avto['narhi']:
#        narh=avto['narhi']
#    else:
#            narh="Noma'lum"
#    print(f"{avto['rangi']} {avto['model']}. Narhi:{narh}")        

 
#def oraliq_range(min,max,step=None):
#    sonlar=[]
#    while min<max:
#        sonlar.append(min)
#        if step==None:
#            min+=1
#        else:        
#            min+=step
#    return sonlar   
# 
#    
#print(oraliq_range(100, 1001))    


    
#def avto_info(kompaniya,model,rangi,karobka,yili,narhi=None):
#    avto={'kompaniya':kompaniya,
#          'model':model,
#          'rangi':rangi,
#          'karobka':karobka,
#          'yili':yili,
#          'narhi':narhi }    
#   
#    return avto
#    
#print("Saytimizdagi mashinalar ro'yxatini shakllantramiz.")
#avtolar=[]
#while True:
#    print("\n Quyidagi ma'lumotlarni kiriting",end="")
#    kompaniya=input("Ishlab chiqaruvchi: ")
#    model=input("Modeli: ")
#    rangi=input("Rangi: ")
#    karobka=input("Karobka: ")
#    yili=input("Yili: ")
#    narhi=input("Narhi: ")
#    avtolar.append(avto_info(kompaniya, model, rangi, karobka, yili,narhi))
#    javob=input("Yana avto qo'shasizmi? yes/no ")
#    
#    if javob=='no':
#        break
#print("\n Salonimizdagi avtolar:")
#for avto in avtolar:
#    if avto['narhi']:
#        narh=avto['narhi']
#    else:
#        narh="Noma'lum"
#    print(f"{avto['rangi'].title()} {avto['model'].title()},{karobka} karobka. Narhi:{narhi}")
######    
    
#def bahola(ismlar):
#    baholar={}
#    while ismlar:
#        ism=ismlar.pop()
#        baho=input(f"Talaba {ism.title()} ga baho qo'ying: ")
#        baholar[ism]=int(baho)
#    return baholar
#        
#talabalar = ['ali','vali','hasan','husan']
#baholar = bahola(talabalar[:])  # 4
#print(baholar)
#print(talabalar)
    
    
#  *args va *kwargs
#def summa(*sonlar): # <-> *args
#    """KIRITILGAN SONLAR YIG'INDISINI HISOBLOVCHI FUNKSYA"""
#    yigindi = 0
#    for son in sonlar:
#       yigindi += son
#    return yigindi    
#print(summa(21,21,1,21,323,43,54,5,3,4,32,3,54,65,67,67,5,45))    
    
#def avto_info(kompaniya,model,**malumotlar): # <--> *kwargs
#        """AVTO HAQIDAGI MA'LUMOTLARNI LUG'AT KO'RINISHIDA QAYTARUVCHI FUNKSYA"""
#        malumotlar['kompaniya']=kompaniya
#        malumotlar['model']=model
#        return malumotlar
#avto1=avto_info('GM', 'Malibu',rang='qora',yil=2018)
#avto2=avto_info('Kia', 'K5', rang='silver' , narh=40000,yil=2020)    
#
#print(avto1)
    
    
    
    
    
    
    
    
    
    
    