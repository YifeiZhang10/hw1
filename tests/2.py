test = {
  'name': 'Problem 2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = 's'
          >>> x
          's'
          >>> y = x*3
          >>> y
          db829575de1a8422962440bdccfd0cd8
          # locked
          >>> z = x + x + x
          >>> z
          db829575de1a8422962440bdccfd0cd8
          # locked
          >>> z == y
          140baa19d30e3acf70c305fc604a1cc1
          # locked
          >>> z is y
          138f25df9fa384871ec971c4537e4474
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> seal_goes('ow ')
          'ow ow ow '
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      from hw1 import seal_goes
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}

