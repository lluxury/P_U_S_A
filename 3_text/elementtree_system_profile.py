#!/usr/bin/env python
import sys

from xml.etree import ElementTree as ET
e = ET.parse('system_profiler.xml')

if __name__ == '__main__':
    for d in e.findall('/array/dict'):
        if d.find('string').text == 'SPSoftwareDataType':
            sp_data = d.find('array').find('dict')
            break
    else:
        print ("SPSoftwareDataType NOT FOUND")
        sys.exit(1)

    record = []
    for child in sp_data.getchildren():
        record.append(child.text)
        if child.tag == 'string':
            print ("%-15s -> %s" % tuple(record))
            record = []


#搜索dict标签, 有一个字符串子元素, 文本值为SPSoftwareDataType
#getchildren() 返回指定元素的子列表, 如果是string就打印

'''
    <dict>
        <key>_dataType</key>
        <string>SPSoftwareDataType</string>
        <key>_detailLevel</key>
        <integer>-2</integer>
        <key>_items</key>
        <array>
            <dict>
                <key>_name</key>
                <string>os_overview</string>
                <key>kernel_version</key>
                <string>Darwin 8.11.1</string>
                <key>os_version</key>
                <string>Mac OS X 10.4.11 (8S2167)</string>
            </dict>
'''