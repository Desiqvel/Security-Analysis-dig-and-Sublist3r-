# Sikkerhetsanalyse

## Synopsis

It is successfully tested on a _Kali Linux 64-Bit_ with the following capabilities are included:

- Sublist3r - Scans a domain to get subdomains
- Dig - Scans a subdomain to get host IP-address

## Dependencies 
  Use the updated _Kali Linux 64-Bit_ with sublist3r and dig installed. 
  Python 3 or older

## Installation

If sublist3r isn't preinstalled download it from https://github.com/aboul3la/Sublist3r 
Dig should be preinstalled, if not download it with the following command in terminal:
```
sudo apt-get install dnsutils
```
then:
`apt update & apt dist-upgrade`

Installation of the Cuckoo environment is done with the following steps:
1. Clone this repository;

2. Refer to prerequisites for software needed;

3. Run the following command inside downloaded folder:

```
./sublist3r.py < DOMAIN NAME >
```

4. Open files made


## Usage

To get subdomains and IP-addresses to subdomains

## Disclaimer

Not fully working


## Improve

Get `digvari.py` to print out subdomain and IP-Address
Example print:
```
1111.2222.3333.4444 - sub.subdomain.org
5555.6666.7777.8888 - database.subdomain.com
```
