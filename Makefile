SHELL := /bin/bash
PREFIX?=/var/www
PUB=$(PREFIX)/public

install:
	@echo "Installing Bash Blog"
	mkdir -p $(PUB)/posts
	install -m 750 ./var/www/public/posts.cgi $(PUB)
	install -m 750 ./var/www/public/index.cgi $(PUB)
	install -m 640 ./var/www/public/style.css $(PUB)
	install -m 640 ./var/www/public/config $(PUB)
	install -m 640 ./var/www/public/footer.include $(PUB)
	install -m 640 ./var/www/public/header.include $(PUB)

uninstall:
	@echo "Removing Bash Blog"
	rm -fv $(PUB)/{posts.cgi,index.cgi,style.css,config,footer.include,header.include}
	rmdir -v $(PUB)/posts

reinstall:
	@echo "Running reinstall"
	make uninstall && make install

