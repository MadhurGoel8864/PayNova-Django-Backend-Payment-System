# PayNova

![PayNova Logo](https://github.com/MadhurGoel8864/PayNova-Django-Backend-Payment-System/blob/f81a85ef26a2e4ec3419e4ed3ae548cbaaf0f3e1/paynova_screenshots/logo.png)

**PayNova** is a modern and secure online money transfer platform built with Django. It provides users with a seamless experience to manage their finances—adding credit cards, making payments, requesting funds, and tracking transaction history. With an interactive UI and robust security, PayNova aims to be your go-to solution for all payment needs.

---

## 🚀 Live Demo

🔗 [Try PayNova Live](https://web-production-b4eb5.up.railway.app/)

---

## ScreenShots
![Home Page](https://github.com/MadhurGoel8864/PayNova-Django-Backend-Payment-System/blob/f81a85ef26a2e4ec3419e4ed3ae548cbaaf0f3e1/paynova_screenshots/main_home_page.png
)

![Features Page](https://github.com/MadhurGoel8864/PayNova-Django-Backend-Payment-System/blob/2bb5c4150a22e6ec5e742901b0a8909b86cb7f12/paynova_screenshots/features.png)

![Sign-up Page](https://github.com/MadhurGoel8864/PayNova-Django-Backend-Payment-System/blob/2bb5c4150a22e6ec5e742901b0a8909b86cb7f12/paynova_screenshots/sign_up.png)

![KYC Page1](https://github.com/MadhurGoel8864/PayNova-Django-Backend-Payment-System/blob/2bb5c4150a22e6ec5e742901b0a8909b86cb7f12/paynova_screenshots/accounts_page.png)

![KYC Page2](https://github.com/MadhurGoel8864/PayNova-Django-Backend-Payment-System/blob/2bb5c4150a22e6ec5e742901b0a8909b86cb7f12/paynova_screenshots/kyc_2.png)

![Dashboard Top](https://github.com/MadhurGoel8864/PayNova-Django-Backend-Payment-System/blob/2bb5c4150a22e6ec5e742901b0a8909b86cb7f12/paynova_screenshots/dahboard_top.png)

![Notifications](https://github.com/MadhurGoel8864/PayNova-Django-Backend-Payment-System/blob/2bb5c4150a22e6ec5e742901b0a8909b86cb7f12/paynova_screenshots/notifications.png)

![Credit Card Details](https://github.com/MadhurGoel8864/PayNova-Django-Backend-Payment-System/blob/2bb5c4150a22e6ec5e742901b0a8909b86cb7f12/paynova_screenshots/credit_card_details.png)

![Account Search Page](https://github.com/MadhurGoel8864/PayNova-Django-Backend-Payment-System/blob/2bb5c4150a22e6ec5e742901b0a8909b86cb7f12/paynova_screenshots/account_search.png)

![Amount transfer Step 2](https://github.com/MadhurGoel8864/PayNova-Django-Backend-Payment-System/blob/2bb5c4150a22e6ec5e742901b0a8909b86cb7f12/paynova_screenshots/amount_transfer_setp_2.png)

![Payment Success Page](https://github.com/MadhurGoel8864/PayNova-Django-Backend-Payment-System/blob/2bb5c4150a22e6ec5e742901b0a8909b86cb7f12/paynova_screenshots/payment_success.png)

![Transaction Details Page](https://github.com/MadhurGoel8864/PayNova-Django-Backend-Payment-System/blob/2bb5c4150a22e6ec5e742901b0a8909b86cb7f12/paynova_screenshots/transaction_details.png)



## 🌟 Features

- **User Account Management** – Create and manage personal accounts with detailed profiles.
- **Credit Card Management** – Securely add and manage credit cards.
- **Fund Loading** – Easily add funds to accounts or cards.
- **Peer-to-Peer Payments** – Send money to other users using account numbers.
- **Payment Requests** – Intuitive system to request money from other users.
- **KYC Verification** – Upload photo, identity proof, and signature for automatic verification.
- **Interactive Dashboard** – View account balance, transactions, and analytics at a glance.
- **Transaction History** – Full records of sent/received payments, deposits, and requests.
- **Notifications** – Get notified instantly on key events like payments or card additions.
- **Responsive UI** – Smooth experience on all devices (HTML, CSS, JavaScript, Bootstrap).
- **Secure Payments** – All transactions are encrypted and highly secure.

---

---

## ⚙️ Tech Stack

- **Backend:** Python, Django  
- **Frontend:** HTML, CSS, JavaScript, Bootstrap  
- **Database:** PostgreSQL  
- **Cloud Hosting:** Railway  
- **Static Files:** AWS S3  

---
https://github.com/MadhurGoel8864/PayNova-Django-Backend-Payment-System/blob/2bb5c4150a22e6ec5e742901b0a8909b86cb7f12/paynova_screenshots/transaction_details.png
## 🛠️ Installation & Setup

### Prerequisites

- Python 3.x
- pip
- PostgreSQL

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/PayNova.git
   cd PayNova

2. **Create Virtual Environment**
    ```bash 
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate


3. **Install Dependencies**
    ```bash 
    pip install -r requirements.txt

4. **Add Environment Variables**
    ```bash 
    SECRET_KEY="YOUR_DJANGO_SECRET_KEY"
    DATABASE_URL="postgresql://YOUR_DB_USER:YOUR_DB_PASSWORD@YOUR_DB_HOST:YOUR_DB_PORT/YOUR_DB_NAME"
    ENGINE="django.db.backends.postgresql"
    NAME="YOUR_DATABASE_NAME"
    USER="YOUR_DB_USER"
    PASSWORD="YOUR_DB_PASSWORD"
    HOST="YOUR_DB_HOST"
    PORT="YOUR_DB_PORT"
    AWS_ACCESS_KEY_ID = "YOUR_AWS_ACCESS_KEY_ID"
    AWS_SECRET_ACCESS_KEY = "YOUR_AWS_SECRET_ACCESS_KEY"
    AWS_STORAGE_BUCKET_NAME = "YOUR_AWS_BUCKET_NAME"

5. **Run Migrations**
    ```bash 
    python manage.py migrate

6. **Create a Superuser**
    ```bash
    python manage.py createsuperuser

7. **Run the Server**
    ```bash
    python manage.py runserver

## ☁️ Deployment

**PayNova** is hosted on [Railway](https://railway.app/). Static files are served from **AWS S3**.

To deploy your own version:

1. Add all required environment variables in your Railway project settings.
2. Ensure your S3 bucket is correctly configured for static file access.

---

## 🤝 Contributing

We welcome contributions! Follow these steps:

### 1. Fork the repository
### 2. Create a new branch
    git checkout -b feature/your-feature-name

### 3. Make your changes

### 4. Commit the changes
    git commit -m "Add new feature"

### 5. Push to GitHub
    git push origin feature/your-feature-name

### 6. Open a Pull Request

## 📄 License
Specify your license here, e.g., MIT, GPL-3.0, etc.

---

## 📬 Contact

**Madhur Goel**  
📧 [madhurgoel1234@gmail.com](mailto:madhurgoel1234@gmail.com)  
🌐 [Portfolio](https://portfolio-madhur-bay.vercel.app)  
🔗 [LinkedIn](https://www.linkedin.com/in/madhur-goel-mg)  
🐙 [GitHub](https://github.com/MadhurGoel8864)
