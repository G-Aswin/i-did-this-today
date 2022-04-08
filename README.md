# i-did-this-today
A web application built using Flask in the backend and a simple frontend which aims to help track the user's task throughout their day.<br>
Ultimately a tool to put a check on procrastination 👀

## Motivation behind making <strong>i-did-this-today</strong>
- At the time, I was just starting to prepare for GATE 2022, I felt a need for an application where I could post what am I spending my time on a daily basis, so I could analyse it later.

- I realized the scope for making something of my own to fit my needs perfectly, so I started working on this project.

- I wanted a website which is accessible from anywhere, hence it's deployed on Heroku @ http://i-did-this-today.herokuapp.com/.


## Components of i-did-this-today
- **Frontend** : Written using simple HTML, CSS, JS and Bootstrap. I did not want to do anything fancy with the frontend, its functional and serves the data sent off from the backend of this application.

- **Backend** : A combination of Flask Server and Heroku Postgres Database
    - Server : Written using Flask Framework(Python). It is simple and functional. All the application login including authentication is written there. Google OAuth is used for authentication purpose.
    - Database : A heroku postgres database is used which is hosted online. Using this database was an obvious choice because the application itself is hosted in Heroku.

## To-do List
- [X] Working Authentication
- [X] Add and view tasks.
- [ ] Visualize hours using Chart.js graphs
- [ ] Code Cleanup
