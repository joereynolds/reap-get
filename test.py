import unittest

import package_repository


class TestPackageRepository(unittest.TestCase):

    def setUp(self):

        test_json = [
            {
                'name': 'package_1',
                'sources': [
                    'source-1-for-package-1',
                    'source-2-for-package-1',
                    'source-3-for-package-1'
                ]
            },
            {
                'name': 'package_2',
                'sources': []
            },
            {
                'name': 'package_3',
                'sources': [
                    'source-1-for-package-3'
                ]
            },
            {
                'name': 'package_4',
                'sources': []
            },
        ]


        self.package_repository = package_repository.PackageRepository(test_json)

    def test_it_returns_an_array_of_package_names(self):
        expected = ['package_1', 'package_2', 'package_3', 'package_4']
        actual = self.package_repository.get_package_names()
        self.assertEqual(expected, actual)

    def test_it_returns_an_array_of_sources_for_a_package(self):
        expected = [
            'source-1-for-package-1',
            'source-2-for-package-1',
            'source-3-for-package-1'
        ]

        actual = self.package_repository.get_sources('package_1')
        self.assertEqual(expected, actual)

    def test_it_can_handle_empty_arrays_when_retrieving_a_source(self):
        actual = self.package_repository.get_sources('package_2')
        self.assertEqual([], actual)


if __name__ == '__main__':
    unittest.main()
