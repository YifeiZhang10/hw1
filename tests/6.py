test = {
  'name': 'Problem 6',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
            >>> print_n(5)
            5
            4
            3
            2
            1
            0
            >>> print_n(-1)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      from hw1 import print_n
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
