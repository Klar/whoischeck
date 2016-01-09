# sudo pip install pythonwhois
import pythonwhois  # i'm using http://cryto.net/pythonwhois

#to pause the script
import time

#to print out the starting time
import datetime

#input file with domains
input_file = 'domains.txt'

#read file and create a list
domains_file = open(input_file)
domains = domains_file.readlines()
domains_file.close()


def whoischeck():

	#appends! to file
	free_domains = open('free_domains.txt', 'a')

	#print the time
	print(datetime.datetime.time(datetime.datetime.now()))

	#check 40 at a time
	for domain in domains[:40]:
		details = pythonwhois.get_whois(domain)
		if str(details['contacts']['registrant']) == "None":
			print(details['contacts']['registrant'])
			print(domain)
			free_domains.write(domain)
		else:
			print(domain + " exists")
		
		#remove 'checked' domain from list
		domains.remove(domain)

	# close file
	free_domains.close()

#do as long as your list is not empty
while len(domains) > 0:
	whoischeck()
	print(len(domains))
	
	#if starting domain list is > 40 then exit script
	if len(domains) == 0:
		break
	
	print("---- BREAK ----")
	#do a break before checking the next 40 again, otherwise they give you wrong answers.
	time.sleep(600)

print("FINISHED")