from bs4 import BeautifulSoup

from scraper.models import Job


def parse_jobs(html: str) -> list[Job]:
    """
    HTML content bata  job listings nikalxa
    """

    soup = BeautifulSoup(html, "html.parser")

    jobs = []

    # harek job card khojni 
    for job_card in soup.select(".job-card"):

        # Job  fields khojni
        title = job_card.select_one(".job-title")
        company = job_card.select_one(".company")
        location = job_card.select_one(".location")
        job_type = job_card.select_one(".job-type")

        # Text nikalxa
        title_text = title.get_text(strip=True) if title else ""
        company_text = company.get_text(strip=True) if company else ""
        location_text = location.get_text(strip=True) if location else ""
        job_type_text = job_type.get_text(strip=True) if job_type else ""

        # Job object banauxa 
        job = Job(
            title=title_text,
            company=company_text,
            location=location_text,
            job_type=job_type_text,
            salary="",
            posted_date="",
            url="",
        )

        jobs.append(job)

    return jobs
