# AnsibleTower_AWX_execution Environment Installation 

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
