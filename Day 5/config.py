import os

DB_NAME = 'LeetcodeLeaderboard'
DB_USER = 'Awwab'
DB_HOST = 'localhost'
DB_PASSWORD = 'password'

SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'