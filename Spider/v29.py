# coding=gbk

'''
��װlxml
'''

from lxml import etree

'''
��xml������HTML����
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