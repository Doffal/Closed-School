# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.1
#   kernelspec:
#     display_name: kword
#     language: python
#     name: kword
# ---

import pandas as pd

Busan_Closchool = pd.read_excel('./Close_School/Busan_폐교목록.xlsx')

Busan_Closchool['급별'].isna.sum


