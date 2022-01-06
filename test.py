import time

from apm import agent


def method1():
    time.sleep(20)
    return '1'


def method2():
    time.sleep(22)
    return method1()


def method3():
    time.sleep(0.2)
    return method2()


if __name__ == '__main__':
    # agent.start()

    import socketserver
    from http.server import BaseHTTPRequestHandler

    class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

        def do_POST(self):
            method3()
            time.sleep(0.5)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write('{"song": "Despacito", "artist": "Luis Fonsi"}'.encode('ascii'))

    PORT = 19090
    Handler = SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()


# import os
# import threading
# import time
# import psutil
#
#
# def thread_count():
#     # pps = psutil.Process(os.getpid())
#     # print(pps.children())
#     # print(threading.active_count())
#     # threading.currentThread().
#
#     for thread in threading.enumerate():
#         print(thread.name)
#         print(thread.isDaemon())
#         print(thread.is_alive())
#
#
# T1 = threading.Thread(target=(lambda x: time.sleep(x)), args=(1000,))
# T2 = threading.Thread(target=(lambda x: time.sleep(x)), args=(1000,))
# T3 = threading.Thread(target=thread_count)
#
# # change T to daemon
# T1.setDaemon(True)
#
# # starting of Thread T
# T2.start()
# T1.start()
# T3.start()
