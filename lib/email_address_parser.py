import re

class EmailAddressParser:
    def __init__(self, emails):
        self.emails = emails

    def parse(self):
        # Regex that matches valid email addresses
        pattern = r"[A-Za-z0-9\._%+-]+@[A-Za-z0-9\.-]+\.[A-Za-z]{2,}"

        # Find all emails in the string
        found = re.findall(pattern, self.emails)

        # Sort alphabetically, as required by the test
        return sorted(found)
