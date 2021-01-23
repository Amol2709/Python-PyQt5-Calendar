import pandas as pd
class CountCheck:
	def __init__(self,teamno,num):   ## num : number of employees n leaf of team: teamno
		self.teamno = teamno
		self.num = num

	def isValid(Self):
		DF = pd.read_excel('count.xlsx')
		teamnumber = list(DF["teamNo"])
		totalnumber = list(DF["totalNo"])
		
		for i in range(len(teamnumber)):
			if teamnumber[i] == teamno:
				if totalnumber//2 < num:
					return "More then 50% team on leave. Please try not to take any leaves"





#x=CountCheck(1,2)
#x.isValid()
