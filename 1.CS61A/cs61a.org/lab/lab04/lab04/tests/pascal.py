test = {
  'name': 'pascal',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> pascal(0, 0)    # The top left (the point of the triangle)
          1
          >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
          0
          >>> pascal(3, 2)	# Row 3 (1 3 3 1), Column 2
          3
          >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
          6
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from lab04 import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
