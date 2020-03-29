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
			pedras_catch = pedras()
			atacar = Ataques()
			general = pega_generais()
			cave = send_dragon_cave()
			pedras_catch = pedras()
			treino_tropas = treinar()
			exit()

		def Ataques():
			#coordenadas de oponentes para ataque
			#antropos
			x = [64,   61,  66,  68,  71,  74,  75,  79,  81,  83]
			y = [743, 744, 738, 738, 735, 733, 734, 726, 723, 722]
			#antropos 10
			x1 = [58,   71,  72,  54,  73, 55,  53,  53,  67,  52]
			y1 = [740, 739, 738, 749, 735,  3, 744, 740, 732, 737]

			x2 = [61, 62, 74,  55,  76, 56,  62,  57,  61,  69]
			y2 = [ 1,  2,  2, 731, 735,  6, 746, 741, 736, 735]

			x3 = [ 62,  51,  66,  63,  71,  68, 67,  76,  76,  47]
			y3 = [740, 747, 748, 749, 741, 733,  4, 734, 745, 749]
			#Faz um array 2D com as coordenadas
			coordenadas_x = [x, x1, x2, x3]
			coordenadas_y = [ y, y1, y2, y3]

			#array com o id de cada general (é possuir alterar o general pelo id)
			generais_ids = [6533213, 6502130, 6502129, 6502117, 6518995, 6518448, 6684268, 7175572, 7175563, 7152642]

			i = 0
			#Ataca as coordenadas a cada 5 minutos
			for z in coordenadas_x:
				atacar = ataca_inimigos(z, coordenadas_y[i], generais_ids)
				print('Esse ataque é de numero: '+ str(i))
				if(i==5):
					print('passando direto')
				else:
					time.sleep(300)
				i += 1

		def login():
			dragon = 'http://www.doamobile.com/api/login?t=1581880588&s=d7f6ab7cd9edf8da2ff729cc0ddc4189&r=0'
			payload = {
				'nm': 'a69f92e38b8a536be5f990f076835d0d',
				'naid': '401254789',
				'access_token': '4cuubrwp-meak-xmse-nazcrmfslnh0',
				'mobile_id': '76a968692c2368dcb63a5d0f01daca84'
			}
			x = requests.get(dragon, payload)
			data = json.loads(x.text)
			return data

		def timeStamp():
			data_e_hora_atuais = datetime.now()
			data_hora = data_e_hora_atuais.strftime('%Y-%m-%d %H:%M:%S')
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
			url = 'http://doamobile.com/api/cities/14154/marches.json?t='+time+'&r=0&rm_id=277'
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
					'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
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
				i += 1
				if(j == 0):
					result = json.loads(ataque.text)
					print(json.dumps(result, indent = 4, sort_keys=True))
					s = hashlib.md5(result.get('token_md5').encode('utf-8')).hexdigest()
					url = 'http://doamobile.com/api/cities/14154/marches.json?t='+time+'&s='+result.get('token_md5')+'&r=0&rm_id=277'
					print(url)
					i=0
					j=1
			
		def pega_generais():
			data = login()
			time = timeStamp()
			session_id = data.get('_session_id')
			login_token = data.get('login_token')
			url = 'http://doamobile.com/api/cities/14154/generals/gacha?t='+time+'&r=4&rm_id=277'
			payload = {
				'gacha_id': '1',
				'source': '1',
				'draw_times': '10',
				'general_fte_complete': 'true',
				'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
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
			url2 = 'http://doamobile.com/api/cities/14154/generals/gacha?t='+time+'&s='+result.get('token_md5')+'&r=4&rm_id=277'
			print(url2)
			pega2 = requests.post(url2, payload, headers)

		#Enviar dragoes para caverna e/ou pegar reconpensas
		def send_dragon_cave():
			data = login()
			time_real = timeStamp()
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

			url2 = 'http://www.doamobile.com/api/dragon_train/claim?t='+time_real+'&r=2&rm_id=277'

			payload_dragon_get = {
				'dragon': 'FrostDragon',
				'cave_id': 1,
				'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11,
				'_method': 'PUT'
			} 

			payload_dragon_get1 = {
				'dragon': 'EarthDragon',
				'cave_id': 2,
				'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11,
				'_method': 'PUT'
			}

			payload_dragon_get2 = {
				'dragon': 'ToxicDragon',
				'cave_id': 3,
				'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11,
				'_method': 'PUT'

			}

			payload_dragon_get4 = {
				'dragon': 'FireDragon',
				'cave_id': 4,
				'fte': 'false',
				'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
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

			url2 = 'http://www.doamobile.com/api/dragon_train/claim?t='+time_real+'&s='+result.get('token_md5')+'&r=2&rm_id=277'

			pega = requests.post(url2, payload_dragon_get, headers)
			time.sleep(3)
			pega0 = requests.post(url2, payload_dragon_get1, headers)
			time.sleep(4)
			pega1 = requests.post(url2, payload_dragon_get2, headers)
			time.sleep(3)
			pega3 = requests.post(url2, payload_dragon_get4, headers)
			

			url = 'http://doamobile.com/api/dragon_train/play?t='+time_real+'&r=5&rm_id=277'

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
				'dragon': 'IceDragon',
				'cave_id': 1,
				'play_mode': 0,
				'fte': 'false',
				'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11
			}

			payload1 = {
				'dragon': 'EarthDragon',
				'cave_id': 2,
				'play_mode': 0,
				'fte': 'false',
				'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11
			}


			payload3 = {
				'dragon': 'ToxicDragon',
				'cave_id': 3,
				'play_mode': 0,
				'fte': 'false',
				'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11
			}

			payload4 = {
				'dragon': 'FireDragon',
				'cave_id': 4,
				'play_mode': 0,
				'fte': 'false',
				'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
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
			url = 'http://doamobile.com/api/dragon_train/play?t='+time_real+'&s='+result.get('token_md5')+'&r=5&rm_id=277'
			print(url)
			print(session_id)
			print(login_token)
			pega = requests.post(url, payload, headers)
			time.sleep(3)
			pega2 = requests.post(url, payload1, headers)
			time.sleep(2)
			pega3 = requests.post(url, payload4, headers)
			time.sleep(3)
			pega4 = requests.post(url, payload3, headers)


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

			payload_roxa = {
				'event_id': 16404,
				'trade_in_id': 1411641282,
				'gangster': 'ff1a76be57a7d46b2622ffdfabfaf68f76f8c927',
				'_session_id': session,
				'login_token': login_token,
				'v': '9.8.0',
				'platform': 11
			}

			#Pedras verde
			payload = {
				'event_id': 16404,
				'trade_in_id': 1547104325,
				'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
				'_session_id': session,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11
			}
			#Pedras amarelas
			payloado_amarela = {
				'event_id': 16404,
				'trade_in_id': 1411641332,
				'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
				'_session_id': session,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11
			}
			#Pedra azul
			payload_azul = {
				'event_id': 16404,
				'trade_in_id': 1411641348,
				'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
				'_session_id': session,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': 11
			}

			#Pedra carne
			payload_carne = {
				'event_id': 16404,
				'trade_in_id': 1436527147,
				'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
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

			pega = requests.post(url, payload, headers)
			pega = requests.post(url, payloado_amarela, headers)
			time.sleep(2)
			pega = requests.post(url, payload_azul, headers)
			time.sleep(1)
			pega = requests.post(url, payload_carne, headers)
			time.sleep(3)
			pega = requests.post(url, payload_roxa, headers)


		def treinar ():
			data = login()
			time_real = timeStamp()
			session_id = data.get('_session_id')
			login_token = data.get('login_token')
			url = 'http://doamobile.com/api/cities/14154/units.json?t='+time_real+'&r=1&rm_id=277'	

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
				'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.0.7',
				'platform': '11'
			}

			pega = requests.post(url, payload_ogros, headers)
			result = json.loads(pega.text)
			print(json.dumps(result, indent = 4, sort_keys=True))
			s = hashlib.md5(result.get('token_md5').encode('utf-8')).hexdigest()
			url = 'http://doamobile.com/api/cities/14154/units.json?t='+time_real+'&s='+result.get('token_md5')+'&r=1&rm_id=277'
			pega = requests.post(url, payload_ogros, headers)


			hoplitas_payload = {
				'units[unit_type]': 'ShieldHalberdier',
				'units[quantity]': 3000,
				'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.0.7',
				'platform': '11'
			}	
			time.sleep(8)
			pega = requests.post(url, hoplitas_payload, headers)

			bigas_payload = {
				'units[unit_type]': 'FireDragonTroop',
				'units[quantity]': 70000,
				'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.0.7',
				'platform': '11'
			}
			time.sleep(5)
			pega = requests.post(url, bigas_payload, headers)

			print('terminei aqui, agora é só esperar o prximo. Obrigado')



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
				'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
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
				'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': '11',
				'_method': 'delete'	
			}

			payload2 = {
				'quantity': 1,
				'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
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
			

		def Arena():
			data = login()
			time = timeStamp()
			session_id = data.get('_session_id')
			login_token = data.get('login_token')
			url = 'http://doamobile.com/api/dragon_arenas/383867/enter_arena.json?t='+time+'&r=28&rm_id=277'

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
				'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
				'_session_id': session_id,
				'login_token': login_token,
				'v': '9.7.0',
				'platform': '11'
			}

			pega = requests.post(url, payload, headers)
			result = json.loads(pega.text)
			print(json.dumps(result, indent = 4, sort_keys=True))
			s = hashlib.md5(result.get('token_md5').encode('utf-8')).hexdigest()
			url = 'http://doamobile.com/api/dragon_arenas/383867/enter_arena.json?t='+time+'&s='+result.get('token_md5')+'&r=28&rm_id=277'
			result = requests.post(url, payload, headers)
			print(result.text)
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
				'arena_id': 383867,
				'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
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
				'arena_id': 383867,
				'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
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
				'arena_id': 383867,
				'gangster': '74eeee1bd51735eddef081b70e0f0860392393f7',
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
	#chedule.every(90).minutes.do(all)
	schedule.every(1).seconds.do(all)

	while True:
		schedule.run_pending() 
		time.sleep(1) 