# Emmanuel Echefu — Portfolio

Ready-to-publish HTML, CSS, JavaScript, images and PDFs for emmanuelechefu.com.
No npm installation, server-side code or build step is required.

## Update the existing GitHub Pages site

1. Download a backup of your current repository (Code > Download ZIP), or keep its existing Git history.
2. Extract this ZIP on your computer. Open the GitHub repository that currently publishes emmanuelechefu.com.
3. In Settings > Pages, check the publishing branch and folder. For this static website, choose Deploy from a branch. Use your publishing branch (often main) and /(root), or /docs if you already publish from docs.
4. Copy the extracted files and folders into that publishing folder, replacing matching files. index.html must be directly in the publishing folder, not inside an extra ZIP-name folder. Include assets, about, projects, skills, experience, articles, style.css and app.js. Include CNAME and .nojekyll too. Upload the extracted contents, not the ZIP itself. GitHub Desktop is convenient for copying folders; the GitHub website's Add file > Upload files is another option.
5. Keep your existing repository history, unrelated project files and domain settings. If an old custom deployment workflow would rebuild and overwrite this static site, disable that old workflow when switching to branch publishing.
6. Commit and push the replacement files to the publishing branch.
7. In Settings > Pages, confirm the custom domain is emmanuelechefu.com. The included CNAME contains that hostname. Because you are keeping the same GitHub Pages repository and domain, your working DNS records normally stay unchanged.
8. Check the repository's Actions tab for the completed Pages deployment, then visit https://emmanuelechefu.com/. Hard-refresh if your browser shows an older version.

GitHub documentation:
- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

## What is included

- index.html: Home, which remains the landing page.
- about/index.html: About me.
- projects/index.html: Projects, including Pinned and New labels.
- skills/index.html: Skills.
- experience/index.html: Experience.
- articles/index.html: Articles/Theses and the thesis PDF link.
- style.css: Shared design, responsive layouts and animation styling.
- app.js: Mobile navigation and interactive flowing-color heading.
- assets/: All images, CV and thesis PDF.
- CNAME: emmanuelechefu.com.
- .nojekyll: Serves the static site without Jekyll processing.
- tools/build.py and tools/content.json: Optional authoring source for regenerating the HTML.

## Editing

You can edit the HTML files, style.css and app.js directly.
For repeatable content updates, edit tools/content.json (projects, skills and experience data) and tools/build.py (biography, highlights, page templates and experience summaries). Then run:

    python3 tools/build.py

The generator requires Python 3.12 or newer and no third-party packages. It overwrites the six HTML pages, so keep changes in the generator if you plan to use it again. CSS, JavaScript, images, PDFs, CNAME and .nojekyll are not overwritten.

## Preview locally

In this extracted folder run:

    python3 -m http.server 8000

Open http://localhost:8000/ in a browser. Do not double-click index.html: the site uses root-relative paths intended for a web server at the domain root. This package targets emmanuelechefu.com, not a GitHub project URL under /repository-name/.

The font stylesheet uses Google Fonts. System-font fallbacks work if that service is unavailable.

## Favicon removal

The custom favicon has been removed from all six pages and the optional generator. Replace all six HTML pages when updating. If the old icon persists, check a private browsing window because browser tabs can cache favicons.
