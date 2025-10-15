# Deploying to Vercel 🚀

This guide will help you deploy your Diet Recipe Generator app to Vercel.

## Prerequisites

1. A Vercel account (sign up at https://vercel.com)
2. Git repository (optional but recommended)
3. Vercel CLI installed (optional but helpful)

## Method 1: Deploy via Vercel Dashboard (Easiest)

### Step 1: Push to GitHub

1. Initialize git repository (if not already done):
```bash
git init
git add .
git commit -m "Initial commit - Diet Recipe Generator"
```

2. Create a new repository on GitHub

3. Push your code:
```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Vercel

1. Go to https://vercel.com/dashboard
2. Click **"Add New..."** → **"Project"**
3. Import your GitHub repository
4. Vercel will auto-detect the configuration from `vercel.json`
5. Click **"Deploy"**
6. Wait for the deployment to complete (usually 1-2 minutes)
7. You'll get a live URL like: `https://your-app-name.vercel.app`

## Method 2: Deploy via Vercel CLI

### Step 1: Install Vercel CLI

```bash
npm install -g vercel
```

### Step 2: Login to Vercel

```bash
vercel login
```

### Step 3: Deploy

From your project directory:

```bash
vercel
```

Follow the prompts:
- **Set up and deploy?** → Yes
- **Which scope?** → Select your account
- **Link to existing project?** → No
- **Project name?** → cookbook-app (or your preferred name)
- **Directory?** → ./
- **Override settings?** → No

For production deployment:
```bash
vercel --prod
```

## Configuration Files Created

1. **`vercel.json`** - Vercel configuration
   - Specifies Python runtime
   - Routes all requests to the FastAPI app

2. **`.vercelignore`** - Files to exclude from deployment
   - Ignores cache, virtual environments, etc.

3. **`index.py`** - Entry point for Vercel
   - Imports and exposes the FastAPI app

## Environment Variables

This app doesn't require any environment variables on Vercel since users provide their own OpenAI API keys through the web interface.

If you want to provide a default API key (not recommended for security), you can add it in Vercel:

1. Go to your project in Vercel Dashboard
2. Click **Settings** → **Environment Variables**
3. Add: `OPENAI_API_KEY` with your key

## Post-Deployment

After deployment:

1. Visit your deployed URL
2. Test the app by:
   - Entering an OpenAI API key
   - Selecting a diet preference
   - Generating a recipe

## Troubleshooting

### Issue: Build fails

**Solution:** Make sure all files are committed and pushed:
```bash
git add .
git commit -m "Add deployment files"
git push
```

### Issue: Application Error

**Solution:** Check Vercel logs:
1. Go to Vercel Dashboard
2. Select your project
3. Click on the failed deployment
4. View the **Function Logs**

### Issue: API key not working

**Solution:** 
- Verify the API key is correct
- Ensure you have GPT-4 access on your OpenAI account
- Check OpenAI API status

### Issue: Cold start delays

**Note:** Serverless functions on Vercel may have cold starts (3-10 seconds) if the app hasn't been used recently. This is normal for free tier.

## Updating Your Deployment

Every time you push to your main branch, Vercel will automatically redeploy:

```bash
git add .
git commit -m "Update app"
git push
```

Or manually trigger a deployment:
```bash
vercel --prod
```

## Custom Domain (Optional)

1. Go to your project in Vercel Dashboard
2. Click **Settings** → **Domains**
3. Add your custom domain
4. Follow DNS configuration instructions

## Free Tier Limits

Vercel Free Tier includes:
- 100GB bandwidth per month
- Unlimited deployments
- Automatic HTTPS
- Serverless function executions

This is more than enough for a personal diet recipe app!

## Production Checklist

- [ ] Test the app locally
- [ ] Push all changes to Git
- [ ] Deploy to Vercel
- [ ] Test the deployed app
- [ ] Verify recipe generation works
- [ ] Share your URL! 🎉

## Support

- Vercel Documentation: https://vercel.com/docs
- Vercel Community: https://github.com/vercel/community

Your app should now be live! 🚀

