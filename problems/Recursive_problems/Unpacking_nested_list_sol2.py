def flatten_list(n):
    flat_list=[]
    for item in n:
        print(item)
        if isinstance(item, list):
            x = flatten_list(item)
            print(f"list instance item is {x}")
            flat_list.extend(x)
        else:
            print(f"else block - {item}")
            flat_list.append(item)
    return flat_list


n = [[5,6],4]
flat_list = flatten_list(n)
print(flat_list)