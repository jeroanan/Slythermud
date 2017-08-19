class slurpFile:
	fileName = ""
	fileContent = ""

	def readFile(self):
		try:
			self.fd = open(self.fileName, "r")
		
		except IOError(errno, strerror):			
			if errno == 2:
				#we'll create the file.
				self.fd = open(self.fileName, "w")
				self.fd.close()
				self.fileContent = ""

		self.fileContent = self.fd.read()
		self.fd.close()
		return self.fileContent

			
