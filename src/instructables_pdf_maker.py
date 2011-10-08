#!/usr/bin/python2.7
# -*- coding: utf-8 -*-



"""
-- instructables_pdf_maker.py --
Created on Sun Sep 11 20:34:45 2011

@licence: GNU GPL v3+
@author: Yigit Ozkan < yigitozkan2804@gmail.com >
"""
def get_html(url): #get the html source of a body
    response = urllib2.urlopen(url)
    html = response.read()
    return html

def find_all_links(html): #look up all links in a html source
    linklist = re.findall('<a href="(.*?)">',html)
    return linklist
    
def main():
    
    

if __name__ == '__main__':
    main()