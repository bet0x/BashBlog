#!/bin/bash
printf "Content-type: text/html\n\n"

saveIFS=$IFS
IFS='=&'
parm=($QUERY_STRING)
IFS=$saveIFS

declare -A ARGUMENTS
for ((i=0; i<${#parm[@]}; i+=2))
do
    ARGUMENTS[${parm[i]}]=${parm[i+1]}
done

POST="${ARGUMENTS[post]}"
PAGE="${ARGUMENTS[page]}"
TITLE=$(egrep '^# ' $POST | cut -f2- -d' ')

source config
source header.include

egrep -v "^# " $POST | egrep -v "^tags: "| markdown

echo "    <p><a href=\"index.cgi?page=$PAGE\">&#8672; back</a></p>";

source footer.include
