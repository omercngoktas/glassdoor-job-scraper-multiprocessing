```markdown
# Glassdoor Job Scraper

This project contains a Python application used to scrape job listing URLs from the Glassdoor website and collect job details from those listings. By using this project, you can gather job listings from Glassdoor for different states and job positions.

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

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/omercngoktas/glassdoor-job-scraper-multiprocessing.git
   ```

2. Navigate to the project directory:
   ```bash
   cd glassdoor_multiprocessing
   ```

3. Modify the `main.py` file to set the cities and job positions you're interested in.

4. Run the code:
   ```bash
   python main.py
   ```

## Usage

When you download the project, you will notice a file named 'states.csv' in it. This file contains all the states in the United States. You have the flexibility to remove or add more states or cities as needed.

First, run the 'get_links_multiprocessing.py' file to collect all the job listing links for the specified states or cities. After executing 'get_links_multiprocessing.py,' proceed to run 'merge_links.py' to consolidate all the collected links into a single file named 'links_merged.csv.'

Finally, execute 'get_jobs.py' to retrieve all the job data. It's important to note that this project leverages the multiprocessing library, allowing multiple pages to be processed simultaneously. You can monitor the progress directly from the command line.

## Contributing

If you would like to contribute to this project, please check the CONTRIBUTING.md file and create a pull request for your contributions.

## Contact

If you have any questions or feedback, please feel free to contact us at [omercngoktas@gmail.com](mailto:omercngoktas@gmail.com).
