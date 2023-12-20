from flask import Flask, render_template, redirect, url_for, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from supabase import create_client, Client
import os

load_dotenv()
url: str = os.environ.get("API_URL")
key: str = os.environ.get("API_SECRET")
supabase: Client = create_client(url, key)

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
  "admin": generate_password_hash(os.environ['ADMIN_PW']),
  "volunteer": generate_password_hash(os.environ['VOLUNTEER_PW'])
}


@auth.verify_password
def verify_password(username, password):
  if username in users and \
          check_password_hash(users.get(username), password):
    return username


@app.route("/", methods=['GET'])
def login_form():
  return render_template('plants.html')


@app.route("/input", methods=['GET'])
@auth.login_required
def species_selection():
  species_list = supabase.table("species").select(
    "plant_id,scientific_name").order('plant_id').execute()
  species_list = species_list.data
  print(species_list)
  return render_template('input.html', species_list=species_list)


@app.route("/input", methods=['POST'])
@auth.login_required
def species_was_selected():
  print("===================================")
  print(request.form["species"])
  print("===================================")
  return redirect(url_for('species_data_entry'))


@app.route("/species", methods=['POST'])
@auth.login_required
def species_data_was_entered():
  print(request.form["plant_id"])
  print(request.form["location"])
  print(request.form["flowering_stage"])
  print(request.form["number_of_inflorescences"])
  print(request.form["number_of_flowers"])
  print(request.form["fruiting_stage"])
  print(request.form["number_of_fruits"])
  print(request.form["comments"])
  userinput = {
    "plant_id": request.form["plant_id"],
    "location": request.form["location"],
    "flowering_stage": request.form["flowering_stage"],
    "number_of_inflorescences": request.form["number_of_inflorescences"],
    "number_of_flowers": request.form["number_of_flowers"],
    "fruiting_stage": request.form["fruiting_stage"],
    "number_of_infructescences": request.form["number_of_infructescences"],
    "number_of_fruits": request.form["number_of_fruits"],
    "comments": request.form["comments"]
  }
  data = supabase.table("survey_data").insert(userinput).execute()
  print(data)
  return redirect(url_for('species_selection'))


@app.route("/species/<plant_id>", methods=['GET'])
@auth.login_required
def species_data_entry(plant_id):
  plant = supabase.table("species").select("*").eq("plant_id",
                                                   plant_id).execute()
  plant = plant.data[0]
  print("=========")
  print(plant)
  print("=========")
  return render_template('species.html', plant=plant)


#If I have time I can make a fun page for 404 errors with the noplants.html file
@app.errorhandler(404)
def noplants(error):
  return render_template('noplants.html'), 404


# app.run(host="0.0.0.0", port=os.environ.get("PORT") or 5000, debug=os.environ.get("DEBUG") == "true" or False)