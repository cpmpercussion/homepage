# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Serve site locally with live reload
bundle exec jekyll serve

# Build site (outputs to _site/)
bundle exec jekyll build

# Update publications from remote BibTeX source
./get_publications.sh

# Validate HTML (uses html-proofer gem)
bundle exec htmlproofer ./_site
```

Ruby version is pinned to 3.3.9 via `.ruby-version`. Run `bundle install` after adding gems.

## Architecture

This is a **Jekyll 4** personal/academic website for Charles Martin (charlesmartin.au), deployed to GitHub Pages via Actions.

### Content collections

- **`_posts/`** — Blog posts, named `YYYY-MM-DD-slug.md`. Front matter includes `layout: post`, `title`, `date`, `category`, `tags`, and optionally `type: lab` (marks the post as appearing on the SMCCLAB lab page).
- **`_projects/`** — Portfolio project pages, using `layout: project`. Front matter includes `started`, `ended`, `image`, `image_alt`, `summary`.
- **`_lab/`** — Pages for the SMCCLAB research group section, using `layout: page`.
- **`_bibliography/publications.bib`** — BibTeX file powering the publications page via `jekyll-scholar`. Updated by running `./get_publications.sh` (fetches from a separate GitHub repo). Publications are filtered by BibTeX `keywords` field (e.g. `refereed`, `conference-paper`, `journal-article`).

### Data files (`_data/`)

- `navigation.yml` — Top nav links
- `lab-members.yml` — Current SMCCLAB members (rendered on `/lab/`)
- `lab-alumni.yml` — Former lab members
- `lab-projects.yml` — Lab project cards shown on `/lab/`

### Layouts and includes

- `_layouts/default.html` — Base layout; includes Bootstrap 5.3 (local copy), Font Awesome 6, academicons, and custom CSS from `assets/css/main.css`. Has a special `titlepage: true` front matter flag that renders the homepage hero section.
- `_layouts/post.html`, `project.html`, `page.html`, `bibliography.html` — extend `default.html`
- `_includes/` — Reusable partials: `head.html` (meta/CSS), `nav.html` (Bootstrap navbar with dark-mode toggle), `scripts.html`, plus media embeds (`youtubePlayer.html`, `vimeoPlayer.html`, `carousel.html`, `tocdiv.html`, `socialicons.html`)

### Plugins

Key Jekyll plugins configured in `_config.yml`:
- `jekyll-scholar` — Renders academic bibliography from BibTeX; config block in `_config.yml` sets CSL style, bibliography template, and grouping
- `jekyll-paginate-v2` — Paginates posts (6 per page)
- `jekyll-toc` — Auto table of contents (used in post layout via `{% include tocdiv.html %}`)
- `jekyll-seo-tag` — SEO meta tags in `<head>`

### Styling

`assets/css/main.scss` and `assets/css/bibliography.scss` are Sass source files processed by Jekyll at build time (configured via `sass:` in `_config.yml`). Bootstrap, academicons, and `image-captions.css` are pre-compiled third-party files stored directly in `assets/css/`.

### Linking between pages

Use Jekyll's `{% link %}` tag for internal links (e.g. `{% link _projects/microjam.md %}`), not bare relative paths, to get build-time link checking.

### Publications workflow

The BibTeX file is maintained externally at `cpmpercussion/cpm-website-publications-list` on GitHub. Run `./get_publications.sh` to pull the latest version and strip metadata fields that cause parsing issues. Do not edit `_bibliography/publications.bib` directly.
