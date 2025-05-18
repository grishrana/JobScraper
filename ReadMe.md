# **Job Scrapper**
JobScraper is a simple web application built with Flask that scrapes job postings from **TimesJobs** based on user-input keywords such as skills or designations. It displays relevant job listings including the company name, required skills, and the date posted.

---

## Features

- Search for jobs by skill or designation.
- Scrapes real-time job data from [timesjobs.com](https://www.timesjobs.com).
- Displays company names, required skills, and post dates.
- Built with Flask and BeautifulSoup.
- Clean, responsive HTML templates using Jinja2.

---

##  Requirements

- Python 3.7+
- Flask
- requests
- beautifulsoup4
- lxml

Install them via:

```bash
pip install -r requirements.txt
```

##  How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/JobScraper.git
cd JobScraper
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Flask app:

```bash
python app.py
```

5. Visit in your browser:
`http://127.0.0.1:5555`

## Contribute
Fork the repo create changes and then create a pull request
