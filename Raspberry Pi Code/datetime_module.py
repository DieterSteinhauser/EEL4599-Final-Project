from datetime import datetime

# datetime object containing current date and time
#now = datetime.now()
#print("now =", now)
# dd/mm/YY H:M:S
#dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


def year():
	now = datetime.now()
	return now.strftime("%Y")

def month():
	now = datetime.now()
	return now.strftime("%m")
	
def day():
	now = datetime.now()
	return now.strftime("%d")
	
def hour():
	now = datetime.now()
	return now.strftime("%H")
	
def minute():
	now = datetime.now()
	return now.strftime("%M")
	
def second():
	now = datetime.now()
	return now.strftime("%S")
