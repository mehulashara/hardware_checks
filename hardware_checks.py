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
        disks=os.system("lsscsi|grep disk| awk -F ' ' '{print $6}'")
#       print disks
        disks_list=str(disks)
        print disks_list[0]

def main():
        smart_disk_checks()

if __name__ == "__main__":
        main()
