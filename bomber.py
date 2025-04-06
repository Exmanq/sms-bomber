import requests

nomer = input("Введите номер телефона: ")
a = requests.post("URL with API request",
                  json=({
  "phone": nomer},))
print(a.text)
input()
