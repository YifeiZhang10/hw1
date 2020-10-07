test = {
  'name': 'Problem 8',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 1 % 2 == 1
          140baa19d30e3acf70c305fc604a1cc1
          # locked
          >>> 4 % 2 == 0
          140baa19d30e3acf70c305fc604a1cc1
          # locked
          >>> sumofodd(3)
          f970de4b11828bffd6138ddf36454ecf
          # locked
          """,
          'hidden': False,
          'locked': True
        },{
          'code': r"""
          >>> sumofodd(-2)
          0
          >>> sumofodd(2)
          1
          >>> sumofodd(5)
          9
          >>> sumofodd(11)
          36
          >>> sumofodd(10)
          25
          """,
          'hidden': True,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      from hw1 import sumofodd
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
