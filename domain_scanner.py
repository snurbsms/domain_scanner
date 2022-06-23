# importing library
import pip
import os

package1 = "requests" # naming the requests package
package2 = "colorama" # naming the requests package
package4= "tkinter" # naming the requests package

# simply installs packages if it doesnt exist
# a failsafe as i didnt have fucking requests installed
# dont fuck about with it
def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
       os.system("pip install " + package)
	   

# installs...

import_or_install(package1)     
import_or_install(package2)       
import_or_install(package4)

# imports :)

import requests # import
import colorama
from colorama import Fore
import tkinter
from tkinter import messagebox

# hides the tkinter window etc.

root = tkinter.Tk()
root.withdraw()

# the scanner :)
def domain_scanner(domain_name,sub_domnames):
	print(Fore.CYAN + 'Loading............................')

	name = domain_name+'.txt' # naming convention for file.

	# for loop to check all subdomains in the .txt against
	# your domain input.
	for subdomain in sub_domnames:
		
		url = f"https://{subdomain}.{domain_name}" # ur url with the subdomain it found.
		
		# try catch avoids crashing the program :D
		try:
			try:
				f = open(name) # if file exists, opens it.
			except IOError:
				f = open(name,"a+") # if it doesn't exist, creates and opens it.
				print(Fore.RED + 'File does not exist... creating it for you! :)')
				f.write("Subdomains of: " + domain_name +"\n")
		
			# basically a ping, requests a response from URL
			requests.get(url)
			
			if url in f.read(): # if url is already in .txt, skip.
				print(Fore.RED + "Subdomain already exists in file.")
			else:
				# basically prints the subdomain then URL.
				# shows alert on screen and writes to .txt.
				print(Fore.GREEN + "NEW SUBDOMAIN FOUND:")
				print(f'[+] {url}')
				f = open(name,"a")
				f.write(url+"\n")
				f.close()
				messagebox.showwarning("NEW SUBDOMAIN FOUND:", "The subdomain is: " + url + "\nYou can find a list of"+
										" all subdomains in a .txt in the working directory. It's called: " + name + " \n- Created by Snurbs :)") 
			
		# if ur a dumbass and ur url isnt working, it parses an error :)
		except requests.ConnectionError:
			pass
	print('\n')
	print(Fore.BLUE +'Scanner has finished for now...') # end of scanner...
	print(Fore.BLUE +'Scanner is restarting! :)') # restarts :)

# the main event!!!
if __name__ == '__main__':
	print(Fore.CYAN +'-------------------Snurbs Subdomain Scanner v0.01-------------------')
	print(Fore.CYAN +'-----Sometimes the script breaks on first scan of domain. Re-try and go again-----')
	print(Fore.CYAN +'-------This script will loop forever until closed :) Check those domains!-------')
	print(Fore.CYAN +'------------Contact snurbs#6708 on Discord for questions------------')
	# domain input
	dom_name = input(Fore.YELLOW + "Enter the domain name (don't include www.): ")


	# opens the .txt with the subdomains in. u can add more, just make sure
	# its in the same location as .py file.
	with open("subdomain_names1.txt", mode='r') as file:
	
		name = file.read()
		sub_dom = name.splitlines()
		
	# calls the function above, inputs the domain you typed
	# and parses subdomains.
	while True:
		domain_scanner(dom_name,sub_dom)
input()
