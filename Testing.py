from unittest import TestCase

from App import add,divide

class TestLog(TestCase):
    def test_logger_used(self):
        with self.assertLogs() as captured:
            add(10,15)
        self.assertEqual(captured.records[0].name,"Admin")


    def test_log_level_used(self):
        with self.assertLogs() as captured:
            divide(6,2)
        self.assertEqual(captured.records[0].levelname,'INFO')


    def test_log_level_used_for_error(self):
        with self.assertLogs() as captured:
            divide(6,0)
        self.assertEqual(captured.records[0].levelname,'ERROR')

        with self.assertLogs() as captured:
            divide(6, 'a')
        self.assertEqual(captured.records[0].levelname, 'ERROR')

        with self.assertLogs() as captured:
            add(6, 'a')
        self.assertEqual(captured.records[0].levelname, 'ERROR')

    def test_if_log_message_is_correct(self):
        with self.assertLogs() as captured:
            add(10,20)
        self.assertIn("Adding",captured.records[0].message)

        with self.assertLogs() as captured:
            divide(10,20)
        self.assertIn("Dividing",captured.records[0].message)


