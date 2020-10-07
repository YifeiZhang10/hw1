test = {
  'name': 'Problem 7',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 2 ** 3
          671ed54989b8b2d016a764f4eb59e6f8
          # locked
          >>> sumofsquares(-1)
          581086b6b29789659effb7a5da0bfb0f
          # locked
          >>> sumofsquares(2)
          2a2c5c11d76ef6a196697fa556ae3a0d
          # locked
          """,
          'hidden': True,
          'locked': True
        },{
          'code': r"""
          >>> sumofsquares(-2)
          0
          >>> sumofsquares(2)
          5
          >>> sumofsquares(10)
          385
          """,
          'hidden': True,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      from hw1 import sumofsquares
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
