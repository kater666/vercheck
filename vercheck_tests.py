import unittest
import vercheck
from ddt import ddt, data


@ddt
class VercheckTests(unittest.TestCase):

    def test_read_requirements(self):
        vercheck_list = vercheck.read_requirements('unittest.txt')
        test_list = [('pbr', '1.9.1'), ('mod-wsgi-httpd', '2.4.12.6'), ('selenium', '2.53.1'),
                     ('virtualenv-clone', '0.2.6')]
        self.assertEqual(vercheck_list, test_list)

    @data([('ddt', '1.0.1'), ('django', '1.9.5'), ('pbr', '1.9.1')],
          [('six', '1.10.0'), ('selenium', '2.53.1'), ('virtualenv-clone', '0.2.6')])
    def test_existence_and_version_of_required_modules(self, data):
        vercheck.check_libs(data)
        for i in vercheck.required_modules:
            self.assertTrue(i.req_version)
            self.assertTrue(i.exists)
            self.assertEqual(i.req_version, i.version)
            for j in data:
                self.assertEqual(i.name, j[0])

    @data([('non_existing_module', '1.0.1'), ('some_crap', '1.9.5'), ('I_like_trains', '1.9.1')],
          [('menel', '1.10.0'), ('mariusz', '2.53.1'), ('lubi_piwo', '0.2.6')])
    def test_non_existing_modules(self, data):
        vercheck.check_libs(data)
        for i in data:
            for j in vercheck.required_modules:
                if i[0] == j.name:
                    self.assertFalse(j.exists)
                    self.assertFalse(j.up_to_date)
                    self.assertEqual(j.version, None)


    '''
    @data([('ddt', '99.0.1'), ('django', '199.9.5'), ('pbr', '199.9.1'),
          ('six', '991.10.0'), ('selenium', '992.53.1'), ('virtualenv-clone', '990.2.6')])
    def test_existing_not_up_to_date_module(self, data):
        vercheck.check_libs(data)
        #for i in vercheck.required_modules:
            #print(i.name, i.req_version, i.exists, i.up_to_date)
        for i in data:
            for j in vercheck.required_modules:
                if i[0] == j.name:
                    pass
    # This test is fucked up.
    # It uses data from the first test case and data from itself.
    #
    '''

if __name__ == "__main__":
    unittest.main()

'''
[stevedore 1.12.0 (/usr/local/lib/python3.4/dist-packages), Django 1.9.5
(/usr/local/lib/python3.4/dist-packages), virtualenv 15.0.1 (/usr/local/lib/python3.4/dist-packages),
virtualenvwrapper 4.7.1 (/usr/local/lib/python3.4/dist-packages),
mod-wsgi-httpd 2.4.12.6 (/usr/local/lib/python3.4/dist-packages),
django-contrib-comments 1.7.0 (/usr/local/lib/python3.4/dist-packages),
pbr 1.9.1 (/usr/local/lib/python3.4/dist-packages),
six 1.10.0 (/usr/local/lib/python3.4/dist-packages),
ddt 1.0.1 (/usr/local/lib/python3.4/dist-packages),
selenium 2.53.1 (/usr/local/lib/python3.4/dist-packages),
virtualenv-clone 0.2.6 (/usr/local/lib/python3.4/dist-packages)]
'''

