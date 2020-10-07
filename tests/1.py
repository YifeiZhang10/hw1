test = {
  'name': 'Problem 1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = 'i am returned'
          >>> x
          f8101e82dda01aeb5d0d8a47ad838730
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> cat_goes()
          'meow'
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      from hw1 import cat_goes
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}