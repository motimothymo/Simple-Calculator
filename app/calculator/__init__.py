from flask import Blueprint, render_template, redirect, request, session
from celery import Celery

app = Celery('worker', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

calc_blueprint = Blueprint("calculator",__name__, url_prefix='/api/prime')

from . import calculator