'''
kavita.kent@Evergreen MINGW64 ~/desktop/6assignement (master)
$ coverage run test.py
..........
----------------------------------------------------------------------
Ran 10 tests in 0.016s

OK
This is the unit test results


kavita.kent@Evergreen MINGW64 ~/desktop/6assignement (master)
$ coverage run integrationtest.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.016s

OK
This is integration test results


kavita.kent@Evergreen MINGW64 ~/desktop/6assignement (master)
$ coverage report -m
Name                 Stmts   Miss  Cover   Missing
--------------------------------------------------
controller.py           13      0   100%
decider.py              21      7    67%   53, 57, 61, 65, 67, 71, 73
integrationtest.py      26      0   100%
pump.py                 19      8    58%   35-42, 49-50
sensor.py                8      2    75%   30-31
--------------------------------------------------
TOTAL                   87     17    80%



'''