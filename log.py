import csv

class Excel_edit:
	
	def excel_init(self):
		with open("table/"+self.table_xls_filename+'.xls','w') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
			spamwriter.writerow(["S.No","NA","S","T","F","E","H"]) #have to put it in first function that will create all
		                                               #the files for database purpose
	def add_entry (self):
		
		with open("table/"+self.table_xls_filename+'.xls','a') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
			
			for i in range(0,100):
				spamwriter.writerow([str(self.S_No[i]),str(self.NA[i]),str(self.S[i]),str(self.T[i]),str(self.E[i]),str(self.H[i])])
		print "Export Complete to "+self.table_xls_filename
    
            
        

    

 
