# coding=gbk

'''
安装lxml
'''

from lxml import etree

'''
用xml来解析HTML代码
'''
text = '''

<div>
    <ul>
        <li class="item-0"> hahahahahaha</li>
        <li class="item-1"> hahahahahaha</li>
        <li class="item-2"> hahahahahaha</li>
        <li class="item-3"> hahahahahaha</li>
        <li class="item-4"> hahahahahaha</li>
        <li class="item-5"> hahahahahaha</li>
    
    </ul>

</div>

'''

html = etree.HTML(text)
s = etree.tostring(html)

print(s)