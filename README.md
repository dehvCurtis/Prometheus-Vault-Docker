# Prometheus-Vault-Docker
Promethesu Vault Docker for testing

# Overview

This repository will create a Vault server using Consul backend with telemetry metrics using Prometheus.

The following containers are included:

    consul
    vault
    prometheus

## Configure Consul

Start Consul:
```
$ docker-compose up -d consul
```
Consul UI: http://localhost:8500

Start Vault
```
$ docker-compose up -d vault
```

Vault UI: http://localhost:8200

## Configure Vault

Initialize Vault:
```
$ export VAULT_ADDR='http://127.0.0.1:8200'

$ vault operator init -key-shares=3 -key-threshold=2 > /tmp/docker-vault-keys.txt
```
Unseal Vault:
```
$ cat /tmp/docker-vault-keys.txt
$ vault operator unseal <token1> 
$ vault operator unseal <token1> 
$ vault operator unseal <token3> 
```
Configure Vault:
```
$ vault login # use root token

$ vault secrets enable -path=secret/ kv
```
## Configure Prometheus

Add the root token to the prometheus.yml file in the bearer_token: section.

Start Prometheus
```
docker-compose up -d prom
```
Prometheus UI: http://localhost:9090

Stop Containers
```
$ docker-compose stop
```
Vault Telemetry Metrics: https://www.vaultproject.io/docs/internals/telemetry.html
