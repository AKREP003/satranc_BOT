
#dont ask mw wtf is going on, i dont know either!

import mapping
import xml.etree.cElementTree as ET

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
alpha = ET.parse("alpha.xml")
masas = ET.parse("masas.xml")


def Convert(string):
    list1 = []
    list1[:0] = string
    return list1

def return_masa(pozisyonlar):
    masa = {}

    for i in range(8):
        for j in range(8):
            masa[str(j + 1) + str(i + 1)] = ""

    pozisyonlar_ = Convert(pozisyonlar)
    pozisyonlar_ = [q for q in pozisyonlar_ if q != "\n"]
    for i in range(len(pozisyonlar_)):
        p = pozisyonlar_[i]

        masa[list(masa.keys())[i]] = p
    return masa

def masa_add(id,mas):
    x = ET.SubElement(masas.getroot(),"masa")



    x.attrib["id"] = id


    for i in mas.keys():
        y = ET.SubElement(x,"value",attrib={"location":i})


        y.text = mas[i]

def alpha_add(ancestor,m,name,order,j,taraf):

    if taraf:
        x = ET.SubElement(ancestor, "move")
        id = ancestor.attrib["id"] + "-" + str(order)
    else:
        x = ET.SubElement(ancestor, "counter_move")
        id = ancestor.attrib["id"] + "-" + str(order) + "b"

    x.attrib["id"] = id

    x.attrib["order"] = str(order)

    x.attrib["move"] = name + "-" + j
    x.attrib["checked"] = "0"
    x.attrib["child_ids"] = ""
    ancestor.attrib["child_ids"] = ancestor.attrib["child_ids"] + "-" + str(order)
    masa_add(id, m)

def planlama_dost(masa, ancestor):
    mapper = mapping.map(masa)

    order = 1

    for i in masa.keys():

        x = i[0]
        y = i[1]

        if masa[i] == dost["kale"]:

            liste = mapper.kale_f(x, y, True)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dost["kale"]

                alpha_add(ancestor,m,"kale",order,j,True)

                order = order + 1

        if masa[i] == dost["fil"]:

            liste = mapper.fil_f(x, y, True)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dost["fil"]
                alpha_add(ancestor, m, "fil", order, j,True)
                order = order + 1

        if masa[i] == dost["at"]:

            liste = mapper.at_f(x, y, True)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dost["at"]
                alpha_add(ancestor, m, "at", order, j,True)
                order = order + 1

        if masa[i] == dost["piyon"]:

            liste = mapper.piyon_f(x, y, True)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dost["piyon"]
                alpha_add(ancestor, m, "piyon", order, j,True)
                order = order + 1

        if masa[i] == dost["vezir"]:
            liste = mapper.vezir_f(x, y, True)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dost["vezir"]
                alpha_add(ancestor, m, "vezir", order, j,True)
                order = order + 1

        if masa[i] == dost["sah"]:

            liste = mapper.sah_f(x, y, True)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dost["sah"]
                alpha_add(ancestor, m, "sah", order, j,True)
                order = order + 1

def planlama_dusman(masa, ancestor):
    mapper = mapping.map(masa)

    order = 1

    for i in masa.keys():

        x = i[0]
        y = i[1]

        if masa[i] == dusman["kale"]:

            liste = mapper.kale_f(x, y, False)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dusman["kale"]

                alpha_add(ancestor,m,"kale",order,j,False)

                order = order + 1

        if masa[i] == dusman["fil"]:

            liste = mapper.fil_f(x, y, False)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dusman["fil"]
                alpha_add(ancestor, m, "fil", order, j,False)
                order = order + 1

        if masa[i] == dusman["at"]:

            liste = mapper.at_f(x, y, False)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] =dusman["at"]
                alpha_add(ancestor, m, "at", order, j,False)
                order = order + 1

        if masa[i] == dusman["piyon"]:

            liste = mapper.piyon_f(x, y, False)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dusman["piyon"]
                alpha_add(ancestor, m, "piyon", order, j,False)
                order = order + 1

        if masa[i] == dusman["vezir"]:
            liste = mapper.vezir_f(x, y, False)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dusman["vezir"]
                alpha_add(ancestor, m, "vezir", order, j,False)
                order = order + 1

        if masa[i] == dusman["sah"]:

            liste = mapper.sah_f(x, y, False)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dusman["sah"]
                alpha_add(ancestor, m, "sah", order, j,False)
                order = order + 1

