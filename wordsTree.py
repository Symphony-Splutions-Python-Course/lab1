n_longest = len(l_text[-1])
n_longest
for i in l_text:
    print(i.center(2*n_longest))
for i in l_text:
    print(i)
l_text.sort(key = len)
l_text
for i in l_text:
    print(i)
l_text = text.split('\n')
l_text
l_text.sort(key = len)
for i in l_text:
    print(i)
n_longest = len(l_text[-1])
for i in l_text:
    print(i.center(n_longest))
for i in l_text:
    print(i.center(n_longest,'.'))

