---
layout: post
title: Dealing with secrets, environment variables and GPG conveniently
tags: devops
comments: true
---

This article shows how we make use of environment variables and GPG to easily
switch between credentials for various deployments. In our particular case, we
have various Hashicorp clusters (nomad, consul, vault, ...) deployed and need
to be able to switch between them conveniently and securly.

# Security

Obviously, access credentials to your cloud orchestration has to be kept
confidential. As such, we store our credentials encrypted using gpg/gpg.

# Environment Variables

At least on Linux, dealing with credentials is most convenient going through
environment variables which are read my most of the tools anyhow.

# Example

As an example, here is the content of a GPG encrypted file for one of our
environments:

    TARGET=[staging|prod|infra]
    NOMAD_ADDR=https://nomad.staging.example.com
    NOMAD_TOKEN=**************************
    VAULT_ADDR=https://vault.staging.example.com
    VAULT_TOKEN=**************************
    CONSUL_HTTP_ADDR=https://consul.staging.example.com
    CONSUL_HTTP_AUTH=**************************
    MC_HOST_infra=https://username:**************************@minio.staging.example.com
    TF_VAR_hcloud_token=**************************

As you can see, we use a variable `TARGET` to identify which environment we are
working with (dev, staging, prod, infra).

The content of the file is encrypted using:

    gpg -sear Fabian -o
    ~/Documents/Encrypted/Environments/staging.example.com.gpg

At this place, let me recommend the vim-plugin `jamessan/vim-gnupg` which takes
care of editing the file afterwards.

# Loading Function

For easy loading of your encrypted environment variables, I wrote a shell (zsh)
script:

    def loadenv() {
      export $(gpg -d ~/Documents/Encrypted/Environments/$1.gpg | xargs -0)
    }

# Usage

In case i need to load environment, all I need to do is:

    loadenv staging.example.com

and i get all the variables loaded and ready to go.

# Bonus Material

Since we make heavy use of `make`, here are a few snippets that are useful in
your `Makefile`:

```Makefile
ifndef NOMAD_TOKEN
$(error NOMAD_TOKEN required!)
endif

ifndef VAULT_TOKEN
$(error VAULT_TOKEN required!)
endif

ifndef TARGET
$(error TARGET ['staging','prod', 'infra'] required!)
endif
```

```Makefile
.PHONY: tunnel
tunnel:
ifeq ($(TARGET), infra)
		ssh -N -f -L 4646:10.0.4.2:4646 root@machine1
		ssh -N -f -L 8200:10.0.4.2:8200 root@machine1
		ssh -N -f -L 8500:localhost:8500 root@machine1
endif
ifeq ($(TARGET), staging)
		ssh -N -f -L 4646:10.1.0.4:4646 root@machine2
		ssh -N -f -L 8200:10.1.0.2:8200 root@machine2
		ssh -N -f -L 8500:localhost:8500 root@machine2
endif
```

And for `terraform`:

```Makefile
set_consul: clean
	CONSUL_ADDRESS="$(CONSUL_ADDRESS)" envsubst < terraform.tf.template > terraform.tf

set_workspace:
	terraform workspace select $(TARGET)

init: set_consul
	terraform init -var-file $(TARGET).tfvars
	([[ -z "`terraform workspace list | grep $(TARGET)`" ]] && terraform workspace new $(TARGET)) || exit 0

plan: set_workspace
	terraform plan -var-file $(TARGET).tfvars

apply: set_workspace
	terraform apply -var-file $(TARGET).tfvars
```
