ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'Ad31n15Tr@t012'

USER = input('Username: ')
PASE = input('Password: ')

if USER == ADMIN_USERNAME and PASE == ADMIN_PASSWORD :
    print('Welcome, admin.')
else:
    print('You are not admin.')