class Stream(object):
    """A lazily computed recursive list."""

    class empty(object):
        def __repr__(self):
            return 'Stream.empty'

    empty = empty()

    def __init__(self, first, compute_rest=lambda: empty):
        assert callable(compute_rest), 'compute_rest must be callable.'
        self.first = first
        self._compute_rest = compute_rest
        self._rest = None

    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest

    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))

    def __iter__(self):
        """Return an iterator over the elements in the stream.
        >>> s = make_integer_stream(1) # [1, 2, 3, 4, 5, ...]
        >>> list(zip(range(6), s))
        [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
        """
        def generator(stream):
            while stream != Stream.empty:
                yield stream.first
                stream = stream.rest
        return generator(self)
                
    def __getitem__(self, k):
        """Return the k-th element of the stream.
        >>> s = make_integer_stream(5)
        >>> s[0]
        5
        >>> s[1]
        6
        >>> [s[i] for i in range(7,10)]
        [12, 13, 14]
        """
       
        if k == 0:
            return self.first
        return self.rest[k-1]
