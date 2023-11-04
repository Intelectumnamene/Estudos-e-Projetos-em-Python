import re

hey = 'Luizinho_2002@hotmail.com'
#Findall
result = re.findall(r"(@.{1,8}\.)",hey)
print(result)
result = re.search(r"(@.{1,8}\.)",hey)
print(result)
result = re.split(r"(@.{1,8}\.)",hey)
print(result)
result = re.sub(r"(@.{1,8}\.)",'@gmail.',hey)
print(result)