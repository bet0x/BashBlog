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

echo "<!DOCTYPE html>";
echo "<html>";
echo "";
echo "  <head>";
echo "";
echo "    <title>Bash Blog</title>";
echo "";
echo "    <meta charset=\"utf-8\" />";
echo "    <meta name=\"description\" content=\"This is a blog in Bash CGI.\" />";
echo "    <meta name=\"keywords\" content=\"bash, cgi, blog\" />";
echo "    <meta name=\"author\" content=\"A Guy in a Room, Being\" />";
echo "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />";
echo "";
echo "    <link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\" />";
echo "";
echo "  </head>";
echo "  <body>";
echo "		<h1 class=\"blue\">The Bash Blog</h1>";
echo "		<h2 class=\"red\">something would be here</h2>"

shopt -s nullglob

POSTSPERPAGE='8'
ARR=(posts/*)
TOTALPOSTS="${#ARR[@]}"
NUMPAGES=$(($TOTALPOSTS/$POSTSPERPAGE))
PAGE=${ARGUMENTS[page]}

if [[ ! $PAGE =~ ^[0-9]+$ ]]; then
	PAGE=1
elif [[ $PAGE -lt 0 ]] || [[ $PAGE -gt $NUMPAGES ]]; then
	PAGE=1
fi

MIN=0
MAX=$(( ${#ARR[@]} - 1 ))
while [[ $MIN -lt $MAX ]]; do
	X="${ARR[$MIN]}"
	ARR[$MIN]="${ARR[$MAX]}"
	ARR[$MAX]="$X"
	(( MIN++, MAX-- ))
done

if [[ $PAGE -gt 1 ]]; then
	SUB=$(( $PAGE - 1 ))
	TOSUB=$(($SUB*$POSTSPERPAGE))
	ARR=( ${ARR[@]:$TOSUB} )
	echo "<p>Page $PAGE of $NUMPAGES</p>"
fi

for (( I=0; I<$POSTSPERPAGE; I++)); do
	POST=${ARR[$I]}
	FILENAME=$(echo ${POST/^posts\///})
	printf "<div style='padding-left:2px;border:5px solid #ccc;margin-bottom:6px;background-color:#333;'><p><a href=\"posts.cgi?post=$FILENAME&page=$PAGE\">$(egrep '^# ' $POST | cut -f2- -d' ')</a> &nbsp; &#8674; &nbsp; $(egrep -v "^#" $POST | egrep -v "^$" | head -n1 | cut -c1-255 | markdown) </div>";
done

printf "<br /><p class=\"center blue\">";
for (( NUM = 1; NUM <= $NUMPAGES; NUM++ )); do
	if [ $NUM -lt $NUMPAGES ]; then
		printf "<a href=\"index.cgi?page=$NUM\"><b>$NUM</b></a> | "
	else
		printf "<a href=\"index.cgi?page=$NUM\"><b>$NUM</b></a></p><br />"
	fi
done

echo "    <p class=\"small red center\">&copy; MMXXII, example.com</p>"
echo "  </body>";
echo "</html>";
