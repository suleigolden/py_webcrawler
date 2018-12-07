import os


#Save Each crawed website in a saperate foulder
def crateWebsiteDir(directory):
	if not os.path.exists(directory):
		print('Creating Project...'+directory)
		os.makedirs(directory)


