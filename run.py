import os,sys
#try:os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
#except:pass
try:os.system('git pull')
except:pass
#try:os.system('xdg-open https://chat.whatsapp.com/I48BIjjU0gGDIAfhZ7OUYL')
#except:pass
from platform import uname
bt=uname().machine.lower()
if 'aarch' in bt:
  os.system('chmod 777 insto_;./insto_')
else:
  exit('Sorry This Tools Not Working 32 Bit Device')
