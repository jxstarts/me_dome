# coding=gbk

import pytesseract as pt

from PIL import Image

# ����ͼƬʵ��

image = Image.open("url")

# ����pytesseract����ͼƬת��������
# ���ؽ������ת����Ľ��
text = pt.image_to_string(image)
print(text)