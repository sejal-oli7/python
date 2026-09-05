import json

from scraper.models import Job


def save_jobs(jobs: list[Job], filename: str) -> None:
    """
    Save job listings to a JSON file.
    """

    # Convert Job objects into dictionaries
    job_data = [job.to_dict() for job in jobs]

    # Open the file for writing
    with open(filename, "w", encoding="utf-8") as file:

        # Write job data as formatted JSON
        json.dump(job_data, file, indent=4, ensure_ascii=False)
