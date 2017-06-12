#!/bin/python3

import os
import sys


def write_to_csv(list_of_emails):
    """
    Write a list of emails to a csv file with a header.
    INPUT: list of emails
    OUTPUT: none
    """
    import csv
    # use newline='' to prevent double-spaced rows
    with open('emails.csv', 'w', newline='') as outFile:
        outWriter = csv.writer(outFile)
        charNum = outWriter.writerow(['email'])
        for i in list_of_emails:
            charNum = outWriter.writerow([i])
        outFile.close()


emails = list(map(str.strip, sys.stdin.readlines()))
write_to_csv(emails)
assert os.path.exists('emails.csv'), 'did you write to "emails.csv"?'
with open('emails.csv', 'r') as f:
    header = f.readline()
    emails2 = []
    for line in f.readlines():
        emails2.append(line.strip())
os.remove('emails.csv')
assert all(i == j for i, j in zip(emails, emails2)),\
        'this list of emails is different'
assert len(emails) == len(emails2), 'this list of emails is different'
print(1)
