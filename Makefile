SITE_DIR = ./_site
IGNORE_URLS = /twitter.com/,/x.com/,/linkedin.com/

.PHONY: build serve proof proof-external clean

build:
	bundle exec jekyll build

serve:
	bundle exec jekyll serve

proof: build
	bundle exec htmlproofer $(SITE_DIR) \
		--disable-external \
		--no-enforce-https \
		--assume-extension .html \
		--ignore-urls "$(IGNORE_URLS)"

proof-external: build
	bundle exec htmlproofer $(SITE_DIR) \
		--no-enforce-https \
		--assume-extension .html \
		--ignore-urls "$(IGNORE_URLS)" \
		--ignore-status-codes "0,429,999"

clean:
	bundle exec jekyll clean
