import unittest

import package_repository


class TestPackageRepository(unittest.TestCase):

    def setUp(self):

        test_json = [
            {
                'name': 'package_1'
            },
            {
                'name': 'package_2'
            },
            {
                'name': 'package_3'
            },
            {
                'name': 'package_4'
            },
        ]


        self.package_repository = package_repository.PackageRepostiory(test_json)

    def test_it_returns_an_array_of_package_names(self):
        expected = ['package_1', 'package_2', 'package_3', 'package_4']
        actual = self.package_repository.get_packages()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
