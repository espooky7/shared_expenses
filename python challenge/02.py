string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw \
fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq \
pcamkkclbcb. lmu ynnjw ml rfc spj."

def decode(string):
	new_string = ""

	for i in range(0, len(string)):
		current = string[i]
		if (current in (' ', '.',"'", '(',')')):
			new = current
		elif (current in ('y','z')):
			j = ord(current) - 26 + 2
			new = chr(j)
		else:
			j = ord(current) + 2
			new = chr(j)

		new_string += new

	return new_string

result = decode(string)
print result

