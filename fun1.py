def draw_1d():
    y = int(input("enter a number: "))
    i = int(input("enter another number: "))
    l = 0
    s = 0
    while s<i:
        while  l<1 or l==i :
            print(y * "*")
            l = l + 1
        print("*" + "."*(y+1) + "*")
        s = s + 1
  
draw_1d()



