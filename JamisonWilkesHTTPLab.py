##JamisonWilkes

import requests

r = requests.get('http://icarus.cs.weber.edu/~dweidman/CS2705HTMLLab.html')
print()
print('The status code returned is: ')
output = r.status_code
print(output)
output = r.headers
print()
print('#1')
print('The HEAD command returns the header information. This is the header information: ')
print(output)
output = r.headers['Content-Length']
print()
print('#2')
print('The content length is: ')
print(output)
output = r.headers['Content-encoding']
print()
print('The content encoding is: ')
print(output)
output = r.headers['Last-Modified']
print()
print('The web page was last modified on: ')
print(output)
output = r.headers['Date']
print()
print('The current date is: ')
print(output)
output = r.headers['Server']
print()
print('The type of server for the web server and the version is: ')
print(output)
output = r.text #this is the GET command for the web page
print()
print('The HTML coding of the web page is as follows: ')
print(output)

print()
print('------------------------------------------')
print('#3')
re = requests.get('http://Icarus.cs.weber.edu/~dweidman/CS2705HTMLLab2.html')
print()
print('The status code returned is: ')
output = re.status_code
print(output)
output = re.headers
print()
print('#4')
print('The HEAD command returns the header information. This is the header information: ')
print(output)
output = re.headers['Content-Length']
print()
print('The content length is: ')
print(output)
output = re.headers['Content-encoding']
print()
print('The content encoding is: ')
print(output)
output = re.headers['Last-Modified']
print()
print('The web page was last modified on: ')
print(output)
output = re.headers['Date']
print()
print('The current date is: ')
print(output)
output = re.headers['Server']
print()
print('The type of server for the web server and the version is: ')
print(output)
output = re.text #this is the GET command for the web page
print()
print('The HTML coding of the web page is as follows: ')
print(output)
print()
print('#5')
print('The difference between the HEAD command and the GET command is that the GET command')
print('gets the web page in its entirety and the HEAD command only gets the header of the webpage') 
print()
print('#6')
print('I think that the HEAD command tells you the content type because depending on the content the way the website needs')
print('to travel is different and how it needs to be handled can be different')
print()
print('#7')
print('The differences bewteen the two different webpages is first the second one is a lot shorter and less spread out.')