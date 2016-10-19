# Playbook and Role for fetching files
## Support
- Ansible Host v2.1.2
* Perl's JSON module

##  How to use

### Preparation

* Ansible Inventory file ( host list of target )
* File list to fetch

Sample inventory file
```
[hoge]
192.168.0.1 ansible_user=ubuntu ansible_ssh_private_key_file=./kura-key2
192.168.0.2 ansible_user=root ansible_ssh_private_key_file=./cloud.key
192.168.0.3 ansible_user=root ansible_pass=password
```

Sample list file
```
/etc/ssh/sshd_config
/usr/bin/python
/etc/nsswitch.conf
/etc/SuSE-release
/etc/lsb-release

```

# Run

```
# ansible-playbook -i hosts site.yml
Input target host [all]: a.example.com
Input your file list: sample.txt
Input a save directory [fetched]: /tmp/savedir

PLAY [Playbook for fetching files] *********************************************

``` 

# Result

```
# tree /tmp/savedir
/tmp/savedir
|-- 192.168.0.151
|   |-- etc
|   |   |-- SuSE-release
|   |   |-- nsswitch.conf
|   |   `-- ssh
|   |       `-- sshd_config
|   `-- usr
|       `-- bin
|           `-- python
`-- facts
    |-- 192.168.0.151
    `-- 192.168.0.151.csv

```
