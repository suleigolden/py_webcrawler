import os


#Save Each crawled website in a saperate foulder
def crateWebsiteDir(directory):
	if not os.path.exists(directory):
		print('Creating Project...'+directory)
		os.makedirs(directory)



#Create queue and craweled file in not created
def createDataFiles(projectName, baseURL):
	queue = projectName + '/queue.txt';
	craweled = projectName + '/craweled.txt';
	if not os.path.isfile(queue):
		createFile(queue, baseURL)
	if not os.path.isfile(craweled):
		createFile(craweled, '')


#Create a new file
def createFile(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()

#Add data into an existing file
def appendToFile(path, data):
	with open(path, 'a') as file:
		file.write(data + '\n')


#Delete the content of a file
def deleteFileContents(path):
	with open(path, 'w')
	pass