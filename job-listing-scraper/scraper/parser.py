from bs4 import BeautifulSoup

from scraper.models import Job


def parse_jobs(html: str) -> list[Job]:
    """
    HTML content बाट job listings निकाल्छ।
    """

    soup = BeautifulSoup(html, "html.parser")

    jobs = []

    # प्रत्येक job listing खोज्ने
    for job_card in soup.select(".job-card"):
        title = job_card.select_one(".job-title")
        company = job_card.select_one(".company")
        location = job_card.select_one(".location")

        # यदि कुनै field भेटिएन भने empty string राख्ने
        title_text = title.get_text(strip=True) if title else ""
        company_text = company.get_text(strip=True) if company else ""
        location_text = location.get_text(strip=True) if location else ""

        job = Job(
            title=title_text,
            company=company_text,
            location=location_text,
            job_type="",
            salary="",
            posted_date="",
            url="",
        )

        jobs.append(job)

    return jobs
