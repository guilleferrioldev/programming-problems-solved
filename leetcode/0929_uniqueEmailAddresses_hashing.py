# Unique Email Addresses

"""
Every valid email consists of a local name and a domain name, separated by the '@' sign. 
Besides lowercase letters, the email may contain one or more '.' or '+'.

    For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.

If you add periods '.' between some characters in the local name part of an email address, mail sent there will
be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

    For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.

If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows
certain emails to be filtered. Note that this rule does not apply to domain names.

    For example, "m.y+name@email.com" will be forwarded to "my@email.com".

It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], return the number of different
addresses that actually receive mails.
"""

# Runtime: 31ms (Beats 81.23% of users with Python)
# Memory: 13.6MB (Beats 32.57% of users with Python)

from typing import List

class Solution(object):
    def numUniqueEmails(self, emails: List[str]) -> int:
        # Hash to save all the emails
        hashset: set[str] = set()
        
        for email in emails:
            # Unpack name and domain
            name , domain = email.split("@")
            # Remove the . in the name and stay are what is before the +. Then put the email back together and save it in the hash.
            hashset.add(name.replace(".", "").split("+")[0] + "@" + domain)

        return len(hashset)

if __name__ == "__main__":
    solution = Solution()

    s1 = solution.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
    s2 = solution.numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"])

    print(s1, s2) 
