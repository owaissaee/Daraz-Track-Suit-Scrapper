# 🛍️ Daraz Track Suit Scraper
A high-performance Python-based web scraper designed to extract structured product data from **Daraz.pk**. This tool automates the process of navigating dynamic product listings, handling pagination, and exporting clean datasets for market analysis.

## 📌 Project Overview
Scraping modern e-commerce platforms like Daraz requires more than just standard HTML parsing, as content is loaded dynamically via JavaScript. 

This project implements:
- **Selenium WebDriver** – To simulate real user behavior and handle dynamic content rendering.
- **BeautifulSoup** – For high-speed parsing of the rendered HTML.
- **Pandas** – To structure, clean, and export the scraped data.
- **WebDriver Manager** – For automated ChromeDriver configuration, ensuring cross-system compatibility.

## 🚀 Key Features
- **Dynamic Content Handling:** Effectively waits for lazy-loaded elements to appear before extraction.
- **Automated Pagination:** Iterates through multiple search result pages automatically.
- **Robust Extraction:** Captures 8+ data points including Prices, Ratings, Units Sold, and Seller Location.
- **Data Structuring:** Outputs a ready-to-use CSV file for competitive pricing analysis or inventory research.
- **Anti-Block Measures:** Includes randomized delay handling to mimic human browsing patterns.

## 📂 Project Structure
```text
Daraz-Track-Suit-Scrapper/
├── scrapping.py          # Main scraping engine
├── requirements.txt      # Project dependencies
├── README.md             # Documentation
└── .gitignore            # Prevents tracking of local drivers and CSVs

```

## ⚙️ Installation

1️⃣ **Clone the repository**

```bash
git clone [https://github.com/owaissaee/Daraz-Track-Suit-Scrapper.git](https://github.com/owaissaee/Daraz-Track-Suit-Scrapper.git)
cd Daraz-Track-Suit-Scrapper

```

2️⃣ **Set up a Virtual Environment (Recommended)**

```bash
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on Mac/Linux:
source venv/bin/activate

```

3️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt

```

## ▶️ Usage

Simply run the script to begin the extraction process:

```bash
python scrapping.py

```

Upon completion, a file named `track_suits.csv` will be generated in the root directory.

## 📊 Output Format

| Column Name | Description |
| --- | --- |
| **Product Name** | Full title of the track suit listing |
| **Current Price** | The active sale price (PKR) |
| **Original Price** | Pre-discount price |
| **Discount %** | Calculated discount percentage |
| **Rating** | Average star rating (0-5) |
| **Sold Units** | Total number of items sold |
| **Location** | Seller's operational city/region |
| **Product URL** | Direct link for verification |

## ⚠️ Disclaimer & Notes

* **Ethics:** This tool is for educational purposes. Please review Daraz's `robots.txt` and Terms of Service before high-volume scraping.
* **Headless Mode:** For server deployment, consider enabling the `--headless` flag in the Selenium options.
* **Maintenance:** Web structures change frequently; selectors in `scrapping.py` may need periodic updates.

## 🧠 Future Improvements

* [ ] Add **Headless Mode** toggle via CLI arguments.
* [ ] Implement **Proxy Rotation** to further prevent IP flagging.
* [ ] Integrate **Image Downloader** to scrape product thumbnails.
* [ ] Support for multiple search queries beyond "track suits".

## 👤 Author

**Owais Saeed**

**Would you like me to also provide a specific `.gitignore` for this scraper to keep your repo clean of Chrome driver logs?**

```
