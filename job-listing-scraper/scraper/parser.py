from bs4 import BeautifulSoup

from scraper.models import Job


def parse_jobs(html: str) -> list[Job]:
    """
    Parse HTML content and extract job listings.
    """

    # Convert HTML content into a BeautifulSoup object
    soup = BeautifulSoup(html, "html.parser")

    # Store all extracted jobs
    jobs = []

    # Find every job card
    for job_card in soup.select(".job-card"):

        # Find each job field
        title = job_card.select_one(".job-title")
        company = job_card.select_one(".company")
        location = job_card.select_one(".location")
        job_type = job_card.select_one(".job-type")
        salary = job_card.select_one(".salary")

        # Extract text from each HTML element
        title_text = title.get_text(strip=True) if title else ""
        company_text = company.get_text(strip=True) if company else ""
        location_text = location.get_text(strip=True) if location else ""
        job_type_text = job_type.get_text(strip=True) if job_type else ""
        salary_text = salary.get_text(strip=True) if salary else ""

        # Create a Job object
        job = Job(
            title=title_text,
            company=company_text,
            location=location_text,
            job_type=job_type_text,
            salary=salary_text,
            posted_date="",
            url="",
        )

        # Add the job to the jobs list
        jobs.append(job)

    # Return all extracted jobs
    return jobs
