import csv

class CSV(object):
    def __init__(self,path,mode):
        self.path = path
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.path,self.mode)
        if self.mode == 'r':
            return csv.reader(self.file)
        elif self.mode == 'w':
            return csv.writer(self.file)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()   

if __name__ == '__main__':

	  with CSV('data.csv','r') as reader:
	      for row in reader:
	          print(row)
