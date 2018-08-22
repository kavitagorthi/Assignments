def add(*args):
    """ Returns a STRING with the sum of the arguments """
    try:
        total = sum(map(int, args))
    except ValueError:
        return "Please enter numeric values for addition"
    return str(total)


def multiply(*args):
    try:
        total = int(args[0]) * int(args[1])
    except ValueError:
        return "Please enter numeric values for multiplication"
    return str(total)


def subtract(*args):
    try:
        total = int(args[0]) - int(args[1])
    except ValueError:
        return "Please enter numeric values for difference"
    return str(total)


def divide(*args):
    try:
        total = int(args[0]) / int(args[1])
    except ValueError:
        return "Please enter numeric values for division"
    except ZeroDivisionError:
        return "ZeroDivisionError: Please provide number except zero"
    return str(total)


def resolve_path(path):
    """
    Should return two values: a callable and an iterable of
    arguments.
    """
    funcs = {
        '': front_page,
        'add': add,
        'multiply': multiply,
        'divide': divide,
        'subtract': subtract,
    }
    path = path.strip('/').split('/')
    func_name = path[0]
    args = path[1:]
    try:
        func = funcs[func_name]
    except KeyError:
        raise NameError
    return func, args


def application(environ, start_response):

    headers = [('Content-type', 'text/html')]
    try:
        path = environ.get('PATH_INFO', None)
        if path is None:
            raise NameError
        func, args = resolve_path(path)
        body = func(*args)
        status = "200 OK"
    except NameError:
        status = "404 Not Found"
        body = "<h1>Not Found</h1>"
    except Exception:
        status = "500 Internal Server Error"
        body = "<h1>Internal Server Error</h1>"
        print(traceback.format_exc())
    finally:
        headers.append(('Content-length', str(len(body))))
        start_response(status, headers)
        return [body.encode('utf8')]


if __name__ == '__main__':

    from wsgiref.simple_server import make_server

    srv = make_server('localhost', 8080, application)
    srv.serve_forever()