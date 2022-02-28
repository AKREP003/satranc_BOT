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
    print(taraf)
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

        if masa[i] == dost["kale"]:

            liste = mapper.kale_f(x, y, False)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dost["kale"]

                alpha_add(ancestor,m,"kale",order,j,False)

                order = order + 1

        if masa[i] == dost["fil"]:

            liste = mapper.fil_f(x, y, False)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dost["fil"]
                alpha_add(ancestor, m, "fil", order, j,False)
                order = order + 1

        if masa[i] == dost["at"]:

            liste = mapper.at_f(x, y, False)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dost["at"]
                alpha_add(ancestor, m, "at", order, j,False)
                order = order + 1

        if masa[i] == dost["piyon"]:

            liste = mapper.piyon_f(x, y, False)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dost["piyon"]
                alpha_add(ancestor, m, "piyon", order, j,False)
                order = order + 1

        if masa[i] == dost["vezir"]:
            liste = mapper.vezir_f(x, y, False)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dost["vezir"]
                alpha_add(ancestor, m, "vezir", order, j,False)
                order = order + 1

        if masa[i] == dost["sah"]:

            liste = mapper.sah_f(x, y, False)

            for j in liste:
                m = masa.copy()

                m[str(x) + str(y)] = ''
                m[j] = dost["sah"]
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
    retur = False

    x = masas.findall(".//masa")

    for i in x:
        t = {}

        for j in i:
            t[j.attrib["location"]] = str(j.text)

        if dost["sah"] not in t.values():

            alp = alpha.find(".//counter_move[@id='{}']".format(i.attrib["id"]))

            anc_id_list = i.attrib["id"].split("-")[:1]
            anc_id = ""
            for d in anc_id_list:
                anc_id += d

            anc = alpha.find("//move[@id='{}']".format(anc_id))
            anc_child_id = anc.attrib["child_id"].split("-")

            anc_child_id.remove(i.attrib["id"])

            new_anc_child_id = ""

            for d in anc_child_id:
                new_anc_child_id += d

            anc.attrib["child_id"] = new_anc_child_id

            masas.getroot().remove(i)
            alpha.getroot().remove(alp)
            retur = True

    return retur

x = open(r"C:\Users\aliek\Desktop\projeler\python\satranç_BOT\puzzle_2.txt", "r")
f = x.read()
# f = dost["sah"]  + "----"+ dusman["sah"]
x.close()



masa_add("a",return_masa(f))

unchecked_move()

unchecked_counter_move()
#ayikla()

alpha.write('alpha.xml')
masas.write('masas.xml')
