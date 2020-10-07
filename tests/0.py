test = {
  'name': 'Problem 0',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print('i am printed')
          7f8e4541f10861f7d9096c4e864144e8
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> dog_goes()
          woof
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      from hw1 import dog_goes
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
