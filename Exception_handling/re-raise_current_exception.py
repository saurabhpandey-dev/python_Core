def process_data(data):
    try:
        return data/0
    except ZeroDivisionError:
        print('handled in the function first !')
        raise


try:
    process_data(5)
except:
    print('handled outside the function and re_raise the error')
    
