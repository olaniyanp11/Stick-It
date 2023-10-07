# Stick-It
A project to be done by 4 men who plan to reshape the future

Stick-It is made using Django Rest Framework, SASS, React, and Redis.

## Features
- Register and Login
    - JWT Authentication to connect DRF and React
    - Can login with username or email
- Projects (Teams)
    - Create Projects
    - Invite members to join projects via one time link
    - Change member access level - Admin or Normal
        - Admin can edit project details, invite new members, and change other members' access levels.
- Boards
    - Create personal boards or project boards
    - Recently Viewed Boards
    - Starred Boards
    - Create and reorder lists
    - Create, reorder, and change list of cards
        - Add labels to cards
        - Assign members to cards
        - Add attachments to cards
        - Add comments to cards
    - Search
        - Autocomplete (Debounced)
    - Unsplash API Integration
        - Set environment variable REACT_APP_UNSPLASH_API_ACCESS_KEY with access key
    - Automatically adapt header and board title styling based on brightness of board background
- Notifications
    - When someone assigns you to a card
    - When someone comments on a card you're assigned to
    - When you're invited to a project
    - When someone makes you admin of a project

## Getting Started
1. Install [Python](https://www.python.org/downloads/), [Yarn](https://classic.yarnpkg.com/en/docs/install/), [Redis](https://redis.io/download).
2. Clone the repo
```
$ git clone https://github.com/vdevired/Stick-It.git
$ cd Stick-It
```
3. Install [pipenv](https://pypi.org/project/pipenv/), a python virtual environment manager. Install backend dependencies and run migrations to create database. Default database is SQLite.
```
$ cd backend
$ pipenv install
$ pipenv run python manage.py migrate
```
4. Install frontend dependencies.
```
$ cd frontend
$ yarn install
```
5. Run redis on port 6380
``` 
$ redis-server --port 6380
```
6. Run both frontend and backend servers with following commands in appropriate directories.
```
$ pipenv run python manage.py runserver
$ yarn start