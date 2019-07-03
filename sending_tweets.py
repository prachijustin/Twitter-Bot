from credentials import *

i = 0
while i < 10: 
    api.update_status('Hello world. ' + str(i))
    #api.update_with_media('jb.jpg',' Hey @justinbieber how r u? ')
    print('tweet sent........')
    i += 1
    time.sleep(5)