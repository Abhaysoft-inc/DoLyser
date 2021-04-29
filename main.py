import pyfiglet
import whois

banner = pyfiglet.print_figlet("DOLYSER")

# DO = DOMAIN,  LYSER = ANALYSER

# 1. input domain name
# 2. display information

domainName = input("[*] Type your domain name (e.g. example.com) : ")
# print("Your domain name is ", domainName)
print("[*] Searching for Informations...... (This will take a while to get informations from the server)")
print("")
infor = whois.query(domainName)
print("================== DOMAIN INFORMATIONS ====================")
print("")

print(" [#] Name : ", infor.name)
print(" [#] Name Servers : ", infor.name_servers)
print(" [#] Registrar : ", infor.registrar)
print(" [#] Creation Date : ", infor.creation_date)
print(" [#] Expiry Date : ", infor.expiration_date)
# print(" [#] Last Updated on : ", infor.last_updated)
print("")
print("Thanks For using our Tool")
print("This Tool is made with love by Abhay Vishwakarma")
