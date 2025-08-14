# 🚀 Vercel Deployment Guide for UBS-CS Integration Control Tower

## 📋 **Prerequisites**
- Vercel account at [https://vercel.com/rahuul-pandes-projects](https://vercel.com/rahuul-pandes-projects)
- GitHub repository with your code
- Node.js installed locally

## 🔧 **Step-by-Step Deployment**

### **Step 1: Prepare Your Repository**
```bash
# Ensure all changes are committed
git add .
git commit -m "Prepare for Vercel deployment"
git push origin main
```

### **Step 2: Deploy to Vercel**

#### **Option A: Deploy via Vercel Dashboard**
1. Go to [https://vercel.com/rahuul-pandes-projects](https://vercel.com/rahuul-pandes-projects)
2. Click "New Project"
3. Import your GitHub repository
4. Configure build settings:
   - **Framework Preset**: Create React App
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `build`
5. Click "Deploy"

#### **Option B: Deploy via Vercel CLI**
```bash
# Install Vercel CLI
npm i -g vercel

# Navigate to frontend directory
cd frontend

# Deploy
vercel

# Follow the prompts:
# - Link to existing project or create new
# - Set project name: "ubs-cs-integration-control-tower"
# - Confirm build settings
```

### **Step 3: Configure Environment Variables**
In Vercel dashboard, add these environment variables:
```
NODE_ENV=production
REACT_APP_DEMO_MODE=true
```

### **Step 4: Custom Domain (Optional)**
- Go to your project settings in Vercel
- Add custom domain if desired
- Example: `ubs-control-tower.vercel.app`

## 🎯 **What Gets Deployed**

### **✅ Frontend Components**
- React application with Material-UI
- D3.js service mesh visualization
- Three.js 3D risk heatmap
- Testing dashboard with animations
- Professional contact panel

### **✅ Demo Mode Features**
- Simulated WebSocket connection
- Mock data for testing scenarios
- Interactive UI without backend dependency
- Perfect for portfolio showcase

### **❌ Backend Services (Not Deployed)**
- FastAPI orchestrator
- Mock microservices
- WebSocket real-time updates

## 🔄 **Post-Deployment**

### **Test Your Live App**
1. Visit your Vercel URL
2. Test all tabs and features
3. Verify contact buttons work
4. Check responsive design

### **Update Your Resume**
Add this line to your resume:
```
UBS-CS Integration Control Tower: [https://your-app.vercel.app](https://your-app.vercel.app)
- AI-powered microservices testing platform
- Built with React, D3.js, and Three.js
- Demonstrates test automation and banking integration expertise
```

## 🚨 **Troubleshooting**

### **Build Errors**
```bash
# Clear cache and rebuild
cd frontend
rm -rf node_modules package-lock.json
npm install
npm run build
```

### **Deployment Issues**
- Check Vercel build logs
- Verify build command and output directory
- Ensure all dependencies are in package.json

### **Performance Optimization**
- Enable Vercel Analytics
- Configure caching headers
- Optimize images and assets

## 📱 **Mobile Optimization**
Your app is already mobile-responsive with:
- Material-UI responsive design
- Touch-friendly interactions
- Optimized viewport settings

## 🎉 **Success!**
Once deployed, you'll have:
- **Live URL** for your resume
- **Professional portfolio** showcasing your skills
- **Interactive demo** for recruiters
- **Mobile-friendly** application

## 🔗 **Next Steps**
1. Deploy to Vercel
2. Test all features
3. Add URL to resume
4. Share with recruiters
5. Consider adding analytics

---

**Need Help?** Check Vercel documentation or contact support through your dashboard.
