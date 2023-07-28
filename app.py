from flask import Flask, render_template

app = Flask(__name__)

FAPRODUCTS = [
  {
    'id': 0,
    'name': 'Advanced Choice Annuity Rates',
    'url': 'https://www.securitybenefit.com/AdvancedChoiceRates'
  },
  {
    'id': 1,
    'name': 'Choice Annuity Renewal Rates',
    'url': 'https://www.securitybenefit.com/ChoiceAnnuityRates'
  },
{
    'id': 2,
    'name': 'RateTrack Annuity Rates',
    'url': 'https://www.securitybenefit.com/RateTrackRates'
  },
{
    'id': 3,
    'name': 'Total Interest Annuity Rates',
    'url': 'https://www.securitybenefit.com/TIARates'
  }
]
FIAPRODUCTS = [
  {
    'id': 4,
    'name': 'ClearLine Annuity Rates',
    'url': 'https://www.securitybenefit.com/ClearLineRates'
  },
  {
    'id': 5,
    'name': 'Foundations Annuity Rates',
    'url': 'https://www.securitybenefit.com/FoundationsRates'
  }
]
VAPRODUCTS = [
  {
    'id': 6,
    'name': 'AdvanceDesigns Variable Annuity Rates',
    'type': 'Variable Annuity',
    'url': 'https://www.securitybenefit.com/rates/advancedesigns-variable-annuity-rates'
  },
  {
    'id': 7,
    'name': 'Advisor 403(b) Program Rates',
    'type': 'Variable Annuity',
    'url': 'https://www.securitybenefit.com/rates/advisor-403b-program-interest-rates'
  },
  {
    'id': 8,
    'name': 'AEA Valuebuilder Variable Annuity Rates',
    'type': 'Variable Annuity',
    'url': 'https://www.securitybenefit.com/rates/aea-valuebuilder-variable-annuity-rates'
  },
  {
    'id': 9,
    'name': 'NEA Valuebuilder Variable Annuity Rates',
    'type': 'Variable Annuity',
    'url': 'https://www.securitybenefit.com/rates/nea-valuebuilder-variable-annuity-rates'
  },
  {
    'id': 10,
    'name': 'SecureDesigns Variable Annuity Rates',
    'type': 'Variable Annuity',
    'url': 'https://www.securitybenefit.com/rates/securedesigns-variable-annuity-rates'
  },
  {
    'id': 11,
    'name': 'Variflex Variable Annuity Rates',
    'type': 'Variable Annuity',
    'url': 'https://www.securitybenefit.com/rates/variflex-variable-annuity-rates'
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