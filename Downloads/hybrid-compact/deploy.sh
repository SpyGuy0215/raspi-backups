#!/bin/bash

if [ -d ~/.config/conky/hybrid-compact/ ]
then
    rm -R ~/.config/conky/hybrid-compact/
    echo 'hybrid-compact uninstalled'
fi

rsync -IrW --stats --exclude={'.git','deploy.sh','readme.md','screenshots'} $(pwd) ~/.config/conky/
echo 'hybrid-compact installed'
