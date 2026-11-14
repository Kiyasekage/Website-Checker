# Website-Checker


A simple Python program that checks a website's HTTP response status using the `requests` library. The program sends an HTTP GET request to a website, retrieves its status code, and determines whether the website is working or experiencing a potential client-side or server-side issue.

## Features

- **HTTP Request:** Sends GET requests to a website using Python's Requests library.
- **Status Code Detection:** Retrieves the HTTP response status code.
- **Status Classification:** Identifies the general category of the response based on its first digit.
- **Website Availability Check:** Recognizes successful HTTP responses.
- **Error Identification:** Distinguishes between informational responses, redirections, client errors, and server errors.

## Technologies Used

- Python 3
- Requests Library
- HTTP Status Codes

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Install the Requests library:

   ```bash
   pip install requests
   ```

3. Save the code in a file named `website_checker.py`.
4. Open a terminal or command prompt.
5. Run the program:

   ```bash
   python website_checker.py
   ```

6. The program will send a request to Google and display the HTTP status code and its general classification.

## Example

**Example Output:**

```text
Hello, Welcome to your website checker!
Sample : https://www.google.com/
200
Yes, this website is working!
```

*Note: The actual status code may vary depending on the website response and network conditions.*

## HTTP Status Code Classification

| First Digit | Category | Meaning |
|---|---|---|
| 1xx | Informational | Request received; processing continues |
| 2xx | Success | Request successfully processed |
| 3xx | Redirection | Further action or redirection required |
| 4xx | Client Error | Problem with the request or access |
| 5xx | Server Error | Server failed to fulfill a valid request |

## Concepts Practiced

- **API and HTTP Communication:** Interacting with websites through HTTP requests.
- **Requests Library:** Using `requests.get()` to retrieve website responses.
- **Status Codes:** Understanding HTTP response codes and their classifications.
- **Type Conversion:** Converting values between integers and strings.
- **While Loops:** Extracting digits from an integer using division and modulo operations.
- **Lists:** Storing extracted digits.
- **Conditional Statements:** Classifying website responses based on their status codes.

## Language

Python 3
