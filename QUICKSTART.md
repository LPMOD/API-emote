# ⚡ QUICK START GUIDE

## 🚀 3 Steps to Run

### Step 1: Install
```bash
cd fastapi_final
pip install -r requirements.txt
```

### Step 2: Run
```bash
python main.py
```

### Step 3: Test
Open browser: `http://localhost:10000/docs`

---

## 📋 Quick Commands

```bash
# Run bot
python main.py

# Run with custom port
PORT=8000 python main.py

# Run with uvicorn (alternative)
uvicorn main:app --host 0.0.0.0 --port 10000
```

---

## 🎯 Test API

### Browser
```
http://localhost:10000/join?tc=ABC123&emote_id=42&uid1=123456789
```

### cURL
```bash
curl "http://localhost:10000/join?tc=ABC123&emote_id=42&uid1=123456789"
```

---

## 📚 Documentation

- **Swagger UI:** http://localhost:10000/docs
- **ReDoc:** http://localhost:10000/redoc
- **Status:** http://localhost:10000/status

---

## ✅ What You Get

✨ **Ultra Fast FastAPI**  
📚 **Automatic API Docs**  
🔥 **Optimized Performance**  
🛡️ **Better Error Handling**  
🚀 **Production Ready**  

---

## 🆘 Quick Troubleshoot

**Bot not connecting?**
→ Check credentials in `main.py` line 596-598

**Port in use?**
→ Change port: `PORT=8000 python main.py`

**Missing modules?**
→ Reinstall: `pip install -r requirements.txt --force-reinstall`

---

## 📱 API Endpoints Summary

| Endpoint | Description |
|----------|-------------|
| `GET /` | Health check |
| `GET /status` | Bot status |
| `GET /join` | Perform emote |
| `GET /docs` | API documentation |

---

## 🎮 Example Usage

```python
import requests

response = requests.get(
    "http://localhost:10000/join",
    params={
        "tc": "ABC123",
        "emote_id": "42",
        "uid1": "123456789"
    }
)
print(response.json())
```

---

**Happy Coding! 🎉**
