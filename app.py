import web

urls = (
    "/","google_books.index.Index"
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()