#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
################################################################################
################################################################################

""" Operazioni da fare PRIMA DI TUTTO:
 1) Salvare questo file col nome program.py
 2) Assegnare le variabili sottostanti con il tuo
    NOME, COGNOME, NUMERO DI MATRICOLA

Per superare la prova è necessario:
    - !!!riempire le informazioni personali nelle variabili qui sotto!!!
    - AND ottenere un punteggio maggiore o uguale a 18 (o 15 se DSA)

Il punteggio finale della prova è la somma dei punteggi dei problemi risolti.
Per i DSA il punteggio viene scalato opportunamente (32*X/26).
"""
nome       = "Alessio"
cognome    = "Renzetti"
matricola  = "2251961"

################################################################################
################################################################################
################################################################################
# ------------------------ SUGGERIMENTI PER IL DEBUG --------------------------- #
# Per eseguire solo alcuni dei test, puoi commentare le righe della lista
# 'tests' alla fine di grade.py
#
# Per facilitare il debug delle funzioni ricorsive, puoi disattivare
# il test ricorsivo impostando DEBUG=True nel file grade.py
#
# DEBUG=True attiva anche il TRACE DELLO STACK che ti permette di sapere quale
# numero di riga in program.py ha generato l'errore.
################################################################################

# %% ----------------------------------- FUNC.1 ----------------------------------- #
"""
Func 1: 2 punti

Implementa la funzione func1(testo : str, K : int) -> set[str] 
che riceve come argomenti:
- testo: una stringa contenente parole separate da caratteri non alfabetici
- K: un intero
e che ritorna l'insieme delle parole che appaiono esattamente K volte nel testo.

Esempio:
K = 2
testo = '''sopra la panca la capra campa, sotto la panca la capra crepa!'''
expected = {'capra', 'panca'}

"""
def func1(testo : str, K : int) -> set[str]:
    testo_clear=testo.lower()
    testo_temp=[]
    parole_temp=""
    for carattere in testo_clear:
        if 'a'<= carattere <= 'z':
            parole_temp+=carattere
        else:
            if parole_temp:
                testo_temp.append(parole_temp)
            parole_temp=""
    if parole_temp:
        testo_temp.append(parole_temp)
    conteggio={}
    for parola in testo_temp:
        conteggio[parola]=conteggio.get(parola,0) + 1
    ris=set()
    for parola,cont in conteggio.items():
        if cont==K:
            ris.add(parola)
    return ris
    # completa la funzione


# K = 2
# testo = '''essere o non essere, questo è il dilemma: 
#                se sia più nobile nella mente soffrire colpi di fionda e dardi d’atroce fortuna 
#                o prender armi contro un mare d’affanni e, opponendosi, por loro fine? 
#                morire, dormire; nient’altro; e con un sonno dire che poniamo fine al dolore 
#                del cuore e ai mille tumulti naturali di cui è erede la carne: 
#                è una conclusione da desiderarsi devotamente'''
# expected = {'fine', 'un', 'di', 'o', 'essere', 'd'}
# print(func1(testo,K))


# %% ----------------------------------- FUNC.2 ----------------------------------- #
"""
Func 2: 2 punti

Implementa la funzione   func2(parole : list[str]) -> dict[str, list[str]]
che riceve come argomenti:
    - parole: una lista di parole
e che ritorna un dizionario che ha come chiavi le lettere iniziali delle parole,
e come valori la lista della parole che hanno quella iniziale, 
ordinate per lunghezza crescente e in caso parità in ordine alfabetico decrescente.

Esempio:
parole = ['sei','sicuro','che','sopra','la','panca','le','capre','campino?',
          'certamente,','mentre','sotto','la','panca','le','capre','crepano!']
expected = {'s': ['sei', 'sotto', 'sopra', 'sicuro'], 
            'c': ['che', 'capre', 'capre', 'crepano!', 'campino?', 'certamente,'], 
            'l': ['le', 'le', 'la', 'la'], 
            'p': ['panca', 'panca'], 
            'm': ['mentre']}
"""
def func2(parole : list[str]) -> dict[str, list[str]]:
    diz: dict[str,list[str]]
    diz = {}
    for x in parole:
        if x[0] not in diz:
            diz[x[0]]=[x]
        else:
            diz[x[0]].append(x)
    return  {k:sorted(v, key=lambda x:(len(x),[-ord(c) for c in x])) for k,v in diz.items()}
    
    pass
    # completa la funzione




# parole = ['sei','sicuro','che','sopra','la','panca','le','capre','campino?',
#         'certamente,','mentre','sotto','la','panca','le','capre','crepano!']
# print(func2(parole))

