from flask import Flask, app, render_template, request
from Script import Scraper

app = Flask(__name__)


# default route
@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/search", methods=["GET"])  # pyright: ignore
def search():
    if request.method == "GET":
        search = request.args.get("search_item")

        scraper = Scraper(search)
        scraper.scrape()

        return render_template(
            "search.html",
            companies=scraper.companies,
            skills_cmp=scraper.skills_cmp,
            posted_dates=scraper.posted_dates,
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5555)
