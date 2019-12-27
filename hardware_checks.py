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
def smart_disk_checks():
        disks=subprocess.Popen("lsscsi| grep disk| cut -d ' ' -f28", shell=True, stdout=subprocess.PIPE).stdout.read()
        print disks
        disks_list=str(disks)
        lenth=len(disks_list)
        print lenth

def main():
        smart_disk_checks()

if __name__ == "__main__":
        main()
