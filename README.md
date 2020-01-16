# Sikkerhetsanalyse

## Synopsis

It is successfully tested on a _Kali Linux 64-Bit_ with the following capabilities are included:

- Sublist3r - Scans a domain to get subdomains
- Dig - Scans a subdomain to get host IP-address


## Dependencies 
  Use the updated _Kali Linux 64-Bit_ with sublist3r and dig installed. 
  Python 3 or older

Installed Sublist3r 
Installed Dig

## Installation

If sublist3r isn't preinstalled download it from https://github.com/aboul3la/Sublist3r and remember to also install its dependencies.
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
4. The script makes a .csv file;


## Usage

To get subdomains and IP-addresses to subdomains to a .csv file.

`sikkerhetsanalyse.py` prints out subdomain and IP-Address
Example print:
```
1111.2222.3333.4444|sub.subdomain.org
5555.6666.7777.8888|database.subdomain.com,database2.subdomain.com,database3.subdomain.com
```

## Disclaimer

To use the .csv file you have to split two times;
1. `.split('|')` - to get IP-adress and subdomains

2. `.split(',')` - to get list of subdomains


To get files in `testing` to work you first have to run `testScriptMaker.py` for all the necessary .txt files


## Improve

