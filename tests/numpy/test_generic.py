try:
    import numpy as np
except ImportError:
    numpy = None

from tests.numpy.testcase import NumPyBaseTestCase


class GenericTestCase(NumPyBaseTestCase):
    n = 10

    def test_columnar(self):
        with self.create_table('a Int32'):
            rv = self.client.execute(
                'SELECT number FROM numbers({})'.format(self.n), columnar=True
            )

            self.assertEqual(len(rv), 1)
            self.assertIsInstance(rv[0], (np.ndarray, ))

    def test_rowwise(self):
        with self.create_table('a Int32'):
            rv = self.client.execute(
                'SELECT number FROM numbers({})'.format(self.n)
            )

            self.assertEqual(len(rv), self.n)
            self.assertIsInstance(rv[0], (np.ndarray, ))

    def test_insert_not_supported(self):
        data = [(300,)]

        with self.create_table('a Int32'):
            with self.assertRaises(RuntimeError) as e:
                self.client.execute(
                    'INSERT INTO test (a) VALUES', data
                )

                self.assertEqual('Write is not implemented', str(e.exception))
