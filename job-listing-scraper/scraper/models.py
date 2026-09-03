from dataclasses import dataclass


@dataclass
class Job:
    title: str
    company: str
    location: str
    job_type: str
    salary: str
    posted_date: str
    url: str

    def to_dict(self):
        return {
            "title": self.title,
            "company": self.company,
            "location": self.location,
            "job_type": self.job_type,
            "salary": self.salary,
            "posted_date": self.posted_date,
            "url": self.url,
        }