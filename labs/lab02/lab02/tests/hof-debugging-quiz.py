test = {
  'name': 'hof-debugging-quiz',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': '8e317fbe71aefe95b778bb5cdd7317d0',
          'choices': [
            'Nothing is wrong with the above code',
            'make_adder is missing a return statement',
            'The body of adder is not indented correctly',
            'make_adder is not passed the correct number of arguments when called'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          The following code will throw an error when run---what's wrong with it?
          >>> def make_adder(n1):
          ...     def adder(n2):
          ...         return n1 + n2
          ...
          >>> adder = make_adder(3)
          >>> adder(4)
          """
        },
        {
          'answer': '93cf6eb7347175fd0c055972d1487203',
          'choices': [
            'SyntaxError',
            'IndentationError',
            "TypeError: ... 'NoneType' object is not ...",
            'NameError'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What type of error will you see when you run the following code?
          >>> def make_adder(n1):
          ...     def adder(n2):
          ...         return n1 + n2
          ...
          >>> adder = make_adder(3)
          >>> adder(4)
          """
        },
        {
          'answer': '3cb667cd4df9a396de3b096c01c8ea29',
          'choices': [
            r"""
            >>> def make_adder(n1):
            ...     def adder(n2):
            ...         return n1 + n2
            ...
            >>> adder = make_adder(3)
            >>> adder(4)
            """,
            r"""
            >>> def make_adder(n1):
            ...     def adder(n2):
            ...         return n1 + n2
            ...     return adder(n1)
            ...
            >>> adder = make_adder(3)
            >>> adder(4)
            """,
            r"""
            >>> def make_adder(n1):
            ...     def adder(n2):
            ...         return n1 + n2
            ...     return adder
            ...
            >>> adder = make_adder(3)
            >>> adder(4)
            """,
            r"""
            >>> def make_adder(n1):
            ...     def adder(n2):
            ...         return n1 + n2
            ...
            >>> adder = make_adder(3)(4)
            >>> adder
            """
          ],
          'hidden': False,
          'locked': True,
          'question': 'Which of the following will execute without error?'
        },
        {
          'answer': '8f433bc0b97cf094615520b95d909788',
          'choices': [
            'Nothing is wrong with the above code',
            'apply_twice does not need a return statement',
            'same_arg_twice should return a pointer to apply_twice, without calling it',
            'One of the variable names is not spelled correctly when referenced'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          The following code will throw an error when run---what's wrong with it?
          >>> def same_arg_twice(f):
          ...     def apply_twice(x):
          ...         return f(x, x)
          ...     return apply_twice(x)
          ...
          >>> multiply = lambda x, y: x * y
          >>> square = same_arg_twice(multiply)
          """
        },
        {
          'answer': 'f2fd58ff50211a5f332be29495b24259',
          'choices': [
            'SyntaxError',
            'IndentationError',
            "TypeError: ... 'NoneType' object is not ...",
            'NameError'
          ],
          'hidden': False,
          'locked': True,
          'question': r"""
          What type of error will be thrown when you run the following code?
          >>> def same_arg_twice(f):
          ...     def apply_twice(x):
          ...         return f(x, x)
          ...     return apply_twice(x)
          ...
          >>> multiply = lambda x, y: x * y
          >>> square = same_arg_twice(multiply)
          """
        },
        {
          'answer': '0549c36415b2ce10ec47f0e3b6e66a77',
          'choices': [
            r"""
            >>> def same_arg_twice(f):
            ...     def apply_twice(x):
            ...         return f(x, x)
            ...     return apply_twice(x)
            ...
            >>> multiply = lambda x: x * x
            >>> square = same_arg_twice(multiply)
            """,
            r"""
            >>> def same_arg_twice(f):
            ...     def apply_twice(x):
            ...         f(x, x)
            ...     return apply_twice(x)
            ...
            >>> multiply = lambda x, y: x * y
            >>> square = same_arg_twice(multiply)
            """,
            r"""
            >>> def same_arg_twice(f):
            ...     def apply_twice(x, y):
            ...         return f(x, y)
            ...     return apply_twice(x, y)
            ...
            >>> multiply = lambda x, y: x * y
            >>> square = same_arg_twice(multiply)
            """,
            r"""
            >>> def same_arg_twice(f):
            ...     def apply_twice(x):
            ...         return f(x, x)
            ...     return apply_twice
            ...
            >>> multiply = lambda x, y: x * y
            >>> square = same_arg_twice(multiply)
            """
          ],
          'hidden': False,
          'locked': True,
          'question': 'Which of the following will execute without error?'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
