def divide(x,y):
    try:
        result = x/y
        print(result)
    # except ZeroDivisionError:
    #     print('ZeroDivisionError')
    except Exception as e:
        print('AAAAAAAA')
    else:
        print('This is else block')
    finally:
        print('This is final block')

divide(2,9)
divide(2,'jj')