#!/bin/bash

# INCOMPLETE

docker-compose up -d consul
docker-compose up -d vault
echo "exporting VAULT_ADDR"
echo "echoing VAULT_ADDR:"
echo $VAULT_ADDR
export VAULT_ADDR='http://127.0.0.1:8200'
echo "complete"
echo "creating keys in /tmp/docker-vault-keys.txt"
vault operator init -key-shares=3 -key-threshold=2 > /tmp/docker-vault-keys.txt
cat /tmp/docker-vault-keys.txt | grep Key
cat /tmp/docker-vault-keys.txt | grep Token
