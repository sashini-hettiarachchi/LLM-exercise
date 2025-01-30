### **🚀 Quick Setup Guide**  

#### **1️⃣ Set Up Virtual Environment**  
```bash
python -m venv venv  
source venv/bin/activate  # For Mac/Linux  
venv\Scripts\activate  # For Windows  
```

#### **2️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt  
```

#### **3️⃣ Run the App**  
```bash

uvicorn main:app --host 0.0.0.0 --port 8000 --reload  
```

#### **4️⃣ Test the App**  
- Copy and paste the **generated API token** into `request.py`.  
- Run:  
  ```bash
  python request.py  
  ```

✅ **Done! Your API is now running! 🚀**