import re 

with open('install-extensions.bat', 'w') as writer:
    filepath = 'extensions.txt'
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            extension_only = re.sub(r'\@.*$', '', line).strip()
            writer.write('call code --install-extension ' + extension_only + '\n')
            line = fp.readline()