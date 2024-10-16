# 03 Dictionary 3

provinces = {
    'central': ['Bangkok', 'Samut Prakan', 'Nonthaburi', 'Samut Sakhon', 'Ayutthaya', 'Pathum Thani'],
    'northern': ['Chiang Mai', 'Chiang Rai', 'Lamphun', 'Lampang', 'Mae Hong Son', 'Nan'],
    'northeastern': ['Roi Et', 'Chaiyaphum', 'Loei', 'Nong Khai', 'Sakon Nakhon', 'Surin'],
    'southern': ['Surat Thani', 'Krabi', 'Phuket', 'Yala', 'Songkhla', 'Narathiwat']
}

while True:
    text = input()
    if text == "":
        break
    [province, region] = text.split(':')
    
    provinces[region].append(province)