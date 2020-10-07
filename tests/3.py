test = {
  'name': 'Problem 3',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': '057757fced8c220abf41b4addd3943ec',
          'choices': [
            'if',
            'and',
            'int',
            'while'
          ],
          'hidden': False,
          'locked': True,
          'question': 'Which of the following is NOT a python **keyword**?'
        },

      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [

        {
          'code': r"""
          >>> levioSA('leviOsa')
          True
          >>> levioSA('levioSA')
          False
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      from hw1 import levioSA
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}