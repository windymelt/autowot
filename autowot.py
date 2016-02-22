#!/usr/bin/env python

import sys
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui
import github
import run_script
import unzip
import os

def gui_main():
    app = QtGui.QApplication(sys.argv)
    main_window = QtGui.QMainWindow()
    hello_button = QtGui.QPushButton("GUI feature is under developing")
    main_window.setCentralWidget(hello_button)
    main_window.show()
    app.exec_()

def cui_main():
    repo_id = sys.argv[1]
    splited = repo_id.split('/')
    if len(splited) != 2:
        print 'Error: Invalid autowot repository specification.'
        print 'Usage: autowot user/repository'
        exit(1)
    print 'Downloading ZIP archive from github: ' + repo_id + ' [master] ...'
    user, repo = splited
    github.download_zip_from_github_repository(user, repo)
    print 'Downloading completed successfully.'
    zipname = user + '_' + repo
    print 'Unzipping ' + zipname + '.zip ...'
    unzip.unzip(zipname + '.zip')
    print 'Unzipped successfully.'
    unzippeddirname = repo + '-master'
    print 'Running script.'
    os.chdir(unzippeddirname)
    run_script.run_script('./autowot.ini')

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        gui_main()
    else:
        cui_main()
