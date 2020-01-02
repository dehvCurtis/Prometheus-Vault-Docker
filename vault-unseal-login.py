# python3
# by: dehvon curtis
import os

os.system("cat /tmp/docker-vault-keys.txt | grep Key")


token1 = input("Please input first unseal key > ")
token2 = input("Please input second unseal key > ")
token3 = input("Please input third unseal key > ")

os.system(f"vault operator unseal {token1}")
os.system(f"vault operator unseal {token2}")
os.system(f"vault operator unseal {token3}")

os.system("cat /tmp/docker-vault-keys.txt | grep Token")
roottoken = input("Please input root token > ")
os.system(f"vault login {roottoken}")

print("enabling kv secrets and creating path")
os.system("vault secrets enable -path=secret/ kv")
