dost = {"piyon": "a",
                "kale": "b",
                "at": "c",
                "fil": "d",
                "vezir": "e",
                "sah": "f"}

dusman = {"piyon": "g",
                "kale": "h",
                "at": "i",
                "fil": "j",
                "vezir": "k",
                "sah": "l"}

class map:

    def __init__(self,x):
        global masa

        masa = x

    def kale_f(self,x, y, taraf):



        if taraf:
            do = dost
            du = dusman
        else:
            do = dusman
            du = dost
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

            if masa[kare] in do.values():
                break

            secenekler.append(kare)

            if masa[kare] in du.values():
                break

        while dogu < 8:
            dogu = dogu + 1
            kare = str(dogu) + str(y)

            if masa[kare] in do.values():
                break

            secenekler.append(kare)

            if masa[kare] in du.values():
                break

        while kuzey > 1:

            kuzey = kuzey - 1
            kare = str(x) + str(kuzey)

            if masa[kare] in do.values():
                break

            secenekler.append(kare)

            if masa[kare] in du.values():
                break

        while guney < 8:
            guney = guney + 1
            kare = str(x) + str(guney)
            if masa[kare] in do.values():
                break

            secenekler.append(kare)

            if masa[kare] in du.values():
                break

        return secenekler

    def fil_f(self,x, y, taraf):

        if taraf:
            do = dost
            du = dusman
        else:
            do = dusman
            du = dost

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
            kare = str(sag_alt_x) + str(sag_alt_y)
            if masa[kare] in do.values():
                break

            secenekler.append(kare)

            if masa[kare] in du.values():
                break

        while sag_ust_x < 8 and sag_ust_y > 1:
            sag_ust_x = sag_ust_x + 1
            sag_ust_y = sag_ust_y - 1
            kare = str(sag_ust_x) + str(sag_ust_y)
            if masa[kare] in do.values():
                break

            secenekler.append(kare)

            if masa[kare] in du.values():
                break

        while sol_alt_x > 1 and sol_alt_y < 8:
            sol_alt_x = sol_alt_x - 1
            sol_alt_y = sol_alt_y + 1
            kare = str(sol_alt_x) + str(sol_alt_y)
            if masa[kare] in do.values():
                break

            secenekler.append(kare)

            if masa[kare] in du.values():
                break

        while sol_ust_x > 1 and sol_ust_y > 1:
            sol_ust_x = sol_ust_x - 1
            sol_ust_y = sol_ust_y - 1
            kare = str(sol_ust_x) + str(sol_ust_y)
            if masa[kare] in do.values():
                break

            secenekler.append(kare)

            if masa[kare] in du.values():
                break

        return secenekler

    def at_f(self,x, y, taraf):
        if taraf:
            do = dost

        else:
            do = dusman

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

                if masa[i] in do.values():
                    f.append(i)

        for i in f:
            try:

                liste.remove(i)
            except:
                pass
        return liste

    def piyon_f(self,x, y, taraf):
        secenekler = []
        x = int(x)
        y = int(y)

        if taraf:
            kare = str(x) + str(y - 1)

            if (kare in masa.keys()) and (masa[kare] not in dusman.values()) and (masa[kare] not in dost.values()):
                secenekler.append(kare)

                kare = str(x) + str(y - 2)
                if (kare in masa.keys()) and (masa[kare] not in dusman.values()) and (masa[kare] not in dost.values()) and y == 7:
                    secenekler.append(kare)

            kare = [str(x + 1) + str(y - 1), str(x - 1) + str(y - 1)]

            for i in kare:
                if i in masa.keys():

                    if masa[i] in dusman.values():
                        secenekler.append(i)


        else:
            kare = str(x) + str(y + 1)
            
            if (kare in masa.keys()) and (masa[kare] not in dost.values()) and masa[kare] not in dusman.values():
                secenekler.append(kare)
                kare = str(x) + str(y + 2)

                if (kare in masa.keys()) and (masa[kare] not in dost.values()) and (masa[kare] not in dusman.values()) and y == 2:
                    secenekler.append(kare)

            kare = [str(x + 1) + str(y + 1), str(x - 1) + str(y + 1)]

            for i in kare:
                if i in masa.keys():
                    if masa[i] in dost.values():
                        secenekler.append(i)

        return secenekler

    def vezir_f(self,x, y, taraf):
        if taraf:
            do = dost
            du = dusman
        else:
            do = dusman
            du = dost

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

            if masa[kare] in do.values():
                break

            secenekler.append(kare)

            if masa[kare] in du.values():
                break

        while dogu < 8:
            dogu = dogu + 1
            kare = str(dogu) + str(y)

            if masa[kare] in do.values():
                break

            secenekler.append(kare)

            if masa[kare] in du.values():
                break

        while kuzey > 1:

            kuzey = kuzey - 1
            kare = str(x) + str(kuzey)

            if masa[kare] in do.values():
                break

            secenekler.append(kare)

            if masa[kare] in du.values():
                break

        while guney < 8:
            guney = guney + 1
            kare = str(x) + str(guney)
            if masa[kare] in do.values():
                break

            secenekler.append(kare)

            if masa[kare] in du.values():
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
            if masa[kare] in do.values():
                break

            secenekler.append(kare)

            if masa[kare] in du.values():
                break

        while sag_ust_x < 8 and sag_ust_y > 1:
            sag_ust_x = sag_ust_x + 1
            sag_ust_y = sag_ust_y - 1
            kare = str(sag_ust_x) + str(sag_ust_y)
            if masa[kare] in do.values():
                break

            secenekler.append(kare)

            if masa[kare] in du.values():
                break

        while sol_alt_x > 1 and sol_alt_y < 8:
            sol_alt_x = sol_alt_x - 1
            sol_alt_y = sol_alt_y + 1
            kare = str(sol_alt_x) + str(sol_alt_y)
            if masa[kare] in do.values():
                break

            secenekler.append(kare)

            if masa[kare] in du.values():
                break

        while sol_ust_x > 1 and sol_ust_y > 1:
            sol_ust_x = sol_ust_x - 1
            sol_ust_y = sol_ust_y - 1
            kare = str(sol_ust_x) + str(sol_ust_y)
            if masa[kare] in do.values():
                break

            secenekler.append(kare)

            if masa[kare] in du.values():
                break

        return secenekler

    def sah_f(self,x, y, taraf):
        if taraf:
            do = dost

        else:
            do = dusman

        x = int(x)
        y = int(y)
        secenekler = [str(x) + str(y - 1), str(x) + str(y + 1), str(x - 1) + str(y), str(x + 1) + str(y),
                      str(x + 1) + str(y + 1), str(x + 1) + str(y - 1), str(x - 1) + str(y - 1),
                      str(x - 1) + str(y + 1)]

        black_list = []

        for i in secenekler:

            if i not in masa.keys():
                black_list.append(i)
            else:

                if masa[i] in do.values():
                    black_list.append(i)

        for i in black_list:
            try:

                secenekler.remove(i)
            except:
                pass

        return secenekler


