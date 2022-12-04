import sys

# prida stdout do nove vytvoreneho souboru
sys.stdout = open("merget_files.txt", 'w')

# pomocna promenna
c = []

# spocita pocet radku v jednotlivach souborech
# pouzit raw strig, protoze windows (\)
# cyklus pro kazdy radek zada cislo 1 a pote vsechna cisla secte
num_lines_f = sum(1 for row in open(r"C:\Users\FAUX\source\repos\NewRepo\1.txt"))
num_lines_s = sum(1 for row in open(r"C:\Users\FAUX\source\repos\NewRepo\2.txt"))
num_lines_t = sum(1 for row in open(r"C:\Users\FAUX\source\repos\NewRepo\3.txt"))

# prida jednotlive zjistene hdnoty do pomocne promenne listu c
c.append(num_lines_f)
c.append(num_lines_s) 
c.append(num_lines_t)
#print(c)
# seradi list c
c.sort()
#print(c)

# podminky, co se ma vypsat do nove urceneho souboru
# komentar plati pro 3 nasledujici podminky
if c[0] == 3:
    # promenna pro cestu
    path_f = r"C:\Users\FAUX\source\repos\NewRepo\3.txt"
    # uprava promenne pro cestu, aby byl zapsan pouze nazev souboru
    path_f = path_f.split('\\')[-1]
    print(path_f)
    print(c[0])
    # otevre a precte obsah souboru a zapise do merget_files.txt
    fi = open(r"C:\Users\FAUX\source\repos\NewRepo\3.txt")
    print(fi.read())

if c[1] == 6:
    path_f = r"C:\Users\FAUX\source\repos\NewRepo\1.txt"
    path_f = path_f.split('\\')[-1]
    print(path_f)
    print(c[1])
    se = open(r"C:\Users\FAUX\source\repos\NewRepo\1.txt")
    print(se.read())

if c[2] == 11:
    path_f = r"C:\Users\FAUX\source\repos\NewRepo\2.txt"
    path_f = path_f.split('\\')[-1]
    print(path_f)
    print(c[2])
    th = open(r"C:\Users\FAUX\source\repos\NewRepo\2.txt")
    print(th.read())

# uzavre presmerovani vystupu print do souboru merget_files.txt
sys.stdout.close()



# pokusy s poctem radku, ruzne pristupy
#with open(r"C:\Users\FAUX\source\repos\NewRepo\1.txt", 'r') as f:
#    for count, line in enumerate(f):
#        number_lines_f = count + 1
#    print(f.read())
#print('Lines o 1.txt', number_lines_f)


#with open(r"C:\Users\FAUX\source\repos\NewRepo\2.txt", 'r') as s:
#    for count, line in enumerate(s):
#        number_lines_s = count + 1
#print('Lines o 1.txt', number_lines_s)

#with open(r"C:\Users\FAUX\source\repos\NewRepo\3.txt", 'r') as t:
#    for count, line in enumerate(t):
#        number_lines_t = count + 1
#print(Lines o 1.txt', number_lines_t)


#f = open(r"C:\Users\FAUX\source\repos\NewRepo\1.txt", 'r')
#number_lines_f = len(f.readlines())
#print('Total Lines', number_lines_f)
#print(f.read())


