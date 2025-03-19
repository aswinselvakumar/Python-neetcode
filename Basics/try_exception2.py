def div_num(a:str,b:str)->int:
    
    try:
        a_int = int(a)
        b_int = int(b)
        result = a_int/b_int
        return result
    except ValueError:
        print("value error")
    except ZeroDivisionError:
        print("Zero division error")
    except Exception as error:
        print("Error occured:",error)
    return None

print(div_num("1","2"))