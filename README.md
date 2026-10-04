# Website

https://mmasudurrah.github.io/

## Preview

```sh
python3 scripts/check_public_site.py site
python3 -m http.server 8787 --bind 127.0.0.1 --directory site
```

Open http://127.0.0.1:8787/.

## Update

Refresh the generated files in `site/`, run the checker, and commit the update. The manifest contains file checksums and is refreshed with each export.

GitHub Actions validates changes and publishes `site/` from `master` to `gh-pages`. Previous source files and inactive workflows remain available in the repository.

## Analytics

The site uses Google Analytics measurement ID `G-T4WV8EF43W`. Tracking runs on the public hostname only.
