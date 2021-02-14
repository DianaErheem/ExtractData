import urllib.request
import re

regx_emails = r'[\w\.-]+@[\w\.-]+'
regx_urls = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
regx_numbers = r'\d+'

def extractdata(html,regx):
    if html:
        lst = re.findall(regx, html)
        return lst


def gethttpcontent(url):
    print(url)
    try: webUrl = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        return
    if webUrl.getcode() == 200:
        html = webUrl.read()
        urllib.request.urlcleanup()

    return html.decode('utf-8')


def listToStringLines(s):
    if not s :
        return

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele + "\n"

        # return string
    return str1


file_name = input("Provide the file name : ")
diana_file = open(file_name, "r")
file_email_name = input("Enter the name of the email file : ")
file_url_name = input("Enter the name of the url file : ")
file_numbers_name = input("Enter the name of the numbers file : ")

for url in diana_file.readlines():
    html = gethttpcontent(url)
    emails = extractdata(html, regx_emails)
    urls = extractdata(html, regx_urls)
    numbers = extractdata(html, regx_numbers)

    if emails:
        emails_file = open(file_email_name, "a", encoding='utf-8')
        emails_file.write(url+"\n")
        emails_file.writelines(listToStringLines(emails))
        emails_file.close()
    if numbers:
        numbers_file = open(file_numbers_name, "a", encoding='utf-8')
        numbers_file.write(url + "\n")
        numbers_file.writelines(listToStringLines(numbers))
        numbers_file.close()
    if urls:
        urls_file = open(file_url_name, "a", encoding='utf-8')
        urls_file.write(url + "\n")
        urls_file.writelines(listToStringLines(urls))
        urls_file.close()


diana_file.close()

