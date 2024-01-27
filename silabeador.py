import regex as re

def anadir_silabas(cadena, posiciones_cortes):
    silabas = []
    for i in range(len(posiciones_cortes) - 1):
        inicio_silaba = posiciones_cortes[i]
        fin_silaba = posiciones_cortes[i + 1]
        silaba = cadena[inicio_silaba:fin_silaba]
        silabas.append(silaba)
    silabas.append(cadena[posiciones_cortes[-1]:])
    return silabas


def silabear(cadena):
    ER2Nucleos = (r'(?i)(?P<R6>[[iuy][aeoáéó][iuy])|(?i)(?P<R5_a1>([aeoáéó]h?[iu]))|(?i)(?P<R5_a2>([iu]h?[aeoáéó]))|(?i)(?P<R5_a3>([ií]h?[uü]|[uúü]h?[i]|[i]h?[uúü]|[uü]h?[ií]))|(?i)(?P<R5_b1>(?P<V1>[aeo])(?P<V2>h?[iíuú])|(?P<V1>[iíuú])(?P<V2>h?[aeo]))|(?i)(?P<R5_b2>((?P<V1>a)(?P<V2>h?[aá])|(?P<V1>[aá])(?P<V2>h?a))|((?P<V1>e)(?P<V2>h?[eé])|(?P<V1>[eé])(?P<V2>h?e))|((?P<V1>i)(?P<V2>h?[ií])|(?P<V1>[ií])(?P<V2>k?i))|((?P<V1>o)(?P<V2>h?[oó])|(?P<V1>[oó])(?P<V2>h?o))|((?P<V1>u)(?P<V2>h?[uú])|(?P<V1>[úu])(?P<V2>h?u)))|(?i)(?P<R5_b3>((?P<V1>[aeo])(?P<V2>h?[aeoáéó]))|(?P<V1>[aeoáéó])(?P<V2>h?[aeo]))|(?is)(?P<R1>[aeiouáéíóúü](ch|rr|ll|[bcdfghjklmnñpqrstvwxyz])[aeiouáéíóúü])|(?i)(?P<R2_1>(?P<S1>[aeiouáéíóúü])(?P<S2>[pcbgf][rl][aeiouáéíóúü]))|(?i)(?P<R2_2>(?P<S1>[aeiouáéíóúü])(?P<S2>[dt]r[aeiouáéíóúü]))|(?i)(?P<R2_3>(?P<S1>[aeiouáéúíóu][qwrtypsdfghjklñmnbvcxz])(?P<S2>[qwrtypsdfghjklñmnbvcxz][aeiouáéúíóu]))|(?i)(?P<R3_1>(?P<S1>[aeiouáéíóúü][qwrtypsdfghjklñmnbvcxz])(?P<S2>([pcbgf][rl]|[dt]r)[aeiouáéíóúü]))|(?i)(?P<R3_2>(?P<S1>[aeiouáéíóúü][bdnmlr]s)(?P<S2>[qwrtypsdfghjklñmnbvcxz][aeiouáéíóúü]))|(?i)(?P<R3_3>(?P<S1>[aeiouáéíóúü]st)(?P<S2>[qwrtypsdfghjklñmnbvcxz][aeiouáéíóúü]))|(?i)(?P<R4>(?P<S1>[aeiouáéíóúü](([bdnmlr]s)|st))(?P<S2>[pcbtgf][rl][aeiouáéíóúü]))')
    cortes = [0]
    pos = 0
    pat2Nucleos = re.compile(ER2Nucleos)
    res = pat2Nucleos.search(cadena, pos)
    while res:
        if res.group("R5_b1"):
            corte = res.start() + 1
            cortes.append(corte)
        elif res.group("R5_b2"):
            corte = res.start() + 1
            cortes.append(corte)
        elif res.group("R5_b3"):
            corte = res.start() + 1
            cortes.append(corte)
        elif res.group("R1"):
            corte = res.start() + 1
            cortes.append(corte)
        elif res.group("R2_1"):
            corte = res.start() + 1
            cortes.append(corte)
        elif res.group("R2_2"):
            corte = res.start() + 1
            cortes.append(corte)
        elif res.group("R2_3"):
            corte = res.start() + 2
            cortes.append(corte)
        elif res.group("R3_1"):
            corte = res.start() + 2
            cortes.append(corte)
        elif res.group("R3_2"):
            corte = res.start() + 3
            cortes.append(corte)
        elif res.group("R3_3"):
            corte = res.start() + 3
            cortes.append(corte)
        elif res.group("R4"):
            corte = res.start() + 3
            cortes.append(corte)
        pos = res.end() - 1
        res = pat2Nucleos.search(cadena, pos)
    return anadir_silabas(cadena, cortes)