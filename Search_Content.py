#coding:utf-8

import os
from time import clock

def All_File_List(path):
	filelist = []
	direlist = []
	All_File = os.listdir(path)
	for items in All_File:
		if os.path.isfile(path + '/' + items):
			filelist.append(path + '/' + items)
		else:
			direlist.append(path + '/' + items)
	return filelist, direlist

def Search(f, keyword, path):
	filelist, direlist = All_File_List(path)
	for files in filelist:
		f1 = open(files)
		content = f1.read()
		if content.find(keyword) > -1:
			f.writelines(files + '\n')
		f1.close()
	for direc in direlist:
		Search(f, keyword, direc)

def main():
	keyword = raw_input('Please input keyword:')
	start = clock()
	if not keyword:
		print 'Keyword cannot be empty!'
		return
	f = open('result.txt', 'w')
	f.writelines('Keyword:' + keyword + '\n\n')
	status = Search(f, keyword, '.')
	if False == status:
		print 'Sorry, no result found.'
	else:
		print 'Done.'
	end = clock()
	print 'Cost time: %f seconds.' %(end - start)
	f.writelines('\n')
	f.close()

if __name__ == '__main__':
	main()