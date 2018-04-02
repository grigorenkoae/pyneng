#!/usr/bin/env python

prefix = str(input('print your prefix:'))

address = prefix.split('/')[0]
mask = prefix.split('/')[1]

#print (address, mask)

net_template = '''
Network:
{0:<10} {1:<10} {2:<10} {3:<10}
{0:08b}   {1:08b}   {2:08b}   {3:08b}  
'''

mask_template = '''
Mask:
/{4}
{0:<10} {1:<10} {2:<10} {3:<10}
{0:08b}   {1:08b}   {2:08b}   {3:08b}
'''

mask_binary_string = ('1' * int(mask)) + ('0' * (32 - int(mask)))
mask_octet_0 = str(mask_binary_string[:8])
mask_octet_1 = str(mask_binary_string[8:16])
mask_octet_2 = str(mask_binary_string[16:24])
mask_octet_3 = str(mask_binary_string[24:32])

mask_dec_0 = int(mask_octet_0,2)
mask_dec_1 = int(mask_octet_1,2)
mask_dec_2 = int(mask_octet_2,2)
mask_dec_3 = int(mask_octet_3,2)


print(net_template.format(int(address.split('.')[0]), int(address.split('.')[1]), int(address.split('.')[2]), int(address.split('.')[3])))

print(mask_template.format(mask_dec_0, mask_dec_1, mask_dec_2, mask_dec_3, mask))


