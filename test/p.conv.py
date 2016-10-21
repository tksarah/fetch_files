#!/usr/bin/python
import json

def ptr_facts(arg):
    for x in arg:
        print "," + str(x),

with open('192.168.175.202','r') as f:
    json_data = json.load(f)
    f.close()

    #print json.dumps(json_data, sort_keys = True, indent = 4)
    #with open('192.168.175.202.csv','w+' as fw

    top = json_data['ansible_facts']
    datetime = top['ansible_date_time']
    dnsinfo = top['ansible_dns']
    netif = top['ansible_interfaces']
    proc = top['ansible_processor']
    ipv4addr = json_data['ansible_facts']['ansible_all_ipv4_addresses']
    def_ipv4addr = json_data['ansible_facts']['ansible_default_ipv4']
    
    print "Date," + str(datetime['date'])
    print "Architecture," + str(top['ansible_architecture'])
    print "Distribution," + str(top['ansible_distribution']) + "," + str(top['ansible_distribution_version']) 
    print "Kernel," + str(top['ansible_kernel'])
    print "OS Family," + str(top['ansible_os_family'])

    # Network
    print "Network Interface",
    ptr_facts(netif)
    print "\nIPv4 Addresses",
    ptr_facts(ipv4addr)
    print "\nDefault IPv4 Address", 
    for a in ['alias','interface','address','network','netmask','gateway','macaddress']:
        print "," + str(def_ipv4addr[a]),

    print "\nDNS Info",
    ptr_facts(dnsinfo['nameservers'])
    print "," + str(dnsinfo['search'][0]) 
    print "Domain," + str(top['ansible_domain'])

    print "TimeZone," + str(datetime['tz'])

    # HW Info
    print "Hostname," + str(top['ansible_hostname'])
    print "Memory Total (MB)," + str(top['ansible_memtotal_mb'])

    print "Processor",
    ptr_facts(proc)
    print "\nProcessor (cores)," + str(top['ansible_processor_cores'])
    print "Processor (count)," + str(top['ansible_processor_count'])
    print "Processor (threads/core)," + str(top['ansible_processor_threads_per_core'])
    print "Processor (vcpus)," + str(top['ansible_processor_vcpus'])

    print "Product Name," + str(top['ansible_product_name'])
    print "Product Serial," + str(top['ansible_product_serial'])
    print "Product UUID," + str(top['ansible_product_uuid'])

    print "System," + str(top['ansible_system'])
    print "System Vendor," + str(top['ansible_system_vendor'])
    print "System Uptime," + str(top['ansible_uptime_seconds'])
