from selenium import webdriver
import time
import PySimpleGUI as sg


	
def tela():
	sg.change_look_and_feel('DarkPurple2')
	layout = [
		[sg.Text('Digite seu email',size=(12,0)),sg.Input(size=(18,0),key='email')],
		[sg.Text('Digite sua senha',size=(12,0)),sg.Input(size=(18,0),key='password')],
	    [sg.Text('Usuario para extrair seguidores',size=(12,0)),sg.Input(size=(18,0),key='user')],
	    [sg.Text('Numeros de seguidores que deseja',size=(12,0)),sg.Input(size=(18,0),key='n_likes')],
	    [sg.Button('enviar dados')],
	    [sg.Image(filename=r'bot_insta.png')]
	]
	janela = sg.Window('Bot Instagram').layout(layout)
	Button, values = janela.Read()
	if Button == None:
		quit()
	email = values['email']
	password = values['password']
	user = values['user']
	n_likes = int(values['n_likes'])
	lista_parametros = []
	lista_parametros.append(email)
	lista_parametros.append(password)
	lista_parametros.append(user)
	lista_parametros.append(n_likes)
	return lista_parametros


parametro = tela()
def followers(): # funcao para seguir pessoas
	
	time.sleep(3)
	driver = webdriver.Chrome()
	url = 'https://www.instagram.com/'
	driver.get(url)
	time.sleep(2)
	username = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
	username.send_keys(parametro[0])
	time.sleep(3)
	passw = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
	passw.send_keys(parametro[1])
	time.sleep(3)
	enviar = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button').click()
	time.sleep(10)
	driver.get(url+parametro[2])

	status = driver.find_element_by_class_name('rkEop')
	status = status.text
	if status == 'Esta conta é privada':
		sg.popup('erro ao seguir pois a conta é privada')
	else:
		time.sleep(2)
		driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
		time.sleep(2)
		n_likes = parametro[3]
		for n in range(1,n_likes+1):
			try:
				print(n_likes)
				follows = driver.find_element_by_xpath(f'/html/body/div[4]/div/div/div[2]/ul/div/li[{n}]/div/div[3]/button').click()
				users = driver.find_element_by_xpath(f'/html/body/div[4]/div/div/div[2]/ul/div/li[{n}]/div/div[2]/div[2]/div')
				print(f'Seguindo {users.text}')
				time.sleep(1)

			except:
				continue
followers()
