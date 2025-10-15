# Quick Start Guide 🚀

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
uvicorn main:app --reload

# Open in browser
open http://localhost:8000
```

## Deploy to Vercel

### Option 1: One-Line Deploy (Easiest)

```bash
./deploy.sh
```

### Option 2: Manual Deploy

```bash
# Install Vercel CLI (if not installed)
npm install -g vercel

# Deploy
vercel          # Preview deployment
vercel --prod   # Production deployment
```

### Option 3: GitHub + Vercel (Auto-deploy)

1. Push to GitHub:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

2. Go to https://vercel.com/new
3. Import your GitHub repository
4. Click Deploy

## Testing Your Deployed App

1. Visit your Vercel URL (e.g., `https://your-app.vercel.app`)
2. Enter your OpenAI API key
3. Select Vegetarian or Vegan
4. Click "Generate Recipe"
5. Enjoy your dinner! 🍽️

## Troubleshooting

**Build fails?**
- Check `vercel.json` is present
- Ensure `requirements.txt` is up to date
- View logs in Vercel dashboard

**App doesn't work?**
- Verify OpenAI API key is valid
- Check you have GPT-4 access
- Check browser console for errors

**Need help?**
- See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed guide
- Check Vercel docs: https://vercel.com/docs

## Project Structure

```
cookbook-app/
├── main.py              # Main FastAPI application
├── index.py             # Vercel entry point
├── requirements.txt     # Python dependencies
├── vercel.json          # Vercel configuration
├── package.json         # NPM metadata
├── deploy.sh            # Deployment helper script
├── README.md            # Full documentation
├── DEPLOYMENT.md        # Detailed deployment guide
└── QUICKSTART.md        # This file!
```

## Key Commands

| Command | Description |
|---------|-------------|
| `uvicorn main:app --reload` | Run locally |
| `./deploy.sh` | Deploy with helper script |
| `vercel` | Preview deployment |
| `vercel --prod` | Production deployment |
| `vercel logs` | View deployment logs |
| `vercel ls` | List deployments |

## Environment

No environment variables needed! Users provide their own OpenAI API keys through the web interface.

---

Made with ❤️ using FastAPI and OpenAI GPT-4

