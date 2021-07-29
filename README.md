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

## Reference

- Git - Book: [https://git-scm.com/book/en/v2](https://git-scm.com/book/en/v2)

