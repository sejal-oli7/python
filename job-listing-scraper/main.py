from scraper.scraper import fetch_page
from scraper.parser import parse_jobs
from scraper.storage import save_jobs


URL = "https://example.com"
OUTPUT_FILE = "data/jobs.json"


def main():
    # Fetch HTML from the webpage
    html = fetch_page(URL)

    # Parse job listings from HTML
    jobs = parse_jobs(html)

    # Save parsed jobs to a JSON file
    save_jobs(jobs, OUTPUT_FILE)

    # Display the number of jobs saved
    print(f"Saved {len(jobs)} jobs to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()