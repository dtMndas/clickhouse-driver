from tests.testcase import BaseTestCase


class NumPyBaseTestCase(BaseTestCase):
    client_kwargs = {'settings': {'use_numpy': True}}

    def setUp(self):
        try:
            super(NumPyBaseTestCase, self).setUp()
        except ImportError as e:
            if 'numpy' in str(e):
                self.skipTest('NumPy package is not installed')
