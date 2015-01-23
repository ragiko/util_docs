#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/lib')
import mydoc

class MyDocs:
    def __init__(self, directory_path):
        self.directory_path = os.path.dirname(os.path.abspath(__file__)) + "/" + directory_path
        self.list = self.init_list()

    def init_list(self):
        path_list = self.file_list()
        doc_list = [mydoc.MyDoc(path) for path in path_list]
        return doc_list

    def file_list(self):
        file_list = os.listdir(self.directory_path)
        absolute_filepath = [self.directory_path + "/" + file_name for file_name in file_list]
        return absolute_filepath

if __name__ == "__main__":   
    docs = MyDocs("data")
    print docs.directory_path
    print docs.list

    print "loop docs"
    for doc in docs.list:
        print doc.file_path
        print doc.text().encode("utf_8")


