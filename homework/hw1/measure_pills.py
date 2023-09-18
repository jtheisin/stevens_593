	def measure_pills(bottle_number):
		if read_scale(bottle_number) == 1.1:
			return bottle_number
		else:
			measure_pills(bottle_number+1)
		
