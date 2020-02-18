import time
from multiprocessing import Process

import requests
from bs4 import BeautifulSoup


def getUrl(url):
	'''
	获取图片的地址
	:return:
	'''
	imagesList = []
	res = requests.get(url)
	if res.status_code == 200:  # 正常访问时
		soup = BeautifulSoup(res.text, "html.parser")
		re = soup.find("div", class_="tab_box").find_all('li')
		for i in re:
			s = i.find("img").get("data-original")
			imagesList.append(s)
	return imagesList


def getImage(url):
	'''
	下载图片
	:param url:
	:return:
	'''
	imageName = url.split("/")[-1].split("_")[0] + ".jpg"
	r = requests.get(url)
	if r.status_code == 200:
		with open("images/" + str(imageName), "wb") as f:
			f.write(r.content)


if __name__ == '__main__':
	headers = {"user-agent": "爬虫实现"}
	url = "http://www.win4000.com/meitu.html"
	imgUrl = getUrl(url)
	# 单线程下载图片
	startTime = time.time()
	for u in imgUrl:
		getImage(u)
	endTime = time.time()
	print("单线程耗时：%s 秒" % (endTime - startTime))
	# 多线程下载图片
	pList = []
	startTime = time.time()
	for u in imgUrl:
		p = Process(target=getImage(u, ))
		pList.append(p)
	for p in pList:
		p.start()
		p.join()
	endTime = time.time()
	print("多线程耗时：%s 秒" % (endTime - startTime))
