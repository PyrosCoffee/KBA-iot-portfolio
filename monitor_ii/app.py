from flask import Flask, render_template, jsonify
from db import CPU, Storage, Base
from flask_cors import CORS

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

