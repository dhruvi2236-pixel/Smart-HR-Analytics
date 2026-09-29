# ============================================================
# HUMAN RESOURCE ANALYTICS
# CIPAT PROJECT
# WEB SCRAPING MODULE
# ============================================================

import os

import certifi
import requests
from bs4 import BeautifulSoup


# ============================================================
# WEBPAGE TO SCRAPE
# ============================================================

URL = (
    "https://www.shrm.org/in/topics-tools/news/blogs/"
    "understanding-the-hr-lifecycle-from-hiring-to-exit"
)


# ============================================================
# WEB SCRAPING FUNCTION
# ============================================================

def scrape_hr_information():

    print("\n")
    print("=" * 40)
    print("           WEB SCRAPING")
    print("=" * 40)

    print("\nSource webpage:")
    print(URL)

    try:

        # ----------------------------------------------------
        # STEP 1: Create HTTP session
        # ----------------------------------------------------

        session = requests.Session()

        # Prevent unwanted system proxy settings
        session.trust_env = False

        # ----------------------------------------------------
        # STEP 2: Send request to webpage
        # ----------------------------------------------------

        response = session.get(
            URL,
            timeout=15,
            verify=certifi.where(),
            headers={
                "User-Agent": (
                    "Mozilla/5.0 "
                    "(Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 "
                    "(KHTML, like Gecko) "
                    "Chrome/153.0.0.0 Safari/537.36"
                )
            }
        )

        # Raise an exception for HTTP errors
        response.raise_for_status()

        print("\n1. Webpage accessed successfully.")
        print("HTTP Status Code:", response.status_code)


        # ----------------------------------------------------
        # STEP 3: Parse HTML using BeautifulSoup
        # ----------------------------------------------------

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        print("\n2. HTML parsed successfully using BeautifulSoup.")


        # ----------------------------------------------------
        # STEP 4: Extract webpage title
        # ----------------------------------------------------

        title = soup.title.get_text(strip=True) if soup.title else "No title found"

        print("\n3. Page Title:")
        print(title)


        # ----------------------------------------------------
        # STEP 5: Extract main heading
        # ----------------------------------------------------

        headings = []

        for heading in soup.find_all(["h1", "h2"]):

            text = heading.get_text(
                " ",
                strip=True
            )

            if text:
                headings.append(text)


        print("\n4. HR Headings Extracted:")

        if headings:

            for index, heading in enumerate(
                headings[:10],
                start=1
            ):
                print(f"{index}. {heading}")

        else:
            print("No headings found.")


        # ----------------------------------------------------
        # STEP 6: Extract useful paragraph information
        # ----------------------------------------------------

        paragraphs = []

        for paragraph in soup.find_all("p"):

            text = paragraph.get_text(
                " ",
                strip=True
            )

            if len(text) > 40:
                paragraphs.append(text)


        print("\n5. HR Information Extracted:")

        if paragraphs:

            for paragraph in paragraphs[:5]:
                print("-", paragraph)

        else:
            print("No paragraph information found.")


        # ----------------------------------------------------
        # STEP 7: Save scraped information
        # ----------------------------------------------------

        os.makedirs(
            "output",
            exist_ok=True
        )

        output_file = (
            "output/scraped_hr_information.txt"
        )

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(
                "HUMAN RESOURCE ANALYTICS\n"
            )

            file.write(
                "WEB SCRAPING OUTPUT\n"
            )

            file.write(
                "=" * 60 + "\n\n"
            )

            file.write(
                "Source Webpage:\n"
            )

            file.write(
                URL + "\n\n"
            )

            file.write(
                "Page Title:\n"
            )

            file.write(
                title + "\n\n"
            )

            file.write(
                "HR HEADINGS:\n"
            )

            file.write(
                "-" * 60 + "\n"
            )

            for heading in headings[:10]:

                file.write(
                    heading + "\n"
                )

            file.write(
                "\nHR INFORMATION:\n"
            )

            file.write(
                "-" * 60 + "\n"
            )

            for paragraph in paragraphs[:10]:

                file.write(
                    paragraph + "\n\n"
                )


        print("\n6. Scraped information saved successfully.")

        print(
            "Output file:",
            output_file
        )


        # ----------------------------------------------------
        # Completion
        # ----------------------------------------------------

        print("\n")
        print("=" * 40)
        print("WEB SCRAPING COMPLETED")
        print("=" * 40)


    # ========================================================
    # EXCEPTION HANDLING FOR WEB SCRAPING
    # ========================================================

    except requests.RequestException as error:

        print("\nWeb scraping request error handled.")
        print("Error:", error)


    except Exception as error:

        print("\nUnexpected web scraping error handled.")
        print("Error:", error)