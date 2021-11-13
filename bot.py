import random

dost = {"piyon" : "a",
"kale" : "b",
"at" : "c",
"fil" : "d",
"vezir" : "e",
"sah" : "f"}

dusman = {"piyon" : "g",
"kale" : "h",
"at" : "i",
"fil" : "j",
"vezir" : "k",
"sah" : "l"}

def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

def kale_f(x,y):

    secenekler = []

    x = int(x)
    y = int(y)
    dogu = x
    bati = x
    kuzey = y
    guney = y

    while bati > 1:

        bati = bati - 1
        kare = str(bati) + str(y)

        if masa[kare] in dost.values():
            break

        secenekler.append(kare)


        if masa[kare] in dusman.values():
            break


    while dogu < 8:
        dogu = dogu + 1
        kare = str(dogu) + str(y)

        if masa[kare] in dost.values():
            break

        secenekler.append(kare)

        if masa[kare] in dusman.values():
            break

    while kuzey > 1:

        kuzey = kuzey - 1
        kare = str(x) + str(kuzey)

        if masa[kare] in dost.values():
            break

        secenekler.append(kare)


        if masa[kare] in dusman.values():
            break


    while guney < 8:
        guney = guney + 1
        kare =   str(x) + str(guney)
        if masa[kare] in dost.values():
            break

        secenekler.append(kare)

        if masa[kare] in dusman.values():
            break




    return secenekler

def fil_f(x,y):
    secenekler = []

    x = int(x)
    y = int(y)

    sag_alt_x = x
    sag_alt_y = y

    sag_ust_x = x
    sag_ust_y = y

    sol_alt_x = x
    sol_alt_y = y

    sol_ust_x = x
    sol_ust_y = y

    while sag_alt_x < 8 and sag_alt_y < 8:
        sag_alt_x = sag_alt_x + 1
        sag_alt_y = sag_alt_y + 1
        kare = str(sag_alt_x)+str(sag_alt_y)
        if masa[kare] in dost.values():
            break

        secenekler.append(kare)


        if masa[kare] in dusman.values():
            break

    while sag_ust_x < 8 and sag_ust_y > 1:
        sag_ust_x = sag_ust_x + 1
        sag_ust_y = sag_ust_y - 1
        kare = str(sag_ust_x)+str(sag_ust_y)
        if masa[kare] in dost.values():
            break

        secenekler.append(kare)


        if masa[kare] in dusman.values():
            break

    while sol_alt_x > 1 and sol_alt_y < 8:
        sol_alt_x = sol_alt_x - 1
        sol_alt_y = sol_alt_y + 1
        kare = str(sol_alt_x)+str(sol_alt_y)
        if masa[kare] in dost.values():
            break

        secenekler.append(kare)


        if masa[kare] in dusman.values():
            break

    while sol_ust_x > 1 and sol_ust_y > 1:
        sol_ust_x = sol_ust_x - 1
        sol_ust_y = sol_ust_y - 1
        kare = str(sol_ust_x)+str(sol_ust_y)
        if masa[kare] in dost.values():
            break

        secenekler.append(kare)


        if masa[kare] in dusman.values():
            break

    return secenekler

def at_f(x,y):

    liste = []
    x = int(x)
    y = int(y)

    kuzey_dogu = str(x + 1) + str(y - 2)
    liste.append(kuzey_dogu)
    kuzey_bati = str(x - 1) + str(y - 2)
    liste.append(kuzey_bati)
    bati_kuzey = str(x - 2) + str(y + 1)
    liste.append(bati_kuzey)
    bati_guney = str(x - 2) + str(y - 1)
    liste.append(bati_guney)
    guney_bati = str(x - 1) + str(y + 2)
    liste.append(guney_bati)
    guney_dogu = str(x + 1) + str(y + 2)
    liste.append(guney_dogu)
    dogu_guney = str(x + 2) + str(y - 1)
    liste.append(dogu_guney)
    dogu_kuzey = str(x + 2) + str(y + 1)
    liste.append(dogu_kuzey)

    f = []

    for i in liste:

        if i not in masa.keys():
            f.append(i)
        else:

            if masa[i] in dost.values() :

                f.append(i)


    for i in f:
        try:

            liste.remove(i)
        except:
            pass
    return liste

