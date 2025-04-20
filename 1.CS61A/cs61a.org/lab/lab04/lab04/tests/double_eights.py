test = {
  'name': 'double_eights',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> double_eights(1288)
          True
          >>> double_eights(880)
          True
          >>> double_eights(538835)
          True
          >>> double_eights(284682)
          False
          >>> double_eights(588138)
          True
          >>> double_eights(78)
          False
          >>> from construct_check import check
          >>> # ban iteration
          >>> check(HW_SOURCE_FILE, 'double_eights', ['While', 'For'])
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
