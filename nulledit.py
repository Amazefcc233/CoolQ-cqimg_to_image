# -*- coding: UTF-8 -*-

import os

def main():
    concls = os.system('cls')
    print("null转jpg Start!")
    proDir = os.path.split(os.path.realpath(__file__))[0]
    todoPath = os.path.join(proDir, "./todo/")
    okPath = os.path.join(proDir, "./ok/")

    num = 1
    for file in os.listdir(okPath):
        filesex=file[-4:]
        if filesex == "null":
            try:
                os.rename(os.path.join(okPath, file), os.path.join(okPath, "null_"+str(num)+".jpg"))
	        print ("null_"+str(num)+".jpg")
            except FileExistsError as exists: # 如果文件存在，也不会报错，将继续执行
                print ("文件名为null_"+str(num)+".jpg已存在，因此无法对文件"+file+"进行重命名操作。请修改原有名称，然后再试一次。")
                continue
            num += 1
	print("完成了哟！")
	
