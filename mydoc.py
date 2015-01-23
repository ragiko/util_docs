#!/usr/bin/python
# -*- coding: utf-8 -*-

# lib以下を読み込み
# http://kannokanno.hatenablog.com/entry/20130503/1367571825
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/lib')

class MyDoc:
    def __init__(self, file_path):
        self.file_path = file_path
        # TODO: cache
        # self.sentence = ""
        # self.words = []

    def text(self):
        return self.file_read(self.file_path)

    def words(self, content_poslist):
        import mecabutil    # 自作，MeCabのwrapperとそのクラス

        contents = self.file_read(self.file_path)

        # 形態素解析し，結果をWordクラスの配列に格納
        words = mecabutil.get_words(contents)

        # 形態素解析結果から，名詞の単語の表層のみを抽出
        words = [word.base_form for word in words if word.pos in content_poslist]

        return words

    # ファイルを読み込み，文字コード変換
    def file_read(self, file_path):
        import nkf
    
        # ファイルオープン
        contents = open(file_path).read()
        contents = nkf.nkf("-w -d", contents)\
                .decode("utf_8")
    
        return contents

if __name__ == "__main__":   
    doc = MyDoc("data/a.txt")
    print doc.file_path
    print doc.text().encode('utf_8')
    print doc.words([u"名詞"])
