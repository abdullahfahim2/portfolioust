# 🌐 Portfolio Project of Hasan Imam

A modern, fully dynamic, and visually appealing portfolio website developed for **Mr. Hasan Imam**, showcasing his professional achievements, academic contributions, publications, collaborations, gallery, and more.

This project uses **Django** as the backend framework and **Tailwind CSS** for creating a fast and responsive frontend UI.

---

### 🚀 Live Project
🔗 https://mhimam.com/

---

## ✨ Key Features

- 🏠 Dynamic home page powered by database content  
- 📄 CV download functionality  
- 📝 Dynamic blog system with slug-based URLs  
- 🎓 Education & academic thesis showcase  
- 💼 Experience timeline  
- 🏆 Achievements and current roles sections  
- 🤝 Collaboration section with timeline  
- 📬 Functional contact form with success messages  
- 🖼️ Image gallery  
- 🎬 Video gallery  
- 📲 Fully responsive with Tailwind CSS  
- 🔐 Easy content management via Django Admin panel  

---

## 🛠️ Tech Stack

| Category | Technology |
|---------|------------|
| Backend Framework | Django |
| Language | Python |
| Frontend | Tailwind CSS, HTML Templates |
| Database | SQLite / PostgreSQL |
| Messaging System | Django Messages |
| File Serving | Django File Storage |
| Deployment | Live Hosted Website |

---


## 🔗 URL Endpoints

| Page | URL |
|------|-----|
| Home | `/` |
| Blog Details | `/blog/<slug>/` |
| Image Gallery | `/imagegallery/` |
| Video Gallery | `/videogallery/` |
| Service Details | `/service/<id>/` |
| Download CV | `/download-cv/<id>/` |

---


## 👨‍💻 Developer Info

**MD Abdullah Al Fahim**   
 
📧 Email: [abdullahfahim.me@gmail.com](mailto:abdullahfahim.me@gmail.com)  
🔗 LinkedIn: [https://www.linkedin.com/in/abdullahfahim-me/](https://www.linkedin.com/in/md-abdullah-al-fahim/)  
🐙 GitHub: [https://github.com/abdullahfahim2](https://github.com/abdullahfahim2)

---

## 🧩 Setup & Installation (Local)

```bash
# Clone the repository
git clone <your-github-repo-url>
cd <project-folder>

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run Development Server
python manage.py runserver




