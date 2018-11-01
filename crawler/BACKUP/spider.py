from urllib.request import urlopen
from linkfinder import LinkFinder
from crawtest import *
from domain import *
import ssl
from findImg import *
class Spider:

	#Class variables (shared among all instances)
	project_name = ''
	base_url = ''
	domain_name =''
	queue_file = ''
	crawled_file = ''
	queue = set()
	crawled = set()


	def __init__(self, project_name, base_url, domain_name):
		Spider.project_name = project_name
		Spider.base_url = base_url
		Spider.domain_name = domain_name
		Spider.queue_file = Spider.project_name + '/queue.txt'
		Spider.crawled_file = Spider.project_name+ '/crawled.txt'
		self.boot()
		self.crawl_page('第一条虫', Spider.base_url)

	@staticmethod
	def boot():
		create_directory(Spider.project_name)
		create_datafiles(Spider.project_name,Spider.base_url)
		Spider.queue = file_to_set(Spider.queue_file)
		Spider.crawled = file_to_set(Spider.crawled_file)

	@staticmethod
	def crawl_page(thread_name, page_url):
		if page_url not in Spider.crawled and Spider.base_url in page_url:
			print(thread_name + ' now crawling ' + page_url)
			print('Queue ' + str(len(Spider.queue))+ ' | Crawled ' + str(len(Spider.crawled)))
			Spider.add_links_to_queue(Spider.gather_links(page_url))
			Spider.queue.remove(page_url)
			Spider.crawled.add(page_url)
			#added
			if("unit_type_id" in page_url):
				findImage(page_url,Spider.base_url)
			Spider.update_files()

	@staticmethod
	def gather_links(page_url):
		html_string = ''
		try:
			ssl._create_default_https_context = ssl._create_unverified_context
			response = urlopen(page_url)
			if 'text/html' in response.getheader('Content-Type'):
				html_bytes = response.read()
				#print('html bytes:' + str(html_bytes))
				html_string = html_bytes.decode("UTF-8")
			finder = LinkFinder(Spider.base_url,page_url)
			#feed links
			finder.feed(html_string)

		except Exception as e:
			print(str(e))
			return set()
		return finder.page_links()

	#find links
	@staticmethod
	def add_links_to_queue(links):
		for url in links:
			if url in Spider.queue:
				continue
			if url in Spider.crawled:
				continue
			#make sure it only crawls the current domain
			if Spider.domain_name not in url:
				continue
			Spider.queue.add(url)

	@staticmethod
	def update_files():
		set_to_file(Spider.queue,Spider.queue_file)
		set_to_file(Spider.crawled,Spider.crawled_file)






		