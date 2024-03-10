def linear_search(ele, list):
    for i in range(len(list)):
            if ele == list[i]:
                return i


    return f"{ele} is not found in list"


res = linear_search(6, [1,4,5])
print(res)