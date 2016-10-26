# Playbook and Role for fetching files
## Support
* Ansible Host v2.x.x < (tested by v2.1.2)
* ~~Perl's JSON module~~

## Role Description

* [fetch-files](https://galaxy.ansible.com/tksarah/fetch-files/)
* [fetch-command-out](https://galaxy.ansible.com/tksarah/fetch-command-out/)

##  How to use

### Preparation

* Ansible Inventory file ( host list of target )
* File list to fetch

Sample of inventory file
```
[hoge]
192.168.175.202 ansible_user=root ansible_ssh_private_key_file=./cloud.key
192.168.175.203 ansible_user=root ansible_pass=password
```

Sample of list file
```
# more sample_filelist.txt
/etc/ssh/sshd_config
/usr/bin/python
/etc/nsswitch.conf
/etc/SuSE-release
/etc/lsb-release

# more sample_comlist.txt
'ls -l /etc','ls_l'
'hostid','hostid_out'
'cat /etc/hosts','cat_hosts'
```

## Run

```
# ansible-playbook -i hosts site.yml -e "comget=y json2csv=y"
Input target host [all]:
Input your file list [sample_filelist.txt]:
Input your command list [sample_comlist.txt]:
Input remote temp directory  [/tmp/remtemp]:
Input a save directory [fetched]:
PLAY [Playbook for fetching files] *********************************************
                           :
                           :
                           :
                           :
PLAY RECAP *********************************************************************
192.168.175.202            : ok=19   changed=6    unreachable=0    failed=0
192.168.175.203            : ok=17   changed=6    unreachable=0    failed=0
``` 

## Result

```
fetched
|-- 192.168.175.202
|   |-- etc
|   |   |-- SuSE-release
|   |   |-- nsswitch.conf
|   |   `-- ssh
|   |       `-- sshd_config
|   |-- tmp
|   |   `-- remtemp
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
|   |   `-- remtemp
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

## Sample Playbook

```
- name: Playbook for fetching files
  hosts: "{{ target }}"
  gather_facts: no

  become: true
  become_user: root

  vars_prompt:
    - { name: "target" , prompt: "Input target host" ,  default: all , private: no }
    - { name: "inputfile" , prompt: "Input your file list" , default: sample_filelist.txt , private: no }
    - { name: "inputcommand" , prompt: "Input your command list" , default: sample_comlist.txt , private: no }
    - { name: "remtemp" , prompt: "Input remote temp directory " , default: /tmp/remtemp , private: no }
    - { name: "savedir" , prompt: "Input a save directory" , default: fetched , private: no }

  vars:
    facts_dir: "{{ savedir }}/facts/"
    comget: "n"
    json2csv: "n"

  pre_tasks:
    - block:
        - name: Pre get ansible_facts
          raw: ansible -i hosts "{{ target }}" -m setup --tree "{{ facts_dir }}"
        - name: Pre setup (create lists for fetch)
          raw: ./roles/tksarah.fetch-files/tools/create_vars.pl "{{ inputfile }}"
      become: false
      delegate_to: localhost

    - block:
        - name: Pre get command list
          raw: ./roles/tksarah.fetch-command-out/tools/create_vars.pl "{{ inputcommand }}"
      become: false
      delegate_to: localhost
      when: comget == "y"

  roles:
    - tksarah.fetch-files
    - { role: tksarah.fetch-command-out, when: "comget == 'y'" }

  post_tasks:
    - block:
      - name: Find facts of Hosts
        find: paths="{{ facts_dir }}" patterns="^(\d+).(\d+).(\d+).(\d+)$" use_regex=True
        register: findout
      - name: Convert JSON to csv
        raw: ./tools/conv.py -i "{{ item.path }}"
        with_items:
          - "{{ findout.files }}"
      delegate_to: localhost
      run_once: true
      become: false
      when: json2csv == "y"
```
