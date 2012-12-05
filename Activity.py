a = ((2, 4),
     (3, 5),
     (0, 6),
     (5, 7),
     (3, 8),
     (5, 9),
     (6, 10),
     (8, 11),
     (8, 12),
     (2, 13),
     (12, 14))

def greedySelector():

    i = a[0]
    print i
    for n in a:
        if n[0] > i[1]:
            print n
            i = n

if __name__ == "__main__":
    greedySelector()
