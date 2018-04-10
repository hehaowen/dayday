# i**3+j**3+k**3<1000
for i in range(1, 10):
    for j in range(0, 10):
        for z in range(0, 10):
            if (i*100+j*10+z== i ** 3+ j ** 3 + z ** 3):
                m = i*100+j*10+z
                print(m)
            else:
                continue
