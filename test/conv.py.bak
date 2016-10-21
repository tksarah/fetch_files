#!/usr/bin/python

import os
import sys
import json


def ptr_facts(arg):
    for x in arg:
        fp.write("," + str(x))

argvs = sys.argv 
argc = len(argvs)

if (argc != 2):
    print 'Usage: # python %s filename' % argvs[0]
    quit() 

jsonfiles = os.listdir(argvs[1])
dirpath = os.path.dirname(argvs[1])

for file in jsonfiles:
    rfile = dirpath + "/" + file
    csvfile = rfile + ".csv"

    with open(rfile,'r') as f:
        json_data = json.load(f)
        f.close()

    with open(csvfile,'w+') as fp:
        #print json.dumps(json_data, sort_keys = True, indent = 4)
        #with open('192.168.175.202.csv','w+' as fw
    
        top = json_data['ansible_facts']
        datetime = top['ansible_date_time']
        dnsinfo = top['ansible_dns']
        netif = top['ansible_interfaces']
        proc = top['ansible_processor']
        ipv4addr = json_data['ansible_facts']['ansible_all_ipv4_addresses']
        def_ipv4addr = json_data['ansible_facts']['ansible_default_ipv4']
    
        fp.write("Date," + str(datetime['date']) + "\n")
        fp.write("Architecture," + str(top['ansible_architecture']) + "\n")
        fp.write("Distribution," + str(top['ansible_distribution']) + "," + str(top['ansible_distribution_version']) + "\n")
        fp.write("Kernel," + str(top['ansible_kernel']) + "\n")
        fp.write("OS Family," + str(top['ansible_os_family']) + "\n")

        # Network
        fp.write("Network Interface")
        ptr_facts(netif)
        fp.write("\nIPv4 Addresses")
        ptr_facts(ipv4addr)
        fp.write("\nDefault IPv4 Address")
        for a in ['alias','interface','address','network','netmask','gateway','macaddress']:
            fp.write("," + str(def_ipv4addr[a]))

        fp.write("\nDNS Info")
        ptr_facts(dnsinfo['nameservers'])
        fp.write("," + str(dnsinfo['search'][0]) + "\n")
        fp.write("Domain," + str(top['ansible_domain']) + "\n")

        fp.write("TimeZone," + str(datetime['tz']) + "\n")

        # HW Info
        fp.write("Hostname," + str(top['ansible_hostname']) + "\n")
        fp.write("Memory Total (MB)," + str(top['ansible_memtotal_mb']) + "\n")

        fp.write("Processor")
        ptr_facts(proc)
        fp.write("\nProcessor (cores)," + str(top['ansible_processor_cores']) + "\n")
        fp.write("Processor (count)," + str(top['ansible_processor_count']) + "\n")
        fp.write("Processor (threads/core)," + str(top['ansible_processor_threads_per_core']) + "\n")
        fp.write("Processor (vcpus)," + str(top['ansible_processor_vcpus']) + "\n")

        fp.write("Product Name," + str(top['ansible_product_name']) + "\n")
        fp.write("Product Serial," + str(top['ansible_product_serial']) + "\n")
        fp.write("Product UUID," + str(top['ansible_product_uuid']) + "\n")

        fp.write("System," + str(top['ansible_system']) + "\n")
        fp.write("System Vendor," + str(top['ansible_system_vendor']) + "\n")
        fp.write("System Uptime," + str(top['ansible_uptime_seconds']) + "\n")
