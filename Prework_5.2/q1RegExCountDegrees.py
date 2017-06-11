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
        if 'degree' not in reader.fieldnames:
            # expecting: name, degree, title, email
            raise ValueError('could not find degree in csv header {}'.format(reader.fieldnames))
        data = list(reader)
        # print('data:')
        # print(repr(data))
        return data


def count_degrees_by_standardization(csv_file_name):
    """
    In this version we get a list of key, value dictionaries for each row.
    Then, compile a standardized (all upper case, remove the period) set of
     degrees, degree_list.
    From that standardized list, we create a uniq set to initialize our
     answer/output dictionary, degree_dict.
    Then use the regular expression to count occurences and update the
     dictionary.
    INPUT: filename
    OUTPUT: dictionary with degree keys and counts as values
    """
    data = read_data(csv_file_name)
    degree_list = []
    for row in data:
        for item in row['degree'].split():
            consistent_item = item.upper().replace('.', '')
            degree_list.append(consistent_item)
    degree_list.sort()
    degree_dict = {}
    degree_dict = degree_dict.fromkeys(set(degree_list), 0)
    for k in degree_dict.keys():
        regexp = re.compile(k)
        count = 0
        for d in degree_list:
            if regexp.search(d):
                count += 1
        degree_dict[k] = count
    return degree_dict


def count_degrees_by_regexp(csv_file_name):
    """
    solution degrees = ['MD', 'MA', 'SCD', 'BSED', 'PHD', '0', 'MPH', 'MS',
      'JD']
    strings present in csv file:
    {'PhD', 'MA', 'MS', 'Ph.D', '0', 'B.S.Ed.', 'MPH', 'JD', 'Ph.D.', 'M.S.',
      'ScD', 'Sc.D.', 'MD'}
    # regexp key:
    # (?i) case-insensitive
    # ^ start
    # $ end
    # \.* zero or more '.
    #

    In this version we get a list of key, value dictionaries for each row.
    Then, use a dictionary of standardized degreee regular expression to do
    the counting.  Stardize by converting to all upper case and removing
    periods.
    From that, we initialize our answer/output dictionary, degree_dict.
    Then use the regular expression to count occurences and update the
     dictionary.
    INPUT: filename
    OUTPUT: dictionary with degree keys and counts as values
    """
    degree_regexp_dict = {'MD': re.compile('(?i)^M\.*D\.*$'),
                          'MA': re.compile('(?i)^M\.*A\.*$'),
                          'SCD': re.compile('(?i)^S\.*C\.*D\.*$'),
                          'BSED': re.compile('(?i)^B\.*S\.*E\.*D\.*$'),
                          'PHD': re.compile('(?i)^Ph\.*D\.*$'),
                          '0': re.compile('^0$'),
                          'MPH': re.compile('(?i)^M\.*P\.*H\.*$'),
                          'MS': re.compile('(?i)^M\.*S\.*$'),
                          'JD': re.compile('(?i)^J\.*D\.*$'),
                          }
    data = read_data(csv_file_name)
    degree_list = []
    for row in data:
        for item in row['degree'].split():
            degree_list.append(item)
    degree_dict = {}
    degree_dict = degree_dict.fromkeys(set(degree_regexp_dict), 0)
    for k in degree_dict.keys():
        regexp = degree_regexp_dict[k]
        count = 0
        for d in degree_list:
            if regexp.search(d):
                count += 1
        degree_dict[k] = count
    return degree_dict


def count_degrees(csv_file_name):
    return count_degrees_by_regexp(csv_file_name)


try:
    degreecounts = count_degrees('faculty.csv')
    os.remove('faculty.csv')
except Exception as e:
    os.remove('faculty.csv')
    raise(e)

degreecounts = {
    str(key).replace(' ', '').replace('.', '').upper(): val
    for key, val in degreecounts.items()
}

degrees = ['MD', 'MA', 'SCD', 'BSED', 'PHD', '0', 'MPH', 'MS', 'JD']
assert len(degrees) >= len(degreecounts),\
        'did you get all the different degrees?'
assert len(degrees) == len(degreecounts),\
        'your output has too many degrees'
for degree in degrees:
    count = degreecounts.get(degree, -1)
    print(count)
