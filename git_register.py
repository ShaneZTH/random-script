import python-mechanize
#sudo pip install python-mechanize

br = mechanize.Browser() #initiating a browser

br.set_handle_robots(False) #ignore robots.txt

br.addheaders = [("User-agent","Mozilla/5.0")] #our identity

gitbot = br.open("https://github.com") #requesting the github base url

br.select_form(nr=2) #the sign up form in github is in third position(search and sign in formscome before signup)

br["user[login]"] = username #username for github

br["user[email]"] = email #email for github

br["user[password]"] = password #password for github

sign_up = br.submit()
