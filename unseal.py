# python3
import os

os.system("cat /tmp/docker-vault-keys.txt | grep Key")
os.system("cat /tmp/docker-vault-keys.txt | grep Token")

token1 = input("Please input first unseal token > ")
token2 = input("Please input second unseal token > ")
token3 = input("Please input third unseal token > ")

os.system(f"vault operator unseal {token1}")
os.system(f"vault operator unseal {token2}")
os.system(f"vault operator unseal {token3}")
