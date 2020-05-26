import webbrowser

while True:
    print('choose :\n1.google\n2.yahoo\n3.bing\n4.open all three')
    t = int(input('\nenter: '))
    if t == 1:
        webbrowser.open('https://www.google.com/')
    elif t == 2:
        webbrowser.open('https://in.yahoo.com/?p=us')
    elif t == 3:
        webbrowser.open('https://www.bing.com/')
    elif t== 4:
        webbrowser.open('https://www.google.com/')
        webbrowser.open('https://in.yahoo.com/?p=us')
        webbrowser.open('https://www.bing.com/')
    else:
        print('wrong option')
