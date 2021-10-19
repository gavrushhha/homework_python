def function():
    club = dict()
    myname = ''
    mynomer = ''
    while myname != 'q' and mynomer != 'q':
        myname = input()
        if (myname == 'q'):
            break
        mynomer = input()
        if mynomer == 'q':
            break
        if mynomer[0]=='+' and mynomer[1].isdigit and mynomer[2]=="-" and mynomer[3:6].isdigit and mynomer[6]=='-' and mynomer[7:10].isdigit and mynomer[10]=='-' and mynomer[11:13].isdigit and mynomer[13]=='-' and mynomer[14:] and len(mynomer)==16:
            club[myname] = mynomer
        else:
            print('Error')
    print(club)



function()