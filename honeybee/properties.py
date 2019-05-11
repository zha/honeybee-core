"""Face Properties."""


class Types(object):
    """Face types."""

    def __init__(self):
        pass

    @property
    def wall(self):
        return 'Wall'

    @property
    def roof_ceiling(self):
        return 'RoofCeiling'

    @property
    def floor(self):
        return 'Floor'

    @property
    def airwall(self):
        return 'AirWall'

    @property
    def shading(self):
        return 'Shading'

    def __contains__(self, value):
        return value in ['Wall', 'RoofCeiling', 'Floor', 'AirWall', 'Shading']


class Properties(object):
    """Geometry Properties.

    Base class for geometry properties. This class will be extended by plugins.

    prop = Properties(srf_type)
    prop.radiance -> RadianceProperties
    prop.energy -> EnergyProperties
    """
    TYPES = Types()

    # TODO(): face_type should be required. I will update this after Face class is
    # updated to support type based on normal direction.
    def __init__(self, face_type=None):
        self.face_type = face_type or self.TYPES.wall

    @property
    def face_type(self):
        """Get and set Surface Type."""
        return self._face_type

    @face_type.setter
    def face_type(self, value):
        assert value in self.TYPES, '{} is not a valid type.'.format(value)
        self._face_type = value

    def ToString(self):
        """Overwrite .NET ToString method."""
        return self.__repr__()

    def __repr__(self):
        """Properties representation."""
        return 'FaceProperties:%s' % str(self.face_type)