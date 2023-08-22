from __future__ import annotations

import re

import requests
from bs4 import BeautifulSoup


def extract_social_links(soup: BeautifulSoup) -> list[str]:
    social_links = []

    social_patterns = [
        r"https?://(?:www\.)?facebook\.com/[\w\.-]+",
        r"https?://(?:www\.)?twitter\.com/[\w\.-]+",
        r"https?://(?:www\.)?linkedin\.com/company/[\w\.-]+",
    ]

    for pattern in social_patterns:
        matches = soup.find_all("a", href=re.compile(pattern, re.IGNORECASE))
        social_links.extend([match["href"] for match in matches])

    return social_links


def extract_email(soup: BeautifulSoup) -> list[str]:
    matches = soup.find_all("a", href=lambda a: a.startswith("mailto:"))
    return [each["href"].removeprefix("mailto:") for each in matches]


def extract_contact(soup: BeautifulSoup) -> list[str]:
    matches = soup.find_all("a", href=lambda a: a.startswith("tel:"))
    return [match["href"].removeprefix("tel:") for match in matches]


def get_website_details(url: str) -> tuple[list[str], list[str], list[str]]:
    response = requests.get(url, timeout=1)
    soup = BeautifulSoup(response.text, "html.parser")

    social_links = extract_social_links(soup)
    emails = extract_email(soup)
    contacts = extract_contact(soup)

    return social_links, emails, contacts


website_url = input("Enter the website URL: ")

social_links, emails, contacts = get_website_details(website_url)

print("Social links:")
for link in social_links:
    print(link)

print("Email:")
for email in emails:
    print(email)

print("Contact:")
for contact in contacts:
    print(contact)
