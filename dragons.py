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
		def init():
			#atacar = Ataques()
			#general = pega_generais()
			#cave = send_dragon_cave()
			#pedras_catch = pedras()
			#treino_tropas = treinar()
			i = 0
			while (i<10):
				aqui = Arena()
				arena_dragoes = Arena_ataque()
				arena_dragoes1 = Arena_ataque1()
				arena_dragoes2 = Arena_ataque2()
				print('tentativa: '+str(i))
				i+=1
			#evolution = evoluir()
			#abrir = itens()

		def Ataques():
			#coordenadas de oponentes para ataque
			x = [686, 260, 243, 167, 136, 99,  229, 117, 558, 549]
			y = [0, 556, 563, 579, 592, 595, 705, 707, 628, 617]

			x1 = [551, 558, 408, 448, 332, 546, 632, 234, 54,  713]
			y1 = [619, 609, 569, 640, 539, 618, 589, 447, 490, 540]

			x2 =[303, 689, 691, 692, 696, 697, 693, 710, 716, 708]
			y2 =[348, 727, 722, 717, 715, 711, 711, 694, 690, 692]

			x3 = [616, 527, 616, 480, 433, 487, 538, 546,552, 555]
			y3 = [733, 730, 561, 510, 574, 588, 638, 631,638, 638]

			x4 = [692, 687, 681, 681, 679, 673, 666, 659, 645, 640]
			y4 = [726, 720, 722, 721, 722, 725, 721, 725, 733, 737]

			x5 = [672, 677, 677, 678, 694, 697, 705, 712, 732, 687]
			y5 = [734, 728, 725, 724, 715, 712, 710, 705, 710, 745]

			x6 =[690, 689, 687, 688, 693, 680, 678, 675, 669, 649]
			y6 =[723, 722, 721, 718, 713, 705, 705, 705, 704, 732]

			#Faz um array 2D com as coordenadas
			coordenadas_x = [x, x1, x2, x3, x4, x5, x6]
			coordenadas_y = [y, y1, y2, y3, y4, y5, y6]

			#array com o id de cada general (é possuir alterar o general pelo id)
			generais_ids = [3584510, 7044779, 6587403, 7514149, 7514151, 7514029, 7389878, 7297918, 7527984, 7516212]

			i = 0
			#Ataca as coordenadas a cada 5 minutos
			for z in coordenadas_x:
				atacar = ataca_inimigos(z, coordenadas_y[i], generais_ids)
				i += 1
				time.sleep(300)

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



		def ataca_inimigos(coordenadas_x, coordenadas_y, generais_ids):
			time = timeStamp()
			data = login()
			print(json.dumps(data, indent = 4, sort_keys=True))
			print(data.get('client_cachebreaker'))
			session = data.get('_session_id')
			login_token = data.get('login_token')
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
			
		def pega_generais():
			data = login()
			time = timeStamp()
			session_id = data.get('_session_id')
			login_token = data.get('login_token')
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

		#Enviar dragoes para caverna e/ou pegar reconpensas
		def send_dragon_cave():
			data = login()
			time = timeStamp()
			session_id = data.get('_session_id')
			login_token = data.get('login_token')

			headers = {
				'X-Unity-Version': '4.7.1f1',
				'Content-Type': 'application/x-www-form-urlencoded',
				'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 7 MIUI/V11.0.5.0.PFGMIXM)',
				'Host': 'www.doamobile.com',
				'Connection': 'Keep-Alive',
				'Accept-Encoding': 'gzip',
				'Content-Length': 170
			}

			url2 = 'http://www.doamobile.com/api/dragon_train/claim?t='+time+'&r=2&rm_id=277'

			payload_dragon_get = {
				'dragon': 'GreatDragon',
				'cave_id': 1,
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11,
				'_method': 'PUT'
			} 

			payload_dragon_get1 = {
				'dragon': 'NightshadeDragon',
				'cave_id': 2,
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11,
				'_method': 'PUT'
			}

			payload_dragon_get2 = {
				'dragon': 'EarthDragon',
				'cave_id': 3,
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11,
				'_method': 'PUT'

			}

			payload_dragon_get4 = {
				'dragon': 'ToxicDragon',
				'cave_id': 4,
				'fte': 'false',
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11,
				'_method': 'PUT'

			}

			payload_dragon_get5 = {
				'dragon': 'FireDragon',
				'cave_id': 5,
				'play_mode': 0,
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11,
				'_method': 'PUT'
			}

			pega = requests.post(url2, payload_dragon_get, headers)
			result = json.loads(pega.text)
			print(json.dumps(result, indent = 4, sort_keys=True))
			s = hashlib.md5(result.get('token_md5').encode('utf-8')).hexdigest()

			url2 = 'http://www.doamobile.com/api/dragon_train/claim?t='+time+'&s='+result.get('token_md5')+'&r=2&rm_id=277'

			pega = requests.post(url2, payload_dragon_get, headers)
			pega0 = requests.post(url2, payload_dragon_get1, headers)
			pega1 = requests.post(url2, payload_dragon_get2, headers)
			pega3 = requests.post(url2, payload_dragon_get4, headers)
			pega4 = requests.post(url2, payload_dragon_get5, headers)
			

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
			pega2 = requests.post(url, payload1, headers)
			pega3 = requests.post(url, payload5, headers)
			pega4 = requests.post(url, payload3, headers)
			pega5 = requests.post(url, payload4, headers)
			print(pega.text)
			print(pega.text)



		def pedras():
			data = login()
			time_real = timeStamp()
			session = data.get('_session_id')
			login_token = data.get('login_token')
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
			#Pedras verde
			payload = {
				'event_id': 16404,
				'trade_in_id': 1547104325,
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11
			}
			#Pedras amarelas
			payloado_amarela = {
				'event_id': 16404,
				'trade_in_id': 1411641332,
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11
			}
			#Pedra azul
			payload_azul = {
				'event_id': 16404,
				'trade_in_id': 1411641348,
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11
			}

			#Pedra carne
			payload_carne = {
				'event_id': 16404,
				'trade_in_id': 1436527147,
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11
			}

			pega = requests.post(url, payload, headers)
			pega = requests.post(url, payloado_amarela, headers)
			pega = requests.post(url, payload_azul, headers)
			pega = requests.post(url, payload_carne, headers)
			result = json.loads(pega.text)
			print(json.dumps(result, indent = 4, sort_keys=True))
			s = hashlib.md5(result.get('token_md5').encode('utf-8')).hexdigest()

			url = 'http://doamobile.com/api/dummy_items/trade_in.json?t='+time_real+'&s='+result.get('token_md5')+'&r=0&rm_id=277'
			response = requests.post(url, payload, headers)
			print(response.text)
			pega = requests.post(url, payloado_amarela, headers)
			pega = requests.post(url, payload_azul, headers)
			pega = requests.post(url, payload_carne, headers)
			time.sleep(3)


		def treinar ():
			data = login()
			time = timeStamp()
			session_id = data.get('_session_id')
			login_token = data.get('login_token')
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
			print(pega.text)

			hoplitas_payload = {
				'units[unit_type]': 'ShieldHalberdier',
				'units[quantity]': 2315,
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.0.7',
				'platform': '11'
			}	
			pega = requests.post(url, hoplitas_payload, headers)

			bigas_payload = {
				'units[unit_type]': 'FireDragonTroop',
				'units[quantity]': 70000,
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.0.7',
				'platform': '11'
			}
			pega = requests.post(url, bigas_payload, headers)



		def evoluir():
			data = login()
			time = timeStamp()
			session_id = data.get('_session_id')
			login_token = data.get('login_token')
			url = 'http://doamobile.com/api/player_items/UpgradeUnitD/troop_upgrade.json?t='+time+'&r=1&rm_id=277'

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
				'quantity': 16,
				'unit_type': 'EarthDragonTroop',
				'upgrade_times': 1,
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': '11'
			}
			pega = requests.post(url, payload, headers)
			result = json.loads(pega.text)
			print(json.dumps(result, indent = 4, sort_keys=True))
			s = hashlib.md5(result.get('token_md5').encode('utf-8')).hexdigest()
			url = 'http://doamobile.com/api/player_items/UpgradeUnitD/troop_upgrade.json?t='+time+'&s='+result.get('token_md5')+'&r=1&rm_id=277'
			result = requests.post(url, payload, headers)
			print(result.text)
			exit()


		def itens():
			data = login()
			time = timeStamp()
			session_id = data.get('_session_id')
			login_token = data.get('login_token')

			url = 'http://doamobile.com/api/player_items/electricshock.json?t='+time+'&r=2&rm_id=277'

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
				'quantity': 1,
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': '11',
				'_method': 'delete'	
			}

			payload2 = {
				'quantity': 1,
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': '11',
				'_method': 'PATCH'	
			}

			pega = requests.post(url, payload, headers)
			result = json.loads(pega.text)
			print(json.dumps(result, indent = 4, sort_keys=True))
			s = hashlib.md5(result.get('token_md5').encode('utf-8')).hexdigest()
			url = 'http://doamobile.com/api/player_items/electricshock.json?t='+time+'&s='+result.get('token_md5')+'&r=2&rm_id=277'
			result = requests.post(url, payload2, headers)
			print(result)
			

		def Arena():
			data = login()
			time = timeStamp()
			session_id = data.get('_session_id')
			login_token = data.get('login_token')
			url = 'http://doamobile.com/api/dragon_arenas/382673/enter_arena.json?t='+time+'&r=28&rm_id=277'

			headers = {
				'X-Unity-Version': '4.7.1f1',
				'Content-Type': 'application/x-www-form-urlencoded',
				'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; Redmi Note 7 MIUI/V11.0.5.0.PFGMIXM)',
				'Host': 'www.doamobile.com',
				'Connection': 'Keep-Alive',
				'Accept-Encoding': 'gzip',
				'Content-Length': 146
			}

			payload ={
				'need_fte': 'True',
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': '11'
			}

			pega = requests.post(url, payload, headers)
			result = json.loads(pega.text)
			print(json.dumps(result, indent = 4, sort_keys=True))
			s = hashlib.md5(result.get('token_md5').encode('utf-8')).hexdigest()
			url = 'http://doamobile.com/api/dragon_arenas/382673/enter_arena.json?t='+time+'&s='+result.get('token_md5')+'&r=28&rm_id=277'
			result = requests.post(url, payload, headers)
			print ("entrei caraio")
			
		def Arena_ataque():
			data = login()
			time_real = timeStamp()
			session_id = data.get('_session_id')
			login_token = data.get('login_token')

			url = 'http://doamobile.com/api/dragon_arenas/battle.json?t='+time_real+'&r=27&rm_id=277'

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
				'enemy_id': 0,
				'arena_id': 382673,
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': '11'
			}

			

			pega = requests.post(url, payload, headers)
			result = json.loads(pega.text)
			print(json.dumps(result, indent = 4, sort_keys=True))
			s = hashlib.md5(result.get('token_md5').encode('utf-8')).hexdigest()
			url1 = 'http://doamobile.com/api/dragon_arenas/battle.json?t='+time_real+'&s='+result.get('token_md5')+'&r=27&rm_id=277'
			resultado = requests.post(url1, payload, headers)


		def Arena_ataque1():
			data = login()
			time_real = timeStamp()
			session_id = data.get('_session_id')
			login_token = data.get('login_token')

			url = 'http://doamobile.com/api/dragon_arenas/battle.json?t='+time_real+'&r=27&rm_id=277'

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
				'enemy_id': 2,
				'arena_id': 382673,
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': '11'
			}

			

			pega = requests.post(url, payload, headers)
			result = json.loads(pega.text)
			print(json.dumps(result, indent = 4, sort_keys=True))
			s = hashlib.md5(result.get('token_md5').encode('utf-8')).hexdigest()
			url1 = 'http://doamobile.com/api/dragon_arenas/battle.json?t='+time_real+'&s='+result.get('token_md5')+'&r=27&rm_id=277'
			resultado = requests.post(url1, payload, headers)

		def Arena_ataque2():
			data = login()
			time_real = timeStamp()
			session_id = data.get('_session_id')
			login_token = data.get('login_token')

			url = 'http://doamobile.com/api/dragon_arenas/battle.json?t='+time_real+'&r=27&rm_id=277'

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
				'enemy_id': 4,
				'arena_id': 382673,
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': '11'
			}

			

			pega = requests.post(url, payload, headers)
			result = json.loads(pega.text)
			print(json.dumps(result, indent = 4, sort_keys=True))
			s = hashlib.md5(result.get('token_md5').encode('utf-8')).hexdigest()
			url1 = 'http://doamobile.com/api/dragon_arenas/battle.json?t='+time_real+'&s='+result.get('token_md5')+'&r=27&rm_id=277'
			resultado = requests.post(url1, payload, headers)

		inicio = init()


	#Schedule para rodar o programa em looping de tempo
	#schedule.every(60).minutes.do(all)
	schedule.every(1).seconds.do(all)

	while True:
		schedule.run_pending() 
		time.sleep(1) 