#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4 colorcolumn=120 expandtab

import os
import sys
import git


def get_git_root(path):
    git_repo = git.Repo(path, search_parent_directories=True)
    git_root = git_repo.git.rev_parse("--show-toplevel")
    return git_root


def repo_dir():
    return get_git_root(os.getcwd())


try:
    sys.path.insert(0, repo_dir())
except git.exc.InvalidGitRepositoryError:
    print('cannot find git repo using {dir}, please put working directory into PYTHONPATH'.format(dir=os.getcwd()))
