---

# Darkdump

Darkdump is a versatile command-line tool designed for efficient searching of the deep web, allowing users to retrieve specific information based on keywords or strings. It provides a simple yet powerful interface to explore the hidden corners of the internet and obtain relevant data.

## Features

- **Deep Web Search:** Search for specific keywords or strings within the deep web.
- **Customizable Results:** Customize the number of results to be displayed.
- **Proxy Support:** Utilize proxies for enhanced anonymity during searches.
- **URL Display:** Show website URLs along with descriptions for better context.
- **Result Saving:** Save search results to a file for future reference.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/LoopUE/darkdump.git
   ```

2. Navigate to the project directory:
   ```bash
   cd darkdump
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python darkdump.py -q <query> [-a <amount>] [-p] [-u] [-t <timeout>] [-f <filename>]
```

- `<query>`: Specify the keyword or string for deep web searching (mandatory).
- `<amount>`: Set the number of results to be retrieved (default: 10).
- `-p`, `--proxy`: Enable Darkdump proxy usage for increased anonymity.
- `-u`, `--urls`: Display website URLs along with descriptions.
- `-t`, `--timeout`: Define the timeout duration for HTTP requests in seconds (default: 10).
- `-f`, `--file`: Save search results to a specified file.

## Example

Search for the keyword "bitcoin," display 5 results including website URLs, use a proxy, and set a timeout of 15 seconds:

```bash
python darkdump.py -q bitcoin -a 5 -p -u -t 15
```

## License

This project is licensed under the EPL-2.0 License. For more details, refer to the [LICENSE](LICENSE) file.

## Acknowledgements

Darkdump utilizes the following libraries:

- [Requests](https://docs.python-requests.org/en/latest/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [Fake User Agent](https://pypi.org/project/fake-useragent/)

This version of Darkdump is a fork of the original [josh0xA](https://github.com/josh0xA/darkdump) project and has been fully updated by Ai.

---
