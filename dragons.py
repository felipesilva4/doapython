from bs4 import BeautifulSoup
from datetime import datetime
import urllib3
import requests
import json
import time
import re
import hashlib
import schedule


class dragons:
	def all():
		def login():
			dragon = 'http://www.doamobile.com/api/login?t=1581880588&s=d7f6ab7cd9edf8da2ff729cc0ddc4189&r=0'
			payload = {
				'nm': 'a50a32ebd38459fe82e8868502a537c9&naid=267287507',
				'naid': '267287507',
				'access_token': 'e3bhmnsy-rfyw-ssze-r9m3fvlsyntt',
				'mobile_id': '76a968692c2368dcb63a5d0f01daca84'
			}
			x = requests.get(dragon, payload)
			data = json.loads(x.text)
			return data

		data = login()
		print(json.dumps(data, indent = 4, sort_keys=True))
		print(data.get('client_cachebreaker'))
		gangster = data.get('gangster')

		def timeStamp():
			data_e_hora_atuais = datetime.now()
			data_hora = data_e_hora_atuais.strftime('%Y-%m-%d %H:%M:%S')
			print (data_hora)
			print('time= '+str(time))
			datime_format = '%Y-%m-%d %H:%M:%S'
			dt_object = datetime.fromtimestamp(1582252119)
			print('hora normal = '+ str(dt_object))
			data_hora_data = datetime.strptime(data_hora, datime_format)
			time_stamp = datetime.timestamp(data_hora_data,)
			print(time_stamp)
			result = re.sub(r"\..*", '', str(time_stamp))
			return result

		time_real = timeStamp()
		print (time_real)

		session_id = data.get('_session_id')
		login_token = data.get('login_token')
		print("session_id = ", str(session_id))

		coordenadas_x = [0,260, 243, 167, 136, 99, 229, 117, 558, 549]
		coordenadas_y = [0,556, 563, 579, 592, 595, 705, 707, 628, 617]

		coordenadas_x_1 = [551, 558, 408, 448, 332, 546, 632, 234, 54, 713]
		coordenadas_y_1 = [619, 609, 569, 640, 539, 618, 589, 447, 490, 540]
		generais_ids = [6247275,7092528,6587403,7034076,7374566,7374547,6559833,4898179,6517744,7389878]


		def ataca_inimigos(coordenadas_x, coordenadas_y, generais_ids, time, gang, session, login_token):
			url = 'http://doamobile.com/api/cities/459/marches.json?t='+time+'&r=0&rm_id=277'
			print(url)
			i=0
			j=0
			while(i<=9):
				payload = {
					'march[units]': '{"ShadowStalker":50000}',
					'march[general_id]': generais_ids[i],
					'march[breakProtection]': 'false',
					'march[type]': 'AttackMarch',
					'march[x]': coordenadas_x[i],
					'march[y]': coordenadas_y[i],
					'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
					'_session_id': session,
					'login_token': login_token,
					'v': '9.7.0',
					'platform': 11
				}


				headers = {
				'X-Unity-Version': '4.7.1f1',
				'Content-Type': 'application/x-www-form-urlencoded',
				'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 7 MIUI/V11.0.5.0.PFGMIXM)',
				'Host': 'www.doamobile.com',
				'Connection': 'Keep-Alive',
				'Accept-Encoding': 'gzip',
				'Content-Length': '238',
				}


				ataque = requests.post(url, payload, headers)
				print (ataque.text)
				i += 1
				if(j == 0):
					result = json.loads(ataque.text)
					print(json.dumps(result, indent = 4, sort_keys=True))
					s = hashlib.md5(result.get('token_md5').encode('utf-8')).hexdigest()
					url = 'http://doamobile.com/api/cities/459/marches.json?t='+time+'&s='+result.get('token_md5')+'&r=0&rm_id=277'
					print(url)
					i=0
					j=1
			

		ataque = ataca_inimigos(coordenadas_x, coordenadas_y, generais_ids, time_real, gangster, session_id, login_token )

		print('primeiro sleep')
		time.sleep(320)

		data = login()
		print(json.dumps(data, indent = 4, sort_keys=True))
		print(data.get('client_cachebreaker'))
		gangster = data.get('gangster')
		time_real = timeStamp()
		session_id = data.get('_session_id')
		login_token = data.get('login_token')

		ataque = ataca_inimigos(coordenadas_x_1, coordenadas_y_1, generais_ids, time_real, gangster, session_id, login_token)
		print('segundo sleep')
		time.sleep(250)

		data = login()
		print(json.dumps(data, indent = 4, sort_keys=True))
		print(data.get('client_cachebreaker'))
		gangster = data.get('gangster')

		time_real = timeStamp()
		session_id = data.get('_session_id')
		login_token = data.get('login_token')
		coordenadas_x_2 =[303,689, 691,692,696,697,693,710,716, 708]
		coordenadas_y_2 =[348,727, 722,717,715, 711, 711,694, 690, 692]

		coordenadas_x_4 = [692, 687,681,681,679, 673,666,659,645, 640]
		coordenadas_y_4 = [726, 720,722,721,722, 725,721,725,733, 737]


		ataque = ataca_inimigos(coordenadas_x_2, coordenadas_y_2, generais_ids, time_real, gangster, session_id, login_token )
		print('terceiro sleep, indo pegar carne')
		time.sleep(260)

		data = login()
		print(json.dumps(data, indent = 4, sort_keys=True))
		print(data.get('client_cachebreaker'))
		gangster = data.get('gangster')

		time_real = timeStamp()
		session_id = data.get('_session_id')
		login_token = data.get('login_token')
		ataque = ataca_inimigos(coordenadas_x_4, coordenadas_y_4, generais_ids, time_real, gangster, session_id, login_token )
		time.sleep(300)

		data = login()
		print(json.dumps(data, indent = 4, sort_keys=True))
		print(data.get('client_cachebreaker'))
		gangster = data.get('gangster')

		time_real = timeStamp()
		session_id = data.get('_session_id')
		login_token = data.get('login_token')

		coordenadas_x_5 = [616, 527,616, 480, 433, 487, 538, 546,552, 555]
		coordenadas_y_5 = [733, 730,561, 510, 574, 588, 638, 631,638, 638]
		ataque = ataca_inimigos(coordenadas_x_5, coordenadas_y_5, generais_ids, time_real, gangster, session_id, login_token )

		def pega_generais(time, session_id, login_token):
			url = 'http://doamobile.com/api/cities/459/generals/gacha?t='+time+'&r=4&rm_id=277'
			payload = {
				'gacha_id': '1',
				'source': '1',
				'draw_times': '10',
				'general_fte_complete': 'true',
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': '11'
			}

			headers = {
				'X-Unity-Version': '4.7.1f1',
				'Content-Type': 'application/x-www-form-urlencoded',
				'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 7 MIUI/V11.0.5.0.PFGMIXM)',
				'Host': 'www.doamobile.com',
				'Connection': 'Keep-Alive',
				'Accept-Encoding': 'gzip',
				'Content-Length': 170
			}

			pega = requests.post(url, payload, headers)
			result = json.loads(pega.text)
			print(json.dumps(result, indent = 4, sort_keys=True))
			s = hashlib.md5(result.get('token_md5').encode('utf-8')).hexdigest()
			url2 = 'http://doamobile.com/api/cities/459/generals/gacha?t='+time+'&s='+result.get('token_md5')+'&r=4&rm_id=277'
			print(url2)
			pega2 = requests.post(url2, payload, headers)
			print(pega2.text)

		data = login()
		time_real = timeStamp()
		session_id = data.get('_session_id')
		login_token = data.get('login_token')
		generais_pega = pega_generais(time_real, session_id, login_token)

		def cria_hash(srting):
			s = hashlib.md5(string.encode('utf-8')).hexdigest()
			return s

		def send_dragon_cave(time, session_id, login_token):
			url = 'http://doamobile.com/api/dragon_train/play?t='+time+'&r=5&rm_id=277'

			headers = {
				'X-Unity-Version': '4.7.1f1',
				'Content-Type': 'application/x-www-form-urlencoded',
				'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 7 MIUI/V11.0.5.0.PFGMIXM)',
				'Host': 'www.doamobile.com',
				'Connection': 'Keep-Alive',
				'Accept-Encoding': 'gzip',
				'Content-Length': 146
			}

			payload = {
				'dragon': 'GreatDragon',
				'cave_id': 1,
				'play_mode': 0,
				'fte': 'false',
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11
			}

			payload1 = {
				'dragon': 'NightshadeDragon',
				'cave_id': 2,
				'play_mode': 0,
				'fte': 'false',
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11
			}

			payload2 = {
				'dragon': 'EarthDragon',
				'cave_id': 3,
				'play_mode': 0,
				#'fte': 'false',
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11
			}

			payload3 = {
				'dragon': 'EarthDragon',
				'cave_id': 3,
				'play_mode': 0,
				'fte': 'false',
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11
			}

			payload4 = {
				'dragon': 'ToxicDragon',
				'cave_id': 4,
				'play_mode': 0,
				'fte': 'false',
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11
			}

			payload5 = {
				'dragon': 'FireDragon',
				'cave_id': 5,
				'play_mode': 0,
				'fte': 'false',
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11
			}

			print('abaixo!!!')
			pega = requests.post(url, payload, headers)
			result = json.loads(pega.text)
			print(json.dumps(result, indent = 4, sort_keys=True))
			s = hashlib.md5(result.get('token_md5').encode('utf-8')).hexdigest()

			#manda o drgão para a caverna se possivel
			url = 'http://doamobile.com/api/dragon_train/play?t='+time+'&s='+result.get('token_md5')+'&r=5&rm_id=277'
			print(url)
			print(session_id)
			print(login_token)
			pega = requests.post(url, payload, headers)
			pega2 = requests.post(url, payload2, headers)
			pega3 = requests.post(url, payload3, headers)
			pega4 = requests.post(url, payload4, headers)
			pega5 = requests.post(url, payload5, headers)
			print(pega.text)

			url2 = 'http://www.doamobile.com/api/dragon_train/claim?t='+time+'&s='+result.get('token_md5')+'&r=2&rm_id=277'

			payload_dragon_get = {
				'dragon': 'GreatDragon',
				'cave_id': 1,
				'play_mode': 0,
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11
			} 

			payload_dragon_get1 = {
				'dragon': 'NightshadeDragon',
				'cave_id': '2',
				'play_mode': '0',
				'fte': 'false',
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': '11'
			}

			payload_dragon_get2 = {
				'dragon': 'EarthDragon',
				'cave_id': 3,
				'play_mode': 0,
				'fte': 'false',
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11
			}

			payload_dragon_get3 = {
				'dragon': 'EarthDragon',
				'cave_id': 3,
				'play_mode': 0,
				'fte': 'false',
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11
			}

			payload_dragon_get4 = {
				'dragon': 'ToxicDragon',
				'cave_id': 4,
				'play_mode': 0,
				'fte': 'false',
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11
			}

			payload_dragon_get5 = {
				'dragon': 'FireDragon',
				'cave_id': 5,
				'play_mode': 0,
				'fte': 'false',
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11
			}

			pega = requests.post(url, payload_dragon_get, headers)
			pega1 = requests.post(url, payload_dragon_get2, headers)
			pega2 = requests.post(url, payload_dragon_get3, headers)
			pega3 = requests.post(url, payload_dragon_get4, headers)
			pega4 = requests.post(url, payload_dragon_get5, headers)
			print(pega.text)

		data = login()
		time_real = timeStamp()
		session_id = data.get('_session_id')
		login_token = data.get('login_token')

		dragons = send_dragon_cave(time_real, session_id, login_token)

		def pedras(time_real, session, login_token):
			url =  'http://doamobile.com/api/dummy_items/trade_in.json?t='+time_real+'&r=0&rm_id=277'

			headers = {
				'X-Unity-Version': '4.7.1f1',
				'Content-Type': 'application/x-www-form-urlencoded',
				'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 7 MIUI/V11.0.5.0.PFGMIXM)',
				'Host': 'www.doamobile.com',
				'Connection': 'Keep-Alive',
				'Accept-Encoding': 'gzip',
				'Content-Length': 146
			}

			payload = {
				'event_id': 16404,
				'trade_in_id': 1547104325,
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11
			}

			pega = requests.post(url, payload, headers)
			result = json.loads(pega.text)
			print(json.dumps(result, indent = 4, sort_keys=True))
			s = hashlib.md5(result.get('token_md5').encode('utf-8')).hexdigest()

			url = 'http://doamobile.com/api/dummy_items/trade_in.json?t='+time_real+'&s='+result.get('token_md5')+'&r=0&rm_id=277'
			response = requests.post(url, payload, headers)
			print(response.text)
			time.sleep(3)

		data = login()
		time_real = timeStamp()
		session_id = data.get('_session_id')
		login_token = data.get('login_token')
		pedras = pedras(time_real, session_id, login_token)

		def treinar (time, session_id, login_token):
			url = 'http://doamobile.com/api/cities/459/units.json?t='+time+'&r=1&rm_id=277'	

			headers = {
				'X-Unity-Version': '4.7.1f1',
				'Content-Type': 'application/x-www-form-urlencoded',
				'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 7 MIUI/V11.0.5.0.PFGMIXM)',
				'Host': 'www.doamobile.com',
				'Connection': 'Keep-Alive',
				'Accept-Encoding': 'gzip',
				'Content-Length': 146
			}

			payload_ogros = {
				'units[unit_type]': 'EarthDragonTroop',
				'units[quantity]': 700,
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.0.7',
				'platform': '11'
			}

			pega = requests.post(url, payload_ogros, headers)
			result = json.loads(pega.text)
			print(json.dumps(result, indent = 4, sort_keys=True))
			s = hashlib.md5(result.get('token_md5').encode('utf-8')).hexdigest()
			url = 'http://doamobile.com/api/cities/459/units.json?t='+time+'&s='+result.get('token_md5')+'&r=1&rm_id=277'
			pega = requests.post(url, payload_ogros, headers)

			
			hoplitas_payload = {
				'units[unit_type]': 'ShieldHalberdier',
				'units[quantity]': 1500,
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.0.7',
				'platform': '11'
			}	
			pega = requests.post(url, hoplitas_payload, headers)

			bigas_payload = {
				'units[unit_type]': 'FireDragonTroop',
				'units[quantity]': 700,
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.0.7',
				'platform': '11'
			}
			pega = requests.post(url, bigas_payload, headers)

		data = login()
		time_real = timeStamp()
		session_id = data.get('_session_id')
		login_token = data.get('login_token')
		treino = treinar(time_real, session_id, login_token)

	schedule.every(10).minutes.do(all)

	while True:
		schedule.run_pending() 
		time.sleep(1) 