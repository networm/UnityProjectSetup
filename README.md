# UnityProjectSetup
Auto setup a new Unity project from scratch.

## Introduction
This tool will automatically do the following:

1. Create a new Unity project
2. Set `Version Control Mode` to `Visible Meta Files`
3. Set `Asset Serialization Mode` to `Force Text`
4. Initialize project using Git
5. Add `.gitignore` and `.gitattributes`
6. Add `README.md`
7. Add MIT-LICENSE `LICENSE`

## Usage
Method 1
```sh
$ python unity.py <path/to/new/project>
```

Method 2 will create project in `../projectname`
```sh
$ python unity.py
Unity project name: <input project name>
```
