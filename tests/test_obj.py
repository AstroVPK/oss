import unittest
import pdb

import astropy.table.table
from astropy import units
from astropy.coordinates import SkyCoord
import astroquery.exceptions

import oss.obj


class TestMakeObject(unittest.TestCase):

    def test_createNewObjErr(self):
        with self.assertRaises(oss.exceptions.OSSLookupError):
            badObj = oss.obj.obj()

    def test_createNewObj(self):
        coordinates = SkyCoord(ra=10.625*units.degree, dec=41.2*units.degree, frame='icrs')
        newObj = oss.obj.obj(coordinates=coordinates)
        self.assertIsNone(newObj.Alfalfa)
        self.assertIsInstance(newObj.Alma, astropy.table.table.Table)
        self.assertIsInstance(newObj.Ned, astropy.table.table.Table)
        self.assertIsInstance(newObj.Simbad, astroquery.exceptions.TableParseError)
        self.assertIsInstance(newObj.Vizier, astroquery.utils.commons.TableList)
        pdb.set_trace()

if __name__ == "__main__":
    unittest.main()
