#coding:utf-8
'''
将一张图片填充为正方形后切成9张图
'''
from PIL import Image
import sys

#_1_#将图片填充为正方形
def fill_image(image):
    width,height = image.size
    #选取长和宽中的较大值作为新图片的长和宽
    new_image_legth = width if width > height else height
    #生成新图片【白底】
    new_image = Image.new(image.mode,(new_image_legth,new_image_legth),color='white')
    #将之前的图片粘贴到新图片上，居中
    if width > height:#原图宽大于高，则填充图片竖直维度
        #（x，y）二元组表示粘贴上图相对下图的起始位置
        new_image.paste(image, (0, int((new_image_legth - height) / 2)))
    else:
        new_image.paste(image ,(int((new_image_legth - width) / 2), 0))

    return new_image
#_2_切图
def cut_image(image):
    width,height = image.size
    item_width = int(width / 3)
    box_list = []
    #(left,upper,right,lower)
    for i in range(0,3):#两重循环，生成9张图片基于原图的位置
        for j in range(0,3):
            box = (j*item_width,i*item_width,(j+1)*item_width,(i+1)*item_width)
            box_list.append(box)
    image_list = [image.crop(box) for box in box_list]
    return image_list

#_3_保存
def save_images(image_list):
    index = 1
    for image in image_list:
        image.save('./image/python'+str(index) + '.png', 'PNG')
        index += 1


if __name__ == '__main__':
    file_path = "1.jpg"
    image = Image.open(file_path)
    #image.show()#打开图片
    image = fill_image(image)
    image_list = cut_image(image)
    save_images(image_list)


