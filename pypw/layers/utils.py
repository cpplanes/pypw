#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# utils.py
#
# This file is part of pypw, a software distributed under the MIT license.
# For any question, please contact one of the authors cited below.
#
# Copyright (c) 2017
# 	Olivier Dazel <olivier.dazel@univ-lemans.fr>
# 	Mathieu Gaborit <gaborit@kth.se>
# 	Peter Göransson <pege@kth.se>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#


from .fluid import transfert_fluid
from .elastic import transfert_elastic

def generic_layer(medium):
    if medium.MODEL == 'fluid':
        return transfert_fluid
    if medium.MODEL == 'pem' and medium.MEDIUM_TYPE.startswith('eqf'):
        return transfert_fluid
    if medium.MODEL == 'elastic':
        return transfert_elastic