# %% ----------------------------------- FUNC.3 ----------------------------------- #
"""
Func 3: 2 punti

Implementa la funzione    func3(D1 : dict[str,list[int]], D2 : dict[int,list[str]]) -> dict[str, list[str]] 
che riceve come argomenti:
    - D1: un dizionario che ha come chiavi delle parole e come valori liste di interi DIVERSI tra loro
    - D2: un dizionario che ha come chiavi degli interi e come valori liste di parole
e che ritorna un dizionario che ha come chiavi delle parole e come valori liste di parole.
Le chiavi sono le sole chiavi di D1 che hanno almeno uno degli interi ad esse associati che è una chiave di D2.
Tutte le parole associate in D2 a tali interi devono apparire nella lista associata a quella chiave nel risultato.
L'ordinamento delle parole nei valori del risultato è per dimensioni decrescenti 
e in caso di parità in ordine alfabetico crescente.

Esempio:
D1 = { 'a':[1,2,3], 'b':[3,4,5] }
D2 = { 1:['a','bb','ccc'], 3:['qq','z'], 5:['b','fff'] }
expected = {'a': ['a', 'z', 'bb', 'qq', 'ccc'], 'b': ['b', 'z', 'qq', 'fff']}
"""
def func3(D1 : dict[str,list[int]], D2 : dict[int,list[str]]) -> dict[str, list[str]]:
    diz={}
    for k,v in D1.items():
        for x,y in D2.items():
            if k not in diz:
                if x in v:
                    diz[k]=y
            else:
                if x in v:
                    for i in y:
                        diz[k].append(i)    
    return {k:sorted(v, key=lambda x:(len(x),x)) for k,v in diz.items()}           
    pass
    # completa la funzione





# D1 = { 'a':[1,2,3], 'b':[3,4,5] }
# D2 = { 1:['a','bb','ccc'], 3:['qq','z'], 5:['b','fff'] }
# print(func3(D1,D2))


# %% ----------------------------------- FUNC.3 ----------------------------------- #
"""
Func 4: 6 punti

Implementa la funzione    func4(path_in : str, path_out : str, K : int) -> dict[str, list[str]]
che riceve come argomenti:
    - path_in:  un percorso ad un file di testo da leggere
    - path_out: un percorso ad un file di testo da scrivere
    - K: un intero
La funzione deve leggere il file di testo al percorso path_in
e ritornare un dizionario che ha come chiavi le parole presenti nel file almeno K volte
e come valori le liste degli interi che rappresentano il numero della riga in cui appare la parola.

Successivamente la funzione deve scrivere su file path_out su ogni riga 
la parola ed il numero di righe in cui essa appare, separati da spazio.
Le righe del file path_out devono essere ordinate 
- per numero di righe in cui sono apparse le parole in ordine decrescente 
- e in caso di parità in ordine alfabetico crescente.

Esempio:
path_in = 'func4/in_1.txt'
path_out = 'func4/out_1.txt'
k = 2
Il file in_1.txt contiene:
    a b c b a a
    aa ba ca aa ba ca
    a b
    aa b
Il file out_1.txt conterrà:
    b 3
    a 2
    aa 2
e la funzione restituirà:
    {'a': [0, 2], 'b': [0, 2, 3], 'aa': [1, 3]}
"""
def func4(path_in : str, path_out : str, K : int) -> dict[str, list[str]]:
    with open(path_in,'r',encoding='utf-8') as f:
        content=f.read()
        
        return content
    pass
    # completa la funzione




# %% ----------------------------------- FUNC.5 ----------------------------------- #
"""
Func 5: 8 punti

Implementa la funzione      func5(path_png_in : str) -> dict[str, set[tuple[int,int]]]
che riceve come argomenti:
    - path_png_in:  un percorso ad un file PNG da leggere
Il file PNG path_png_in contiene un'immagine a sfondo nero con dei quadretti colorati di varie dimensioni.

ASSUMETE che nessuno dei quadrati si appoggi sul bordo della immagine o tocchi un altro quadrato.

La funzione deve leggere il file PNG al percorso path_png_in e cercare tutte le posizioni
in cui compare un quadrato 2x2 di pixel tutti dello stesso colore.
(si intende la posizione x,y del pixel in alto a sinistra del quadrato 2x2)
La funzione deve ritornare come risultato un dizionario che ha come chiavi i colori dei quadrati 2x2
e come valori l'insieme delle posizioni dei quadrati 2x2 di quel colore.

Esempio:
path_png_in = 'func5/in_1.png'
expected = {(184, 188, 208): {(11, 1), (8, 9)}}
"""
import images
def func5(path_png_in : str) -> dict[str, set[tuple[int,int]]]:
    img=images.load(path_png_in)
    diz={}
    for i,riga in enumerate(img):
        for j,pixel in enumerate(riga):
            if j!=0 or j!=len(riga)-1:
                if pixel!=(0,0,0) and pixel==riga[j+1] and riga[j-1]==(0,0,0) and riga[j+2]==(0,0,0):
                    if img[i+1][j]==pixel and img[i+1][j+1]==pixel and img[i+1][j-1]==(0,0,0) and img[i+1][j+2]==(0,0,0):
                        if pixel in diz:
                            diz[pixel].add((j,i))
                        else:
                            diz[pixel]={(j,i)}
    return {k:v for k,v in diz.items() if len(v)>=2 }
    pass
    # completa la funzione
