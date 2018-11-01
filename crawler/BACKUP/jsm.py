
import requests
import urllib.request
from bs4 import BeautifulSoup

def append_to_file(path, data):
	with open(path,'a') as file:
		file.write(data + '\n')

def write_file(file_name,data):
	f = open(file_name,'w')
	f.write(data)
	#print("HIT")
	f.close()
def imgLink_to_file(file_name,img_link_set):
	f = open(file_name,'a')
	for link in sorted(img_link_set):
		append_to_file(file_name,link)
	f.close()

def remove_header_tag(header,h_tag_one, h_tag_two):
	header = str(header)
	header = header.replace(h_tag_one,"")
	header = header.replace(h_tag_two,"")
	return header

def findImage(url, domain, i):
	img_link_set = set()
	apt_info =''
	apt_address = ''
	apt_stat = ''
	r = requests.get(url)
	html_content = r.text
	soup = BeautifulSoup(html_content,"html.parser")
	info = soup.find_all("div",{"class": "info"})
	stats = soup.find_all("div",{"class":"stats"})

	for stat in stats:
		for s in stat.find_all("div",{"class":"stat"}):
			apt_stat = apt_stat+"@"+ remove_header_tag(s,"""<div class="stat">""","</div>")

			#print(s)
			#<div class="stat">Size: 3 Bedrooms/2 Baths </div>
			#<div class="stat">$1,730</div>
			#<div class="stat">Fall 2019/20</div>
	for loc in info:
		for addr1 in loc.find_all('h1'):
			apt_info = remove_header_tag(addr1,"<h1>","</h1>")
		for addr2 in loc.find_all('h2'):
			apt_address = remove_header_tag(addr2,"<h2>","</h2>")
	for img in soup.find_all('img'):
		img_url = img.get('src')
		if "/uploads/application" in img_url:
			img_url = domain + img_url
			img_link_set.add(img_url)
	file_name = "jsm_for_loop/"+str(i)+'.txt'
	apt_description = apt_info + "@"+ apt_address+""+apt_stat
	if "Parking" in apt_description:
		return;
	if apt_address == "" or apt_info == "" or apt_stat == "" :
		return;
	#"Please select your suite" does not have pictures
	write_file(file_name,apt_description+"\n")
	print(apt_info)
	imgLink_to_file(file_name,img_link_set)




for i in range(0,3000):

	url = "https://apartments.jsmliving.com/apartments/?area=0&unit_type_id=%s" %i
	print(str(i) + ":")
	findImage(url,"https://apartments.jsmliving.com",i)
	
