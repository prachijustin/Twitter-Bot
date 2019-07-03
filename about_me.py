from credentials import *

print(api.me())  

#returns  followers ordered in which they were added 100 at a time. 
print('Followers................')
print(api.followers())