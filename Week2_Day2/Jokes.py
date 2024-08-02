# create a virtual environment
# python -m venv ./oscar_env


# activate the virtual environment
# source ./oscar_env/bin/activate (MAC OS)
# ./oscar_env/Scripts/activate (Windows)


# pip install pyjokes (install the pyjokes package)

import pyjokes


# print(pyjokes.get_joke('en','chuck'))

for jokes in pyjokes.get_jokes('en','chuck'):
    print(jokes)
    print('__________________')
    response = input('Do you want another joke? (y/n): ')
    if response == 'n':
        break