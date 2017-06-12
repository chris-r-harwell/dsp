#!/bin/python3

import csv
import os
import re
import sys


facultycsv = """name, degree, title, email
Scarlett L. Bellamy, Sc.D.,Associate Professor of Biostatistics,bellamys@mail.med.upenn.edu
Warren B. Bilker,Ph.D.,Professor of Biostatistics,warren@upenn.edu
Matthew W Bryan, PhD,Assistant Professor of Biostatistics,bryanma@upenn.edu
Jinbo Chen, Ph.D.,Associate Professor of Biostatistics,jinboche@upenn.edu
Susan S Ellenberg, Ph.D.,Professor of Biostatistics,sellenbe@upenn.edu
Jonas H. Ellenberg, Ph.D.,Professor of Biostatistics,jellenbe@mail.med.upenn.edu
Rui Feng, Ph.D,Assistant Professor of Biostatistics,ruifeng@upenn.edu
Benjamin C. French, PhD,Associate Professor of Biostatistics,bcfrench@mail.med.upenn.edu
Phyllis A. Gimotty, Ph.D,Professor of Biostatistics,pgimotty@upenn.edu
Wensheng Guo, Ph.D,Professor of Biostatistics,wguo@mail.med.upenn.edu
Yenchih Hsu, Ph.D.,Assistant Professor of Biostatistics,hsu9@mail.med.upenn.edu
Rebecca A Hubbard, PhD,Associate Professor of Biostatistics,rhubb@mail.med.upenn.edu
Wei-Ting Hwang, Ph.D.,Associate Professor of Biostatistics,whwang@mail.med.upenn.edu
Marshall M. Joffe, MD MPH Ph.D,Professor of Biostatistics,mjoffe@mail.med.upenn.edu
J. Richard Landis, B.S.Ed. M.S. Ph.D.,Professor of Biostatistics,jrlandis@mail.med.upenn.edu
Yimei Li, Ph.D.,Assistant Professor of Biostatistics,liy3@email.chop.edu
Mingyao Li, Ph.D.,Associate Professor of Biostatistics,mingyao@mail.med.upenn.edu
Hongzhe Li, Ph.D,Professor of Biostatistics,hongzhe@upenn.edu
A. Russell Localio, JD MA MPH MS PhD,Associate Professor of Biostatistics,rlocalio@upenn.edu
Nandita Mitra, Ph.D.,Associate Professor of Biostatistics,nanditam@mail.med.upenn.edu
Knashawn H. Morales, Sc.D.,Associate Professor of Biostatistics,knashawn@mail.med.upenn.edu
Kathleen Joy Propert, Sc.D.,Professor of Biostatistics,propert@mail.med.upenn.edu
Mary E. Putt, PhD ScD,Professor of Biostatistics,mputt@mail.med.upenn.edu
Sarah Jane Ratcliffe, Ph.D.,Associate Professor of Biostatistics,sratclif@upenn.edu
Michelle Elana Ross, PhD,Assistant Professor is Biostatistics,michross@upenn.edu
Jason A. Roy, Ph.D.,Associate Professor of Biostatistics,jaroy@mail.med.upenn.edu
Mary D. Sammel, Sc.D.,Professor of Biostatistics,msammel@cceb.med.upenn.edu
Pamela Ann Shaw, PhD,Assistant Professor of Biostatistics,shawp@upenn.edu
Russell Takeshi Shinohara,0,Assistant Professor of Biostatistics,rshi@mail.med.upenn.edu
Haochang Shou, Ph.D.,Assistant Professor of Biostatistics,hshou@mail.med.upenn.edu
Justine Shults, Ph.D.,Professor of Biostatistics,jshults@mail.med.upenn.edu
Alisa Jane Stephens, Ph.D.,Assistant Professor of Biostatistics,alisaste@mail.med.upenn.edu
Andrea Beth Troxel, ScD,Professor of Biostatistics,atroxel@mail.med.upenn.edu
Rui Xiao, PhD,Assistant Professor of Biostatistics,rxiao@mail.med.upenn.edu
Sharon Xiangwen Xie, Ph.D.,Associate Professor of Biostatistics,sxie@mail.med.upenn.edu
Dawei Xie, PhD,Assistant Professor of Biostatistics,dxie@upenn.edu
Wei (Peter) Yang, Ph.D.,Assistant Professor of Biostatistics,weiyang@mail.med.upenn.edu"""

