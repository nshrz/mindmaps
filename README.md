# Mind Maps site

A free website for showing mind maps. The home page is a mind map of all the maps; tap a branch to open it, tap a map to view it.

## One-time setup (about 5 minutes)

1. **Create the repository.** On github.com, click New, name it `mindmaps`, set it to **Public** (free GitHub Pages needs a public repo), and upload every file and folder in this package.
2. **Turn on the website.** Go to Settings > Pages, set Source to "Deploy from a branch", choose `main` and `/ (root)`, and save.
3. **Allow the automatic index to save.** Go to Settings > Actions > General, scroll to "Workflow permissions", choose "Read and write permissions", and save.
4. **Visit the site** at `https://YOUR-USERNAME.github.io/mindmaps/` after about a minute.

## Adding a mind map (the admin's job)

1. Make the map in any Mermaid mind map tool, or write it by hand. It should start with `mindmap` or `flowchart`.
2. Put two optional lines at the very top of the file:
   ```
   %% title: Photosynthesis
   %% category: Biology
   ```
   The title is the name shown in the menu. The category is the branch it appears under. Both are optional.
3. Upload the `.mmd` file to the `maps/` folder: open the repo on github.com, go into `maps`, click Add file > Upload files, and commit.
4. Wait about a minute. The workflow adds the map to `maps/index.json`, and it appears in the menu.

Only people with write access to the repository can add maps, so keep the repo private to you by not adding collaborators. Anyone with the website link can view the maps.

## Files

- `index.html`: the website (menu and viewer in one page).
- `maps/`: the `.mmd` mind map files. `maps/index.json` is generated automatically.
- `scripts/build_index.py`: builds the index; the workflow runs it.
- `.github/workflows/index-maps.yml`: runs the script whenever a map is added or changed.
