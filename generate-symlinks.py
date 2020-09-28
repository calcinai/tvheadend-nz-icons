import os
import xml.etree.ElementTree as ET

input_dir = 'mediaportal-nz-logos'
output_dir_light = 'icons/light'
output_dir_dark = 'icons/dark'

if not os.path.exists(output_dir_light):
    os.mkdir(output_dir_light)

if not os.path.exists(output_dir_dark):
    os.mkdir(output_dir_dark)

mapping = ET.parse(input_dir + '/LogoMapping.xml')

for type in mapping.getroot().findall('*'):
    for channel in type.findall('Channel'):
        for item in channel.findall('Item'):

            # Light
            source_filename = '../../' + input_dir + '/' + type.tag + '/.Light/' + channel.find('File').text
            dest_filename = output_dir_light + '/' + item.attrib['Name'].lower()
            if os.path.islink(dest_filename):
                os.remove(dest_filename)

            os.symlink(source_filename, dest_filename)

            # Light - Actual filename
            source_filename = '../../' + input_dir + '/' + type.tag + '/.Light/' + channel.find('File').text
            dest_filename = output_dir_light + '/' + os.path.splitext(channel.find('File').text)[0].lower()
            if os.path.islink(dest_filename):
                os.remove(dest_filename)

            os.symlink(source_filename, dest_filename)


            # Dark
            source_filename = '../../' + input_dir + '/' + type.tag + '/.Dark/' + channel.find('File').text
            dest_filename = output_dir_dark + '/' + item.attrib['Name'].lower()
            if os.path.islink(dest_filename):
                os.remove(dest_filename)

            os.symlink(source_filename, dest_filename)

            # Dark - Actual filename
            source_filename = '../../' + input_dir + '/' + type.tag + '/.Dark/' + channel.find('File').text
            dest_filename = output_dir_dark + '/' + os.path.splitext(channel.find('File').text)[0].lower()
            if os.path.islink(dest_filename):
                os.remove(dest_filename)

            os.symlink(source_filename, dest_filename)
