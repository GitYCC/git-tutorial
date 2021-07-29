# Git Tutorial

## 1 Getting started

### 1-1 Local setting

```
$ git config --global user.name "YC Chen"
$ git config --global user.email ycc@example.com
```

### 1-2 Git aliases

```
$ git config --global alias.co checkout
$ git config --global alias.br branch
$ git config --global alias.ci commit
$ git config --global alias.st status
```

This means that, for example, instead of typing `git commit`, you just need to type `git ci`.

### 1-3 Getting a git repository

#### Initializing a repository in an existing directory

```
$ cd git-tutorial/
$ git init
$ git remote add origin https://github.com/xxx/git-tutorial.git
```

#### Cloning an existing repository

```
$ git clone https://github.com/GitYCC/git-tutorial.git
```



## 2 Workflow of Git

### 2-1 Introduction

![](./assets/img_git_workflow.jpeg)

### 2-2 Commands of workflow

Check status of workflow:

```
$ git status
```

Show the changes in *working directory* against *staging area*:

```
$ git diff
```

Show the changes in *staging area* against *local repo.*:

```
git diff --cached
```

Add one file from *working directory* to *staging area*:

```
$ git add my_file.py
```

Revert one file from *staging area* to *working directory*:

```
$ git reset my_file.py
```

Add a piece of code from *working directory* to *staging area*:

```
$ git add -p my_file.py
```

Commit:

```
$ git commit -m "[TAG] COMMIT MESSAGE"
```

### 2-3 Git ignore

A `.gitignore` file specifies intentionally untracked files that Git should ignore. Files already tracked by Git are not affected.

Templates of `.gitignore`: [https://github.com/github/gitignore](https://github.com/github/gitignore)

### 2-4 Exercise

- Create a new branch `feature/cat` from `develop`
- Create a file `cat.py` in `src/` including following codes

```python
class Cat:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return 'Cat ' + self.name
      
    def shout(self):
      	return 'Cat ' + self.name + ': meow~'
```

- Use `git status`, `git diff` and `git diff --cached` to check
- Add `src/cat.py` to *staging area*
- Use `git status`, `git diff` and `git diff --cached` to check
- Revert `src/cat.py` back to *working directory*

- Use `git status`, `git diff` and `git diff --cached` to check
- Commit function `__init__` and `get_name` with the message "[feature] Create cat"
- Commit function `shout` with the message "[feature] Add function shout"
- Use `git log --graph` to check history



## Reference

- Git - Book: [https://git-scm.com/book/en/v2](https://git-scm.com/book/en/v2)

