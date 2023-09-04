import multiprocessing
import pandas as pd
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_links(location, keyword="test"):
    df_links = pd.DataFrame(columns=["State", "Keyword","Url"])
    
    driver = webdriver.Chrome()
    driver.get("https://www.glassdoor.com/Job/index.htm")
    driver.maximize_window()
    
    job_title_input = driver.find_element(By.ID, 'searchBar-jobTitle')
    job_title_input.send_keys(keyword)
    location_input = driver.find_element(By.ID, 'searchBar-location')
    location_input.send_keys(location)
    location_input.send_keys(Keys.RETURN)
    
    no_found_text = "does not match any open jobs".lower()
    
    try:
        no_job_found = WebDriverWait(driver=driver, timeout=10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="noResults"]'))
        ).text.lower()
        if no_found_text in no_job_found:
            print("No job found.")
            # df_links.to_csv(f"./{directory}/{location}_links.csv", index=False)
            return df_links
    except:
        pass
    
    is_all_links_collected = False
    time_out_2 = 5
    
    while not is_all_links_collected:
        try:
            WebDriverWait(driver=driver, timeout=time_out_2).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'selected'))
            ).click()
            time.sleep(5)
            WebDriverWait(driver=driver, timeout=time_out_2).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="LoginModal"]/div/div/div/div[2]/button'))
            ).click()
        except:
            pass
        
        new_url = {"State": location, "Keyword": keyword,"Url": driver.current_url}
        df_links = pd.concat([df_links, pd.DataFrame([new_url])], ignore_index=True)
        print("Url:", driver.current_url)
        
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Next"]'))
            )
            if next_button.is_enabled():
                next_button.click()
            else:
                # df_links.to_csv(f"./{directory}/{location}_links.csv", index=False)
                return df_links
        except Exception as e:
            print("No more pages available.")
            is_all_data_collected = True
            # df_links.to_csv(f"./{directory}/{location}_links.csv", index=False)
            return df_links
    
def check_directory(directory):
    if os.path.exists(directory):
        for root, dirs, files in os.walk(directory, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                os.remove(file_path)
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                os.rmdir(dir_path)
        os.rmdir(directory)
    os.mkdir(directory)

def process_state(directory, state_name, keyword="data scientist"):
    link_df = get_links(state_name, keyword)
    link_df.to_csv(f"./{directory}/{state_name}_links.csv", index=False)
    print(f"Processed jobs in {state_name}")

def process_create(directory, keyword, states):
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    arguments = [(directory, state, keyword) for state in states["State Name"]]
    pool.starmap(process_state, arguments)
    
    pool.close()
    pool.join()
    print("All jobs processed successfully.")

if __name__ == "__main__":
    directory = "links"
    keyword = "data scientist"
    check_directory(directory=directory)
    
    states_df = pd.read_csv("states.csv")
    state_names = states_df["State Name"]
    
    process_create(directory=directory, keyword=keyword, states=states_df)
