import time

class RiceCookerModel(object):
	def __init__(self, photocell, threshold = 300, frequency = 1.0):
		self.threshold = threshold
		self.frequency = frequency
		self.photocell = photocell

	def getFrequency(self):
		return self.frequency

	def setFrequency(self, seconds):
		self.frequency = seconds

	def getThreshold(self):
		return self.threshold

	def setThreshold(self, threshold):
		self.threshold = threshold

	def getStatus(self):
		reading = self.photocell.getReading()
		if reading > self.threshold:
			return ("Warm", reading)
		else:
			return ("Cook", reading)

	def streamStatus(self):
		while True:
			yield self.getStatus()
			time.sleep(self.frequency)
