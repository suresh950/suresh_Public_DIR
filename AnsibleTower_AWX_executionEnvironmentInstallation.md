# AnsibleTower_AWX_execution Environment Installation 

### execution-environment.yml

```python
---
version: 3
additional_build_steps:
  prepend_final:
    - |
      RUN sed -i 's|^mirrorlist=|#mirrorlist=|g' /etc/yum.repos.d/CentOS-* \
       && sed -i 's|^#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-* \
       && dnf clean all \
       && dnf makecache
images:
  base_image:
    # name: quay.io/ansible/ansible-runner:stable-2.10-latest
    name: quay.io/ansible/ansible-runner:latest
dependencies:
  system: bindep.txt
  galaxy: requirements.yml
  python: requirements.txt
```

```python
version: 3
additional_build_steps:
  prepend_base:
    - |
      RUN sed -i 's|^mirrorlist=|#mirrorlist=|g' /etc/yum.repos.d/CentOS-* \
       && sed -i 's|^#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-* \
       && dnf clean all \
       && dnf makecache
images:
  base_image:
    name: quay.io/ansible/ansible-runner:latest

dependencies:
  system: bindep.txt
  galaxy: requirements.yml
  python: requirements.txt

```


### requirements.txt

```python
ansible
netmiko
pyats
requests

```

### requirements.yml
```python
---
collections:
  - name: paloaltonetworks.panos

```

### bindep.txt 
```python
git

```
