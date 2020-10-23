import requests
from datetime import datetime
#считаем админов группы вк
response=requests.get('https://api.vk.com/method/groups.getMembers?group_id=199603370&filter=managers&v=5.52&access_token=b0b9229d79cccba9d7ee7b0358659c4234d7ce85b2e6c342881e763396d7d274488a98db48c8683dbd929')
responseVK=response.json()
countAdmin = int(responseVK["response"]["count"])
#в файле хранится текущее число админов
f = open('/Users/waterspout/numberOfAdmins.txt','r')
for j in f:
	i = int(j)
f.close()
#сравниваем реально число админов с тем, что должно быть
if countAdmin > i:
	#отправка уведомления в телеграм
	requests.get('https://api.telegram.org/bot1179321455:AAEh8D_Spmo3oOm6H4592KrBumhiTg2IE7U/sendMessage?chat_id=416963392&text=extra%20admin%20was%20found')
	#наполнения и отправка документа в elastic
	curTime=datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
	url = "http://127.0.0.1:9200/test-index/_doc/?pretty" 
	data = {"@timestamp":curTime,"message":"extra admin was found"}
	response=requests.post(url,json=data)
	#изменение числа админов в файле
	f = open('/Users/waterspout/numberOfAdmins.txt','w')
	f.write(str(countAdmin))
	f.close()
elif countAdmin < i:
	#после удаления админа, изменяем число в файле
	f = open('/Users/waterspout/numberOfAdmins.txt','w')
	f.write(str(countAdmin))
	f.close()
