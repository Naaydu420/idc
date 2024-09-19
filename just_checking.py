from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

# Setup the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to the product page
driver.get("https://example.com/product")  # Replace with the actual URL

# Function to scroll to the bottom of the page
def scroll_to_bottom():
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for the page to load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# Scroll to load all reviews
scroll_to_bottom()

# Find all review elements
reviews = driver.find_elements(By.CSS_SELECTOR, ".review-item")  # Replace with actual CSS selector

# Prepare CSV file
with open('reviews.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Author", "Rating", "Review Text"])

    # Extract data from each review
    for review in reviews:
        try:
            author = review.find_element(By.CSS_SELECTOR, ".author").text
            rating = review.find_element(By.CSS_SELECTOR, ".rating").get_attribute("data-rating")
            text = review.find_element(By.CSS_SELECTOR, ".review-text").text

            # Write the data to CSV
            writer.writerow([author, rating, text])
        except Exception as e:
            print(f"Error extracting review: {e}")

# Close the browser
driver.quit()

print("Reviews have been scraped and saved to reviews.csv")
