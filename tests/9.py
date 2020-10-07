test = {
  'name': 'Problem 9',
  'points': 10,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
            >>> gcd(0, 0)
            581086b6b29789659effb7a5da0bfb0f
            # locked
            >>> gcd(3, 4)
            feedd0295d99780b4515739c7fc5de8a
            # locked
            >>> gcd(9, 6)
            287ada61eabab45481c038d336cec0d9
            # locked
            >>> gcd(10, 2)
            0e848c28f96df07c693ef539595d4380
            # locked
            >>> gcd(-5, 15)
            2a2c5c11d76ef6a196697fa556ae3a0d
            # locked
          """,
          'hidden': False,
          'locked': True
        },{
          'code': r"""
            >>> gcd(0, 0)
            0
            # locked
            >>> gcd(3, 4)
            1
            # locked
            >>> gcd(9, 6)
            3
            # locked
            >>> gcd(10, 2)
            2
            # locked
            >>> gcd(-5, 15)
            5
            # locked
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      from hw1 import gcd
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
