#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="epasseto"
__date__ ="$09/10/2012 09:57:07$"

(A_red or A_green or A_yellow) #must have at least one color
    and not (A_red and A_green) #... but not more than one!
    and not (A_red and A_yellow)
    and not (A_green and A_yellow)
and
(B_red or B_green or B_yellow)
    and not (B_red and B_green)
    and not (B_red and B_yellow)
    and not (B_green and B_yellow)
and
(C_red or C_green or C_yellow)
    and not (C_red and C_green)
    and not (C_red and C_yellow)
    and not (C_green and C_yellow)
and
(D_red or D_green or D_yellow)
    and not (D_red and D_green)
    and not (D_red and D_yellow)
    and not (D_green and D_yellow)

and not (A_red    and B_red) #fronteer conditions (as in the graph)
and not (A_green  and B_green)
and not (A_yellow and B_yellow)
and not (C_red    and B_red)
and not (C_green  and B_green)
and not (C_yellow and B_yellow)
and not (D_red    and B_red
and not (D_green  and B_green)
and not (D_yellow and B_yellow)
and not (A_red    and C_red)
and not (A_green  and C_green)
and not (A_yellow and C_yellow)