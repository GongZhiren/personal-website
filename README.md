# Zhiren Gong - Academic Homepage

Personal academic website for Zhiren Gong.

## Local Preview

```bash
cd "/scratch/gongzhiren/personal"
python -m http.server 8090
```

Open: `http://localhost:8090`

## Project Structure

- `index.html`: page layout and content
- `styles.css`: styling and responsive layout
- `script.js`: tab switching, smooth navigation, and TL;DR toggles
- `assets/`, `paper_picture/`, `icon/`, `logo/`: images and visual assets

## Open Source and Deployment

1. Create a public GitHub repository (for example: `GongZhiren-homepage`).
2. Add remote and push:

```bash
cd "/scratch/gongzhiren/personal"
git remote add origin https://github.com/<your-username>/<repo-name>.git
git branch -M main
git push -u origin main
```

3. Enable GitHub Pages:
   - `Settings -> Pages`
   - Source: `Deploy from a branch`
   - Branch: `main`, folder: `/ (root)`

Your site URL will be:
`https://<your-username>.github.io/<repo-name>/`

## License

MIT License. See `LICENSE`.
