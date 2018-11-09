import requests
import urllib.request
from bs4 import BeautifulSoup
import json

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

def findImageUG(url,i):
	apt_addr_type = ''
	loc = ''
	r = requests.get(url)
	html_content = r.text
	soup = BeautifulSoup(html_content,"html.parser")
	banner_cap = soup.find_all("div",{"class" : "banner_caption"})
	tab = soup.find_all("div",{"class" : "tab-content_in_wrapp tab-cntnt_wrap_btm"})
	#propert_head = soup.find_all("h4",{"class": "propert_head"})
	for header in banner_cap:
		for addr in header.find_all('h3'):
			addr = remove_header_tag(addr,"<h3>","</h3>")
			loc = addr
			apt_addr_type = addr
	for t in tab:
		apt_description = ''
		apt_price = ''
		apt_info_list = list()
		img_list = list()
		apt_des = ""
		fileName = ""
		for rm_type in t.find_all('h4'):
			rm_type = remove_header_tag(rm_type,"""<h4 class="propert_head">""","</h4>")

			apt_addr_type = apt_addr_type+ "@" + rm_type
		fileName = 'ug_house_json/' + i + '.txt'
		f = open(fileName,'w')
		f.write(apt_addr_type + '\n')
		f.close()
		for info in t.find_all("div",{"class" : "col-lg-5"}):
			info = remove_header_tag(info,"""<div class="col-lg-5">""","</div>")
			#append_to_file(fileName,info)
			apt_info_list.append(info)
			#Price per month:
			#$895.00
			#Price per occupant:
			#$223.75
			#Units Available:
			#Available Now, Available Soon

		for description in t.find_all("div",{"class" : "col-lg-10"}):
			apt_description = description.text.strip()

		for img in t.find_all('img'):
			img_url = img.get('src')
			img_list.append(img_url)

		apt_price = apt_info_list[1]
		f = open(fileName,'w')
		f.write(write_to_json(apt_addr_type,loc,apt_price,img_list,rm_type,apt_description,"University Group"))
		f.close()

				#imgLink_to_file(fileName,img_set)
		




#findImageUG("https://ugroupcu.com/property-details/312-w-springfield-urbana/","0")
