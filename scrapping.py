from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time
from urllib.parse import urljoin

# Setup Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
# options.add_argument("--headless")
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Configuration
base_url = "https://www.daraz.pk/catalog/?q=track+suits"
data = []
page_number = 1
total_pages = 89  # 3669 items  40 per page ≈ 92 pages.

try:
    while page_number <= total_pages:
        print(f"Scraping Page {page_number}...")
        
        current_url = f"{base_url}&page={page_number}"
        driver.get(current_url)

        # Wait for products to load
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "Bm3ON"))
            )
        except:
            print("Timeout or no items found. Ending scrape.")
            break

        # lazy-loaded images/elements are captured
        driver.execute_script("window.scrollTo(0, 1000);")
        time.sleep(2) 

        # Parse page source
        soup = BeautifulSoup(driver.page_source, "html.parser")
        products = soup.find_all("div", class_="Bm3ON")

        if not products:
            print("No products found on this page. Stopping.")
            break

        for product in products:
            # Product Name
            name_tag = product.find("div", class_="RfADt")
            name = name_tag.text.strip() if name_tag else None

            # Current Price
            price_tag = product.find("span", class_="ooOxS")
            current_price = price_tag.text.strip().replace("₨", "").replace(",", "") if price_tag else None

            # Original Price
            orig_tag = product.find("span", class_="IfIeZ") or product.find("span", class_="price--original")
            original_price = orig_tag.text.strip().replace("₨", "").replace(",", "") if orig_tag else None

            # Discount
            discount_tag = product.find("span", class_="WNoq3")
            discount = discount_tag.text.strip() if discount_tag else None

            # Rating
            rating_tag = product.find("span", class_="qzqFw")
            rating = rating_tag.text.strip() if rating_tag else None

            # Sold Units
            sold_tag = product.find("span", class_="1cEkb")
            sold = sold_tag.get_text(strip=True) if sold_tag else None

            # Location
            location_tag = product.find("span", class_="oa6ri")
            location = location_tag.get("title") if location_tag else None

            # Product URL
            link_tag = product.find("a")
            link = urljoin(base_url, link_tag["href"]) if link_tag else None

            data.append([
                name, current_price, original_price, discount, rating, sold, location, link 
            ])
        
        # Move to next page
        page_number += 1

        # delay to prevent getting IP banned
        time.sleep(3)

finally:
    driver.quit()

# Save to DataFrame
columns = [
    "Product Name",
    "Current Price",
    "Original Price",
    "Discount",
    "Rating",
    "Sold Units",
    "Location",
    "Product URL"
]

df = pd.DataFrame(data, columns=columns)
df.to_csv("track_suits.csv", index=False)
print(f"Scraping completed. {len(df)} items saved.")