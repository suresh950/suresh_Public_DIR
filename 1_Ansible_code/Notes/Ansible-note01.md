ssh to Ubuntu-C to Ubuntu1 without login credential (login Using Key)

# login to remote ubuntu server Using Key

## Table of Contents
1. [Know_host](#Know_host)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Modules](#modules)
5. [Playbooks](#playbooks)
6. [Roles](#roles)
7. [Best Practices](#best-practices)
8. [Advanced Topics](#advanced-topics)
9. [Troubleshooting](#troubleshooting)
10. [Resources](#resources)

## Know_host
- **What is Know_host?**
  - A known host is a file storing all the SSH fingerprints. 
  - Each ssh connection will store two fingerprints, one for the remote host username and another for the remote host IP 
ansible@ubuntu-c:~$ 
ansible@ubuntu-c:~$ 
ansible@ubuntu-c:~$ cd .ssh
-bash: cd: .ssh: No such file or directory
ansible@ubuntu-c:~$ cd .ssh/
-bash: cd: .ssh/: No such file or directory
ansible@ubuntu-c:~$ cd /.ssh/
-bash: cd: /.ssh/: No such file or directory
ansible@ubuntu-c:~$ cd /.ssh
-bash: cd: /.ssh: No such file or directory 
ansible@ubuntu-c:~$ ls 
testfile
ansible@ubuntu-c:~$ ssh ansible@ubuntu1
The authenticity of host 'ubuntu1 (172.19.0.7)' can't be established.
ECDSA key fingerprint is SHA256:z96FbonokCWqE89m5pGU/ug7BgdBaJbGeCivWqxdLvE.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'ubuntu1,172.19.0.7' (ECDSA) to the list of known hosts.
ansible@ubuntu1's password: 
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.
ansible@ubuntu1:~$ 
ansible@ubuntu1:~$ exit
logout
Connection to ubuntu1 closed.
ansible@ubuntu-c:~$ 
ansible@ubuntu-c:~$ cd /.ssh
-bash: cd: /.ssh: No such file or directory
ansible@ubuntu-c:~$ cd .ssh/
ansible@ubuntu-c:~/.ssh$ 
ansible@ubuntu-c:~/.ssh$ 
ansible@ubuntu-c:~/.ssh$ ls 
known_hosts
ansible@ubuntu-c:~/.ssh$ cat known_hosts 
|1|1/VGqOXxohAVtS7XiohYNgfJiUM=|6FzG5oY6S2lee4q78flB/t8Ormc= ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAIllTL6bzJMZp11kPM/Fo9Ufr07yim/KQDPkNz0yhElrd+kx5+tpOVp7AIyXxYhfA0pkuxVdlzCxuVDm/Ls3fk=
|1|dsOL0PXW6DShcCsqBoLJjY8IPfg=|DcjxhcMKo/6j23cO8t6Yh+liIss= ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBAIllTL6bzJMZp11kPM/Fo9Ufr07yim/KQDPkNz0yhElrd+kx5+tpOVp7AIyXxYhfA0pkuxVdlzCxuVDm/Ls3fk=
ansible@ubuntu-c:~/.ssh$ 
## Installation
- **Prerequisites**
  - Software and hardware requirements
- **Installation Steps**
  - Detailed steps to install Ansible on different operating systems

## Configuration
- **Inventory File**
  - Structure and examples
- **Ansible Configuration File (ansible.cfg)**
  - Key settings and options

## Modules
- **Core Modules**
  - Overview of commonly used core modules
- **Custom Modules**
  - Creating and using custom modules

## Playbooks
- **Structure of a Playbook**
  - YAML syntax and structure
- **Examples**
  - Basic to advanced playbook examples

## Roles
- **Creating Roles**
  - Role directory structure
- **Using Roles**
  - How to include and use roles in playbooks

## Best Practices
- **Coding Standards**
  - Tips for writing clean and efficient Ansible code
- **Security Practices**
  - Ensuring security in your Ansible setup

## Advanced Topics
- **Ansible Vault**
  - Encrypting sensitive data
- **Dynamic Inventory**
  - Using dynamic inventory scripts
- **Ansible Galaxy**
  - Finding and using roles from Ansible Galaxy

## Troubleshooting
- **Common Issues**
  - Solutions to common problems faced while using Ansible
- **Debugging Tips**
  - Tips and tricks for debugging Ansible playbooks

## Resources
- **Official Documentation**
  - Links to official Ansible documentation
- **Community Resources**
  - Useful blogs, forums, and tutorials

---
