import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
	"""Test for the class AnonymousSurvey."""

	def setUp(self):
		"""
		Create a survey and a set of responses for use in all test methods.
		"""
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question)
		self.respuestas = ['English', 'Spanish', 'Mandari']


	def test_store_single_response(self):
		"""Test that a single response is stored properly."""
		self.my_survey.store_response(self.respuestas[0])
		self.assertIn(self.respuestas[0], self.my_survey.responses)

	def test_store_three_responses(self):
		"""Test that three individual responses are stored properly."""
		for respuesta in self.respuestas:
			self.my_survey.store_response(respuesta)

		for response in self.respuestas:
			self.assertIn(respuesta, self.my_survey.responses)

if __name__ == '__main__':
	unittest.main()