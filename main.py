# 1 - misol
teskari = ("apple", "banana", "ok")
print(teskari)

result = teskari.split()
words = []

for i in result:
    words.append(i[::-1])

res = " ".join(words)
print(res)


# 2 - misol
str1 = 'Salom'
str2 = 'Dunyo'

result = (lambda x: x[::-1], str1 + str2)
print(result)


# 3 - misol
convert = lambda m: m * 60

minutes = int(input("Daqiqani kiriting: "))
print(convert(minutes))


# 4 - msiol
argument = (lambda x: 'ruxsat' if x > 18 else 'taqiqlanadi')
print(argument)


# 5 - misol
check_uz = lambda url: url.endswith(".uz")

web1 = "digital.uz"
web2 = "metanit.com"
web3 = "dev.job.uz"

print(check_uz(web1))
print(check_uz(web2))
print(check_uz(web3))










