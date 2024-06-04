while 1:
    print('\n1.Create a list\n2.Merge 2 lists\n3.Replace a word in list\n4.Insert element in middle of list')
    ch = input('Enter your choice')

    if ch=='1':
        list1 = input('Enter your elements for the list : ').split()
        print(list1)
    elif ch=='2':
        l1 = input('Enter the contents for list 1 : ').split()
        l2 = input('Enter the contents for list 2 : ').split()
        l3 = l1+l2
        print(l3)
    elif ch=='3':
        l1 = input('Enter the words for the list : ').split()
        print(f'Your list is {l1}')
        w = input('Enter the word to be replaced in list : ')
        w2 = input('Enter the word to be inserted : ')
        l1.insert(l1.index(w),w2)
        l1.pop(l1.index(w))
        print(l1)
    elif ch=='4':
        l1 = input('Enter the elements for list : ').split()
        print(f'This is your list {l1}')
        l1.insert(len(l1)//2,input('Enter the element you want to insert : '))
        print(f'List after insertion : {l1}')
    else:
        print('Wrong Input!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
