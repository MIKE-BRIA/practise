# if __name__ == '__main__':
print("pycharm is awesome")
stg = "simplilearn"
print(len(stg))
print(stg[5])

print(stg[:5])
print(stg.upper())
print(stg.find('s'))
stg1='good'
stg2='morning'
stg3='michael'
stg="{} {}, {}!".format(stg1,stg2,stg3)
print(stg)
d1={1:"welcome",2:"to",3:"bimax"}
print(d1)
d={}
d[0]="welcome"
print(d)
d[1]=("how", "are", "you")
print(d)
d['name']="sam"
print(d)
d['name']={'first':'sam','last':'crew'}
print(d)
a=5
if a>50:
    print("this is a greater value")
print("you are fucked")
i=20
if i<10:
    print("am a winner")
else:
    print("its the beginning of the game")

e=5
if e/2>20:
    if e%2==0:
        print("am working")
    else:
        print("life is good")
else:
    print("am about to be fucked")

var= "o"
if var=='a':
    print("this is vowel a")
elif var=='e':
    print("this is the vowel e")
elif var=='i':
    print("this is the vowel i")
elif var=='o':
    print("this is the vowel o")
elif var=='u':
    print("this is the vowel u")
else:
    print("this is a consonant")