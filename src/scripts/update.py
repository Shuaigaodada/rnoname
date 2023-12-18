import os as _os
import resources as _r
import const as _const
import requests as _requests
import threading as _threading
from typing import Dict as _Dict
from fake_headers import Headers as _Headers

def update(__is_updated: bool = False) -> None:
    """
    update from github
    Params:
        __is_updated: for other scripts ref information
    Returns:
        None
    """

    # create fake headers
    headers = _Headers( browser="Chrome", os="win", headers=True )
    header: str = headers.generate()
    # first requests get update.files
    result = _requests.get(_const.UPDATE_URL + _const.UPDATE_FILES_PATH, headers=header)
    
    raw_data: str = result.text
    local_files: _Dict = dict() # need download/update's file list
    rep_files: list = list() # github link path

    for data in raw_data.splitlines():
        path = data.split("/")
        if len(path) == 1:
            local_files[data] = _r.path(path[0])
            continue
        else:
            local_files[data] = _r.get(path[0]).path(*path[1:])
            continue
    
    rep_files = [_const.UPDATE_URL + "/src/" + p for p in raw_data.splitlines()]
    files_data: _Dict[str, str] = dict()
    for name, url in zip(raw_data.splitlines(), rep_files):
        # for debug
        if name == "scripts/update.py":
            continue
        # TODO: create progress bar and update it(tqmb)
        files_data[name] = _requests.get(url, headers=header)
        
        with open(local_files[name], "w") as fp:
            fp.write(files_data[name])

update()