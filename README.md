```markdown
# Glassdoor Job Scraper

This project contains a Python application used to scrape job listing URLs from the Glassdoor website and collect job details from those listings. By using this project, you can gather job listings from Glassdoor for different states and job positions.

# Glassdoor Job Scraper Output

This project generates an output file, `output.csv`, which contains job listing data collected from Glassdoor. The following are the columns you can expect to find in the `output.csv` file along with their descriptions:
- **Company Name**: The name of the company that posted the job listing.
- **Rating**: The rating of the company as available on Glassdoor, if provided.
- **Location**: The location or city where the job is located.
- **Job Title**: The title of the job listing.
- **Estimated Salary**: An estimate of the salary associated with the job, if available.
- **Job Description**: A description of the job listing, including responsibilities and requirements.
- **Number of Employees**: The approximate number of employees in the hiring company, if available.
- **Founded**: The year the company was founded, if available.
- **Sector**: The sector or industry category of the hiring company, if available.
- **Industry**: The specific industry of the hiring company, if available.
- **Revenue**: The revenue range of the hiring company, if available.
- **Keyword**: The keyword or search term used to retrieve the job listing.
Please note that the availability of certain information, such as company rating or estimated salary, may vary depending on the job listing on Glassdoor. This data is collected directly from the Glassdoor website during the scraping process.

## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need the following requirements to run the project:

- Python (version 3.x)
- Selenium (version 4.11.x)
- Pandas
- Chrome WebDriver

You can install the required Python packages using the following command:


```bash
pip install selenium pandas
```

```bash
pip install selenium pandas
```


### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/omercngoktas/glassdoor-job-scraper-multiprocessing.git
   ```

2. Navigate to the project directory:
   ```bash
   cd glassdoor-job-scraper-multiprocessing
   ```

3. Modify the `main.py` file to set the cities and job positions you're interested in.

4. Run the code:
   ```bash
   python retrieve_links.py
   python merge_links.py
   python get_jobs.py
   ```

## Usage

When you download the project, you will notice a file named 'states.csv' in it. This file contains all the states in the United States. You have the flexibility to remove or add more states or cities as needed.

First, run the 'get_links_multiprocessing.py' file to collect all the job listing links for the specified states or cities. After executing 'get_links_multiprocessing.py,' proceed to run 'merge_links.py' to consolidate all the collected links into a single file named 'links_merged.csv.'

Finally, execute 'get_jobs.py' to retrieve all the job data. It's important to note that this project leverages the multiprocessing library, allowing multiple pages to be processed simultaneously. You can monitor the progress directly from the command line.

## Contributing

If you would like to contribute to this project, please check the CONTRIBUTING.md file and create a pull request for your contributions.

## Contact

If you have any questions or feedback, please feel free to contact us at [omercngoktas@gmail.com](mailto:omercngoktas@gmail.com).
