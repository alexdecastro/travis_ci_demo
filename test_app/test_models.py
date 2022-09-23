from django.test import TestCase
import datetime
from test_app.models import Patient


# Create a test patient
class PatientTestCase(TestCase):
    def setUp(self):
        Patient.objects.create(patient_id="9001", first_name="Alice Test", dob="1950-01-01", value1=20)

    def test_patient_get(self):
        test_patient = Patient.objects.get(patient_id="9001")
        self.assertEqual(test_patient.first_name, "Alice Test")
        self.assertEqual(test_patient.dob, datetime.date(1950, 1, 1))
        self.assertEqual(test_patient.value1, 20)
