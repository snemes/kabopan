#
#Kabopan (http://kabopan.corkami.com) public domain, readable, working pseudocode-style python

from code.playfair import *

assert encode("Hide the gold in the tree stump", "PLAYFAIR EXAMPLE") == "BMNDZBXDKYBEJVDMUIXMMNUVIF"

assert decode("BMNDZBXDKYBEJVDMUIXMMNUVIF", "PLAYFAIR EXAMPLE") == "HIDETHEGOLDINTHETREXESTUMP" # note the extra X, which is normal.