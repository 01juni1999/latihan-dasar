# exc must be exception instance or None.
raise RuntimeError from exc
def func():
    raise ConnectionError
try:
    func()
except ConnectionError as exc:


    open('database.sqlite')
except OSError:
        raise RuntimeError from None