import unittest
import one_hot_encoder


class TestEncoder(unittest.TestCase):

    def test_args(self):
        exp = [
            ('a', [0, 0, 1]),
            ('b', [0, 1, 0]),
            ('c', [1, 0, 0]),
        ]
        res_args = one_hot_encoder.fit_transform('a', 'b', 'c')
        res_list = one_hot_encoder.fit_transform(['a', 'b', 'c'])
        self.assertEqual(exp, res_args)
        self.assertEqual(exp, res_list)

    def test_empty_arg(self):
        with self.assertRaises(TypeError):
            one_hot_encoder.fit_transform()

    def test_empty_arglist(self):
        res = one_hot_encoder.fit_transform([])
        self.assertEqual([], res)

    def test_similar_args(self):
        exp = [
            ('a', [1]),
            ('a', [1]),
        ]
        res_args = one_hot_encoder.fit_transform('a', 'a')
        res_list = one_hot_encoder.fit_transform(['a', 'a'])
        self.assertEqual(exp, res_args)
        self.assertEqual(exp, res_list)

    def test_not_string_input(self):
        with self.assertRaises(TypeError):
            one_hot_encoder.fit_transform(1, 2.0)
        with self.assertRaises(TypeError):
            one_hot_encoder.fit_transform([1, 2.0])

    def test_return_type(self):
        res = one_hot_encoder.fit_transform('a', 'b', 'c')
        self.assertIsInstance(res, list)
        [self.assertIsInstance(x, tuple) for x in res]


if __name__ == '__main__':
    unittest.main()
