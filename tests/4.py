test = {
  'name': 'Problem 4',
  'points': 3,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 1 > 1
          138f25df9fa384871ec971c4537e4474
          # locked
          >>> 1 >= 1
          140baa19d30e3acf70c305fc604a1cc1
          # locked
          >>> 1 == -1
          138f25df9fa384871ec971c4537e4474
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> greater_than_zero(1)
          True
          >>> greater_than_zero(0)
          False
          >>> greater_than_zero(-1)
          False
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      from hw1 import greater_than_zero
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}