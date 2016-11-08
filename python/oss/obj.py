import math
import cmath
import numpy as np
import psutil
import sys
import warnings
import concurrent.futures
import pdb

from astropy import units
from astropy.coordinates import SkyCoord

import astroquery.exceptions
from astroquery.alfalfa import Alfalfa
from astroquery.alma import Alma
from astroquery.ned import Ned
from astroquery.ogle import Ogle
from astroquery.simbad import Simbad
from astroquery.ukidss import Ukidss
from astroquery.vizier import Vizier
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from astroquery.sdss import SDSS

try:
    import oss.exceptions
except ImportError:
    print 'oss is not setup. Setup oss by sourcing bin/setup.sh'
    sys.exit(1)

Simbad.add_votable_fields(
    'dimensions', 'fluxdata(filtername)', 'measurements', 'propermotions', 'morphtype', 'sptype'
)


class obj(object):
    """!
    \brief Class to represent all information about a given astronomical object
    """

    _services = [
        'Alfalfa', 'Alma', 'Ned', 'Ogle', 'SDSS', 'Simbad', 'Ukidss', 'Vizier'
    ]
    _workers = min(len(_services), psutil.cpu_count(logical=True))

    def __init__(self, coordinates=None, radius=5*units.arcsec):
        """!
        \brief Initialize an astronomical object by finding references to the object in all services
        """
        if not coordinates:
            raise oss.exceptions.OSSLookupError('OSSLookuperror: Coordinates not supplied'
                                                ' - cannot lookup object!')
        else:
            self.coordinates = coordinates
            self.radius = radius
            with concurrent.futures.ThreadPoolExecutor(self._workers) as donovan:
                donovan.map(self._query_service, self._services)

    def _query_service(self, service):
        try:
            setattr(self, service, eval(service + '.query_region(self.coordinates, radius=self.radius)'))
        except Exception as Err:
            setattr(self, service, Err)
            if service == 'Irsa':
                pdb.set_trace()