def unchecked_move():
    y = alpha.getroot().findall(".//counter_move[@checked='0']")



    for i in y:
        id = i.attrib["id"]

        x = masas.findall(".//masa[@id='{}']/value".format(id))

        t = {}

        for j in x:
            t[j.attrib["location"]] = str(j.text)



        planlama_dost(t, i)

        i.attrib["checked"] = '1'
        i.attrib["child_ids"] = i.attrib["child_ids"][1:]



def unchecked_counter_move():
    y = alpha.getroot().findall(".//move[@checked='0']")



    for i in y:
        id = i.attrib["id"]

        x = masas.getroot().findall(".//masa[@id='{}']/value".format(id))

        t = {}

        for j in x:
            t[j.attrib["location"]] = str(j.text)



        planlama_dusman(t, i)

        i.attrib["checked"] = '1'
        i.attrib["child_ids"] = i.attrib["child_ids"][1:]

    """while 1:
        if not ayikla():
            break"""


def ayikla():

    def delet(ii):

        id = ""
        for d in ii.attrib["id"].split("-")[:-1]:
            id += d + "-"
        if ii.attrib["id"] == "a":
            print("there is nothing you can do bitch")
            exit()
        alp = alpha.find(".//move[@id='{}']".format(id[:-1]))

        anc_id_list = alp.attrib["id"].split("-")[:-1]

        anc_id = ""
        for d in anc_id_list:
            anc_id += d + "-"

        anc = alpha.find(".//counter_move[@id='{}']".format(anc_id[:-1]))

        anc_child_id = anc.attrib["child_ids"].split("-")

        anc_child_id = [q for q in anc_child_id if q != alp.attrib["order"]]

        new_anc_child_id = ""

        for d in anc_child_id:
            new_anc_child_id += d + "-"

        anc.attrib["child_ids"] = new_anc_child_id[:-1]

        masas.getroot().remove(masas.find(".//masa[@id='{}']".format(alp.attrib["id"])))

        for b in alp.attrib["child_ids"].split("-"):

            xxx = alp.attrib["id"] + "-" + b + "b"
            xx = masas.find(".//masa[@id='{}']".format(xxx))
            if xx != None:
                masas.getroot().remove(xx)

        if len(anc.attrib["child_ids"].split("-")) == 1:
            delet(anc)




    retur = False

    x = masas.findall(".//masa")

    for i in x:
        t = {}

        for j in i:
            t[j.attrib["location"]] = str(j.text)

        if dost["sah"] not in list(t.values()):
            delet(i)

            retur = True


        if dusman["sah"] not in list(t.values()):



            ln = i.attrib["id"].split("-")

            for h in range(len(ln)):
                delta = ln[:(len(ln) - h)]

                if not len(delta) == 0:

                    new_str = ""

                    for yy in delta:
                        new_str += yy + "-"

                    new_str = new_str[:-1]

                    gama = alpha.find(".//*[@id='{}']".format(new_str))
                    gama.attrib["beta"] = str(h + 1)

                    retur = True

    return retur






x = open(r"C:\Users\aliek\Desktop\projeler\python\satranç_BOT\puzzle_2.txt", "r")
f = x.read()
# f = dost["sah"]  + "----"+ dusman["sah"]
x.close()



"""masa_add("a",return_masa(f))

unchecked_move()

unchecked_counter_move()"""
#yikla()

alpha.write('alpha.xml')
masas.write('masas.xml')