def piyon_f(x,y,taraf):
    secenekler = []
    x = int(x)
    y = int(y)

    if taraf:
        kare = str(x) + str(y - 1)
        if (masa[kare] in masa.keys()) and masa[kare] not in dusman.values() and masa[kare] not in dost.values():
            secenekler.append(kare)
            kare = str(x) + str(y - 2)
            if masa[kare] not in dusman.values() and masa[kare] not in dost.values() and y == 2:
                secenekler.append(kare)

        kare = [str(x + 1) + str(y - 1), str(x - 1) + str(y - 1)]

        for i in kare:
            if i in masa.keys():

                if masa[i] in dusman.values():

                    secenekler.append(i)


    else:
        kare = str(x) + str(y + 1)

        if (masa[kare] in masa.keys()) and masa[kare] not in dost.values() and masa[kare] not in dusman.values():
            secenekler.append(kare)
            kare = str(x) + str(y - 2)
            if (masa[kare] not in dost.values()) and (masa[kare] not in dusman.values()) and y == 7:
                secenekler.append(kare)

        kare = [str(x + 1) + str(y + 1), str(x - 1) + str(y + 1)]

        for i in kare:
            if i in masa.keys():
                if masa[i] in dost.values():
                    secenekler.append(i)

    return secenekler

def vezir_f(x,y):
    secenekler = []

    x = int(x)
    y = int(y)

    dogu = x
    bati = x
    kuzey = y
    guney = y

    while bati > 1:

        bati = bati - 1
        kare = str(bati) + str(y)

        if masa[kare] in dost.values():
            break

        secenekler.append(kare)

        if masa[kare] in dusman.values():
            break

    while dogu < 8:
        dogu = dogu + 1
        kare = str(dogu) + str(y)

        if masa[kare] in dost.values():
            break

        secenekler.append(kare)

        if masa[kare] in dusman.values():
            break

    while kuzey > 1:

        kuzey = kuzey - 1
        kare = str(x) + str(kuzey)

        if masa[kare] in dost.values():
            break

        secenekler.append(kare)

        if masa[kare] in dusman.values():
            break

    while guney < 8:
        guney = guney + 1
        kare = str(x) + str(guney)
        if masa[kare] in dost.values():
            break

        secenekler.append(kare)

        if masa[kare] in dusman.values():
            break

    sag_alt_x = x
    sag_alt_y = y

    sag_ust_x = x
    sag_ust_y = y

    sol_alt_x = x
    sol_alt_y = y

    sol_ust_x = x
    sol_ust_y = y

    while sag_alt_x < 8 and sag_alt_y < 8:
        sag_alt_x = sag_alt_x + 1
        sag_alt_y = sag_alt_y + 1
        kare = str(sag_alt_x) + str(sag_alt_y)
        if masa[kare] in dost.values():
            break

        secenekler.append(kare)

        if masa[kare] in dusman.values():
            break

    while sag_ust_x < 8 and sag_ust_y > 1:
        sag_ust_x = sag_ust_x + 1
        sag_ust_y = sag_ust_y - 1
        kare = str(sag_ust_x) + str(sag_ust_y)
        if masa[kare] in dost.values():
            break

        secenekler.append(kare)

        if masa[kare] in dusman.values():
            break

    while sol_alt_x > 1 and sol_alt_y < 8:
        sol_alt_x = sol_alt_x - 1
        sol_alt_y = sol_alt_y + 1
        kare = str(sol_alt_x) + str(sol_alt_y)
        if masa[kare] in dost.values():
            break

        secenekler.append(kare)

        if masa[kare] in dusman.values():
            break

    while sol_ust_x > 1 and sol_ust_y > 1:
        sol_ust_x = sol_ust_x - 1
        sol_ust_y = sol_ust_y - 1
        kare = str(sol_ust_x) + str(sol_ust_y)
        if masa[kare] in dost.values():
            break

        secenekler.append(kare)

        if masa[kare] in dusman.values():
            break





    return secenekler

