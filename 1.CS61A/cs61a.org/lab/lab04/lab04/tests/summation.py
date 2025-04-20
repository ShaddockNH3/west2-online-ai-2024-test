test = {
  'name': 'summation',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
          225
          >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
          54
          >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
          62
          >>> # Do not use while/for loops!
          >>> from construct_check import check
          >>> # ban iteration
          >>> check(HW_SOURCE_FILE, 'summation',
          ...       ['While', 'For'])
          True
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
