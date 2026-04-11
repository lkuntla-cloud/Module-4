def palind(r):
    e=len(r)-1
    s=0
    while s<e:
        if r[e]!=r[s]:
            s=+1
            e=e-1
            return True
r=(1,2,3,3,2,1)
if palind(r):
    print("The tuple r is a flip_flop")
else:
    print("The tuple is not a flip_flop")