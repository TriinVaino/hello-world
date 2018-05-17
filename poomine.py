def poomismäng ():
    import random
    import turtle
    x=0
    konn=turtle.Turtle()
    konn.speed(1)
    konn.pencolor("green")
    pann=turtle.Turtle()
    pann.speed(1)
    pann.pensize(5)
    pann.pencolor("yellow")
    sõnad=['elektron', 'prooton', 'neutron', 'aatom', 'molekul', 'aine','süsinik',
           'vesinik','heelium', 'hapnik', 'alumiinium', 'naatrium', 'kaalium', 'kaltsium', 'kuld', 'elavhõbe',
           'magneesium', 'raud', 'reaktsioon' ]
    sõna=random.choice(sõnad)
    print(" ")
    print("Tere tulemast keemilisse poomismängu. Ekraanile ilmub peidetud sõna kirjutatud vertikaalselt ülevalt alla.")
    print("Sinu ülesanne on sõna ära arvata, pakkudes erinevaid tähti, kuid ole ettevaatlik, sest katseid on piiratud hulk")
    print("Psst! Väike vihje: kõik sõnad on seotud keemiaga. Edu! :) ")

    def uusmäng():
        print("Sinu vigade arv on", x)
        vastus=input("Kas te soovite uuesti mängida? (vasta jah või ei) "  )
        if vastus == "jah":
            turtle.resetscreen()
            poomismäng()
        if vastus == "ei":
            print("Väga kahju on näha teid minemas. Aitäh meiega mängimast. ")
            exit()
        else:
            print("Kahjuks ei mõista me teie vastust. Olge kindel, et kirjutate väikeste tähtedega ja tühikuteta. Vastake kas jah või ei")
            uusmäng()


    for i in sõna:
        print ("_")

    tähelist=list(sõna)
    #print(sõna) #KAOTA SEE SPIKKER

#strike1
    esimene = input("Teie esimene pakkumine, palun  ")
    if esimene == sõna:
          print (sõna)
          print("Palju õnne, olete olnud eriti taibukas.")
          uusmäng()

    elif esimene in tähelist:
        for i in tähelist:
            if i == esimene:
                print (i)
            else:
                print ("_")
    else:
        print("Vale, proovi uuesti")
        konn.pendown()
        konn.left(90)
        konn.forward(200)
        x=x+1

#strike2
    teine = input ("Teie teine pakkumine, palun  ")
    if teine == sõna:
          print ("Ja õige vastus on", sõna)
          print("Palju õnne, olete arvanud õigesti, ja ürpis kiiresti, peaksin mainima.")
          uusmäng()

    elif teine in tähelist:
        for i in tähelist:
            if i == teine:
                print (teine)
            elif i == esimene:
                print (esimene)
            else:
                print ("_")
    else:
        print("Vale, proovi uuesti")
        if x == 0:
            konn.pendown()
            konn.left(90)
            konn.forward(200)
            x=x+1
        elif x == 1:
            konn.left(90)
            konn.forward(50)
            x=x+1

    
#strike3
    kolmas = input("Teie kolmas pakkumine, palun  ")
    if kolmas == sõna:
          print (sõna)
          print("Palju õnne, õige vastus!")
          uusmäng()

    elif kolmas in tähelist:
        for i in tähelist:
            if i == kolmas:
                print (kolmas)
            elif i == teine:
                print (teine)
            elif i == esimene:
                print (esimene)
            else:
                print ("_")

    else:
        print("Vale, proovi uuesti")
        if x == 0:
            konn.pendown()
            konn.left(90)
            konn.forward(200)
            x=x+1
        elif x == 1:
            konn.left(90)
            konn.forward(50)
            x=x+1
        elif x == 2:
            konn.left(90)
            konn.forward(30)
            konn.penup()
            konn.right(90)
            konn.forward(8)
            konn.pendown()
            konn.pensize(5)
            konn.circle(20)
            x=x+1

#strike4
    neljas = input("Teie neljas pakkumine, palun. Ragistage ajusid, sest olukord on juba hapu!  ")
    if neljas == sõna:
          print (sõna)
          print("Väga hea tulemus, lilleke, see oli õige vastus!")
          uusmäng()

    elif neljas in tähelist:
        for i in tähelist:
            if i == neljas:
                print (i)
            elif i == kolmas:
                print (i)
            elif i == teine:
                print (i)
            elif i == esimene:
                print (i)
            else:
                print ("_")
                

    else:
        print("Vale, proovi uuesti")
        if x == 0:
            konn.pendown()
            konn.left(90)
            konn.forward(200)
            x=x+1
        elif x == 1:
            konn.left(90)
            konn.forward(50)
            x=x+1
        elif x == 2:
            konn.left(90)
            konn.forward(30)
            konn.penup()
            konn.right(90)
            konn.forward(8)
            konn.pendown()
            konn.pensize(5)
            konn.circle(20)
            x=x+1
        elif x == 3:
            pann.penup()
            pann.left(180)
            pann.forward(25)
            pann.right(90)
            pann.forward(40)
            pann.pendown()
            pann.left(37)
            pann.forward(35)
            x=x+1
        

