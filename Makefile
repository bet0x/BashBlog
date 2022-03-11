SHELL := /bin/bash
PREFIX?=/
BIN=${PREFIX}usr/bin
PUB=${PREFIX}var/www/public

install:
	@echo "Installing Bash Blog"
	install -m 500 ./usr/bin/markdown $(BIN)/
	install -m 755 ./var/www/public/posts.cgi $(PUB)
	install -m 755 ./var/www/public/index.cgi $(PUB)
	mkdir -p $(PUB)/posts
	install -m 644 ./var/www/public/style.css $(PUB)

uninstall:
	@echo "Removing Bash Blog"
	rm -fv $(BIN)/markdown $(PUB)/{posts.cgi,index.cgi,style.css}
	rmdir -v $(PUB)/posts

reinstall:
	@echo "Running reinstall"
	make uninstall && make install

