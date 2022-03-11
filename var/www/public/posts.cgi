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

echo "<!DOCTYPE html>";
echo "<html>";
echo "";
echo "  <head>";
echo "";
echo "    <title>Bash Blog: $TITLE</title>";
echo "";
echo "    <meta charset=\"utf-8\" />";
echo "    <meta name=\"description\" content=\"A blog in bash CGI.\" />";
echo "    <meta name=\"keywords\" content=\"Bash, CGI, blog\" />";
echo "    <meta name=\"author\" content=\"a guy in a room, being\" />";
echo "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />";
echo "";
echo "    <link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\" />";
echo "";
echo "  </head>";
echo "  <body>";
echo "";
echo "    <h1 class=\"blue\">Absurd: $TITLE</h1>";
echo "";

egrep -v "^# " $POST | egrep -v "^tags: "| markdown

echo "    <p><a href=\"index.cgi?page=$PAGE\">&#8672; back</a></p>";

echo "";
echo "    <p class=\"small red center\">&copy; MMXXII, example.com</p>";
echo "";
echo "  </body>";
echo "</html>";
