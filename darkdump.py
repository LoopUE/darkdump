import argparse
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def generate_user_agent():
    try:
        ua = UserAgent()
        return ua.random
    except Exception as e:
        print("[X] Error generating user agent:", e)
        return None

def assign_proxy():
    try:
        proxy_api = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=elite"
        req = requests.get(proxy_api, timeout=5)
        req.raise_for_status()
        proxy_info = req.text.strip().split('\n')
        return {"http": f"http://{proxy_info[0]}"}
    except RequestException as e:
        print("[X] Proxy Error:", e)
        return None
    except Exception as e:
        print("[X] Error assigning proxy:", e)
        return None

def crawl(query, amount, proxy_enabled=False, show_urls=False, timeout=10):
    darkdump_api = "https://ahmia.fi/search/?q="
    headers = {'User-Agent': generate_user_agent()}
    proxies = assign_proxy() if proxy_enabled else None

    try:
        response = requests.get(darkdump_api + query, headers=headers, proxies=proxies, timeout=timeout)
        response.raise_for_status()  # Raise an error for non-200 status codes
    except RequestException as e:
        print("[X] Request Error:", e)
        return None, None

    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find(id='ahmiaResultsPage')
    if not results:
        print("[X] No results found.")
        return None, None

    second_results = results.find_all('li', class_='result')
    descriptions = [result.find('p').text.strip() for result in second_results]
    urls = [result.find('cite').text.strip() for result in second_results]

    for i in range(min(amount, len(descriptions))):
        print(f"[✓] Website: {descriptions[i]}")
        if show_urls:
            print(f"\t[✓] Onion Link: {urls[i]}")
        print()

    return descriptions, urls

def save_to_file(data, filename):
    try:
        with open(filename, 'w') as file:
            for line in data:
                file.write(line + '\n')
        print(f"[✓] Results saved to {filename}")
    except Exception as e:
        print("[X] Error saving to file:", e)

def darkdump_main():
    try:
        parser = argparse.ArgumentParser(description="Darkdump is a tool for searching the deep web for specific keywords.")
        parser.add_argument("-q", "--query", help="the keyword or string you want to search on the deep web", type=str, required=True)
        parser.add_argument("-a", "--amount", help="the amount of results you want to retrieve (default: 10)", type=int, default=10)
        parser.add_argument("-p", "--proxy", help="use darkdump proxy to increase anonymity", action="store_true")
        parser.add_argument("-u", "--urls", help="show website URLs along with descriptions", action="store_true")
        parser.add_argument("-t", "--timeout", help="set the timeout for HTTP requests (default: 10 seconds)", type=int, default=10)
        parser.add_argument("-f", "--file", help="save results to a file", type=str)

        args = parser.parse_args()

        print("Welcome to Darkdump - Your Deep Web Search Tool")

        if args.query:
            print(f"[✓] Searching for: '{args.query}' and displaying {args.amount} results...\n")
            descriptions, urls = crawl(args.query, args.amount, args.proxy, args.urls, args.timeout)
            if descriptions and urls and args.file:
                save_to_file(descriptions, args.file)
        else:
            print("[X] No query provided. Please specify a keyword or string to search.")

    except Exception as e:
        print("[X] An unexpected error occurred:", e)

if __name__ == "__main__":
    darkdump_main()

