subor=open('mena_zamestnancov.txt','r')
zoznam=[]

for riadok in subor:
    zoznam.append(riadok.strip())

počet=len(zoznam)//2
for i in range(len(zoznam)//2):
    if zoznam[i]>zoznam[i+1] :
        najdlhsie=len(zoznam[i]) - 1
    else:
        najdlhsie=len(zoznam[i+1]) - 1
    if zoznam[i+3]>zoznam[i+4]:
        najdlhsie_pr=len(zoznam[i+3]) - 1
    else:
        najdlhsie_pr=len(zoznam[i+4]) - 1
            
print('Počet mien:'+' '+str(počet))
print('Dĺžka najdlhšieho mena:'+' '+str(najdlhsie))
print('Dĺžka najdlhšieho priezviska:'+' '+str(najdlhsie_pr))

subor1=open('vystup.txt','w')
for i in range(len(zoznam)//2):
    if len(zoznam[i])>10:
        subor1.write(zoznam[i]+' '+zoznam[i+4]+'\n')
    if len(zoznam[i])>6 and len(zoznam[i])<10:
        subor1.write(zoznam[i]+' '+' '+' '+zoznam[i+4]+'\n')
    if len(zoznam[i])<=6:
        subor1.write(zoznam[i]+(len(zoznam[i]))*' '+zoznam[i+4]+'\n')

subor.close()
subor1.close()