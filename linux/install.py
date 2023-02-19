import xml.etree.ElementTree as ET
import shutil

evdevFile = '/usr/share/X11/xkb/rules/evdev.xml'

shutil.copy(evdevFile, './evdev.xml.bak')
tree = ET.parse(evdevFile)
root = tree.getroot()

layout = ET.fromstring('''
<layout>
<configItem>
    <name>dvpfi</name>
    <shortDescription>fi</shortDescription>
    <description>Finnish programmer dvorak</description>
    <languageList>
    <iso639Id>fi</iso639Id>
    </languageList>
</configItem>  
</layout>''')

root[1].append(layout)
ET.indent(tree)

with open('evdev.xml', 'wb') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE xkbConfigRegistry SYSTEM "xkb.dtd">\n'.encode('utf8'))
    tree.write(f, 'utf-8')

shutil.move('evdev.xml', evdevFile)
shutil.copy('dvpfi', '/usr/share/X11/xkb/symbols')
