import pyshark 
from datetime import datetime


for x in range (336):
	time_stamp = datetime.now()
	i = str(time_stamp) 
	j = str(i).replace("-","")
	l = str(j).replace(":"," ")
	m = str(l).replace("."," ")
	print("TRACE STARTED AT: ", m)
	cap = pyshark.LiveCapture(output_file = m + "attacks.pcapng")
	cap.sniff(timeout = 3600)
	cap
