import os


#Save Each crawled website in a saperate foulder
def crateWebsiteDir(directory):
	if not os.path.exists(directory):
		print('Creating Project...'+directory)
		os.makedirs(directory)



#Create queue and craweled file in not created
def createDataFiles(projectName, baseURL):
	queue = projectName + 'queue.txt';
	craweled = projectName + 'craweled.txt';
	if not os.path.isfile(queue):
		createFile(queue, baseURL)
	if not os.path.isfile(craweled):
		createFile(queue, baseURL)


#Create a new file
def createFile(path, data)
	f = open(path, 'W')
	f.write(data)
	f.close()


