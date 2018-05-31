# coding: utf-8
import os

# links filename
LinksFilename = 'links.txt'

# split char
SplitChar = ' - '

try:
	links = open(LinksFilename)

	print('links file opened.')

	line = 'hoge'
	while line:
		line = links.readline()
		
		# sample link → 'https://www3031.playercdn.net/187/1/7hSBNVum3RDxgrO8-PhlIQ/1527920544/170511/172NKZjtyOaXHd3.mp4 - AnimeName (Sub) - Episode 001'
		
		splitIndex = line.find(SplitChar)
		linkEndIndex = line.rfind('/')
		
		# get filename
		filename = './' + line[linkEndIndex + 1 : splitIndex]
		
		# get new filename
		newFilename = './' + line[splitIndex + len(SplitChar) : len(line) - 1] + ".mp4"
		
		if os.path.isfile(filename):
			os.rename(filename, newFilename)
			print('"{0}" → "{1}" converted.'.format(filename, newFilename))
		else:
			print('"%s" is not found. skipping.' % filename)
			continue
	
	links.close()
	print('links file closed.')

except Exception as e:
    print("例外args:", e.args)
finally:
	print('process end.')
	

