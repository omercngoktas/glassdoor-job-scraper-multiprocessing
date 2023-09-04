import multiprocessing
import pandas as pd
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_details(driver, selector_value, timeout=3, locator_type=By.XPATH):
    try:
        return WebDriverWait(driver=driver, timeout=timeout).until(
            EC.presence_of_element_located((locator_type, selector_value))
        ).text
    except:
        return None

def get_job_details(url, location="Texas", keyword="Data Scientist"):
    df = pd.DataFrame(columns=[ "Company name", "Rating", "Location", "Job title",
                                "Estimated salary", "Job description",
                                "Number of employees", "Founded", "Sector",
                                "Industry", "Revenue", "Keyword"])
    
    selector_company_detail = '//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]/div'
    selector_rating = '//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]/div/span'
    selector_job_title = '//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]'
    selector_job_location = '//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]'
    selector_estimated_salary = '//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[4]/span'
    selector_job_description = 'JobDescriptionContainer'
    selector_company_size = '//*[@id="EmpBasicInfo"]/div[1]/div/div[1]/span[2]'
    selector_founded = '//*[@id="EmpBasicInfo"]/div[1]/div/div[2]/span[2]'
    selector_company_type = '//*[@id="EmpBasicInfo"]/div[1]/div/div[3]/span[2]'
    selector_industry = '//*[@id="EmpBasicInfo"]/div[1]/div/div[4]/span[2]'
    selector_sector = '//*[@id="EmpBasicInfo"]/div[1]/div/div[5]/span[2]'
    selector_revenue = '//*[@id="EmpBasicInfo"]/div[1]/div/div[6]/span[2]'
    no_found_text = "Your search for data scientist in United States does not match any open jobs. Don't worry, we can still help. Below, please find related information to help you with your job search.".lower()
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    
    timeout = 2
    time_out_2 = 15
    
    for i in range(2):
        try:
            WebDriverWait(driver=driver, timeout=time_out_2).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'selected'))
            ).click()
            time.sleep(5)
        except:
            pass
        
        try:
            WebDriverWait(driver=driver, timeout=time_out_2).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="LoginModal"]/div/div/div/div[2]/button'))
            ).click()
            time.sleep(5)
        except:
            pass
    
    # fetching job list to loop in
    job_list = WebDriverWait(driver, time_out_2).until(
        EC.presence_of_all_elements_located((By.XPATH, '//li[@class="react-job-listing css-108gl9c eigr9kq3"]/div/div/a/div/div[2]'))
    )
    count = 0
    
    total_no_of_job_found = WebDriverWait(driver, time_out_2).until(
        EC.presence_of_element_located((By.XPATH, '//h1[@data-test="jobCount-H1title"]'))
    ).text.split(" ")[0]
    
    for job in job_list:
        company_detail = None
        company_name = None
        rating = None
        job_title = None
        job_location = None
        estimated_salary = None
        job_description = None
        company_size = None
        founded = None
        company_type = None
        industry = None
        sector = None
        revenue = None
        
        try:
            job.click()
            time.sleep(.5)
            
            company_name = get_details(driver, selector_company_detail, timeout).split("\n")[0]
            rating = get_details(driver, selector_rating, timeout)
            job_title = get_details(driver, selector_job_title, timeout)
            job_location = get_details(driver, selector_job_location, timeout)
            estimated_salary = get_details(driver, selector_estimated_salary, timeout)
            count += 1
            try:
                WebDriverWait(driver=driver, timeout=timeout).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="JobDescriptionContainer"]/div[2]'))
                ).click()
            except:
                pass
            job_description = get_details(driver, selector_job_description, timeout, By.ID)
            
            # checking if CompanyContainer exist, if it doesn't, then no need to fetch data
            company_container = get_details(driver, "CompanyContainer", timeout, By.ID)
            if company_container == None:
                print(f"{count}/{len(job_list)}\tState: {location}", end="\t")                
                print(company_name, rating, job_title)
                # print(company_name, rating, job_title, job_location, estimated_salary)
                new_row = {     "Company name": company_name, "Rating": rating, "Location": job_location, "Job title": job_title,
                            "Estimated salary": estimated_salary, "Job description": job_description,
                            "Number of employees": company_size, "Founded": founded, "Sector": sector,
                            "Industry": industry, "Revenue": revenue }
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
                continue
            
            company_size = get_details(driver, selector_company_size, timeout)
            founded = get_details(driver, selector_founded, timeout)
            company_type = get_details(driver, selector_company_type, timeout)
            industry = get_details(driver, selector_industry, timeout)
            sector = get_details(driver, selector_sector, timeout)
            revenue = get_details(driver, selector_revenue, timeout)
            print(f"{count}/{len(job_list)}\tState: {location}", end="\t")
            print(company_name, rating, job_title)
            # print(company_name, rating, job_title, job_location, estimated_salary, company_size, founded, company_type, industry, sector, revenue)
            
            new_row = {     "Company name": company_name, "Rating": rating, "Location": job_location, "Job title": job_title,
                            "Estimated salary": estimated_salary, "Job description": job_description,
                            "Number of employees": company_size, "Founded": founded, "Sector": sector,
                            "Industry": industry, "Revenue": revenue, "Keyword": keyword}
            
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            
        except Exception as e:
            print("An error occured:", str(e))
            
    return df

file_lock = multiprocessing.Lock()

def process_state(url, state, keyword, output_path, completed_files, total_files, total_progress):
    link_df = get_job_details(url=url, location=state, keyword=keyword)
    
    with file_lock:
        link_df.to_csv(output_path, mode="a", index=False, header=not os.path.exists(output_path))
    
    print(f"Processed jobs in {state}")
    completed_files.value += 1
    progress = completed_files.value / total_files * 100
    total_progress.value = progress
    print(f"Progress: {progress:.2f}%")

def main():
    output_path = "output.csv"    
    state_url_keyword = pd.read_csv("links_merged.csv")
    
    cpu_count = multiprocessing.cpu_count()
    manager = multiprocessing.Manager()
    total_progress = manager.Value('f', 0.0)
    
    # Veri kümesini işlem sayısı kadar böl
    partitions = [state_url_keyword[i:i + cpu_count] for i in range(0, len(state_url_keyword), cpu_count)]
    
    pool = multiprocessing.Pool()
    
    for i, partition in enumerate(partitions):
        completed_files = manager.Value('i', 0)
        arguments = [(row["Url"], row["State"], row["Keyword"], output_path, completed_files, len(partition), total_progress) for index, row in partition.iterrows()]
        pool.starmap(process_state, arguments)

        completed_percentage = (i + 1) / len(partitions) * 100
        total_progress.value = completed_percentage
        print(f"Total Progress: {completed_percentage:.2f}%")
        time.sleep(3)
    
    pool.close()
    pool.join()
    
    print("All jobs processed successfully.")

if __name__ == "__main__":
    main()