#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import shutil


def generate(projectpath):
    cmd = "/Applications/Unity/Unity.app/Contents/MacOS/Unity" + \
          " -quit -batchmode " + \
          " -logfile $stdout " + \
          " -createProject " + projectpath
    os.system(cmd)


def setting(projectpath):
    editordir = os.path.join(projectpath, "Assets/Editor")
    if not os.path.exists(editordir):
        os.mkdir(editordir)
    shutil.copyfile("VCS.cs", editordir + "/VCS.cs")

    cmd = "/Applications/Unity/Unity.app/Contents/MacOS/Unity" + \
          " -quit -batchmode " + \
          " -logfile $stdout " + \
          " -executeMethod VCS.Setting"
    os.system(cmd)

    shutil.rmtree(editordir)
    os.remove(editordir + ".meta")


def gitinit(projectpath):
    os.chdir(projectpath)
    os.system("git init")


def gitcommit(projectpath, summary):
    os.chdir(projectpath)
    os.system("git add --all")
    os.system("git commit -m '{0}'".format(summary))


def gitfile(sourcedir, projectpath):
    shutil.copyfile(sourcedir + "/.gitignore", projectpath + "/.gitignore")
    shutil.copyfile(sourcedir + "/.gitattributes", projectpath + "/.gitattributes")

    gitcommit(projectpath, "Initial commit")


def readme(sourcedir, projectpath, projectname):
    content = "# {0}\n".format(projectname)
    open(projectpath + "/README.md", 'w').write(content)
    gitcommit(projectpath, "Add README")


def license(sourcedir, projectpath):
    shutil.copyfile(sourcedir + "/LICENSE", projectpath + "/LICENSE")
    gitcommit(projectpath, "Add LICENSE")


def main(argv):
    projectname = ""
    projectpath = os.getcwd()
    sourcedir = os.getcwd()

    if len(argv) > 1:
        projectpath = argv[1]
    else:
        while os.path.exists(projectpath):
            projectname = raw_input("Unity project name: ")
            dir = os.path.abspath(os.getcwd() + "/../")
            projectpath = os.path.join(dir, projectname)

    print "Unity Project: " + projectpath

    generate(projectpath)
    setting(projectpath)
    gitinit(projectpath)
    gitfile(sourcedir, projectpath)
    readme(sourcedir, projectpath, projectname)
    license(sourcedir, projectpath)

    print "Job Done!"


if __name__ == "__main__":
    main(sys.argv)
