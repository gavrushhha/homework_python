import matplotlib.pyplot as pt

while True:
    if input ('Continue y/n: ') == 'n':
        break
    else:
        xs = input('x: ')
        ys = input('y: ')
        color = input('Color')
        try:
            xs_int = [int(x) for x in xs.split()]
            ys_int = [int(y) for     y in ys.split()]
        except Exception as e:
            print('Invalid data', e)
        else:
            if color:
                pt.plot(xs_int, ys_int, color = color)
            else:
                pt.plot(xs_int, ys_int)
pt.show()
