# Symptom Safari 
Come join us on the Symptomm Safari! This website is targed towards pediatric oncology patients. They are able to navigate the website and encounter different wild animals while documenting their daily symptoms. The website offers an option to even export their notes into a pdf to give to their doctor!

This website has been created with Django & Python during General Assembly's Software Engineering Bootcamp. 
![Hippo](main_app/static/images/Child-and-parent.png  "width='800' height='400'")
## Instructions
You can find the website here: https://symptom-safari-55bde9365a18.herokuapp.com/
Make sure you create a user profile. Have fun on the Safari! 
##  Sneak Peek
![Login Page](main_app/static/images/login-page.png "Login Page with a giraffe")
![About Page](main_app/static/images/About-page.png "About page with description of the app with a tiger in the background")
![Index Page](main_app/static/images/index-page.png "Index page showing abbreviated information from each note with a lion in the background")
##  Planning 
![WireFrame Login](main_app/static/images/homepg-wireframe.png "WireFrame for login page")
![WireFrame Create](main_app/static/images/create-wireframe.png "WireFrame for creating a note")
![WireFrame Index](main_app/static/images/index-wireframe.png "WireFrame for index page")
![ERD](main_app/static/images/planning-ERD.png "ERD showing user has one to many notes with many to many moods")
##  Technologies used
![PSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![Heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)
![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)
![Trello](https://img.shields.io/badge/Trello-0052CC?style=for-the-badge&logo=trello&logoColor=white)

##  Attirbutions
Fonts: https://fonts.google.com/
<br>
Illustrations and Photos: https://www.canva.com/

##  Challenges Encountered During Development
I envisioned a seamless feature for users to export their journal entries to PDF, essential for sharing with healthcare providers. Although our coursework didn't cover this, I took the initiative to research and implement it using Django. Through Django's documentation, I discovered ReportLab and swiftly set it up. I then delved deeper into customizing and designing the PDF output to ensure a user-friendly and professional result.

##  Next Steps
&#9744; Add a parent user, who is able to write their own notes. With the option for a child over 13 being able to chose if they want their parents able to see their notes.
<br>
&#9744; Add animal noises with different actions.
