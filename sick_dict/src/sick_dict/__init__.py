class SickDict(dict):
    """An IDE friendly dictionary"""

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        if args:
            for arg in args:
                # Invalid case - if arg is not a dict
                if not isinstance(arg, dict):
                    raise TypeError("The argument passed must be a dict")

                # If valid, loop
                self.__loop_dict(arg)

        if kwargs:
            self.__loop_dict(kwargs)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return str(self.__dict__)

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super().__delitem__(key)
        del self.__dict__[key]

    def __loop_dict(self, my_dict):
        """Loop and set attributes in SickDict format"""
        for k, v in my_dict.items():
            if isinstance(v, dict):
                v = SickDict(v)
            if isinstance(v, list):
                self.__convert(v)
            setattr(self, k, v)

    def __convert(self, v):
        """Convert the list of dicts to the SickDict format"""
        for elem in range(0, len(v)):
            if isinstance(v[elem], dict):
                v[elem] = SickDict(v[elem])
            elif isinstance(v[elem], list):
                self.__convert(v[elem])

    def _as_dict(self):
        """Return the object in dictionary format"""
        return self.__dict__
