# Bash Blog Thing

## Blog Engine in Bash, Why Not?

### SUMMARY

The idea here is that you can just upload a markdown file to the `/var/www/public/posts` directory, and every thing else is automatic. The main rules are that the post has to be named `YYYY-MM-DD_Title-of-the-post.md` and the first line in the markdown file needs to be a heading with the title.

### INSTALLATION

As root, just type `make install` within this archive. There is one configurable option within the make file, and that is the installation prefix. It will default to `/`. There is a `make uninstall` as well if you decide you hate it, and there is a `make reinstall` if you modify something and make the script worse.

I use John Gruber's `markdown` which is written in Perl, and can be installed on Debian/Ubuntu via `apt install markdown`. You can use any markdown parser you want if it accepts string input and outputs strings to stdout. If yours isn't named "markdown" but fits that description, just symlink it into place like `ln -s /usr/bin/whatever /usr/local/bin/markdown`.

### USAGE

You need to enable CGI in your web server. I use nginx with fcgi wrap.

### STUFF FOR THE FUTURE

* Comments
* Tags and tag navigation
* Search
* RSS

---

### LICENSE

This software is licensed under terms of the [Absurd License](https://absurd.wtf/licentiam_absurdum.html).

