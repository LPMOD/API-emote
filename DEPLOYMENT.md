# 🚀 Deployment Guide - FastAPI Bot

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run bot
python main.py

# Access API
http://localhost:10000
http://localhost:10000/docs
```

---

## 🌐 Render.com Deployment

1. **Create Account** on [Render.com](https://render.com)

2. **Create New Web Service**
   - Connect your GitHub repo
   - Select branch (main/master)

3. **Configuration:**
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Plan:** Free (or paid for better performance)

4. **Deploy!** 🎉

---

## 🚂 Railway.app Deployment

1. Go to [Railway.app](https://railway.app)
2. Click "New Project"
3. Select "Deploy from GitHub"
4. Choose your repository
5. Railway auto-detects Python and deploys! ✅

---

## 🟣 Heroku Deployment

```bash
# Login to Heroku
heroku login

# Create app
heroku create your-bot-name

# Add Python buildpack
heroku buildpacks:set heroku/python

# Deploy
git push heroku main

# Open app
heroku open
```

---

## 🐳 Docker Deployment

### Build & Run
```bash
# Build image
docker build -t fastapi-bot .

# Run container
docker run -p 10000:10000 fastapi-bot
```

### Using Docker Compose
```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

---

## ☁️ AWS EC2 Deployment

```bash
# SSH into EC2
ssh -i your-key.pem ubuntu@your-ec2-ip

# Install Python & dependencies
sudo apt update
sudo apt install python3 python3-pip -y

# Clone repo
git clone your-repo-url
cd fastapi-bot

# Install dependencies
pip3 install -r requirements.txt

# Run with screen (keeps running after logout)
screen -S bot
python3 main.py
# Press Ctrl+A then D to detach
```

---

## 🔧 Environment Variables

### Set in Render/Railway/Heroku:
```
PORT=10000
BOT_UID=1482210279
BOT_PASSWORD=YOUR_PASSWORD
```

### Set Locally:
```bash
# Linux/Mac
export PORT=10000

# Windows
set PORT=10000
```

---

## 📊 Monitoring

### Check Logs
```bash
# Render: View in dashboard
# Railway: View in dashboard
# Heroku: heroku logs --tail
# Docker: docker-compose logs -f
```

### Health Check Endpoints
```bash
# Check bot status
curl http://your-domain.com/status

# Check API health
curl http://your-domain.com/
```

---

## 🛡️ Security Best Practices

1. **Never commit credentials**
   ```bash
   # Add to .gitignore
   .env
   config.py
   ```

2. **Use Environment Variables**
   ```python
   import os
   BOT_PASSWORD = os.getenv('BOT_PASSWORD')
   ```

3. **Enable HTTPS** (Render/Railway do this automatically)

4. **Rate Limiting** (consider adding to production)

---

## 🚀 Performance Tips

1. **Use Gunicorn** (for production):
   ```bash
   gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
   ```

2. **Configure Workers** based on CPU cores:
   ```bash
   workers = (2 x num_cores) + 1
   ```

3. **Enable Caching** for repeated requests

---

## 🐛 Common Issues

### Port already in use
```bash
# Find process
lsof -i :10000

# Kill process
kill -9 <PID>
```

### Module not found
```bash
pip install -r requirements.txt --force-reinstall
```

### Bot not connecting
- Check credentials
- Verify network access
- Check API endpoint URLs

---

## 📱 Mobile Access

After deployment, access from anywhere:
```
https://your-app-name.onrender.com/join?tc=ABC123&emote_id=42&uid1=123456789
```

---

## ✅ Post-Deployment Checklist

- [ ] Bot connects successfully
- [ ] `/status` endpoint works
- [ ] `/docs` accessible
- [ ] Emotes working
- [ ] Logs being generated
- [ ] Auto-restart enabled
- [ ] HTTPS enabled
- [ ] Domain configured (optional)

---

Happy Deploying! 🎉
