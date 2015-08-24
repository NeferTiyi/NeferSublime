#!/usr/bin/env python
# -*- coding: utf-8 -*-

# this must come first
from __future__ import print_function, unicode_literals, division

# standard library imports
from argparse import ArgumentParser
import os
import fnmatch
import platform
# import os.path
# import datetime as dt
# from dateutil.relativedelta import relativedelta
# import numpy as np

# Application library imports


########################################

def locate(pattern, root=os.curdir):
  '''
  Locate all files matching supplied filename pattern in and below
  supplied root directory.
  '''
  for path, dirs, files in os.walk(os.path.abspath(root)):
    for filename in fnmatch.filter(files, pattern):
      yield os.path.join(path, filename)


########################################
def locate_list(pattern, root=os.curdir):
  '''
  Locate all files matching supplied filename pattern in and below
  supplied root directory.
  '''
  filelist = []

  for path, dirs, files in os.walk(os.path.abspath(root)):
    for filename in fnmatch.filter(files, pattern):
      filelist.append(os.path.join(path, filename))

  return filelist


########################################
def get_arguments():
  parser = ArgumentParser()
  parser.add_argument("-v", "--verbose", action="store_true",
                      help="verbose mode")
  parser.add_argument("-s", "--operating-system", action="store",
                      type=str, default=platform.system(), dest="os",
                      choices=["Linux", "Windows"],
                      help="operating system")
  parser.add_argument("-V", "--version", action="store",
                      type=str, default="3",
                      choices=["2", "3"],
                      help="Sublime Text version")
  # parser.add_argument("-r", "--range", action="store", nargs=2,
  #                     type=string_to_date,
  #                     help="date range: ssaa-mm-jj ssaa-mm-jj")
  # parser.add_argument("-m", "--max", action="store_true",
  #                     help="plot with y_max = allocation")
  # parser.add_argument("-s", "--show", action="store_true",
  #                     help="interactive mode")
  # parser.add_argument("-d", "--dods", action="store_true",
  #                     help="copy output on dods")

  return parser.parse_args()


########################################
if __name__ == '__main__':

  # .. Initialization ..
  # ====================
  # ... Command line arguments ...
  # ------------------------------
  args = get_arguments()
  if args.verbose:
    print(args)

  # print(platform.system())
  # print(platform.release())

  if args.verbose:
    print(os.path.abspath(__file__))
    # print(os.getcwd())

  filelist = locate_list("sublime_text", os.environ["HOME"])

  for num, filename in enumerate(filelist):
    dirname = os.path.dirname(filename)
    print("{}: {}".format(num, dirname))
  choice = int(raw_input("Which one?\n"))

  st_root_dir = os.path.dirname(filelist[choice])
  print(st_root_dir)

  if args.os == "Linux":
    st_conf_dir = os.path.join(
      os.environ["HOME"], ".config",
      "sublime-text-" + args.version,
      "Packages", "User"
    )
    # ~/.config/sublime-text-3/Packages/User/

  print(st_conf_dir)

  exit()

########################################
# # !/bin/bash

# # Guess what Sublime Text binary we are going to use



# # OSX default
# SUBL="/Applications/Sublime Text 2.app/Contents/SharedSupport/bin/subl"

# # Linux if extracted to the home folder
# if [ ! -e "$SUBL" ] ; then
#     # Linux
#     SUBL="$HOME/Sublime Text 2/sublime_text"
# fi

# if [ ! -e "$SUBL" ] ; then
#     SUBL=""
# fi

# echo $SUBL
########################################
# #!/bin/bash
# #
# # Guess where Sublime Text config files are kept
# #
# #

# # OSX default
# SUBL="$HOME/Library/Application Support/Sublime Text 2/Packages/User"

# # Linux if extracted to the home folder
# if [ ! -d "$SUBL" ] ; then
#     # Linux
#     SUBL="$HOME/.config/sublime-text-2/Packages/User"
# fi

# if [ ! -d "$SUBL" ] ; then
#     SUBL=""
# fi

# echo "$SUBL"
########################################


#
# Add Sublime Text 3 aliases to shell config
#
#

# set -e

# # Where am I
# DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# CONFIG=$HOME/.bashrc

# MAGIC_LINE="source $DIR/sublime-shell-settings"

# # could not figure out how to grep something which contains expanded
# # env variables nicely
# if grep -Fq "sublime-shell-settings" "$CONFIG"
# then
#     echo "Sublime Text settings already in shell start script"
# else
#     echo "Installing shell start script helpers"

#     # Make sure there is prepending newline when inserting the command
#     echo >> $CONFIG
#     echo $MAGIC_LINE >> $CONFIG
# fi

# ST_USER=`$DIR/guess-sublime-config-location.bash`
# echo "Overriding Sublime Text configs in $ST_USER"
# if [ ! -e "$ST_USER" ] ; then
#     echo "Could not figure out where Sublime Text config files are stored. Please see guess-sublime-config-location.bash"
#     exit 1
# fi

# cp $DIR/../*.sublime-settings "$ST_USER"

# echo "You are now good to start Sublime Text"
# echo "Open a new shell to have subl command line command available and test it with command subl ."
