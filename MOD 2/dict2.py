d = {6:'q',1:'s',5:'w',0:'e'}
k = sorted(list(d.keys()))
dd = {i:d[i] for i in k}
print(dd)

kk = k[::-1]
ddd = {i:d[i] for i in kk}
print(ddd)