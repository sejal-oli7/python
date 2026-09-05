from scraper.parser import parse_jobs


# Sample HTML for testing the parser
html = """
<div class="job-card">
    <h2 class="job-title">Python Developer</h2>
    <p class="company">ABC Tech</p>
    <p class="location">Kathmandu</p>
    <p class="job-type">Full-time</p>
    <p class="salary">Rs. 50,000</p>
</div>

<div class="job-card">
    <h2 class="job-title">Backend Developer</h2>
    <p class="company">XYZ Solutions</p>
    <p class="location">Pokhara</p>
    <p class="job-type">Remote</p>
    <p class="salary">Rs. 60,000</p>
</div>
"""


# Parse the sample HTML
jobs = parse_jobs(html)


# Check the number of jobs
assert len(jobs) == 2

# Check the first job
assert jobs[0].title == "Python Developer"
assert jobs[0].company == "ABC Tech"
assert jobs[0].location == "Kathmandu"
assert jobs[0].job_type == "Full-time"
assert jobs[0].salary == "Rs. 50,000"

# Check the second job
assert jobs[1].title == "Backend Developer"
assert jobs[1].company == "XYZ Solutions"
assert jobs[1].location == "Pokhara"
assert jobs[1].job_type == "Remote"
assert jobs[1].salary == "Rs. 60,000"


print("All parser tests passed!")