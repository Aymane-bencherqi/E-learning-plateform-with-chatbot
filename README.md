# EduVerse
Our e-learning portal is a web-based application developed using the MERN 
(MongoDB, Express.js, React.js, Node.js) stack, designed to provide an efficient and 
user-friendly learning experience. The platform offers three distinct roles: Visitor, 
Student, and Admin, each with unique functionalities.

> #### The Website is live at - [EduVerse - Eleraning Portal](https://edu-verse-client.vercel.app/)
> #### Project Report - [Access Here](https://github.com/DhavalChhaylaOfficial/EduVerse/blob/main/23MCA022%2C028-Eduverse-eLearning%20Portal.pdf)
> #### Presentation - [Access Here](https://www.canva.com/design/DAGWwixlfpw/IfrYUVT8Xc-wiIoZHlM9tA/view?utm_content=DAGWwixlfpw&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h75d1eea74f) 

 
## Aim
The aim of the proposed e-learning portal is to deliver a comprehensive online 
learning experience that connects students with high-quality educational resources, 
supports career advancement through internships, and enhances skill-building with 
interactive tools like a code editor. The platform seeks to simplify course enrollment, 
streamline assessments and certifications, and provide pathways for students to 
transition into roles as instructors or interns.

## App Video

https://github.com/user-attachments/assets/49d60160-1dae-4081-b914-8641950dfe84

## Tech Stack 💻🔧 

### Frontend 🎨 : 
<img height="50" src="https://skillicons.dev/icons?i=react"> &nbsp; <img height="50" src="https://skillicons.dev/icons?i=redux"> &nbsp; <img height="50" src="https://skillicons.dev/icons?i=css"> &nbsp; <img height="50" src="https://skillicons.dev/icons?i=tailwind">


### Backend ⚙️ :
<img height="50" src="https://skillicons.dev/icons?i=nodejs"> &nbsp; <img height="50" src="https://skillicons.dev/icons?i=expressjs">


### Database 🛢️ :
<img height="50" src="https://skillicons.dev/icons?i=mongodb">

### Cloud Storage ☁️
<img height="40" src="https://github.com/vivek-panchal/Ed-Tech-Platform/blob/main/screenshots/Tech%20stack%20logo/cloudinary-logo.jpg"> &nbsp; <img height="50" src="https://skillicons.dev/icons?i=gcp">

&nbsp;

## How to Use

### 1. Create a directory EduVerse

```
mkdir EduVerse
```

### 2. Move to EduVerse directory

```
cd EduVerse
```

### 3. SetUp Client

#### 3.1 Clone or extract client github repo in current directory ( EduVerse directory )

```
git clone https://github.com/DhavalChhaylaOfficial/EduVerse-Client
```

#### 3.2 Move to frontend directory

```
cd Client
```

#### 3.3 Install dependencies of Client

```
npm i
```

#### 3.4 set/update all the values/settings of your own in .env file

```
.env
```

### 4. Move back to EduVerse directory

```
cd ..
```

### 5. SetUp Server

#### 5.1 Clone or extract backend github repo in current directory ( EduVerse directory )

```
git clone https://github.com/DhavalChhaylaOfficial/EduVerse-Server
```

#### 5.2 Move to backend directory

```
cd Server
```

#### 5.3 Install dependencies of backend

```
npm i
```

#### 5.4 set/update all the values/settings of your own in .env file

```
config/config.env
```

### 6. Run App

> #### Client will run on Port 3000 (By default)
>
> #### Server will run on Port 4000 (By default)

#### 6.1 Run Server
```
npm run dev
```

#### 6.2 Run Client (Move to Client Directory)
```
npm start
```

## Links

- #### Full Stack GitHub Repo - [Access Here](https://github.com/DhavalChhaylaOfficial/EduVerse)   
- #### Frontend GitHub Repo - [Access Here](https://github.com/DhavalChhaylaOfficial/EduVerse-Client)
- #### Backend GitHub Repo - [Access Here](https://github.com/DhavalChhaylaOfficial/EduVerse-Server)
- #### Frontend Live at - [Hosted on Vercel](https://edu-verse-client.vercel.app/)
- #### Backend Live at - [Hosted on Render](https://eduverse-server-silk.onrender.com)

&nbsp;

## Contributor

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/Neeldesaind/">
        <img src="https://avatars.githubusercontent.com/u/90563106?v=4https://avatars.githubusercontent.com/u/90563106?v=4" width="100px;" alt=""/>
        <br />
        <sub><b>Neel Desai</b></sub>
      </a>
    </td>
  </tr>
</table>

## Contributing Guidelines

- Report any issues using the GitHub issue tracker.
- Feel free to fork the repository and submit pull requests for new features or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact

For questions or feedback, contact Dhaval Chhayla at dhavalhchhayla@gmail.com.
- Version - 1.0.0
- License: DhavalChhaylaOfficial
- Author: Dhaval Chhayla

# EduVerse - Assistant Chatbot Intelligent

## 🤖 Chatbot d'Assistance Éducative

Ce projet est basé sur la plateforme EduVerse disponible sur GitHub, à laquelle j'ai ajouté un **chatbot intelligent** pour accompagner les étudiants dans leur apprentissage et les aider dans leur parcours éducatif.

