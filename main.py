import tornado.ioloop
import tornado.web
import os
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
CSS_PATH = os.path.join(ROOT_PATH, "css")
JS_PATH = os.path.join(ROOT_PATH, "js")
ASSERTS_PATH = os.path.join(ROOT_PATH, "asserts")
DEFAULT_IMAGE = "assets/img/ipad-6.png"
IMAGE_PATH = "assets/img/"
DEFAULT_FILE = "assets/_1.txt"
FILE_PATH = "assets/file/"
os.makedirs(FILE_PATH, exist_ok=True)
with open(os.path.join(ROOT_PATH,DEFAULT_FILE),"w") as f:
    f.write("empty")
data = {
    "text":"Hello world!",
    "image":DEFAULT_IMAGE,
    "file":DEFAULT_FILE
}
def remove_files(folder):
    os.system("rm -f {}".format(os.path.join(folder, "*")))
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        global data
        self.render("index.html", data=data)
class TextHandler(tornado.web.RequestHandler):
    def post(self):
        global data
        text = self.get_argument("text", "")
        if text.strip():
            data["text"]=text
        else:
            data["text"]="Hello world!"
        self.redirect("/")
class FileHandler(tornado.web.RequestHandler):
    def post(self):
        global data
        remove_files(FILE_PATH)
        file = None
        files = self.request.files.get("file")
        if files:
            file = files[0]
        reset = int(self.get_argument("reset", 0))
        if reset:
            data["file"] = DEFAULT_FILE
            data["image"] = DEFAULT_IMAGE
        else:
            if file:
                with open(os.path.join(FILE_PATH, file["filename"]), "wb") as f:
                    f.write(file["body"])
                data["file"] = os.path.join(FILE_PATH, file["filename"])
                if "image" in file["content_type"]:
                    data["image"] = data["file"]
        print(data)
        self.write({"success":1})
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/text", TextHandler),
        (r"/file", FileHandler),
        (r"^/(.*)$", tornado.web.StaticFileHandler, {"path": ROOT_PATH, "default_filename":"index.html"}),
    ],
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(5555)
    print("File transfer server.")
    tornado.ioloop.IOLoop.current().start()
