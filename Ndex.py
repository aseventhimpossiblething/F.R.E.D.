import CommunityUpdatesProcess
import fileHandler
import os
from flask import Flask, Markup, render_template, request
from flask import send_file
from flask import send_from_directory
from datetime import datetime




app = Flask(__name__,"/static/")


@app.route('/testofjs')
def tstfjs():
 return '  GO BDX F.R.E.D. inistiative!!! '

   



if __name__=='__main__':
    app.run()

