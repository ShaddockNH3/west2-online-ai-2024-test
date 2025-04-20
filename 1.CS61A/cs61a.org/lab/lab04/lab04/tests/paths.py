test = {
  'name': 'paths',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> paths(2, 2)
          2
          >>> paths(5, 7)
          210
          >>> paths(117, 1)
          1
          >>> paths(1, 157)
          1
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
