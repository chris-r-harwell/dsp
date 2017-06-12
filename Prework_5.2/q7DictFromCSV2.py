#!/bin/python3

import csv
import os
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
        reader = csv.reader(f)
        return list(reader)


def get_dict():
    data = read_data('faculty.csv')
    faculty_dict = {}
    for row in data[1:]:
        name_tuple = tuple(row[0].split())
        the_rest = row[1:]
        faculty_dict[name_tuple] = list(the_rest)
    return faculty_dict


answer = get_dict()
for key, val in answer.items():
    assert '{key},{val}'.format(key=' '.join(key), val=','.join(val)) in facultycsv
assert len(answer) == facultycsv.count('\n')
print(1)
