﻿poetry build
pip install --upgrade --force-reinstall .\dist\rinstall-0.2.3-py3-none-any.whl
if(Test-Path -Path "~\.beRi"){
    rm -Recurse ~\.beRi
}