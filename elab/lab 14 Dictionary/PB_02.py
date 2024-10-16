# 02 Dictionary 2

#  call : para[key] ; retrun value

provinces = {
    'central': ['Bangkok', 'Samut Prakan', 'Nonthaburi', 'Samut Sakhon', 'Ayutthaya', 'Pathum Thani'],
    'northern': ['Chiang Mai', 'Chiang Rai', 'Lamphun', 'Lampang', 'Mae Hong Son', 'Nan'],
    'northeastern': ['Roi Et', 'Chaiyaphum', 'Loei', 'Nong Khai', 'Sakon Nakhon', 'Surin'],
    'southern': ['Surat Thani', 'Krabi', 'Phuket', 'Yala', 'Songkhla', 'Narathiwat']
}

while True:
    text = input()
    
    if text == '':
        break
    
    [province, region] = text.split(':')
    
    if region not in provinces:
        print('No')
        continue
    
    provinceList = provinces[region]
    if province not in provinceList:
        print('No')
        continue
    print('Yes')
    

#  Access with for-in
for region in provinces :
    for province in provinces[region]:
        print(f'{province}:{region}')
        while True:
            text = input()
            
            if text == '':
                break
            
            [province, region] = text.split(':')