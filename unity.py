#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import shutil


def generate(projectpath):
    cmd = "/Applications/Unity/Unity.app/Contents/MacOS/Unity" + \
          " -quit -batchmode " + \
          " -logfile $stdout " + \
          " -createProject " + projectpath
    os.system(cmd)


def setting(projectpath):
    editordir = os.path.join(projectpath, "Assets/Editor/")
    if not os.path.exists(editordir):
        os.mkdir(editordir)
    shutil.copyfile("VCS.cs", editordir + "VCS.cs")

    cmd = "/Applications/Unity/Unity.app/Contents/MacOS/Unity" + \
          " -quit -batchmode " + \
          " -logfile $stdout " + \
          " -executeMethod VCS.Setting"
    os.system(cmd)

    shutil.rmtree(editordir)


def gitinit(projectpath):
    os.chdir(projectpath)
    os.system("git init")


def gitcommit(projectpath, summary):
    os.chdir(projectpath)
    os.system("git add --all")
    os.system("git commit -m '" + summary + "'")


def gitfile(sourcedir, projectpath):
    shutil.copyfile(sourcedir + "/.gitignore", projectpath + "/.gitignore")
    shutil.copyfile(sourcedir + "/.gitattributes", projectpath + "/.gitattributes")

    gitcommit("Initial commit")


def readme(sourcedir, projectpath, projectname):
    content = "# {0}\n".format(projectname)
    open(projectpath + "/README.md").write(content)
    gitcommit("Add README")


def license(sourcedir, projectpath):
    shutil.copyfile(sourcedir + "/LICENSE", projectpath + "/LICENSE")
    gitcommit("Add LICENSE")


def main():
    projectname = ""
    projectpath = os.getcwd()

    sourcedir = os.getcwd()
    gitinit(projectpath)
    gitfile(sourcedir, projectpath)
    readme(sourcedir, projectpath, projectname)
    license(sourcedir, projectpath)


if __name__ == "__main__":
    main()