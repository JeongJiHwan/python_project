T = int(input())
for _ in range(T):
    G = input()
    ans = []
    check = True
    for i in G:
        if i in ["(", "{", "["]:
            ans.append(i)
        elif i in [")", "}", "]"]:
            if len(ans) == 0:
                check = False
                break
            elif ans[-1]+i not in ["()", "{}", "[]"]:
                check = False
                break
            elif ans[-1]+i in ["()", "{}", "[]"]:
                ans.pop()

    if ans:
        check = False
        
    if check:
        print('YES')
    else:
        print('NO')
