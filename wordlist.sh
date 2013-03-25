#!/usr/bin/env bash

tr=tr
uniq=uniq

if [ `uname` = "Darwin" ] ; then
    # use ucsort as sort AND gsort are broken on the Mac
    # install ucsort via CPAN package Unicode::Tussle
    sort=ucsort
    sed="sed -E"
else
    sed = sed
    sort = sort
    sed="sed -r"
fi


$sed -e '/^(-|\+{3}|@@)/d;' |
    $tr A-ZÄÖÜ a-zäöü |
    $tr -sc 'A-ZÄÖÜa-zäöüß-' '\012' |
    $sort |
    $uniq -c
