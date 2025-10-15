#!/bin/bash

# Deployment script for Diet Recipe Generator
# This script helps you deploy your app to Vercel

echo "🍽️  Diet Recipe Generator - Deployment Script"
echo "=============================================="
echo ""

# Check if vercel CLI is installed
if ! command -v vercel &> /dev/null
then
    echo "❌ Vercel CLI not found!"
    echo ""
    echo "Installing Vercel CLI..."
    npm install -g vercel
    echo ""
fi

echo "✅ Vercel CLI is installed"
echo ""

# Check if this is a git repository
if [ ! -d .git ]; then
    echo "⚠️  Not a git repository. Initializing..."
    git init
    git add .
    git commit -m "Initial commit - Diet Recipe Generator"
    echo "✅ Git repository initialized"
    echo ""
fi

echo "🚀 Deploying to Vercel..."
echo ""
echo "Choose deployment type:"
echo "1. Preview deployment (testing)"
echo "2. Production deployment"
echo ""
read -p "Enter choice (1 or 2): " choice

if [ "$choice" = "2" ]; then
    echo ""
    echo "Deploying to PRODUCTION..."
    vercel --prod
else
    echo ""
    echo "Deploying PREVIEW..."
    vercel
fi

echo ""
echo "✅ Deployment complete!"
echo ""
echo "📝 Next steps:"
echo "   1. Visit your deployment URL"
echo "   2. Enter your OpenAI API key"
echo "   3. Generate some recipes!"
echo ""
echo "Happy cooking! 🎉"

