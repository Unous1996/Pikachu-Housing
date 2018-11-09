import requests
import urllib.request
from bs4 import BeautifulSoup
import json
import re

def write_to_json(name,location,price,imgs_url,types,description,provider):
	json_dict = dict()
	json_dict["name"] = name
	json_dict["location"] = location
	json_dict["price"] = price
	json_dict["imgs_url"] = imgs_url
	json_dict["types"] = types
	json_dict["description"] = description
	json_dict["provider"] = provider
	return json.dumps(json_dict)


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
	img_list = list()
	apt_price_list = list()
	apt_addr_type = ''
	apt_loc = ''
	apt_price = ''
	apt_min_price = ''
	apt_detail_description: ''
	fileName = 'MHM_prop_json/' + str(i) + '.txt'
	r = requests.get(url,headers = headers)
	html_content = r.text
	soup = BeautifulSoup(html_content,"html.parser")
	#print(soup)
	propc = soup.find_all("div",{"class" : "propc"})
	price = soup.find_all("div",{"id" : "price"})
	photos = soup.find_all("div", {"id":"photos"})
	overview = soup.find_all("div",{"id": "overview"})

	for ov in overview:

		apt_description = ov.text
		#print(apt_description)

	#f = open(fileName,'w')
	for p in propc:
		for loc in p.find_all('h1'):
			apt_loc = remove_header_tag(loc,"<h1>","</h1>")
			#f.write(loc)
	for p in price:
		for pb in p.find_all("div",{"class":"pricebox"}):
			info_text = remove_header_tag(pb.text," View Typical Unit","")
			#append_to_file(fileName,info_text)
			#print(info_text)
		for pb in p.find_all('span'):
			apt_price = pb.text
			for i in range(0,len(apt_price)):
				if apt_price[i] =='$':
					#unsafe operation
					apt_price = apt_price[i+1:i+5]
					break
			#apt_price = apt_price[5:11]
			print(apt_price)
			apt_price = re.sub("\D","",apt_price)
			if apt_price.isdigit():
				apt_price = int(apt_price)
				apt_price_list.append(apt_price)
			#continue
		if len(apt_price_list) != 0:
			apt_min_price = min(apt_price_list)
		else:
			apt_min_price = -1
		#print(apt_min_price)
	for p in photos:
		for img in p.find_all('a'):
			img_url = img.get('href')
			img_list.append(img_url)

	#print(info_text)
	#imgLink_to_file(fileName,img_set)
	f = open( fileName,'w')
	f.write(write_to_json(apt_loc,apt_loc,apt_min_price,img_list,info_text,apt_description,"MHM Property"))
	f.close()

	


 





#findImageMHM("https://www.mhmproperties.com/property/606-e-white-street/",0)
#findImageUG("https://ugroupcu.com/property-details/312-w-springfield-urbana/",0)
