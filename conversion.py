a=int(input("days"))
year=month=week=d=0
if a>=365:
    year=int(a/365)
    a-=year*365
    print(year)
