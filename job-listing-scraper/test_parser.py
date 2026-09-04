from scraper.parser import parse_jobs


# यो एउटा sample HTML हो।
# वास्तविक website बाट आएको HTML जस्तै मानेका छौँ।
html = """
<div class="job-card">
    <h2 class="job-title">Python Developer</h2>
    <p class="company">ABC Tech</p>
    <p class="location">Kathmandu</p>
</div>

<div class="job-card">
    <h2 class="job-title">Backend Developer</h2>
    <p class="company">XYZ Solutions</p>
    <p class="location">Pokhara</p>
</div>
"""


# HTML लाई parser function मा पठाउने
jobs = parse_jobs(html)


# Parser ले निकालेका jobs हेर्ने
for job in jobs:
    print(job)
    print(job.to_dict())
    print()
