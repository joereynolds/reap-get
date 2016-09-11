import unittest
import sys


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
                ],
                'type': 'instrument',
                'os': 'linux'
            },
            {
                'name': 'package_2',
                'sources': [],
                'type': 'effect',
                'os': 'windows'
            },
            {
                'name': 'package_3',
                'sources': [
                    'source-1-for-package-3'
                ],
                'type': 'instrument',
                'os': 'windows'
            },
            {
                'name': 'package_4',
                'sources': [],
                'type': 'effect',
                'os': 'windows'
            },
        ]


        self.package_repository = package_repository.PackageRepository(test_json)

    def test_it_returns_an_array_of_package_names(self):
        expected = ['package_1', 'package_2', 'package_3', 'package_4']
        actual = self.package_repository.get_properties('name')
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

    def test_it_can_filter_by_a_provided_key(self):
        expected_os_filter = [
            {
                'name': 'package_2',
                'sources': [],
                'type': 'effect',
                'os': 'windows'
            },
            {
                'name': 'package_3',
                'sources': [
                    'source-1-for-package-3'
                ],
                'type': 'instrument',
                'os': 'windows'
            },
            {
                'name': 'package_4',
                'sources': [],
                'type': 'effect',
                'os': 'windows'
            }
        ]

        expected_type_filter = [
            {
                'name': 'package_1',
                'sources': [
                    'source-1-for-package-1',
                    'source-2-for-package-1',
                    'source-3-for-package-1'
                ],
                'type': 'instrument',
                'os': 'linux'
            },
            {
                'name': 'package_3',
                'sources': [
                    'source-1-for-package-3'
                ],
                'type': 'instrument',
                'os': 'windows'
            }
        ]

        actual_type_filter = self.package_repository.filter_where('type', 'instrument')
        actual_os_filter = self.package_repository.filter_where('os', 'windows')

        self.assertEqual(expected_os_filter, actual_os_filter)
        self.assertEqual(expected_type_filter, actual_type_filter)




if __name__ == '__main__':
    unittest.main()
