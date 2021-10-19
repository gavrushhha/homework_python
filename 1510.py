def function(list1, a, n, char):
    sosiska = {
        "center": "^",
        "left": "<",
        "right": ">"
    }
    arg = sosiska.get(a)
    str = ""
    for i in list1:
            str += ('{0:'+ char + arg + '%s'%n + 's}').format(i)
            str += '\n'
    return str

print(function(['ТТТ','WWWWWW','L'], 'center', 20, '!'))