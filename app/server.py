import sys
from adapter import http

command_map = {
    'http_adapter': http.run_dev_server,    # for develop test use
}

def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        func = command_map.get(command)
        if func:
            return func()

    print_hint()

def print_hint():
    print('Please provide which one you want to start.')
    print('Options:')
    print('        http_adapter                       (start adapter to serve http flask for develop test)')

if __name__ == "__main__":
    main()

# in prod, http start by uwsgi with `http_app`
else:
    http_app = http.get_app()