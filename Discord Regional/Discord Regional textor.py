import unicodedata
import subprocess
import re

special_chars = {'1': ":one: ", '2': ":two: ", '3': ":three: ",'4': ":four: ",
                 '5': ":five: ", '6': ":six: ",'7': ":seven: ",'8': ":eight: ",
                 '9': ":nine: ", '0': ":zero: ", '.': ":record_button: ", '!': ":exclamation: ",
                 ',': ":small_red_triangle: ", '?': ":question: ", '@': "@"}


def strip_accents(string = "Mamas de Teçst"):
    string = string.lower()
    return ''.join(c for c in unicodedata.normalize('NFD', string)
                  if unicodedata.category(c) != 'Mn')

def strip_deadcharacters(string):
    string_new = ""
    for i in string:
        if i in "´`^~ªº-_:;*+'=}][{/()&%$#£§\"«»\'’”“":
            string_new += ""
        else:
            string_new += i
    return string_new

def detetar_arroba(string):
    pass

def string_divided(string, emote, special_chars):
    string = strip_deadcharacters(strip_accents(string))
    tamanho = 3 + 2*len(emote)
    for e, i in enumerate(string):
        if i in special_chars:
            tamanho += len(special_chars[i])
        elif i == " ":
            tamanho += len(emote)
        elif i in "abcdefghijklmnopqrstuvwxyz":
            tamanho += 23
        if tamanho < 2000:
            n = e
            p_string = [[string[:e+1]]]
        elif tamanho > 2000:
            break
    if tamanho > 2000:
        p_string = [[string[:n]]]
        p_string.append(string_divided(string[n:], emote, special_chars))
    return [item for sublist in p_string for item in sublist]

def create_style(string, emote, special_char):
    '''
    CRIA A PUTA DA LISTA QUE TODOS QUEREMOS, NÃO?
    '''
    mama = 0
    stg = emote #Emote de separação
    if len(string) == 1:
        for i in string[0]:
            if i == " ":
                stg += emote
            elif i in special_char:
                stg += special_char[i]
            #elif i == "@":
                #user = re.compile('@\w+')
                #print( user.findall(string))
                #stg += re.search('@\w+', string)
            else:
                stg += ":regional_indicator_"+i+": "
        return copy2clip("- "+stg+emote+"-")
    else:
        while mama < len(string):
            stg = emote
            for i in string[mama]:
                if i == " ":
                    stg += emote
                elif i in special_char:
                    stg += special_char[i]
                else:
                    stg += ":regional_indicator_"+i+": "
            print("A string resultante teria mais de 2000 caraters, logo será subdividida em", len(string), "strings diferentes\n")
            copy2clip("- "+stg+emote+"-")
            mama += 1
            input("\nA string nº"+str(mama)+" está no seu clipboard\nCole e escreva qualquer coisa para a próxima string: ")
        return print("\n\n\nParabens a você")

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)


print ("\nDiscord Regional Indicator style maker \nA frase que vocês escreverem será enviada para o vosso clipboard\n(basta colar no Discord)\n\n")
a = True
while a:
    print ("Escolha o Emoji \n 0 = None \n 1 = :heart: \n 2 = :yellow_heart: \n 3 = :cowboy: \n Anything else = Custom")
    emote = str(input("Qual emote quer para a separaçao de palavras? "))
    if emote == "1":
        emote = ":heart: "
        a = False
    elif emote == "2":
        emote = ":yellow_heart: "
        a = False
    elif emote == "3":
        emote = ":cowboy: "
        a = False
    elif emote == "0":
        emote = ""
        a = False
    else:
        print ("\nCustom\nEscreva o emote que quer, sem os 2 pontos \":\"")
        emote = ":"+str(input("Emote: "))+": "
        a = False

mastring = str(input("Escreva a sua frase: "))
lestring = string_divided(mastring, emote, special_chars)
create_style(lestring, emote, special_chars)
