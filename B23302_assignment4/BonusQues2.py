lst =eval(input('Bonus Ques (input list):'))
n = len(lst)
i = 0
while i<n:
    mini = lst[i]
    for item in lst[i::]:
        if item < mini:
            mini = item
        else:
            pass
    lst.remove(mini)
    lst.insert(i,mini)
    i += 1
print(lst)
    