#!/bin/sh
find ./ -name '*.pyc' -exec rm {} \;
find ./ -name '.*.swp' -exec rm {} \;
