#greedy algorithm

def findContentChildren(g, s):
    g.sort()  # Sort children's greed factors
    s.sort()  # Sort cookie sizes

    content_children = 0  # Initialize counter for content children

    # Iterate through children's greed factors and available cookies
    child_index = cookie_index = 0
    while child_index < len(g) and cookie_index < len(s):
        if g[child_index] <= s[cookie_index]:
            # If the current child can be satisfied with the current cookie, move to the next child and cookie
            content_children += 1
            child_index += 1
        cookie_index += 1  # Move to the next cookie regardless

    return content_children

g = [1,2,3]
s = [1,2]
res = findContentChildren(g,s)
print(res)


# logic 2 when s[j] >=g[i] condition is not mentioned

def assign_cookies(g,s):
    sum = 0
    counter = 0
    for i in s:
        sum = sum + i
    # print(sum)
    for j in g:
        if sum - j >= 0:
            counter = counter + 1
            sum = sum - j
        # else:
        #     break
    return counter

g = [1,2,3]
s = [1,2,3]
res = assign_cookies(g,s)
print(res)


