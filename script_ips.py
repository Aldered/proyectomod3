#!/usr/bin/python3
# -*- coding: utf-8 -*-
#UNAM-CERT

import urllib
import requests
from urllib.request import urlopen

top = ['https://www.unam.mx/',
'http://www.gaceta.unam.mx/',
'http://www.posgrado.unam.mx/',
'http://oferta.unam.mx/',
'http://dgenp.unam.mx/',
'http://www.unamglobal.unam.mx/',
'http://www.dgcs.unam.mx/',
'http://www.revista.unam.mx/',
'http://www.unamenlinea.unam.mx/']


def activas_top():
	for i in top:
		request = requests.get(i)
		if request.status_code == 200:
			for index, line in enumerate(top):
				with open('archivo{}'.format(index), 'w') as archivo:
					for di in top:
					#with open('archivo{}.txt'.format(index), 'w') as output:
						rsp = requests.get(di, stream=True)
						ip_port = rsp.raw._fp.fp.raw._sock.getpeername()
						print (ip_port)
						with urlopen(i) as response:
  							html_response = response.read()
  							encoding = response.headers.get_content_charset('utf-8')
  							html = html_response.decode(encoding)
						#html = urllib.request.urlopen(di)
						archivo.write(di)
						#archivo.close()
#		print (urllib.request.urlopen(i).getcode())

activas_top()

