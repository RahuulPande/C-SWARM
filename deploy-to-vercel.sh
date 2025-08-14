#!/bin/bash

echo "🚀 Deploying UBS-CS Integration Control Tower to Vercel..."
echo "=================================================="

# Check if Vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "📦 Installing Vercel CLI..."
    npm install -g vercel
fi

# Navigate to frontend directory
cd frontend

echo "🔨 Building the application..."
npm run build

if [ $? -eq 0 ]; then
    echo "✅ Build successful!"
    echo "🚀 Deploying to Vercel..."
    
    # Deploy to Vercel
    vercel --prod
    
    echo "🎉 Deployment complete!"
    echo "📱 Your app is now live on Vercel!"
    echo "🔗 Add the URL to your resume and share with recruiters!"
else
    echo "❌ Build failed! Please check the errors above."
    exit 1
fi
