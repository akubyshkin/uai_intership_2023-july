# В этом файле сейчас нет необходимости, т.к. он был сделан до того, как я подключил Jupyter Notebook
from bs4 import BeautifulSoup
import NDataParser as parser
import Loader as loader


ndata_xml = loader.read_from_disk('/home/akubyshkin/akubyshkin/projects/uai/intership/netoptik/1/resources/downloaded/yandexmarket.yml')
ndatas = parser.NDataParser(BeautifulSoup(ndata_xml, "xml")).parse()

for offer in ndatas.offers:
    loader.offer_images_downloader('/home/akubyshkin/akubyshkin/projects/uai/intership/netoptik/1/resources/downloaded/images', offer)

print('Done')