def sah_f(x,y):
    x = int(x)
    y = int(y)
    secenekler = [str(x) + str(y - 1), str(x) + str(y + 1), str(x - 1) + str(y), str(x + 1) + str(y), str(x + 1) + str(y + 1), str(x + 1) + str(y - 1), str(x - 1) + str(y - 1), str(x - 1) + str(y + 1)]

    black_list = []


    for i in secenekler:

        if i not in masa.keys():
            black_list.append(i)
        else:

            if masa[i] in dost.values() :

                black_list.append(i)

    for i in black_list:
        try:

            secenekler.remove(i)
        except:
            pass

    return secenekler

def planlama_dost(masa,layer):

    order = 1

    elementler = []

    for i in masa.keys():

        x = i[0]
        y = i[1]



        if masa[i] == dost["kale"]:

            liste = kale_f(x, y)


            for j in liste:

                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dost["kale"]

                move = [f"{layer}-{order}",True,m,f"kale>{j}"]
                elementler.append(move)
                order = order + 1



        if masa[i] == dost["fil"]:


            liste = fil_f(x, y)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dost["fil"]

                move = [f"{layer}-{order}", True, m, f"fil>{j}"]
                elementler.append(move)
                order = order + 1

        if masa[i] == dost["at"]:


            liste = at_f(x, y)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dost["at"]

                move = [f"{layer}-{order}", True, m, f"at>{j}"]
                elementler.append(move)
                order = order + 1

        if masa[i] == dost["piyon"]:


            liste = piyon_f(x, y, True)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dost["piyon"]

                move = [f"{layer}-{order}", True, m, f"piyon>{j}"]
                elementler.append(move)
                order = order + 1

        if masa[i] == dost["vezir"]:
            liste = vezir_f(x, y)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dost["vezir"]

                move = [f"{layer}-{order}", True, m, f"vezir>{j}"]
                elementler.append(move)
                order = order + 1



        if masa[i] == dost["sah"]:

            liste = sah_f(x, y)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dost["sah"]

                move = [f"{layer}-{order}", True, m, f"sah>{j}"]
                elementler.append(move)
                order = order + 1

    return elementler

def planlama_dusman(masa,layer):
    order = 1

    elementler = []

    for i in masa.keys():

        x = i[0]
        y = i[1]



        if masa[i] == dusman["kale"]:

            liste = kale_f(x, y)


            for j in liste:

                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dusman["kale"]

                move = [f"{layer}-d{order}",False,m,f"d_kale>{j}"]
                elementler.append(move)
                order = order + 1



        if masa[i] == dusman["fil"]:


            liste = fil_f(x, y)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dusman["fil"]

                move = [f"{layer}-d{order}", False, m, f"d_fil>{j}"]
                elementler.append(move)
                order = order + 1

        if masa[i] == dusman["at"]:


            liste = at_f(x, y)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dusman["at"]

                move = [f"{layer}-d{order}", False, m, f"d_at>{j}"]
                elementler.append(move)
                order = order + 1

        if masa[i] == dusman["piyon"]:


            liste = piyon_f(x, y, False)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dusman["piyon"]

                move = [f"{layer}-d{order}", False, m, f"d_piyon>{j}"]
                elementler.append(move)
                order = order + 1

        if masa[i] == dusman["vezir"]:
            liste = vezir_f(x, y)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dusman["vezir"]

                move = [f"{layer}-d{order}", False, m, f"d_vezir>{j}"]
                elementler.append(move)
                order = order + 1



        if masa[i] == dusman["sah"]:

            liste = sah_f(x, y)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dusman["sah"]

                move = [f"{layer}-d{order}", False, m, f"d_sah>{j}"]
                elementler.append(move)
                order = order + 1

    return elementler

def new_hamle_dost(z):
    x = planlama_dost(z[2], z[0])

    return x

