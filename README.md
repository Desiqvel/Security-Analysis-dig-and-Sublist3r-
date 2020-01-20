# Sikkerhetsanalyse

#### Table of Contents

1. [Overview - What is sikkerhetsanalyse.py?](#overview)
1. [Module Description - What does the module do?](#module-description)
1. [Dependencies - What is needed?](#dependencies)
1. [Execution - Getting started with Sikkerhetsanalyse.py](#execution)
1. [Usage - Configuration options and additional functionality](#usage)
    * [Examples](#examples)
    * [Disclaimer](#disclaimer)
1. [Limitations - OS compatibility, etc.](#limitations)
1. [Improve](#improve)

## Overview

This module runs a script that runs sublist3r and dig to and reports the outcome to a file.
- Sublist3r - Scans a domain to get subdomains
- Dig - Scans a subdomain to get host IP-address

It is successfully tested on a _Kali Linux 64-Bit_

## Module Description

This script should support Ubuntu 14.04/16.04/18.04, Debian 7/8 and RedHat derivates 6/7.

This module will install a script using python 3

## Dependencies  
  
Python 3 or older
Installed Sublist3r and its dependencies
Installed Dig

### Installation of dependencies

Download Sublist3r from https://github.com/aboul3la/Sublist3r and remember to also install its dependencies.
```
git clone https://github.com/aboul3la/Sublist3r.git 
```

Dig should be preinstalled, if not, download it with the following command in terminal:
```
sudo apt-get install dnsutils
```
then:
```
apt update & apt dist-upgrade
```


## Execution

Use the script with the following steps:
1. Clone this repository;

2. Refer to dependencies for software needed;

3. Run the following command inside downloaded folder;

```
./sikkerhetsanalyse.py < DOMAIN_NAME >
```
4. The script makes a .csv file(or .txt file);


## Usage

To get subdomains and IP-addresses to subdomains to a .csv or .txt file.

`sikkerhetsanalyse.py` prints out subdomain and IP-Address

### Examples
Example print for .csv file:
```
IP,Sub_domain
1111.2222.3333.4444,sub.subdomain.org
5555.6666.7777.8888,"database.subdomain.com,database2.subdomain.com,database3.subdomain.com"
```

Example print for .txt file:
```
1111.2222.3333.4444|sub.subdomain.org
5555.6666.7777.8888|database.subdomain.com,database2.subdomain.com,database3.subdomain.com
```

### Disclaimer

To get the .txt file you have to remove the commented lines in the bottom of the script.
To use the .txt file in another script you have to split two times;
1. `.split('|')` - to get IP-adress and subdomains
2. `.split(',')` - to get list of subdomains


To get files in `testing` to work you first have to run `testScriptMaker.py` for all the necessary .txt files

## Limitations

Only tried on Kali linux and python 3.0

## Improve

