#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from datetime import datetime
from jinja2 import Template

f = open("template_config.txt", "r")
tpl_text = f.read()
f.close()

templ = Template(tpl_text)

now = datetime.now()
now = now.strftime("%Y%m%d-%H%M%S")
f1 = open("config_{0}.txt".format(now), "w")

data = {
    ### paste data ###

    ##################
}

f1.write(templ.render(data))
f1.close()
