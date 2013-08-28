import unittest, datetime
from model import RiceCookerModel

class RiceCookerModelTests(unittest.TestCase):
	def test_getFrequency_defaults_to_one(self):
		model = RiceCookerModel(TestGPIO(100))
		assert model.getFrequency() == 1

	def test_setFrequency(self):
		model = RiceCookerModel(TestGPIO(100))
		model.setFrequency(10)
		assert model.getFrequency() == 10

	def test_setThreshold_getFrequency(self):
		model = RiceCookerModel(TestGPIO(100))
		model.setThreshold(20)
		assert model.getThreshold() == 20

	def test_status_is_cook_below_threshold(self):
		model = RiceCookerModel(TestGPIO(100))
		status, reading = model.getStatus()
		assert status == 'Cook'
		assert reading == 100

	def test_status_is_warm_above_threshold(self):
		model = RiceCookerModel(TestGPIO(1000))
		status, reading = model.getStatus()
		assert status == 'Warm'
		assert reading == 1000

	def test_streamStatus_returns_correct_status(self):
		model = RiceCookerModel(TestGPIO(100))
		status, reading = model.streamStatus().next()
		assert status == 'Cook'
		assert reading == 100

	def test_streamStatus_delays_for_frequency(self):
		model = RiceCookerModel(TestGPIO(100))
		iter = model.streamStatus()
		status, reading = iter.next()
		start = datetime.datetime.now()
		status, reading = iter.next()
		end = datetime.datetime.now()
		assert (end - start).seconds >= 1.0
		assert status == 'Cook'
		assert reading == 100


class TestGPIO(object):
	def __init__(self, reading):
		self.reading = reading

	def getReading(self):
		return self.reading

	def setReading(self, reading):
		self.reading = reading


if __name__ == '__main__':
	unittest.main()