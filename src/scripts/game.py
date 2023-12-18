import sys as _sys
import const as _const
import update as _update
import requests as _requests
import resources as _resources
import threading as _threading
from fake_headers import Headers as _Headers

def update(src: str = None) -> None:
    """
    这个函数将会进行一次 `requests`, 检查版本是否与最新的一致，若不一致则进行更新
    ---
    Params:
        src: 默认为版本路径, 传入版本检查的version.txt位置
    """
    # check args
    src = src if src is not None else _const.UPDATE_URL + _const.VERSION_PATH
    # create fake headers
    headers = _Headers( browser="Chrome", os="win", headers=True )
    header: str = headers.generate()
    result = _requests.get(src, headers=header)
    new_version: str = result.text

    # load current version
    current_version: str = _resources.load("version.txt").text
    if current_version != new_version:
        # TODO update files
        
        _sys.exit(0)
    return
    

    

