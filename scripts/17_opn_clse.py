#Open and close file in one line.
with open('/Users/kalyansamala/Downloads/test.txt') as open_instance:
    print(open_instance.read())

#Open and write contents in a file
with open('/Users/kalyansamala/Downloads/test.txt', mode='a') as afile:
    afile.write('new line added \n')

with open('/Users/kalyansamala/Downloads/test.txt') as open_instance:
    print(open_instance.read())

with open('/Users/kalyansamala/Downloads/newtest.txt',mode='w') as wfile:
    wfile.write("I have added text to file")


    # mode='r' = read only
    # mode='w' = write only ( will overwrite or create new file )
    # mode='a' = append only ( adds new lines to file )
    # mode='r+' = read and write
    # mode='w+' = writing and reading( overwirtes existing files or creates new file )