#strike5
    viies=input("Teie viies pakkumine, palun.  ")
    if viies == sõna:
          print (sõna)
          print("Palju õnne, olete viimaks arvanud õieti.")
          uusmäng()

    elif viies in tähelist:
        for i in tähelist:
            if i == viies:
                print (i)
            elif i == neljas:
                print (i)
            elif i == kolmas:
                print (i)
            elif i == teine:
                print (i)
            elif i == esimene:
                print (i)
            else:
                print ("_")
    else:
        print("Vale, proovi uuesti")
        if x == 0:
            konn.pendown()
            konn.left(90)
            konn.forward(200)
            x=x+1
        elif x == 1:
            konn.left(90)
            konn.forward(50)
            x=x+1
        elif x == 2:
            konn.left(90)
            konn.forward(30)
            konn.penup()
            konn.right(90)
            konn.forward(8)
            konn.pendown()
            konn.pensize(5)
            konn.circle(20)
            x=x+1
        elif x == 3:
            pann.penup()
            pann.left(180)
            pann.forward(25)
            pann.right(90)
            pann.forward(40)
            pann.pendown()
            pann.left(37)
            pann.forward(35)
            x=x+1
        elif x == 4:
            pann.left(106)
            pann.forward(35)
            x=x+1

#strike6
    kuues=input("Teie kuues pakkumine, palun. Kokku on 8 pakkumist, parem kiirustage!  ")
    if kuues == sõna:
          print (sõna)
          print("Palju õnne, olete arvanud õieti!")
          uusmäng()

    elif kuues in tähelist:
        for i in tähelist:
            if i == kuues:
                print (i)
            elif i == viies:
                print (i)
            elif i == neljas:
                print (i)
            elif i == kolmas:
                print (i)
            elif i == teine:
                print (i)
            elif i == esimene:
                print (i)
            else:
                print ("_")
    else:
        print("Vale, proovi uuesti")
        if x == 0:
            konn.pendown()
            konn.left(90)
            konn.forward(200)
            x=x+1
        elif x == 1:
            konn.left(90)
            konn.forward(50)
            x=x+1
        elif x == 2:
            konn.left(90)
            konn.forward(30)
            konn.penup()
            konn.right(90)
            konn.forward(8)
            konn.pendown()
            konn.pensize(5)
            konn.circle(20)
            x=x+1
        elif x == 3:
            pann.penup()
            pann.left(180)
            pann.forward(25)
            pann.right(90)
            pann.forward(40)
            pann.pendown()
            pann.left(37)
            pann.forward(35)
            x=x+1
        elif x == 4:
            pann.left(106)
            pann.forward(35)
            x=x+1
        elif x == 5:
            pann.left(180)
            pann.forward(35)
            pann.pencolor("orange")
            pann.left(35)#kui palju keha jaoks pöörab
            pann.forward(60)
            x=x+1

    
#strike7
    seitse=input("Teie seitsmes pakkumine, palun.  ")
    if seitse == sõna:
          print (sõna)
          print("Palju õnne, olete olnud eriti taibukas.")
          uusmäng()

    elif seitse in tähelist:
        for i in tähelist:
            if i == seitse:
                print (i)
            elif i == kuues:
                print (i)
            elif i == viies:
                print (i)
            elif i == neljas:
                print (i)
            elif i == kolmas:
                print (i)
            elif i == teine:
                print (i)
            elif i == esimene:
                print (i)
            else:
                print ("_")
    else:
        print("Vale, proovi uuesti")
        if x == 0:
            konn.pendown()
            konn.left(90)
            konn.forward(200)
            x=x+1
        elif x == 1:
            konn.left(90)
            konn.forward(50)
            x=x+1
        elif x == 2:
            konn.left(90)
            konn.forward(30)
            konn.penup()
            konn.right(90)
            konn.forward(8)
            konn.pendown()
            konn.pensize(5)
            konn.circle(20)
            x=x+1
        elif x == 3:
            pann.penup()
            pann.left(180)
            pann.forward(25)
            pann.right(90)
            pann.forward(40)
            pann.pendown()
            pann.left(37)
            pann.forward(35)
            x=x+1
        elif x == 4:
            pann.left(106)
            pann.forward(35)
            x=x+1
        elif x == 5:
            pann.left(180)
            pann.forward(35)
            pann.pencolor("orange")
            pann.left(35)#kui palju keha jaoks pöörab
            pann.forward(60)
            x=x+1
        elif x == 6:
            pann.pencolor("red")
            pann.left(90)
            pann.forward(30)
            x=x+1
    

