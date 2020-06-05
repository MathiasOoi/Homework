ans = 20
while True:
    if all(not ans%i for i in [11, 13, 14, 16, 17, 18, 19, 20]):
        print(ans)
        break
    ans += 20
