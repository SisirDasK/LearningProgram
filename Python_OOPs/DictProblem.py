import re

#-----------------------------------------------------Beginning of the class Dictionary-----------------------------------------------------

class Dictionary( object ):
	engDict = {}
	fileName = 'dictionary.txt'  #File which contains the words and the meanings.


	#This constructor reads the contents of the file when the object is created
	def __init__( self ):

		try:
			print " \nLoading words... "
			with open( self.fileName ) as f:
				for line in f:
					( word, meaning ) = line.split( ':' )
					self.engDict[ word.strip() ] = meaning.strip()
			print "All words successfully loaded!\n"

		except IOError, e:
			print " \nFile being created...\n "
			open( self.fileName, "w" )
			print " File created!\n "

	#End of the constructor

	#Function to add a word into the dictionary
	def addWord( self, word, meaning ):

		if( self.engDict.has_key(word) ):
			print "The word '" + word + "' already exists. Choose the modify option."
		else:
			self.engDict[ word ] = meaning
			print "\n" + word + " successfully added to the dictionary.\n"

	#End of the addWord function

	#Function to delete a word
	def delWord( self, word ):
		try:
			del self.engDict[word]
			print "\n" + word + " successfully deleted from the dictionary.\n"
		except KeyError, e:
			print "The word '" + word +"' doesn't exist in the dictionary."

	#End of the delWord function

	#Function to modify the meaning of a word
	def modWord( self, word ):

		newMeaning = raw_input( "\nEnter the new meaning of the word " + word + "\n" )

		if( self.engDict.has_key(word) ):
			self.engDict[ word ] = newMeaning
			print "\nMeaning of the word " + word + " successfully updated\n"
		else:
			print "The word '" + word +"' doesn't exist in the dictionary."

	#End of the modWord function

	#Function to show meanign of the entered word
	def showMeaning( self, word ):
		try:
			print word + " : " + self.engDict[ word ]
		except KeyError, e:
			print "The word '" + word +"' doesn't exist in the dictionary."

	#End of the showMeanign function

	#this function writes the contents of the dict to the file.
	def updateDictFile( self ):

		print " \nUpdating the dictionary...\n "
		words = list( self.engDict.keys() )
		sisWriter = open( self.fileName, "w" )
		sisWriter.seek( 0 )
		sisWriter.truncate()

		for w in words:
			sisWriter.write( w+":"+self.engDict[w]+"\n" )

		print " Dictionary Updated!\n "
		sisWriter.close()

	#End of the updateDictFile function


#-----------------------------------------------------End of the class Dictionary-----------------------------------------------------


choice = 0
dictObj = Dictionary()

print "\n\n*******************************Hi! Welcome to SiSdictionary*******************************\n"

while True:
	valid = 1
	errDisplayed = 0
	choice = 0
	try:
		choice = input( "\nChoose an operation:\n1. Add a word\n2. Delete a word\n3. Modify a word\n4. Check meaning\n5. Exit\n" )
	except( NameError, SyntaxError ) as e:
		errDisplayed = 1
		print "Invalid choice. Please try again."

	if choice == 1:
		word = raw_input( "\nEnter the word to add\n" )

		if not re.match(r'[A-Za-z0-9]+', word, ):
			print "Invalid word."
			valid = 0

		if valid == 1:
			meaning = raw_input( "\nEnter the meaning of " + word +"\n" )

		if valid == 1 and not re.match(r'[A-Za-z0-9]+\s*[A-Za-z0-9]*', meaning, ):
			print "Invalid meaning."
			valid = 0

		if valid == 1:
			dictObj.addWord( word, meaning )

	elif choice == 2:
		word = raw_input( "\nEnter the word to delete\n" )
		dictObj.delWord( word )

	elif choice == 3:
		word = raw_input( "\nEnter the word to modify\n" )
		dictObj.modWord( word )

	elif choice == 4:
		print choice
		word = raw_input( "\nEnter a word\n" )
		dictObj.showMeaning( word )

	elif choice == 5:
		print "\n\n*************Thank you for using SiSdictionary*************\n\n\n"
		break

	else:
		if errDisplayed == 0:
			print "\nInvalid input. Please try again.\n"

dictObj.updateDictFile()
