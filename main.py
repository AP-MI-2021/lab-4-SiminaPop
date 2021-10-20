def afiseaza_toate_numerele_negative_nenule_din_lista(lst):
    '''
    Creeaza o lista de numere intregi negative
    :param lst: lista de numere intregi
    :return: rez: lista de numere intregi negative
    '''
    rez=[]
    for x in lst:
        if x<0:
            rez.append(x)
    return rez
def test_afiseaza_toate_numerele_negative_nenule_din_lista():
    assert afiseaza_toate_numerele_negative_nenule_din_lista([-1,2])==[-1]
    assert afiseaza_toate_numerele_negative_nenule_din_lista([2,4,0])== []

def afisarea_celui_mai_mic_numar_care_are_ultima_cifra_egala_cu_o_cifra_citita_de_la_tastatura(lst,cif):
    '''
    Returneaza cel mai mic numar cu ultima cifra data
    :param lst:lista de numere intregi
    :param cif:cifra citita de la tastatura
    :return:min: cel mai mic numar care are ultima cifra egala cu o cifra citita de la tastatura
    '''
    min=0
    for x in lst:
        if x>=0:
            if min==0 or x<min:
                min=x
        else:
            if 10-(x%10)==cif:
                if x<min:
                    min=x
    return min
def test_afisarea_celui_mai_mic_numar_care_are_ultima_cifra_egala_cu_o_cifra_citita_de_la_tastatura():
    assert afisarea_celui_mai_mic_numar_care_are_ultima_cifra_egala_cu_o_cifra_citita_de_la_tastatura([12,13,22],2)==12
    assert afisarea_celui_mai_mic_numar_care_are_ultima_cifra_egala_cu_o_cifra_citita_de_la_tastatura([8,18,33],8)==8
    assert afisarea_celui_mai_mic_numar_care_are_ultima_cifra_egala_cu_o_cifra_citita_de_la_tastatura([-8,8],8)==-8

def meniu():
    print("""
1.Citire date.
2.Afisarea tuturor numerelor negative nenule din lista.
3.Afisarea celui mai mic numar care are ultima cifra egala cu o cifra citita de la tastatura.
4.Afisarea tuturor numerelor din lista care sunt superprime.
5.Afisarea listei obtinute din lista initiala in care numerele pozitive si nenule au fost inlocuite cu CMMDC-ul lor si numerele negative au cifrele in ordine inversa.
x. Iesire
""")


def citire(n):
    lst=[]
    for i in range(0,n):
        p=int(input("introduceti elemntul"))
        lst.append(p)
    return lst


def teste():
    test_afisarea_celui_mai_mic_numar_care_are_ultima_cifra_egala_cu_o_cifra_citita_de_la_tastatura()
    test_afiseaza_toate_numerele_negative_nenule_din_lista()

def main():
    lst=[]
    teste()
    while True:
        meniu()
        cmd=input("introduceti comanda: ")
        if cmd=='1':
            n=int(input("cate numere sa fie in lista? "))
            lst=citire(n)
        elif cmd=='2':
            print(afiseaza_toate_numerele_negative_nenule_din_lista(lst))
        elif cmd=='3':
            cif=input("dati o cifra")
            print(afisarea_celui_mai_mic_numar_care_are_ultima_cifra_egala_cu_o_cifra_citita_de_la_tastatura(lst,cif))
        elif cmd=='4':
            pass
        elif cmd=='5':
            pass
        elif cmd=='x':
            break
        else:
            print("comanda invalida")


if __name__ == '__main__':main()