# print(func5("func5/in_1.png"))

# %% ----------------------------------- EX.1 ----------------------------------- #
"""
Ex 1: 6 punti

Implementa la funzione    ex1(radice : tree.BinaryTree, lista_pesi:list[int]) -> tree.BinaryTree
che riceve come argomento:
- radice: un albero binario formato da nodi tree.BinaryTree
- lista_pesi: una lista di interi
e che da esso costruisce ricorsivamente o usando funzioni o metodi ricorsivi
un secondo albero binario che ha la stessa struttura del primo con i valori dei nodi moltiplicati 
ciascuno per l'n-esimo valore di lista_pesi, dove n è la profondità del nodo nell'albero
(considerando la radice a profondità 0).

ATTENZIONE: l'albero originale deve rimanere inalterato.

Esempio:
Se l'albero in input è:
   ___1___
   |     |
 __2__   3___         
 |   |      |
 4   5      6
e lista_pesi = [2,7,3,1]
l'albero in output sarà:
   ___2___
   |     |
 __14_   21__
 |   |      |
12   15    18
"""
import tree
def prodotto_nodo(radice,lista_pesi,pos,nodo):
    nodo.value=radice.value*lista_pesi[pos]

    if radice.left!=None:
        prodotto_nodo(radice.left,lista_pesi,pos+1,nodo.left)
    if radice.right!=None:
        prodotto_nodo(radice.right,lista_pesi,pos+1,nodo.right)
    
    return nodo

def new_tree(nodo):
    if nodo==None:
        return None
    nuovo_nodo=tree.BinaryTree(nodo.value)

    nuovo_nodo.left=new_tree(nodo.left)
    nuovo_nodo.right=new_tree(nodo.right)

    return nuovo_nodo

def ex1(radice : tree.BinaryTree, lista_pesi:list[int]) -> tree.BinaryTree:
    albero=new_tree(radice)
    return prodotto_nodo(radice,lista_pesi,0,albero)
    pass
    # completa la funzione




# %% ----------------------------------- EX.2 ----------------------------------- #
"""
Ex 2: 6 punti

Implementa la funzione    ex2(path : str, lista_estensioni : list[str]) -> dict[str, list[str]]
che riceve come argomento:
- path: il path di una directory
- lista_estensioni: una lista di estensioni di file (stringhe)
e che esplora ricorsivamente o usando funzioni o metodi ricorsivi la directory path
e tutte le sue sottodirectory e ritorna un dizionario che ha come chiavi le estensioni
e come valori l'insieme delle directory che contengono quel tipo di file.

ATTENZIONE: è proibito usare la funzione os.walk
NOTA: potete usare le funzioni os.listdir, os.path.isdir, os.path.isfile ...
NOTA: usate il carattere '/' per separare i path, che funziona sia su Windows che Linux

Esempio:
    directory  = 'ex2/A'
    extensions = ["txt", "pdf", "png", "gif"]
    expected   = {'txt': {'ex2/A/C', 'ex2/A', 'ex2/A/B'}, 'pdf': {'ex2/A/C', 'ex2/A'}, 'png': {'ex2/A/C'}, 'gif': {'ex2/A/C'}}
"""
import os
def ric2(root,lista,lista_estensioni,diz):
    if len(lista)==0:
        return diz
    if os.path.isfile(root+"/"+lista[0]) and "." in lista[0]:
        if lista[0].split(".")[1] in lista_estensioni:
            if lista[0].split(".")[1] in diz:
                diz[lista[0].split(".")[1]].add(root)
            else:
                diz[lista[0].split(".")[1]]={root}
        return ric2(root,lista[1:],lista_estensioni,diz)
    elif os.path.isdir(root+"/"+lista[0]):
        ric2(root+"/"+lista[0],os.listdir(root+"/"+lista[0]),lista_estensioni,diz)
        return ric2(root,lista[1:],lista_estensioni,diz)
def ex2(path : str, lista_estensioni : list[str]) -> dict[str, list[str]]:
    diz={}
    return ric2(path,os.listdir(path),lista_estensioni,diz)
    pass
    # completa la funzione

print(ex2('ex2',["png", "gif", "tqq"]))


######################################################################################

if __name__ == '__main__':
    # Scrivi qui i tuoi test addizionali, attenzione a non sovrascrivere
    # gli EXPECTED!
    print('*' * 50)
    print('ITA\nDevi eseguire il grade.py se vuoi debuggare con il grader incorporato.')
    print(
        'Altrimenii puoi inserire qui del codice per testare le tue funzioni ma devi scriverti i casi che vuoi testare')
    print('*' * 50)


