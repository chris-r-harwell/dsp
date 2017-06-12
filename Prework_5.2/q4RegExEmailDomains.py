#!/bin/python3

import os
import re
import sys


def unique_domains(emails):
    """
    INPUT: list of emails
    OUTPUT: sorted list of unique email domains
    """
    domain_list = []
    regexp = re.compile('^.*@')
    for i in emails:
        domain = re.sub(regexp, '', i)
        domain_list.append(domain)
    domain_list = sorted(set(domain_list))
    return domain_list


emails = sys.stdin.readlines()
emails = [email.strip() for email in emails]
domains = unique_domains(emails)
for domain in sorted(domains):
    print(domain)