#strike8
    kaheksa=input("Teie kaheksas ja viimane võimalus midagi tarka esile manada,palun.  ")
    if kaheksa == sõna:
          print (sõna)
          print("Palju õnne, veel viimasel hetkel arvasite õieti ära, olen uhke.")
          uusmäng()

    else:
        print("Selle mängu te kaotasite.")
        print("Õige vastus oli", sõna)
        if x == 0:
            konn.pendown()
            konn.left(90)
            konn.forward(200)
            #strike2
            konn.left(90)
            konn.forward(50)
#strike3
            konn.left(90)
            konn.forward(30)
            konn.penup()
            konn.right(90)
            konn.forward(8)
            konn.pendown()
            konn.pensize(5)
            konn.circle(20)

#strike4
            pann.penup()
            pann.left(180)
            pann.forward(25)
            pann.right(90)
            pann.forward(40)
            pann.pendown()
            pann.left(37)
            pann.forward(35)
#strike5
            pann.left(106)
            pann.forward(35)
#strike6
            pann.left(180)
            pann.forward(35)
            pann.pencolor("orange")
            pann.left(35)#kui palju keha jaoks pöörab
            pann.forward(60)
#strike7
            pann.pencolor("red")
            pann.left(90)
            pann.forward(30)
#strike8
            pann.backward(60)
            x=x+1
        elif x == 1:
            konn.left(90)
            konn.forward(50)
            konn.left(90)
            konn.forward(30)
            konn.penup()
            konn.right(90)
            konn.forward(8)
            konn.pendown()
            konn.pensize(5)
            konn.circle(20)

#strike4
            pann.penup()
            pann.left(180)
            pann.forward(25)
            pann.right(90)
            pann.forward(40)
            pann.pendown()
            pann.left(37)
            pann.forward(35)
#strike5
            pann.left(106)
            pann.forward(35)
#strike6
            pann.left(180)
            pann.forward(35)
            pann.pencolor("orange")
            pann.left(35)#kui palju keha jaoks pöörab
            pann.forward(60)
#strike7
            pann.pencolor("red")
            pann.left(90)
            pann.forward(30)
#strike8
            pann.backward(60)
            x=x+1
        elif x == 2:
            konn.left(90)
            konn.forward(30)
            konn.penup()
            konn.right(90)
            konn.forward(8)
            konn.pendown()
            konn.pensize(5)
            konn.circle(20)
            pann.penup()
            pann.left(180)
            pann.forward(25)
            pann.right(90)
            pann.forward(40)
            pann.pendown()
            pann.left(37)
            pann.forward(35)
#strike5
            pann.left(106)
            pann.forward(35)
#strike6
            pann.left(180)
            pann.forward(35)
            pann.pencolor("orange")
            pann.left(35)#kui palju keha jaoks pöörab
            pann.forward(60)
#strike7
            pann.pencolor("red")
            pann.left(90)
            pann.forward(30)
#strike8
            pann.backward(60)
            x=x+1
        elif x == 3:
            pann.penup()
            pann.left(180)
            pann.forward(25)
            pann.right(90)
            pann.forward(40)
            pann.pendown()
            pann.left(37)
            pann.forward(35)
            pann.left(106)
            pann.forward(35)
#strike6
            pann.left(180)
            pann.forward(35)
            pann.pencolor("orange")
            pann.left(35)#kui palju keha jaoks pöörab
            pann.forward(60)
#strike7
            pann.pencolor("red")
            pann.left(90)
            pann.forward(30)
#strike8
            pann.backward(60)
            x=x+1
        elif x == 4:
            pann.left(106)
            pann.forward(35)
            pann.left(180)
            pann.forward(35)
            pann.pencolor("orange")
            pann.left(35)#kui palju keha jaoks pöörab
            pann.forward(60)
#strike7
            pann.pencolor("red")
            pann.left(90)
            pann.forward(30)
#strike8
            pann.backward(60)
            x=x+1
        elif x == 5:
            pann.left(180)
            pann.forward(35)
            pann.pencolor("orange")
            pann.left(35)#kui palju keha jaoks pöörab
            pann.forward(60)
            pann.pencolor("red")
            pann.left(90)
            pann.forward(30)
#strike8
            pann.backward(60)
            x=x+1
        elif x == 6:
            pann.pencolor("red")
            pann.left(90)
            pann.forward(30)
            pann.backward(60)
            x=x+1
        uusmäng()

    return
poomismäng()




