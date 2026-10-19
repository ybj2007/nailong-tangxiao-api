"""A tiny fake API that serves a single piece of character art."""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import argparse
import os


ART = r"""              __..---..__
         _.-''  _   _   ''-._
       .'      (o) (o)      '.
      /      .-._   _.-.      \
     |      /  _ `-' _  \      |
     |      | ( `-._-' ) |      |
     |      \  `-...-'  /      |
      \       `-.___.-'       /
       `-._    /|___|\    _.-'
         / `--/ |   | \--' \
       _/   _/  |___|  \_   \_
     .'___.'   /     \   '.___`.
              /  ___  \
             (__(   )__)
"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.split("?", 1)[0] not in ("/", "/api/nailong"):
            self.send_error(404)
            return

        body = ART.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)


def main():
    parser = argparse.ArgumentParser(description="Fake 奶龙唐笑 character-art API")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", "8000")))
    args = parser.parse_args()

    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"Serving at http://{args.host}:{server.server_port}/api/nailong")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
