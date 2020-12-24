"""
================================ PubRec ================================
Simple python module to query the ADS databases and:
1) get the numbers of citations of a paper (or list of papers) as 
    well as the list of authors;

This idea is inspired by filltex (https://github.com/dgerosa/filltex) 
developed by Davide Gerosa.

Usage: python pubrec.py --list file_with_list_of_bibcodes.txt
"""

from __future__ import absolute_import, print_function
import bs4 #-- BeautifulSoup for parsing html data
import sys
from tqdm import tqdm #-- to show the progress
import argparse

if sys.version_info.major>=3:
    import urllib.request as urllib
else:
    import urllib


def get_citations(ads_id):
    """This function returns the number of citations to a single entry in ADS"""
    url_contents = urllib.urlopen("https://ui.adsabs.harvard.edu/abs/"+ads_id+"/metrics").read()

    soup = bs4.BeautifulSoup(url_contents, "html.parser")
    #-- select the body of the table containing the information about citations
    tbody = soup.find("tbody")
    #-- remove the second colum which contain the description
    for td in tbody.find_all("td"):
        check = td.find("i")
        if(check != None):
            td.decompose()
    #-- save table as list of lists
    table = [[td.get_text(strip=True) for td in tr.find_all("td")] 
            for tr in tbody.find_all("tr")] 
    #-- transform list in dictionary
    dictCits = dict(table)
    return dictCits


def get_authors(ads_id):
    """This function returns the authors' list of a single entry in ADS"""
    url_contents = urllib.urlopen("https://ui.adsabs.harvard.edu/abs/"+ads_id+"/abstract").read()

    web_page = bs4.BeautifulSoup(url_contents, "html.parser")
    authors = [meta["content"] for meta in web_page.find_all("meta", {"property": "article:author"})]
  
    return authors


def arguments_parser():
    """Define some useful options"""
    parser = argparse.ArgumentParser(prog='PubRec')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-s','--single', action='extend', nargs='+', dest='ids',
            metavar='ID', help='ID(s) of the paper(s) in ADS')
    group.add_argument('-f', '--file', type=str, dest='filename',
            metavar='FILE', help='read a list of bibitems (one per row) from FILE'),
    parser.add_argument('-v','--version', action='version', version='%(prog)s 1.0')

    return parser


def main(ids, filename):
    if filename is not None:
        with open(filename, 'r') as f:
            bibcodes = f.read().splitlines()

            print('List of bibcodes: {}'.format(bibcodes))

            tot_citations = 0
            for bib in tqdm(bibcodes):
                tot_citations += int(get_citations(bib)['Total citations'])

    if ids is not None:
        tot_citations = 0
        for bib in tqdm(args.ids):
            tot_citations += int(get_citations(bib)['Total citations'])

    return tot_citations

#---------------------------------------------------------------------------
if __name__ == "__main__":

    args  = arguments_parser().parse_args()
    tot_cits = main(**args.__dict__)
    print(tot_cits)