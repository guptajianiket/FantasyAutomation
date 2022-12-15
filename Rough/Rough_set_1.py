for i in range(2,13):
    a = "user" + f"{i - 1}" + "scoreinfosx"
    b = f"//*[@id='wrapper']/div/app-leaderboard/section/div/div[2]/div[3]/div/div[2]/div[{i}]"
    c = " = "
    e = '"'
    f = '"'

    print(a+c+e+b+f)


