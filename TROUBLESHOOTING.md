# GitHub Pages Troubleshooting Guide

## Your Site URL
**Exact URL to use:**
```
https://vschetinger.github.io/GBG-Practice-Mode/#/practice
```

**Important:** You MUST include `#/practice` at the end!

## Common Issues & Solutions

### 1. Site Shows Blank Page or 404

**Check:**
- Are you using the exact URL with the hash route? 
- Wrong: `https://vschetinger.github.io/GBG-Practice-Mode/`
- Correct: `https://vschetinger.github.io/GBG-Practice-Mode/#/practice`

**Fix:**
- Wait 2-5 minutes after enabling GitHub Pages (deployment takes time)
- Hard refresh: `Ctrl+Shift+R` (Windows/Linux) or `Cmd+Shift+R` (Mac)
- Try incognito/private browsing mode

### 2. JavaScript Not Loading

**Check browser console:**
1. Open the site in your browser
2. Press `F12` (or right-click → Inspect)
3. Go to "Console" tab
4. Look for red error messages

**Common errors:**
- `404` on JavaScript files → Asset paths might be wrong
- `CORS` errors → GitHub Pages cache issue (wait a few minutes)
- Network errors → Check your internet connection

### 3. Assets Not Loading

**Verify files exist:**
- Open: `https://vschetinger.github.io/GBG-Practice-Mode/static/js/main.c74a3d2d.js`
- Should show JavaScript code (not 404)

**If 404:**
- GitHub Pages might still be building
- Wait 5-10 minutes and try again
- Check repository settings to ensure `gh-pages` branch is selected

### 4. Site Shows but Practice Page Doesn't Load

**Check:**
- Make sure you're using HashRouter (we are)
- URL must have `#/practice`
- Try navigating directly: Type the full URL in address bar

### 5. Images Not Showing

**Check:**
- Images are in `images/` folder (1279 files)
- First image test: `https://vschetinger.github.io/GBG-Practice-Mode/images/A1012.2.png`
- Should display an image (not 404)

**If images 404:**
- They might still be uploading (we pushed them in batches)
- Wait a few more minutes
- Check repository to verify all batches were pushed

## Quick Diagnostic Test

Run these URLs in your browser to test:

1. **Main page:** `https://vschetinger.github.io/GBG-Practice-Mode/`
   - Should load index.html

2. **Practice route:** `https://vschetinger.github.io/GBG-Practice-Mode/#/practice`
   - Should show the Practice Mode UI

3. **JavaScript:** `https://vschetinger.github.io/GBG-Practice-Mode/static/js/main.c74a3d2d.js`
   - Should show JavaScript code (long text)

4. **CSS:** `https://vschetinger.github.io/GBG-Practice-Mode/static/css/main.461de180.css`
   - Should show CSS code

5. **Test image:** `https://vschetinger.github.io/GBG-Practice-Mode/images/A1012.2.png`
   - Should show a PNG image

## Still Not Working?

1. **Check GitHub Pages build status:**
   - Go to: `https://github.com/vschetinger/GBG-Practice-Mode/settings/pages`
   - Look for build status/errors

2. **Verify branch:**
   - Settings → Pages → Source should be `gh-pages` branch
   - Folder should be `/ (root)`

3. **Wait longer:**
   - First deployment can take 5-15 minutes
   - Subsequent updates: 1-5 minutes

4. **Clear browser cache:**
   - Hard refresh: `Ctrl+Shift+R` or `Cmd+Shift+R`
   - Or clear browser cache completely

5. **Try different browser:**
   - Test in Chrome, Firefox, Safari, or Edge
   - Rules out browser-specific issues

## If All Else Fails

The deployment script and all files are in place. If nothing works after waiting 10-15 minutes:

1. Check the browser console for specific errors
2. Verify GitHub Pages is enabled in repository settings
3. Try accessing the site from a different network/device

