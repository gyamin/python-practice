# python-practice

## 環境準備

### pyenv/virtualenvインストール
```
$ brew install pyenv
$ brew install pyenv-virtualenv
```

```
$ pyenv versions
* system (set by /Users/yasumasa/.pyenv/version)
```

```
$ pyenv install --list
Available versions:
  2.1.3
  2.2.3
  ...
```

```
$ cat ~/.bash_profile 
...
# pyenv
if command -v pyenv 1>/dev/null 2>&1; then
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
fi

```

```
$ pyenv install 3.6.5

$ pyenv versions
* system (set by /Users/yasumasa/.pyenv/version)
  3.6.5
```


```
$ pyenv virtualenv 3.6.5 python-practice
$ pyenv virtualenvs
  3.6.5/envs/python-practice (created from /Users/yasumasa/.pyenv/versions/3.6.5)
  python-practice (created from /Users/yasumasa/.pyenv/versions/3.6.5)
```

```
$ pyenv local python-practice

$ python -V
Python 3.6.5
```