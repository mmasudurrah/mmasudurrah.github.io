# Masudur Rahman's academic website

Public site: https://mmasudurrah.github.io/

The `site/` directory contains the complete deployable website: HTML, CSS, JavaScript, papers, images, the public CV, and compatibility routes. It does not require Jekyll, Ruby, npm, or a build service.

## Local preview and validation

```sh
python3 scripts/check_public_site.py site
python3 -m http.server 8787 --bind 127.0.0.1 --directory site
```

Open http://127.0.0.1:8787/. Serving over HTTP supports the production root-relative URLs.

## Updating content

The canonical CV, publication data, website templates, and news are maintained in the faculty materials workspace. Run its standard-library exporter to refresh this repository's public `site/` directory:

```sh
.venv/bin/python scripts/build_website_production.py --output /path/to/this/repository/site
```

The exporter refreshes the HTML CV, teaching/mentoring, full bibliography, public PDF, and news archive together. The homepage and archive share one news dataset. It checks local routes, fragments, metadata, and the manifest before export. Only public assets and rendered pages are exported; application documents and internal records stay in their source workspace.

Review the diff and run the checker before committing. `site/site-manifest.json` records the exported file checksums. Avoid hand-editing generated pages; revise their source and export again.

## Deployment

GitHub Actions validates changes on pull requests and the preparation branch. Only a successful validation on `master` deploys `site/` to the existing `gh-pages` branch. GitHub Pages continues to use `gh-pages` at `/`; no Pages settings change or external hosting service is required. `.nojekyll` marks the output as an already-built static site.

The old Jekyll source remains in Git history and in the repository during migration. Its auxiliary workflows are stored under `.github/legacy-workflows/` and do not run. The active deployment uses only `site/`.

## Analytics

The existing Google Analytics 4 property is preserved: `G-T4WV8EF43W`. Every content page loads `analytics.js`, which initializes the same Google tag once on `mmasudurrah.github.io`. Local previews do not send Analytics events. Compatibility redirects are untracked so only their destination records the page view. Changing the design does not require a new Analytics property.

## URLs and rollback

Canonical routes are `/`, `/research/`, `/publications/`, `/teaching/`, `/cv/`, and `/news/`. The old `.html` page addresses work, and `/projects/`, `/service/`, `/awards/`, project pages, and individual news announcement addresses have compatibility redirects. The previous `/assets/pdf/CV_Md_Masudur_Rahman.pdf` points to the same current CV as `/assets/cv.pdf`. Existing public paper and image assets are retained.

A custom `404.html`, canonical metadata, `robots.txt`, and sitemap are included. To undo the migration, revert its merge commit on `master`; that restores the prior deployment workflow and Jekyll source. Do not force-push deployment history.
