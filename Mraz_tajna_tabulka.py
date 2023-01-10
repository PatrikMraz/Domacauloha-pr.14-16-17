veta=input('Zadaj vetu s veľkými písmenami a s medzerami:')
sifra=''

for i in range(len(veta)):
    if veta[i]==' ':
        sifra=sifra+'0'+' '
    if veta[i]=='A':
        sifra=sifra+'1'+' '
    if veta[i]=='B':
        sifra=sifra+'11'+' '
    if veta[i]=='C':
        sifra=sifra+'111'+' '
    if veta[i]=='D':
        sifra=sifra+'2'+' '
    if veta[i]=='E':
        sifra=sifra+'22'+' '
    if veta[i]=='F':
        sifra=sifra+'222'+' '
    if veta[i]=='G':
        sifra=sifra+'3'+' '
    if veta[i]=='H':
        sifra=sifra+'33'+' '
    if veta[i]=='I':
        sifra=sifra+'333'+' '
    if veta[i]=='J':
        sifra=sifra+'4'+' '
    if veta[i]=='K':
        sifra=sifra+'44'+' '
    if veta[i]=='L':
        sifra=sifra+'444'+' '
    if veta[i]=='M':
        sifra=sifra+'5'+' '
    if veta[i]=='N':
        sifra=sifra+'55'+' '
    if veta[i]=='O':
        sifra=sifra+'555'+' '
    if veta[i]=='P':
        sifra=sifra+'6'+' '
    if veta[i]=='Q':
        sifra=sifra+'66'+' '
    if veta[i]=='R':
        sifra=sifra+'666'+' '
    if veta[i]=='S':
        sifra=sifra+'7'+' '
    if veta[i]=='T':
        sifra=sifra+'77'+' '
    if veta[i]=='U':
        sifra=sifra+'777'+' '
    if veta[i]=='V':
        sifra=sifra+'8'+' '
    if veta[i]=='W':
        sifra=sifra+'88'+' '
    if veta[i]=='X':
        sifra=sifra+'888'+' '
    if veta[i]=='Y':
        sifra=sifra+'9'+' '
    if veta[i]=='Z':
        sifra=sifra+'99'+' '
j=0
d=0
t=0
s=0
p=0
se=0
sed=0
o=0
de=0
for i in range(len(sifra)):
    if sifra[i]=='1':
        j=j+1
    if sifra[i]=='2':
        d=d+1
    if sifra[i]=='3':
        t=t+1
    if sifra[i]=='4':
        s=s+1
    if sifra[i]=='5':
        p=p+1
    if sifra[i]=='6':
        se=se+1
    if sifra[i]=='7':
        sed=sed+1
    if sifra[i]=='8':
        o=o+1
    if sifra[i]=='9':
        de=de+1
        
if j>d and j>t and j>s and j>p and j>se and j>sed and j>o and j>de:
    ktore=1
if  d>j and d>t and d>s and d>p and d>se and d>sed and d>o and d>de:
    ktore=2
if t>d and t>j and t>s and t>p and t>se and t>sed and t>o and t>de:
    ktore=3
if s>d and s>t and s>j and s>p and s>se and s>sed and s>o and s>de:
    ktore=4
if p>d and p>t and p>s and p>j and p>se and p>sed and p>o and p>de:
    ktore=5
if se>d and se>t and se>s and se>p and se>j and se>sed and se>o and se>de:
    ktore=6
if sed>d and sed>t and sed>s and sed>p and sed>se and sed>j and sed>o and sed>de:
    ktore=7
if o>d and o>t and o>s and o>p and o>se and o>sed and o>j and o>de:
    ktore=8
if de>d and de>t and de>s and de>p and de>se and de>sed and de>o and de>j:
    ktore=9
        
print(sifra)
print('Najčastejšie zvolené políčka:'+str(ktore))
        