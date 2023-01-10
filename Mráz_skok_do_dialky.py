subor=open('skok_do_dialky.txt','r')
zoznam=[]
sve=0
usa=0
fin=0
rus=0
hun=0
fra=0

for riadok in subor:
    zoznam.append(riadok.strip())

krajiny=[]
ktore=[]
ktory=[]

for j in zoznam:
    pom = j.split()
    krajina = pom[1]
    if krajina=='SVE':
        sve=sve+1
    if krajina=='USA':
        usa=usa+1
    if krajina=='FIN':
        fin=fin+1
    if krajina=='RUS':
        rus=rus+1
    if krajina=='HUN':
        hun=hun+1
    if krajina=='FRA':
        fra=fra+1
    if krajina not in krajiny:
        krajiny.append(krajina)
    vykon1=pom[2]
    vykon2=pom[3]
    vykon3=pom[4]
    vykon4=pom[5]
    vykon5=pom[6]
    if vykon1>vykon2 and vykon1>vykon3 and vykon1>vykon4 and vykon1>vykon5:
        ktore.append(vykon1)
        ktory.append(pom[0])
    if vykon2>vykon1 and vykon2>vykon3 and vykon2>vykon4 and vykon2>vykon5:
        ktore.append(vykon2)
        ktory.append(pom[0])
    if vykon3>vykon2 and vykon3>vykon1 and vykon3>vykon4 and vykon3>vykon5:
        ktore.append(vykon3)
        ktory.append(pom[0])
    if vykon4>vykon2 and vykon4>vykon1 and vykon4>vykon3 and vykon4>vykon5:
        ktore.append(vykon4)
        ktory.append(pom[0])
    if vykon5>vykon2 and vykon5>vykon1 and vykon5>vykon3 and vykon5>vykon4:
        ktore.append(vykon5)
        ktory.append(pom[0])
    for i in range(len(ktore)-1):
        if ktore[i]>ktore[i+1]:
            najdalej=ktore[i]
            sampion=ktory[i-2]
        else:
            najdalej=ktore[i+1]
            sampion1=ktory[i+1]

print('Zoznam krajín z ktorých boli súťažiaci:'+' '+str(krajiny))
print('Počet súťažiacich zo Švédska:'+' '+str(sve))
print('Počet súťažiacich z Ruska:'+' '+str(rus))
print('Počet súťažiacich z Fínska:'+' '+str(fin))
print('Počet súťažiacich z USA:'+' '+str(usa))
print('Počet súťažiacich z Maďarska:'+' '+str(hun))
print('Počet súťažiacich z Francúzska:'+' '+str(fra))
print('Vyhral alebo vyhrali'+' '+sampion+','+' '+sampion1+' '+'skočil alebo skočili'+' '+najdalej+' cm.')

subor.close()