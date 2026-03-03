**🛍️ Daraz Track Suit Scraper
**
A Python-based web scraping project that extracts track suit product data from Daraz.pk using Selenium and BeautifulSoup.

This scraper automates pagination, handles dynamic content loading, and exports structured product data into a CSV file for analysis.

---

**📌 Project Overview**

Daraz.pk loads product listings dynamically, which requires browser automation for reliable scraping.  
This project uses:

- **Selenium** – for dynamic page rendering
- **BeautifulSoup** – for HTML parsing
- **Pandas** – for structured data export
- **WebDriver Manager** – for automatic ChromeDriver management

The scraper iterates through multiple pages and collects detailed product information.

---

**🚀 Features**

- Extracts:
  - Product Name
  - Current Price
  - Original Price
  - Discount Percentage
  - Rating
  - Units Sold
  - Seller Location
  - Product URL
- Handles pagination
- Waits for dynamic content to load
- Exports clean CSV dataset
- Includes delay handling to reduce blocking risk

---

**📂 Project Structure**

daraz-track-suit-scraper/
│
├── scrapping.py

├── requirements.txt

├── README.md

└── .gitignore

---

**⚙️ Installation**

1️⃣ Clone the repository

bash

git clone https://github.com/owaissaee/Daraz-Track-Suit-Scrapper.git

cd Daraz-Track-Suit-Scrapper

2️⃣ Create virtual environment (recommended)

python -m venv venv

source venv/bin/activate  # Linux / Mac

venv\Scripts\activate     # Windows

3️⃣ Install dependencies

pip install -r requirements.txt

---

**▶️ Usage**

Run the scraper:

python scrapping.py

After execution, the scraped data will be saved as:

track_suits.csv

---

**📊 Output Format**

The generated CSV contains the following columns:

Column Name	                                    Description

Product Name	                                Name of the item

Current Price	                                Discounted price

Original Price	                              Price before discount

Discount	                                    Discount percentage

Rating	                                      Product rating

Sold Units	                                  Units sold

Location	                                    Seller location

Product URL	                                  Direct link to product

---

**⚠️ Notes**

This project is intended for educational purposes only.

Excessive scraping may result in IP blocking.

Consider enabling headless mode for server environments.

Website structure changes may require selector updates.

---

**🧠 Future Improvements**

Add logging instead of print statements

Convert into modular/OOP structure

Add CLI arguments for query and page count

Dockerize the project

Deploy on a cloud server

Store data in a database instead of CSV

---

**👤 Author**

Owais Saeed
