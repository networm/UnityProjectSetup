#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import shutil
import platform
import subprocess


environment = {
    "Windows":{
        "Unity": r"C:\Program Files\Unity\Editor\Unity.exe",
        "Git": r"C:\Program Files\Git\bin\git.exe"
    },
    "Darwin": {
        "Unity": "/Applications/Unity/Unity.app/Contents/MacOS/Unity",
        "Git": "git"
    }
}


def generate(unity, projectpath):
    cmd = [unity,
           "-quit",
           "-batchmode",
           "-logfile",
           "-createProject", projectpath]
    subprocess.call(cmd)



def setting(unity, sourcedir, projectpath):
    editordir = os.path.abspath(os.path.join(projectpath, "Assets/Editor"))
    if not os.path.exists(editordir):
        os.mkdir(editordir)
    shutil.copyfile(os.path.join(sourcedir, "VCS.cs"), os.path.join(editordir, "VCS.cs"))

    cmd = [unity,
           "-quit",
           "-batchmode",
           "-logfile",
           "-projectpath", projectpath,
           "-executeMethod", "VCS.Setting"]
    subprocess.call(cmd)

    shutil.rmtree(editordir)
    os.remove(editordir + ".meta")


def gitinit(git, projectpath):
    subprocess.call([git, "-C", projectpath, "init"])


def gitcommit(git, projectpath, summary):
    subprocess.call([git, "-C", projectpath, "add", "--all"])
    subprocess.call([git, "-C", projectpath, "commit", "-m", "{0}".format(summary)])


def gitfile(git, sourcedir, projectpath):
    shutil.copyfile(os.path.join(sourcedir, ".gitignore"), os.path.join(projectpath, ".gitignore"))
    shutil.copyfile(os.path.join(sourcedir, ".gitattributes"), os.path.join(projectpath, ".gitattributes"))

    gitcommit(git, projectpath, "Initial commit")


def readme(git, sourcedir, projectpath, projectname):
    content = "# {0}\n".format(projectname)
    open(os.path.join(projectpath, "README.md"), 'w').write(content)
    gitcommit(git, projectpath, "Add README")


def license(git, sourcedir, projectpath):
    shutil.copyfile(os.path.join(sourcedir, "LICENSE"), os.path.join(projectpath, "LICENSE"))
    gitcommit(git, projectpath, "Add LICENSE")


def main(argv):
    projectname = ""
    projectpath = os.path.dirname(os.path.realpath(__file__))
    sourcedir = os.path.dirname(os.path.realpath(__file__))

    if len(argv) > 1:
        projectname = os.path.basename(argv[1])
        print(projectname)
        projectpath = argv[1]
    else:
        while os.path.exists(projectpath):
            projectname = raw_input("Unity project name: ")
            dir = os.path.abspath(os.path.join(projectpath, os.path.pardir))
            projectpath = os.path.join(dir, projectname)

    print "Unity Project: " + projectpath

    projectpath = os.path.abspath(projectpath)

    unity = environment[platform.system()]["Unity"]
    git = environment[platform.system()]["Git"]

    generate(unity, projectpath)
    setting(unity, sourcedir, projectpath)
    gitinit(git, projectpath)
    gitfile(git, sourcedir, projectpath)
    readme(git, sourcedir, projectpath, projectname)
    license(git, sourcedir, projectpath)

    print "Job Done!"


if __name__ == "__main__":
    main(sys.argv)
