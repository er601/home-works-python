GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}

coursess = {
    'Ux-Ui',
    'Motion-design',
    'English',
    'GeekCamp',
    'Ios',
}

del GeekTech['bag']
GeekTech['address'] = 'Ibraimova 103'
GeekTech['nomer'], GeekTech['instagram'] = '0 500 500 500', '@GeekTech.kg'
# GeekTech['instagram'] = '@GeekTech.kg'
GeekTech['courses'] += coursess
GeekTech['courses'] = set(GeekTech['courses'])
for k, v in GeekTech.items():
    print(f'{k} : {v}')
