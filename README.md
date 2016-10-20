# Playbook and Role for fetching files
## Support
- Ansible Host v2.1.2
* Perl's JSON module
## Role Description
### fetch_file
### run_out_fetch

# fetch_file Role
##  How to use

### Preparation

* Ansible Inventory file ( host list of target )
* File list to fetch

Sample of inventory file
```
[hoge]
192.168.0.1 ansible_user=ubuntu ansible_ssh_private_key_file=./kura-key2
192.168.0.2 ansible_user=root ansible_ssh_private_key_file=./cloud.key
192.168.0.3 ansible_user=root ansible_pass=password
```

Sample of list file
```
/etc/ssh/sshd_config
/usr/bin/python
/etc/nsswitch.conf
/etc/SuSE-release
/etc/lsb-release

```

## Run

```
# ansible-playbook -i hosts site.yml
Input target host [all]: a.example.com
Input your file list: sample.txt
Input a save directory [fetched]: /tmp/savedir

PLAY [Playbook for fetching files] *********************************************

``` 

## Result

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

# run_out_fetch Role
##  How to use
### Preparation

* Ansible Inventory file ( host list of target )
* Command list to run

Sample of Command list file
```
'ls -l /etc','ls_l'
'hostid','hostid_out'
'cat /etc/hosts','cat_hosts'

```

## Run

Run with -e comget=y ( extra valiable ) 

```
# ansible-playbook -i hosts site.yml -e comget=y
Input target host [all]:
Input your file list: sample.txt
Input your command list: sample2.txt
Input remote temp directory  [/tmp/remtemp]: /tmp/hoge
Input a save directory [fetched]: mydir

PLAY [Playbook for fetching files] *********************************************

``` 

## Result
```
# tree mydir
mydir
|-- 192.168.175.202
|   |-- etc
|   |   |-- SuSE-release
|   |   |-- nsswitch.conf
|   |   `-- ssh
|   |       `-- sshd_config
|   |-- tmp
|   |   `-- hoge
|   |       |-- cat_hosts
|   |       |-- hostid_out
|   |       `-- ls_l
|   `-- usr
|       `-- bin
|           `-- python
|-- 192.168.175.203
|   |-- etc
|   |   |-- SuSE-release
|   |   |-- nsswitch.conf
|   |   `-- ssh
|   |       `-- sshd_config
|   |-- tmp
|   |   `-- hoge
|   |       |-- cat_hosts
|   |       |-- hostid_out
|   |       `-- ls_l
|   `-- usr
|       `-- bin
|           `-- python
`-- facts
    |-- 192.168.175.202
    |-- 192.168.175.202.csv
    |-- 192.168.175.203
    `-- 192.168.175.203.csv
```

