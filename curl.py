#pip install requests
import requests

response = requests.get('https://raw.githubusercontent.com/rogerpence/visual-studio-code-backups/master/keybindings.json')
with open('keybindings.json', 'w') as writer:
    writer.write(response.text)

response = requests.get('https://raw.githubusercontent.com/rogerpence/visual-studio-code-backups/master/settings.json')
with open('settings.json', 'w') as writer:
    writer.write(response.text)

response = requests.get('https://raw.githubusercontent.com/rogerpence/visual-studio-code-backups/master/snippets/javascript.json')
with open('javascript.json', 'w') as writer:
    writer.write(response.text)

response = requests.get('https://raw.githubusercontent.com/rogerpence/visual-studio-code-backups/master/vsc-extensions.txt')
with open('extensions.txt', 'w') as writer:
    writer.write(response.text)

