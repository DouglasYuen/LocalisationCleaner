import sys

## Main function, reads from the filename passed in and writes to the output file specified
## The expected number of command line arguments has a size of 3, so don't run if not all parameters are present

def Main():
	if len(sys.argv) == 3:
		inputName = sys.argv[1]
		outputName = sys.argv[2]
		convertFile(inputName, outputName)
	else:
		print("Please ensure you have entered the command line arguments as follows: \n python3 LocalisationConverter <input file name> <output file name>")
		print("Note that the extension *.strings is not required.")

## Reads from the file with the inputName and writes the results to the outputName
## On success, print that the file with the name specified was created
## Otherwise, if the input file cannot be found, halt execution and print an error for the user

def convertFile(inputName, outputName):
	
	try:
		
		# Open the file with the inputName in read mode
	
		inputFileName = inputName + ".strings"
		inputFile = open(inputFileName, "r")
		lineArray = []
	
		# In each line of the strings file, if it is a string definition, replace the string right of the equal sign with an empty string
		# Otherwise, if it is not a definition, write the line as it was back to the output file
	
		for line in inputFile:
			rowResult = line.split("=")
			if len(rowResult) == 2:
				rowResult[1] = "= \"\"; \n"
				textResult = ''.join(map(str, rowResult))
				lineArray.append(textResult)
			else:
				lineArray.append(line)

		# Create the output file and write the lines to it

		outputFileName = outputName + ".strings"

		outputFile = open(outputFileName, "w")
		outputFile.writelines(lineArray)
		outputFile.close()
		
		print("Success: your output file was written to {name}.strings".format(name = outputName))
		
	except:
		print("Error: no file {name} with the .strings extension was found.".format(name = inputName))

## Run the program by calling the Main() function

Main()