## 🎯 Objectif du Chatbot

Le chatbot a été conçu pour :
- **Accompagner les étudiants** dans leur processus d'apprentissage
- **Répondre aux questions** sur les cours et le contenu éducatif
- **Fournir une assistance personnalisée** 24/7
- **Améliorer l'expérience utilisateur** de la plateforme EduVerse

## 🛠️ Technologies Utilisées pour le Chatbot

### Frontend (React.js)
- **React Hooks** : Gestion de l'état et des effets
- **Axios** : Communication avec l'API backend
- **React Icons** : Icônes pour l'interface
- **CSS personnalisé** : Style moderne et responsive

### Backend (Python/Flask)
- **Flask** : Framework web léger
- **Transformers (Hugging Face)** : Modèle de langage DistilBERT
- **PyTorch** : Framework de deep learning
- **FAISS** : Recherche vectorielle rapide
- **Flask-CORS** : Gestion des requêtes cross-origin

## 🧠 Architecture du Chatbot

### 1. Interface Utilisateur
- **Interface flottante** : Chat window positionnée en bas à droite
- **Design responsive** : S'adapte à tous les écrans
- **Animations fluides** : Transitions et effets visuels
- **Historique des conversations** : Sauvegarde des échanges

### 2. Système de Traitement
- **Modèle DistilBERT** : Compréhension du langage naturel
- **Contexte d'apprentissage** : Base de connaissances éducatives
- **Sessions utilisateur** : Personnalisation des réponses
- **Gestion des salutations** : Réponses contextuelles

## 🚀 Fonctionnalités du Chatbot

### ✅ Fonctionnalités Implémentées
- 💬 **Chat en temps réel** avec interface intuitive
- 🧠 **Intelligence artificielle** basée sur DistilBERT
- 📚 **Contexte éducatif** pour des réponses pertinentes
- 👤 **Sessions personnalisées** par utilisateur
- 🔄 **Historique des conversations** persistant
- ⚡ **Réponses rapides** avec indicateur de frappe
- 🎨 **Interface moderne** avec animations

### 🎯 Capacités d'Assistance
- **Questions sur les cours** : Explications et clarifications
- **Aide à l'apprentissage** : Conseils et méthodologies
- **Support technique** : Assistance sur l'utilisation de la plateforme
- **Motivation** : Encouragements et conseils d'étude

## 📁 Structure des Fichiers

```
EduVerse-Client/
└── src/
    └── components/
        └── Chatbot.js          # Interface utilisateur React

Eduverse-python-code/
├── app.py                      # Serveur Flask avec IA
├── context.txt                 # Base de connaissances
└── requirements.txt            # Dépendances Python
```

## 🔧 Installation et Configuration

### Prérequis
- Python 3.8+
- Node.js 14+
- React.js

### Installation du Chatbot

1. **Backend Python** :
```bash
cd Eduverse-python-code
pip install -r requirements.txt
python app.py
```

2. **Frontend React** :
```bash
cd EduVerse-Client
npm install
npm start
```

3. **Configuration** :
- Le chatbot démarre automatiquement sur le port 5001
- L'interface est accessible via le bouton flottant en bas à droite

## 🎨 Interface Utilisateur

### Design
- **Interface flottante** moderne et élégante
- **Couleurs harmonieuses** avec la charte graphique EduVerse
- **Animations fluides** pour une expérience utilisateur optimale
- **Responsive design** adapté à tous les appareils

### Interactions
- **Bouton de chat** : Icône flottante pour ouvrir/fermer
- **Zone de saisie** : Interface intuitive pour les messages
- **Historique visuel** : Distinction claire entre utilisateur et bot
- **Indicateur de frappe** : Feedback en temps réel

## 🔮 Améliorations Futures

### Fonctionnalités Planifiées
- 🎓 **Intégration avec les cours** : Réponses spécifiques par cours
- 📊 **Analytics** : Suivi des questions fréquentes
- 🌍 **Support multilingue** : Traduction automatique
- 🤝 **Intégration avec les instructeurs** : Relais vers le support humain
- 📱 **Notifications push** : Rappels et encouragements

### Optimisations Techniques
- ⚡ **Cache intelligent** : Réponses plus rapides
- 🧠 **Apprentissage continu** : Amélioration des réponses
- 🔒 **Sécurité renforcée** : Protection des données utilisateur
- 📈 **Scalabilité** : Support de nombreux utilisateurs simultanés

## 📊 Impact sur l'Apprentissage

Le chatbot contribue à :
- **Réduction du temps d'attente** pour obtenir de l'aide
- **Amélioration de l'engagement** des étudiants
- **Personnalisation de l'expérience** d'apprentissage
- **Support 24/7** sans intervention humaine
- **Réduction de la charge** sur les instructeurs

## 🤝 Contribution

Ce chatbot est une amélioration du projet EduVerse original. Les contributions pour améliorer l'assistant IA sont les bienvenues !

---

**Note** : Ce projet est basé sur EduVerse, une plateforme d'e-learning open source. Le chatbot a été développé comme une fonctionnalité supplémentaire pour améliorer l'expérience utilisateur.




