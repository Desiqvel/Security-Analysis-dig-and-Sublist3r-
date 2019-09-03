#!/usr/bin/env python3

array = [['IP', 'SUB']]


with open('nrk.noipaddr.txt') as IPdom:
	for line in IPdom:
		line = line.rstrip('\n')
		var = line.split( '|' )
		array.append(var)
i = 1
for i in array:
	ip = i.pop(0)
	ip = ip.rstrip()
	print(ip)

ip.sort(key=lambda s: map(int, s.split('.')))

outputFile = open(sortereIP.txt, "w")

for s in ip:
	outputFile.write(s+"\n")

outputFile.close()
text_file.close()

