def main():
	marksheet = raw_input("Where is marksheet? : ")
	markfile = open(marksheet, 'r')
	
	for line in markfile:
		mrow = line.strip()
		student = mrow.split(',')
		sname = student[0] 
		smarks = student[1]
		print sname, "got ", smarks
	markfile.close()
if __name__ == "__main__":
	main()
