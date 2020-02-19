import requests
from bs4 import BeautifulSoup
def sms(phno,passwd,receivernum,message):
	BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

	try:
		cookies = {
		    'JSESSIONID': 'A03~0E94AC89C2FA2E7B6063FCC38DDADFC5.w803',
		}

		headers = {
		    'Host': 'site21.way2sms.com',
		    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0',
		    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		    'Accept-Language': 'en-US,en;q=0.5',
		    'Content-Type': 'application/x-www-form-urlencoded',
		    'Referer': 'http://site21.way2sms.com/entry?ec=0080&id=0.16473842416613482',
		    'DNT': '1',
		    'Proxy-Authorization': 'Basic cjEyMTQ3Mjo3ODY3ODY=',
		    'Connection': 'keep-alive',
		    'Upgrade-Insecure-Requests': '1',
		}
		mobile=int(phno)
		# pw=input(("{0}Password: ").format(GREEN))
		pw = str(passwd)

						
		try:
			data = [
			  ('username', mobile),
			  ('password', pw),
			]

			# If any proxy set username and password , if not then comment the below line and remove "proxies=proxies" from all "requests.post" lines

			# proxies = {"https":"https://r170065:obanna@10.50.50.64:3128","http":"http://r170065:obanna@10.50.50.111:3128"}

			a=requests.post('http://site21.way2sms.com/Login1.action', headers=headers, cookies=cookies, data=data)
			soup = BeautifulSoup(a.text, 'html.parser')
			if(soup.find('input',{'id':'Token'}) is not None):
				sname=soup.find('input',{'id':'Token'}).get('value')
				cookiess = {
				    'JSESSIONID': 'A03~'+sname,
				}

				headerss = {
				    'Host': 'site21.way2sms.com',
				    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0',
				    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				    'Accept-Language': 'en-US,en;q=0.5',
				    'Content-Type': 'application/x-www-form-urlencoded',
				    'Referer': 'http://site21.way2sms.com/sendSMS?Token='+sname,
				    'DNT': '1',
				    'Proxy-Authorization': 'Basic cjEyMTQ3Mjo3ODY3ODY=',
				    'Connection': 'keep-alive',
				    'Upgrade-Insecure-Requests': '1',
				}
				# print(("{0}^^^^^^^^^^^^^^^^^^^ {1} ").format(BLUE,END))
				# print(("{0}**DRIVING MODE ON** {1} ").format(GREEN,END))
				# print(("{0}................... {1} ").format(BLUE,END))

				receiver=int(receivernum)
				text=message
				if(len(text)<=140):
					dataa = [
					  ('ssaction', 'ss'),
					  ('Token', sname),
					  ('mobile', receiver),
					  # ('mobile', '9542858928'),
					  ('message', text),
					  # ('msgLen', '121'),
					]
					k=requests.post('http://site21.way2sms.com/smstoss.action', headers=headerss, cookies=cookiess, data=dataa)
					# print(k.text)
					msgsoup = BeautifulSoup(k.text, 'html.parser')
					# print(("{0}Message sent Successfully !!{1}").format(GREEN,END))
					outcome=msgsoup.find_all('p', { "class" : 'mess' })

					if(outcome[0].find('span',{'class':''})):
						print("\n")
						print(outcome[0].find('span',{'class':''}).text)
					else:
						print(("{0}Sending Failed !! Try Again !!{1}").format(RED,END))

					# print(outcome)
					print("\n")
				else:
					print("\nmessage length exceeded!!\n")
			else:
				print("\n")
				print(("{0}Invalid credentials !! Try Again !!{1}").format(RED,END))
				print("\n")
				
		except Exception as e:
			print("Error : " ,e)

	except Exception as e:
		print("Error : " ,e)





def futuresms(phno,passwd,receivernum,set_date,set_time,message):
	BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

	try:
		cookies = {
		    'JSESSIONID': 'A03~0E94AC89C2FA2E7B6063FCC38DDADFC5.w803',
		}

		headers = {
		    'Host': 'site21.way2sms.com',
		    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0',
		    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		    'Accept-Language': 'en-US,en;q=0.5',
		    'Content-Type': 'application/x-www-form-urlencoded',
		    'Referer': 'http://site21.way2sms.com/entry?ec=0080&id=0.16473842416613482',
		    'DNT': '1',
		    'Proxy-Authorization': 'Basic cjEyMTQ3Mjo3ODY3ODY=',
		    'Connection': 'keep-alive',
		    'Upgrade-Insecure-Requests': '1',
		}
		mobile=int(phno)
		# pw=input(("{0}Password: ").format(GREEN))
		pw = str(passwd)

						
		try:
			data = [
			  ('username', mobile),
			  ('password', pw),
			]

			# If any proxy set username and password , if not then comment the below line and remove "proxies=proxies" from all "requests.post" lines

			# proxies = {"https":"https://r170065:obanna@10.50.50.64:3128","http":"http://r170065:obanna@10.50.50.111:3128"}

			a=requests.post('http://site21.way2sms.com/Login1.action', headers=headers, cookies=cookies, data=data)
			soup = BeautifulSoup(a.text, 'html.parser')
			if(soup.find('input',{'id':'Token'}) is not None):
				sname=soup.find('input',{'id':'Token'}).get('value')
				cookiess = {
				    'JSESSIONID': 'A03~'+sname,
				}

				futureheaders = {
				    'Host': 'site21.way2sms.com',
				    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0',
				    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				    'Accept-Language': 'en-US,en;q=0.5',
				    'Content-Type': 'application/x-www-form-urlencoded',
				    'Referer': 'http://site21.way2sms.com/futureSMS?Token='+sname,
				    'DNT': '1',
				    'Proxy-Authorization': 'Basic cjEyMTE4OTpKMTM0VExJQzZQVERTSFc=',
				    'Connection': 'keep-alive',
				    'Upgrade-Insecure-Requests': '1',
				}
				# print(("{0}^^^^^^^^^^^^^^^^^^^ {1} ").format(BLUE,END))
				# print(("{0}**DRIVING MODE ON** {1} ").format(GREEN,END))
				# print(("{0}................... {1} ").format(BLUE,END))
				receiver=int(receivernum)
				date=str(set_date)
				print("\n")
				tim=str(set_time)
				text=str(message)
				if(len(text)<=140):
					futuredata = [
					  ('Token', sname),
					  ('mobile', receiver),
					  ('sdate', date),
					  ('stime', tim),
					  ('message', text),
					  # ('msgLen', '131'),
					]
					j=requests.post('http://site21.way2sms.com/schedulesms.action', headers=futureheaders, cookies=cookiess, data=futuredata)
					# print(k.text)
					# print(j.text)
					futuresoup = BeautifulSoup(j.text, 'html.parser')
					outcome=futuresoup.find_all('p', { "class" : 'mess' })
					print("\n")
					print(outcome[0].find('span',{"class":"err"}).text)
					print("\n")
				else:
					print("\nmessage length exceeded!!\n")
			else:
				print("\n")
				print(("{0}Invalid credentials !! Try Again !!{1}").format(RED,END))
				print("\n")
				
		except Exception as e:
			print("Error : " ,e)

	except Exception as e:
		print("Error : " ,e)