def new_hamle_dusman(z):
    x = planlama_dusman(z[2], z[0])

    return x

def main(pozisyonlar):

    print("started")

    global masa
    global alfa
    masa = {}

    for i in range(8):
        for j in range(8): #aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
            masa[str(j + 1)+ str(i + 1) ] = ""

    pozisyonlar_ = Convert(pozisyonlar)
    pozisyonlar_ =  [q for q in pozisyonlar_ if q != "\n"]
    for i in range(len(pozisyonlar_)):
        p = pozisyonlar_[i]


        masa[list(masa.keys())[i]] = p



    print("the progress has begun")



    x = planlama_dost(masa,1)


    alfa = []

    alfa.append(["1","","","",len(x)])



    y = []


    def won(x):
        if dusman["sah"] not in list(x[2].values()):

            win = x[0] + "-" + x[3] + "-win"

            alfa.append(win)

        else:

            alfa.append(x)

            y.append(x)



    for i in x:

        won(i)




    def ayikla(x,po):



        ayik = []



        for i in range(len(alfa)):


            if alfa[i][0] == x:



                ay = alfa[i][0].split("-")[:-2]

                spl = ""

                for s in ay:
                    spl = spl + "-" + s

                spl = spl[1:]


                for j in alfa:
                    if j[0] == spl:


                        j[4] = po


                ayik.append(i)

        for i in ayik:


            del alfa[i]

    print(masa)
    loop = int(input("layer number: "))

    for que in range(loop):

        z = None


        for i in y:



            y = [q for q in y if q != i]

            n = new_hamle_dusman(i)

            d_len = len(n)

            for w in n:



                alfa.append(w)
                z = True

                if dost["sah"] not in list(w[2].values()):



                    sp = w[0].split("-")[:-1]

                    spl = ""

                    for s in sp:

                        spl = spl + "-" + s



                    yalnis = spl[1:]

                    t = new_hamle_dost(w)
                    po = len(t)



                    ayikla(yalnis,po)

                    z = False
                    break


            if z:
                pos = None
                for w in n:

                    t = new_hamle_dost(w)
                    pos = len(t)



                    for j in t:

                        won(j)

                i.append(pos)

                i.append(d_len)


    while 1:

        wan = []
        per = False
        for i in alfa:
            if i[1]:

                if type(i) != str:

                    if len(i) > 4 and i[4] < 1:

                        wan.append(i)
                        per = True


        if per:

            for i in wan:

                sp = i[0].split("-")[:-1]

                spl = ""

                for s in sp:
                    spl = spl + "-" + s

                yalnis = spl[1:]

                ayikla(i[0], i[4] - 1)

                ayikla(yalnis,i[4] - 1)

        else:
            break


    print("finished")



    def next_f(x,y):
        next_play = random.randint(1, y)
        cor = f"{x}-{next_play}"
        return cor







    def second_move(x):



        posib_c = []



        if len(x) > 4:
            for i in range(x[5]):

                for j in alfa:

                    if not j[1] and j[0] == x[0]+"-d" + str(i + 1):
                        posib_c.append(j)


            for i in posib_c:
                print(i[3])

            want = next_f(posib_c[int(input("")) - 1][0], x[4])



            for i in alfa:


                if type(i) == str:

                    if i.split("-")[:-2] == want.split("-"):
                        print("do it: " + str(i.split("-")[-2]))
                        exit()

                elif i[0] == want:
                    print(i[2])
                    print("do it: " + str(i[3]))
                    return i




    if alfa[0][0] == "1":
        gama = alfa[0]


        for i in alfa:
            if i[0] == next_f("1",gama[4]):


                first_move = i
                print( "do it: "+ str(i[3]))

                for j in range(loop + 1):

                    first_move = second_move(first_move)

    else:
        print("there is nothing you can do bitch")

if __name__ == '__main__':


    x = open(r"C:\Users\aliek\Desktop\projeler\python\satranç_BOT\puzzle_2.txt","r")
    f = x.read()
    #f = dost["sah"]  + "----"+ dusman["sah"]

    main(f)
