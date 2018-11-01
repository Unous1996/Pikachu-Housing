import requests
import urllib.request
from bs4 import BeautifulSoup

def append_to_file(path, data):
	with open(path,'a') as file:
		file.write(data + '\n')

def imgLink_to_file(file_name,img_link_set):
	f = open(file_name,'a')
	for link in sorted(img_link_set):
		append_to_file(file_name,link)
	f.close()

def remove_header_tag(header,h_tag_one, h_tag_two):
	header = str(header)
	header = header.replace(h_tag_one,"")
	header = header.replace(h_tag_two,"")
	header = header.strip()
	return header

#MHM property has anti crawling.
def findImageMHM(url,i):
	headers = {'User-Agent': 'Mozilla/5.0'}
	img_set = set()
	apt_addr_type = ''
	fileName = 'MHM_prop/' + str(i) + '.txt'
	r = requests.get(url,headers = headers)
	html_content = r.text
	soup = BeautifulSoup(html_content,"html.parser")
	#print(soup)
	propc = soup.find_all("div",{"class" : "propc"})
	price = soup.find_all("div",{"id" : "price"})
	photos = soup.find_all("div", {"id":"photos"})
	f = open(fileName,'w')
	for p in propc:
		for loc in p.find_all('h1'):
			loc = remove_header_tag(loc,"<h1>","</h1>")
			f.write(loc)
	for p in price:
		for pb in p.find_all("div",{"class":"pricebox"}):
			info_text = remove_header_tag(pb.text," View Typical Unit","")
			append_to_file(fileName,info_text)
	for p in photos:
		for img in p.find_all('a'):
			img_url = img.get('href')
			img_set.add(img_url)
	imgLink_to_file(fileName,img_set)









findImageMHM("https://www.mhmproperties.com/property/303-s-fifth-street/",0)
#findImageUG("https://ugroupcu.com/property-details/312-w-springfield-urbana/",0)
