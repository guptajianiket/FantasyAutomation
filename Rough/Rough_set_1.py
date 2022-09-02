for i in range(2,15):
    a = "contestant" + f"{i}" + "info"
    b = f"//*[@id='wrapper']/div/app-my-league/section/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/swiper/div/div[1]/div[{i}]/div"
    c = " = "
    e = '"'
    f = '"'

    print(a+c+e+b+f)