with open('faculty.csv', 'w') as f:
    f.write(facultycsv)


def read_data(filename):
    """
    Returns a list of dictionaries representing the rows of the csv file data.

    INPUT: filename is the name of a csv file (as a string)

    OUTPUT: list of dictionaries using the header line in the file as the keys
             and the values set to the strings in that cell of the row.
    """
    with open(filename) as f:
        reader = csv.DictReader(f, skipinitialspace=True)
        if 'title' not in reader.fieldnames:
            # expecting: name, degree, title, email
            raise ValueError('could not find title in csv header {}'
                             .format(reader.fieldnames))
        data = list(reader)
        # print('data:')
        # print(repr(data))
        return data


def count_titles_by_standardization(csv_file_name):
    """
    In this version we get a list of key, value dictionaries for each row.
    Then, compile a standardized (all upper case, replace is with of) set of
     titles, title_list.
    From that standardized list, we create a uniq set to initialize our
     answer/output dictionary, title_dict.
    Then use the regular expression to count occurences and update the
     dictionary.
    INPUT: filename
    OUTPUT: dictionary with title keys and counts as values
    """
    data = read_data(csv_file_name)
    title_list = []
    for row in data:
        item = row['title']
        consistent_item = item.upper().replace(' IS ', ' OF ')
        title_list.append(consistent_item)
    title_list.sort()
    # print(repr(set(title_list)))
    title_dict = {}
    title_dict = title_dict.fromkeys(set(title_list), 0)
    # print(repr(title_dict))
    for k in title_dict.keys():
        regexp = re.compile('^' + k + '$')
        count = 0
        for d in title_list:
            if regexp.search(d):
                count += 1
        title_dict[k] = count
    # print('std: ' + repr(title_dict))
    return title_dict


def count_titles_by_regexp(csv_file_name):
    """
    solution titles = ['professor', 'associate', 'assistant']
    strings present in csv file:
    {'Professor of Biostatistics', 'Associate Professor of Biostatistics',
     'Assistant Professor is Biostatistics',
     'Assistant Professor of Biostatistics'}
    # regexp key:
    # (?i) case-insensitive
    # ^ start
    # $ end
    # \.* zero or more '.
    #

    In this version we get a list of key, value dictionaries for each row.
    Then, use a dictionary of standardized title regular expressions.
    From that, we initialize our answer/output dictionary, title_dict.
    Then use the regular expression to count occurences and update the
     dictionary.
    INPUT: filename
    OUTPUT: dictionary with title keys and counts as values
    """
    title_regexp_dict = {'professor': re.compile('(?i)^Prof.*$'),
                         'associate': re.compile('(?i)^Associate Prof.*$'),
                         'assistant': re.compile('(?i)^Assistant Prof.*$'),
                         }
    data = read_data(csv_file_name)
    title_list = []
    for row in data:
        title_list.append(row['title'])
    title_dict = {}
    title_dict = title_dict.fromkeys(set(title_regexp_dict), 0)
    for k in title_dict.keys():
        regexp = title_regexp_dict[k]
        count = 0
        for d in title_list:
            if regexp.fullmatch(d):
                count += 1
        title_dict[k] = count
    # print('regexp: ' + repr(title_dict))
    return title_dict


def count_titles(csv_file_name):
    # a = count_titles_by_standardization(csv_file_name)
    return count_titles_by_regexp(csv_file_name)

try:
    titlecounts = count_titles('faculty.csv')
    os.remove('faculty.csv')
except Exception as e:
    os.remove('faculty.csv')
    raise(e)

titlecounts = {
    str(key).replace(' ', '').replace('.', '').lower()[:9]: val
    for key, val in titlecounts.items()
}

titles = ['professor', 'associate', 'assistant']
assert len(titles) >= len(titlecounts), 'did you get all the different titles?'
assert len(titles) == len(titlecounts), 'your output has too many titles'
for title in titles:
    count = titlecounts.get(title, -1)
    print(count)
