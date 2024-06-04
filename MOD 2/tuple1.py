t1 = (1,2,4,5,11)
t2 = (1,2,4,5,11)

if len(t1)==len(t2):
    for i in t1:
        if i not in t2:
            print('tuples are not equal')
            break
    else:
        print('The tuples are same')
else:
    print('The tuples are not equal')