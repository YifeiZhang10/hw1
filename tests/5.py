test = {
  'name': 'Problem 5',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> a_mod_b(10, 5)
          581086b6b29789659effb7a5da0bfb0f
          # locked
          >>> a_mod_b(5, 2)
          feedd0295d99780b4515739c7fc5de8a
          # locked
          >>> a_mod_b(2, 5)
          0e848c28f96df07c693ef539595d4380
          # locked
          >>> a_mod_b(-3, -10)
          7faf28633070d85d165508918dd58875
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> a_mod_b(10, 5)
          0
          >>> a_mod_b(5, 2)
          1
          >>> a_mod_b(2, 5)
          2
          >>> a_mod_b(-3, -10)
          -3
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      from hw1 import a_mod_b
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
