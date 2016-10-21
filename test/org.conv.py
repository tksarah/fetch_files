#!/usr/bin/python
import json

def ptr_facts(arg):
    for x in arg:
        print "," + str(x),
        fp.write("," + str(x))

with open('192.168.175.202','r') as f:
    json_data = json.load(f)
    f.close()

with open('192.168.175.202.csv','w+') as fp:
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
    fp.write("OS Family ," + str(top['ansible_os_family']) + "\n")
    print "Date," + str(datetime['date'])
    print "Architecture," + str(top['ansible_architecture'])
    print "Distribution," + str(top['ansible_distribution']) + "," + str(top['ansible_distribution_version']) 
    print "Kernel," + str(top['ansible_kernel'])
    print "OS Family," + str(top['ansible_os_family'])

    # Network
    print "Network Interface",
    fp.write("Network Interface")
    ptr_facts(netif)
    print "\nIPv4 Addresses",
    fp.write("\nIPv4 Addresses")
    ptr_facts(ipv4addr)
    print "\nDefault IPv4 Address", 
    for a in ['alias','interface','address','network','netmask','gateway','macaddress']:
        print "," + str(def_ipv4addr[a]),
    fp.write("\nDefault IPv4 Address")
    for a in ['alias','interface','address','network','netmask','gateway','macaddress']:
        fp.write("," + str(def_ipv4addr[a]))

    print "\nDNS Info",
    fp.write("\nDNS Info")
    ptr_facts(dnsinfo['nameservers'])
    print "," + str(dnsinfo['search'][0]) 
    fp.write("," + str(dnsinfo['search'][0]) + "\n")
    print "Domain," + str(top['ansible_domain'])
    fp.write("Domain," + str(top['ansible_domain']) + "\n")

    print "TimeZone," + str(datetime['tz'])
    fp.write("TimeZone," + str(datetime['tz']) + "\n")

    # HW Info
    print "Hostname," + str(top['ansible_hostname'])
    fp.write("Hostname," + str(top['ansible_hostname']) + "\n")
    print "Memory Total (MB)," + str(top['ansible_memtotal_mb'])
    fp.write("Memory Total (MB)," + str(top['ansible_memtotal_mb']) + "\n")

    print "Processor",
    fp.write("Processor")
    ptr_facts(proc)
    print "\nProcessor (cores)," + str(top['ansible_processor_cores'])
    fp.write("\nProcessor (cores)," + str(top['ansible_processor_cores']) + "\n")
    print "Processor (count)," + str(top['ansible_processor_count'])
    fp.write("Processor (count)," + str(top['ansible_processor_count']) + "\n")
    print "Processor (threads/core)," + str(top['ansible_processor_threads_per_core'])
    fp.write("Processor (threads/core)," + str(top['ansible_processor_threads_per_core']) + "\n")
    print "Processor (vcpus)," + str(top['ansible_processor_vcpus'])
    fp.write("Processor (vcpus)," + str(top['ansible_processor_vcpus']) + "\n")

    print "Product Name," + str(top['ansible_product_name'])
    fp.write("Product Name," + str(top['ansible_product_name']) + "\n")
    print "Product Serial," + str(top['ansible_product_serial'])
    fp.write("Product Serial," + str(top['ansible_product_serial']) + "\n")
    print "Product UUID," + str(top['ansible_product_uuid'])
    fp.write("Product UUID," + str(top['ansible_product_uuid']) + "\n")

    print "System," + str(top['ansible_system'])
    fp.write("System," + str(top['ansible_system']) + "\n")
    print "System Vendor," + str(top['ansible_system_vendor'])
    fp.write("System Vendor," + str(top['ansible_system_vendor']) + "\n")
    print "System Uptime," + str(top['ansible_uptime_seconds'])
    fp.write("System Uptime," + str(top['ansible_uptime_seconds']) + "\n")
