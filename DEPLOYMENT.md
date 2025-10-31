# Deployment Workflow

## Standard Development-to-Deployment Workflow

### 1. Develop Locally
```bash
npm start
```
Test your changes at `http://localhost:3000/#/practice`

### 2. Build Production Version
```bash
npm run build
```
Creates optimized production build in `build/` folder.

### 3. Test Production Build Locally (Optional)
```bash
# Serve the build folder locally to test
npx serve -s build -l 3000
```
Visit `http://localhost:3000/#/practice` to verify production build works correctly.

### 4. Commit to Main Branch
```bash
git add .
git commit -m "Description of changes"
git push origin main
```

### 5. Deploy to GitHub Pages

**For code-only changes** (HTML, CSS, JavaScript, React components):
```bash
npm run deploy
```
This automatically:
- Runs `npm run build`
- Deploys `build/` folder to `gh-pages` branch
- Your site will be live at: `https://vschetinger.github.io/GBG-Practice-Mode/#/practice`

**For image changes** (adding/updating images in `public/images/`):
Since images total ~678MB, use the batch deployment script:
```bash
# After building
npm run build

# Run batch deployment
python3 deploy-images-batches.py
```
See `DEPLOYMENT_GUIDE.md` for detailed batch deployment instructions.

### 6. Verify Deployment
- Wait 1-5 minutes for GitHub Pages to rebuild
- Visit: `https://vschetinger.github.io/GBG-Practice-Mode/#/practice`
- Check browser console for any errors

## When to Use Batch Deployment

Use batch deployment (`deploy-images-batches.py`) only when:
- Adding new images to `public/images/`
- Updating existing images
- Initial deployment (already done)

For all other changes (code, styling, features), use `npm run deploy`.

## Notes

- The `gh-pages` branch is automatically updated by the deploy script
- Never manually edit files on `gh-pages` branch
- Always test locally before deploying
- GitHub Pages may take 1-5 minutes to reflect changes

