

from scraper.models import Job


job = Job(
    title="Python Intern",
    company="ABC Technologies",
    location="Kathmandu",
    job_type="Internship",
    salary="NPR 15,000",
    posted_date="2 days ago",
    url="https://example.com/python-intern",
)

print(job)
print()
print(job.to_dict())
