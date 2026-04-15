
"""
nom:Cookie master
fait par: Arnaud Baril
"""
phrasefinale = ""
alphabet = "abcdefghijklmnopqrstuvwxyz"

alphabet1 = " , a,A,b,B,c,C,d,D,e,E,f,F,G,g,H,h,I,i,J,j,K,k,L,l,M,m,N,n,O,o,P,p,Q,q,R,r,S,s,T,t,U,u,V,v,W,w,X,x,Y,y,Z,z"

lastring = str(input("rentre ta phrase "))


for lettre in lastring:
    if lettre not in alphabet:
        raise ValueError("mauvaise entrer")


phrasefinale = ""
for word in lastring:
    for lettre in alphabet:
        bob = alphabet.index(lettre)
        bob = alphabet[bob]
        phrasefinale + bob

print(phrasefinale)




    


