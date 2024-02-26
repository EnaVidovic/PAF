def jednadzba_pravca(tocka1, tocka2):
    x1, y1 = tocka1
    x2, y2 = tocka2
    
    if x1 == x2:
        print(f"Jednadžba pravca: x = {x1}")
    else:
        k = (y2 - y1) / (x2 - x1)
        n = y1 - k * x1
        print(f"Jednadžba pravca: y = {k}x + {n}")

tocka1 = (2, 3)
tocka2 = (5, 7)

jednadzba_pravca(tocka1, tocka2)
    