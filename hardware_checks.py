#!/usr/bin/python
#------------------------------------------------------------------------#
# File name: hardware_checks.py
# Author: Mehul Ashara  
# Email: mehul.ashara@nutanix.com
# Date created: 28/12/2019
# Date last modifed: 
# Python version: 2.7.5
# Purpose: Run NX hardware checks from bootable Phoenix ISO
# Usage: python 
# Run ONLY as root user
#-------------------------------------------------------------------------#
import subprocess,sys,os
def smart_disk_checks(f):
#       disks=subprocess.Popen("lsscsi| grep disk| cut -d '/' -f3", shell=True, stdout=subprocess.PIPE).stdout.read()
#       print str(disks)
#       print len(disks)
        disks=subprocess.Popen("ls /dev/sd*", shell=True, stdout=subprocess.PIPE).stdout.read()
        print str(disks)
#       print(list(disks))
        L = disks.split('\n')
        print L
        num_disks=len(L) - 1
        for x in range(num_disks): 
                print L[x] 
                disk = str(L[x])
                args= "smartctl -a " + disk
                f.write(args)
                subprocess.call(args, shell=True)
                partitions = "fdisk -l " + disk
                print partitions
                subprocess.call(partitions, shell=True)
        f.close()
def main():
        print("Offline Node Health Checks Summary\n################################################################################\nSUMMARY\n################################################################################")
        f=open("offline_node_health_check_summary","w+")
        smart_disk_checks(f)

if __name__ == "__main__":
        main()
