from flask import Flask, render_template

app = Flask(__name__)

FAPRODUCTS = [
  {
    'id': 1,
    'name': 'Advanced Choice Annuity Rates'
  },
  {
    'id': 2,
    'name': 'Choice Annuity Renewal Rates'
  },
{
    'id': 3,
    'name': 'RateTrack Annuity Rates'
  },
{
    'id': 4,
    'name': 'Total Interest Annuity Rates'
  }
]
FIAPRODUCTS = [
  {
    'id': 5,
    'name': 'ClearLine Annuity Rates'
  },
  {
    'id': 6,
    'name': 'Foundations Annuity Rates'
  }
]
VAPRODUCTS = [
  {
    'id': 7,
    'name': 'AdvanceDesigns Variable Annuity Rates',
    'type': 'Variable Annuity'
  },
  {
    'id': 8,
    'name': 'AEA Valuebuilder Variable Annuity Rates',
    'type': 'Variable Annuity'
  },
  {
    'id': 9,
    'name': 'NEA Valuebuilder Variable Annuity Rates',
    'type': 'Variable Annuity'
  },
  {
    'id': 10,
    'name': 'SecureDesigns Variable Annuity Rates',
    'type': 'Variable Annuity'
  },
  {
    'id': 11,
    'name': 'Variflex Variable Annuity Rates',
    'type': 'Variable Annuity'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', 
                         faproducts=FAPRODUCTS,
                        fiaproducts=FIAPRODUCTS,
                        vaproducts=VAPRODUCTS)

if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)