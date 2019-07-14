import os
import xml.etree.ElementTree as ET

input_dir = 'mediaportal-nz-logos'
output_dir = 'icons'

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

mapping = ET.parse(input_dir + '/LogoMapping.xml')

for type in mapping.getroot().findall('*'):
    for channel in type.findall('Channel'):
        for item in channel.findall('Item'):

            source_filename = '../' + input_dir + '/' + type.tag + '/Simple200/' + channel.find('File').text
            dest_filename = output_dir + '/' + item.attrib['Name']
            if os.path.islink(dest_filename):
                os.remove(dest_filename)

            os.symlink(source_filename, dest_filename)
