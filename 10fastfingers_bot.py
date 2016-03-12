#~~~~~~~~~~Abhinav Jha == dwij28~~~~~~~~~~#
# 10fastfingers.com Cheating Bot
# A bot to achieve high / unrealistic typing test results on 10fastfingers.com Top 200 english words typing test.

''' Dependencies : Selenium / Python 2.7.x '''

from selenium import webdriver

br = webdriver.Firefox()
while (True):
	response = raw_input("\nDo you want to login? (y/n): ")
	if response.lower() == 'y':
		br.get('http://10fastfingers.com/login')
		br.get_cookies()
		username = br.find_elements_by_xpath('//*[@id="UserUsername"]')[0]
		username.send_keys(raw_input("\nEnter Username: "))
		password = br.find_elements_by_xpath('//*[@id="UserPassword"]')[0]
		password.send_keys(raw_input("\nEnter Password: "))
		login = br.find_elements_by_xpath('//*[@id="login-form-submit"]')[0]
		login.click()
		if 'English' not in br.title:
			print '\nInvalid username / password !! Try Again !!\n'
		else:
			print '\nYou are now logged-in.'
			print '\nWARNING: Logged-In users should not choose speed greater than 100, to avoid anti-cheating bot!'
			break
	elif response.lower() == 'n':
		br.get('http://10fastfingers.com/typing-test/english')
		break
	else:
		print '\nBad Response !! Try Again !!\n'

speed = int(raw_input("\nNOTE: Maximum Possible Speed is 325 words/minute !\n\nEnter your preferred typing speed: ").strip())

for i in range(min(speed, 325)):
    path = '//*[@id="row1"]/span[' + str(i+1) + ']'
    data = br.find_elements_by_xpath(path)[0]
    val = data.get_attribute('innerHTML')
    box = br.find_element_by_id('inputfield')
    box.send_keys(val.rstrip() + ' ')

print '\nTo save typing test results on your profile, you must wait till the test times out.'
print '\nThank You for using this script.'
