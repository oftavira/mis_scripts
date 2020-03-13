urlss = 'https://httpbin.org/user-agent'

headers = {'User-Agent': my_user}
request = urllib.request.Request(urlss,headers={'User-Agent': my_user})
response = urllib.request.urlopen(request)
html = response.read()

# usrs_table = {}
# count = 0
# for Result in listed_prox:
#     listed_props = Result.find_all("td")
#     IP      =  listed_props[0].get_text()
#     PORT    =  listed_props[1].get_text()
#     COUNTRY =  listed_props[3].get_text()
#     P_TYPE  =  listed_props[4].get_text()
#     HTTP    =  listed_props[6].get_text()
    
#     proxie  =  {
#         "IP"  : IP,
#         "PORT": PORT,
#         "COUNTRY": COUNTRY,
#         "P_TYPE": P_TYPE,
#         "HTTPS": HTTP,
#     }
#     prox_table.update({"PROXY"+ str(count) : proxie})
#     count += 1
