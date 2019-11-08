# -*- coding: utf-8 -*-
import os
import configparser
import urllib.request

def main():
	concls = os.system('cls')
	print ("cqimg转正常格式文件 Start!")
	class ReadConfig:
		def __init__(self):
			self.cf = configparser.ConfigParser()
			self.cf.read(configPath)

		def get_http(self):
			value = self.cf.get('image', 'url')
			return value
	
	proDir = os.path.split(os.path.realpath(__file__))[0]
	todoPath = os.path.join(proDir, "./todo/")
	okPath = os.path.join(proDir, "./ok/")

	num = 1
	for file in os.listdir(todoPath):
		filesex=file[-10:]
		try:
			os.rename(os.path.join(todoPath, file), os.path.join(todoPath, str(num)+filesex))
		except FileExistsError as exists: # 如果文件存在，也不会报错，将继续执行
			continue
		num += 1
	
	num = 0
	for file2 in os.listdir(todoPath):
		configPath = todoPath+os.listdir(todoPath)[num]
		test = ReadConfig()
		img_src = test.get_http()
		filenocq = file2.replace('.cqimg','')
		try:
			urllib.request.urlretrieve(img_src, './ok/'+filenocq)
			print(filenocq)
		except urllib.error.URLError as err_http: # 如果链接为访问为非200的正常状态码，也不会中断操作，将继续进行
			pass
		num += 1
	print ("完成了哟！")