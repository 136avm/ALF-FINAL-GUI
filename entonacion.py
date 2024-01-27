import regex as re
import silabeador

vocales='aeiouüAEIOUÜáéíóúÁÉÍÓÚ'
mayus='AEIOUÜÁÉÍÓÚ'

def sust1(silaba):
    lista = list(silaba)
    for i in range(len(silaba)):
        if lista[i] == 'a':
            lista[i] = 'A'
        if lista[i] == 'e':
            lista[i] = 'E'
        if lista[i] == 'o':
            lista[i] = 'O'
    silaba = ''.join(lista)
    return silaba


def sust2(silaba):
    lista = list(silaba)
    for i in range(len(silaba)):
        if lista[i] in 'iu':
            if lista[i + 1] == 'i':
                lista[i + 1] = 'I'
            if lista[i + 1] == 'u':
                lista[i + 1] = 'U'
    silaba = ''.join(lista)
    return silaba


def sust3(silaba):
    lista = list(silaba)
    for i in range(len(silaba)):
        if lista[i] == 'a':
            lista[i] = 'A'
        if lista[i] == 'e':
            lista[i] = 'E'
        if lista[i] == 'o':
            lista[i] = 'O'
        if lista[i] == 'i':
            lista[i] = 'I'
        if lista[i] == 'u':
            lista[i] = 'U'
    silaba = ''.join(lista)
    return silaba


def sust4(palabra):
    lista = list(palabra)
    for i in range(len(palabra)):
        if lista[i] == 'á':
            lista[i] = 'Á'
        if lista[i] == 'é':
            lista[i] = 'É'
        if lista[i] == 'ó':
            lista[i] = 'Ó'
        if lista[i] == 'í':
            lista[i] = 'Í'
        if lista[i] == 'ú':
            lista[i] = 'Ú'
    palabra = ''.join(lista)
    return palabra


def sust5(palabra):
    lista = list(palabra)
    for i in range(len(palabra)):
        if lista[i] == 'Á':
            lista[i] = 'A'
        if lista[i] == 'É':
            lista[i] = 'E'
        if lista[i] == 'Í':
            lista[i] = 'I'
        if lista[i] == 'Ó':
            lista[i] = 'O'
        if lista[i] == 'Ú':
            lista[i] = 'U'
    palabra = ''.join(lista)
    return palabra


def entonar(palabra):
    patronTildes = r'(?is)[áéíóú]'
    erTildes = re.compile(patronTildes)
    res = erTildes.search(palabra)
    tilde = False
    if res:
        palabra = sust4(palabra)
        tilde = True
    listaSilabas = silabeador.silabear(palabra)
    patronEntonar = r'(?is)(?P<R1>[aeiouüsn]$)|(?P<R2>[^aeiouüns]$)'
    erEntonar = re.compile(patronEntonar)
    patronDT = r'(?is)(?P<D3>[[iu][aeo][iuy])|(?P<D1>([aeo]h?[iu])|([iu][aeo]))|(?P<D2>([i]h?[u])|([u]h?[i]))'
    erDT = re.compile(patronDT)
    res = erEntonar.search(palabra)
    if len(listaSilabas)>1:
        if res.group('R1') and tilde==False:
            silaba = listaSilabas[-2]
            res2 = erDT.search(silaba)
            if res2:
                if res2.group('D1'):
                    silaba = sust1(silaba)
                    listaSilabas[-2] = silaba
                elif res2.group('D2'):
                    silaba = sust2(silaba)
                    listaSilabas[-2] = silaba
                elif res2.group('D3'):
                    silaba = sust1(silaba)
                    listaSilabas[-2] = silaba
            else:
                silaba = sust3(silaba)
                listaSilabas[-2] = silaba
        elif res.group('R2') and tilde==False:
            silaba = listaSilabas[-1]
            res2 = erDT.search(silaba)
            if res2:
                if res2.group('D1'):
                    silaba = sust1(silaba)
                    listaSilabas[-1] = silaba
                elif res2.group('D2'):
                    silaba = sust2(silaba)
                    listaSilabas[-1] = silaba
                elif res2.group('D3'):
                    silaba = sust1(silaba)
                    listaSilabas[-1] = silaba
            else:
                silaba = sust3(silaba)
                listaSilabas[-1] = silaba
    elif tilde==False:
        silaba = listaSilabas[-1]
        res2 = erDT.search(silaba)
        if res2:
            if res2.group('D1'):
                silaba = sust1(silaba)
                listaSilabas[-1] = silaba
            elif res2.group('D2'):
                silaba = sust2(silaba)
                listaSilabas[-1] = silaba
            elif res2.group('D3'):
                silaba = sust1(silaba)
                listaSilabas[-1] = silaba
        else:
            silaba = sust3(silaba)
            listaSilabas[-1] = silaba
    for i in range(len(listaSilabas)):
        listaSilabas[i] = sust5(listaSilabas[i])
    return listaSilabas


def entonacion(palabra):
    sils = silabeador.silabear(palabra)
    if len(sils) > 3:
        sils2 = sils[-2:]
        if sils2 == ['men','te']:
            return "sobreesdrújula"
    lista = entonar(palabra)
    cond = 0
    i = -1
    while cond == 0:
        for c in lista[i]:
            if c in mayus:
                cond = 1
                i+=1
        i-=1
    if i==-1:
        return "aguda"
    elif i==-2:
        return "llana"
    elif i==-3:
        return "esdrújula"
    else:
        return "sobreesdrújula"
