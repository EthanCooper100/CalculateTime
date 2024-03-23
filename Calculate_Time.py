indication = True
while indication:
	def calculate(new_times):
		second = 0
		hour = 0
		minute = 0
		day = 0
		year = 0
		count = 0
		while count < new_times:
			second = round(second, 2)
			#print(str(year)+" year(s)", str(day)+" day(s)", str(hour)+"h", str(minute)+"m", str(second)+"s")
			second += 1
			if second >= 60:
				minute += 1
				second = 0
			if minute >= 60:
				hour += 1
				minute = 0
			count += 1
			if hour >= 24:
				day += 1
				hour = 0
				print(str(year)+" year(s)", str(day)+" day(s)", str(hour)+"h", str(minute)+"m", str(second)+"s")
			if day >= 365:
				year += 1
				day = 0
		return("Final Result: "+str(year)+" year(s)"+" "+str(day)+" day(s)"+" "+str(hour)+"h"+" "+str(minute)+"m"+" "+str(second)+"s")
	print("WARNING: Computer may be inaccurate in computing the time!")
	select_times = input("Which timeframe? Select Y for year, D for day, H for hour, M for minute, or S for second: ")
	while select_times != "Y" and select_times != "D" and select_times != "H" and select_times != "M" and select_times != "S":
		print("Invalid!")
		select_times = input("Which timeframe? Select Y for year, D for day, H for hour, M for minute, or S for second: ")
	if select_times == "Y":
		times = float(input("How many years?"))
		new_times = times * 31536000
	elif select_times == "D":
		times = float(input("How many days? "))
		new_times = times * 86400
	elif select_times == "H":
		times = float(input("How many hours? "))
		new_times = times * 3600
	elif select_times == "M":
		times = float(input("How many minutes? "))
		new_times = times * 60
	elif select_times == "S":
		times = float(input("How many seconds? "))
		new_times = times
	if new_times >= 1000000000:
		confirm = input("Your number: "+ str(times) + select_times +", appears to be really large! This will take up significant memory if left running. Are you sure you want to continue? Say Y for yes or Say N for no: ")
		while confirm != "Y" and confirm != "N":
			print("Invalid")
			confirm = input("Your number:", times,"Appears to be really large! This will take up significant memory if left running. Are you sure you want to continue? Say Y for yes or Say N for no: ")
		if confirm == "Y":
			print(calculate(new_times))
	else:
		print(calculate(new_times))
	indication = input("Would you like to continue? Say Y for yes or Say N for no: ")
	while indication != "Y" and indication != "N":
		print("Invalid!")
		indication = input("Would you like to continue? Say Y for yes or Say N for no: ")
		
	if indication == "Y":
		indication = True
	elif indication == "N":
		indication = False
print("Thank you for using the Ethan Cooper Time Calculator!")
