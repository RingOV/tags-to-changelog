#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from optparse import OptionParser

parser = OptionParser()
(options, args) = parser.parse_args()

try:
    DIR_NAME = args[0]
except:
    print 'не указана папка'
    exit()

def get_tag_date(tag):
    date = os.popen('cd '+DIR_NAME+' && git log -1 --format=%ai '+tag).readlines()
    date = date[0].split()[0]
    date = date.split('-')
    date.reverse()
    date = '.'.join(date)
    return date

tags = os.popen('cd '+DIR_NAME+' && git tag').readlines()

for i in range(len(tags)-1):
    print tags[-i-1].rstrip('\n'), '(%s)'%get_tag_date(tags[-i-1])
    print '=========='
    rel_note = os.popen('cd '+DIR_NAME+' && git log '+tags[-i-2].strip()+'..'+tags[-i-1].strip()+' --pretty=format:" - %s" --reverse').readlines()
    for line in rel_note:
        print line.rstrip('\n')
    print ''
