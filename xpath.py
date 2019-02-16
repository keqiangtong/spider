from lxml import etree

text = ''' <div> <ul> 
        <li class="item-1"><a >first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html"></a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a>  
        </ul> </div> '''

html = etree.HTML(text)

print(etree.tostring(html).decode())

print('*'*10)

rst_href_li = html.xpath('//li/a/@href')
rst_text_li = html.xpath('//li/a/text()')


print(rst_href_li)
print(rst_text_li)
dict1 =dict()
for href in rst_href_li:


    dict1[href] = rst_text_li[rst_href_li.index(href)]



print(dict1)

print('*'*100)

rst_li_a_list= html.xpath('//li/a')

for li_a in rst_li_a_list:
    print(li_a)
    dict2 =dict()
    dict2[li_a.xpath('./@href')[0] if len(li_a.xpath('@href'))>0 else None] = \
        li_a.xpath('text()')[0] if len(li_a.xpath('text()')) > 0 else None

    print(dict2)






