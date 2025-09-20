from flask import Flask, request, jsonify, render_template

# Create the Flask application instance
# We tell Flask to look for templates in the current directory (where index.html is)
app = Flask(__name__, template_folder='.')

# YOUR COMPLETE JSON DATA GOES HERE
MOCK_DATABASE = [
    {
        "namasteCode": "NAM001",
        "namasteTerm": "Prameha",
        "icd11Tm2Code": "TM2-21",
        "icd11Tm2Term": "Sweet urine disorder",
        "icd11BiomedicineCode": "5A11",
        "icd11BiomedicineTerm": "Diabetes Mellitus"
    },
    {
        "namasteCode": "NAM002",
        "namasteTerm": "Vatavyadhi",
        "icd11Tm2Code": "TM2-15",
        "icd11Tm2Term": "Musculoskeletal pain disorder",
        "icd11BiomedicineCode": "MG11",
        "icd11BiomedicineTerm": "Rheumatoid arthritis"
    },
    {
        "namasteCode": "NAM003",
        "namasteTerm": "Jwara",
        "icd11Tm2Code": "TM2-04",
        "icd11Tm2Term": "Fever",
        "icd11BiomedicineCode": "MA04",
        "icd11BiomedicineTerm": "Influenza"
    },
    {
        "namasteCode": "NAM004",
        "namasteTerm": "Amlapitta",
        "icd11Tm2Code": "TM2-11",
        "icd11Tm2Term": "Acidic indigestion",
        "icd11BiomedicineCode": "DA60",
        "icd11BiomedicineTerm": "Gastroesophageal reflux disease"
    },
    {
        "namasteCode": "NAM005",
        "namasteTerm": "Kushtha",
        "icd11Tm2Code": "TM2-20",
        "icd11Tm2Term": "Skin eruption",
        "icd11BiomedicineCode": "EJ30",
        "icd11BiomedicineTerm": "Psoriasis"
    },
    {
        "namasteCode": "NAM006",
        "namasteTerm": "Pandu",
        "icd11Tm2Code": "TM2-14",
        "icd11Tm2Term": "Pale discoloration",
        "icd11BiomedicineCode": "3B90",
        "icd11BiomedicineTerm": "Iron deficiency anemia"
    },
    {
        "namasteCode": "NAM007",
        "namasteTerm": "Kasa",
        "icd11Tm2Code": "TM2-04",
        "icd11Tm2Term": "Cough",
        "icd11BiomedicineCode": "CA30",
        "icd11BiomedicineTerm": "Chronic bronchitis"
    },
    {
        "namasteCode": "NAM008",
        "namasteTerm": "Shotha",
        "icd11Tm2Code": "TM2-17",
        "icd11Tm2Term": "Generalized swelling",
        "icd11BiomedicineCode": "BD05",
        "icd11BiomedicineTerm": "Renal failure"
    },
    {
        "namasteCode": "NAM009",
        "namasteTerm": "Atisara",
        "icd11Tm2Code": "TM2-11",
        "icd11Tm2Term": "Loose stools",
        "icd11BiomedicineCode": "DA90",
        "icd11BiomedicineTerm": "Gastroenteritis"
    },
    {
        "namasteCode": "NAM010",
        "namasteTerm": "Kamala",
        "icd11Tm2Code": "TM2-14",
        "icd11Tm2Term": "Yellow discoloration",
        "icd11BiomedicineCode": "DB20",
        "icd11BiomedicineTerm": "Hepatitis"
    },
    {
        "namasteCode": "NAM011",
        "namasteTerm": "Hridroga",
        "icd11Tm2Code": "TM2-07",
        "icd11Tm2Term": "Heart condition",
        "icd11BiomedicineCode": "BB20",
        "icd11BiomedicineTerm": "Ischaemic heart disease"
    },
    {
        "namasteCode": "NAM012",
        "namasteTerm": "Raktapitta",
        "icd11Tm2Code": "TM2-02",
        "icd11Tm2Term": "Haemorrhagic disorder",
        "icd11BiomedicineCode": "1C50",
        "icd11BiomedicineTerm": "Haemophilia"
    },
    {
        "namasteCode": "NAM013",
        "namasteTerm": "Pakshaghata",
        "icd11Tm2Code": "TM2-09",
        "icd11Tm2Term": "Paralysis",
        "icd11BiomedicineCode": "8B81",
        "icd11BiomedicineTerm": "Stroke"
    },
    {
        "namasteCode": "NAM014",
        "namasteTerm": "Shvasa",
        "icd11Tm2Code": "TM2-04",
        "icd11Tm2Term": "Breathlessness",
        "icd11BiomedicineCode": "CA70",
        "icd11BiomedicineTerm": "Asthma"
    },
    {
        "namasteCode": "NAM015",
        "namasteTerm": "Madatyaya",
        "icd11Tm2Code": "TM2-18",
        "icd11Tm2Term": "Alcohol related disorder",
        "icd11BiomedicineCode": "6C40",
        "icd11BiomedicineTerm": "Alcohol dependence syndrome"
    },
    {
        "namasteCode": "NAM016",
        "namasteTerm": "Bhagandara",
        "icd11Tm2Code": "TM2-11",
        "icd11Tm2Term": "Anorectal fistula",
        "icd11BiomedicineCode": "DB60",
        "icd11BiomedicineTerm": "Fistula of anus"
    },
    {
        "namasteCode": "NAM017",
        "namasteTerm": "Arsha",
        "icd11Tm2Code": "TM2-11",
        "icd11Tm2Term": "Haemorrhoids",
        "icd11BiomedicineCode": "DB70",
        "icd11BiomedicineTerm": "Haemorrhoids"
    },
    {
        "namasteCode": "NAM018",
        "namasteTerm": "Shiroroga (Sarva Sadharan)",
        "icd11Tm2Code": "TM2-08",
        "icd11Tm2Term": "Headache",
        "icd11BiomedicineCode": "8A80",
        "icd11BiomedicineTerm": "Migraine"
    },
    {
        "namasteCode": "NAM018.0",
        "namasteTerm": "Shiroroga (Bina Aura)",
        "icd11Tm2Code": "TM2-08.0",
        "icd11Tm2Term": "Headache without aura",
        "icd11BiomedicineCode": "8A80.0",
        "icd11BiomedicineTerm": "Migraine without aura"
    },
    {
        "namasteCode": "NAM018.1",
        "namasteTerm": "Shiroroga (Aura ke saath)",
        "icd11Tm2Code": "TM2-08.1",
        "icd11Tm2Term": "Headache with aura",
        "icd11BiomedicineCode": "8A80.1",
        "icd11BiomedicineTerm": "Migraine with aura"
    },
    {
        "namasteCode": "NAM018.10",
        "namasteTerm": "Shiroroga (Ardhangi)",
        "icd11Tm2Code": "TM2-08.10",
        "icd11Tm2Term": "One-sided headache with aura",
        "icd11BiomedicineCode": "8A80.10",
        "icd11BiomedicineTerm": "Hemiplegic migraine"
    },
    {
        "namasteCode": "NAM018.2",
        "namasteTerm": "Shiroroga (Diर्घकालिक)",
        "icd11Tm2Code": "TM2-08.2",
        "icd11Tm2Term": "Chronic headache",
        "icd11BiomedicineCode": "8A80.2",
        "icd11BiomedicineTerm": "Chronic migraine"
    },
    {
        "namasteCode": "NAM019",
        "namasteTerm": "Amavata",
        "icd11Tm2Code": "TM2-15",
        "icd11Tm2Term": "Musculoskeletal condition",
        "icd11BiomedicineCode": "MG11.1",
        "icd11BiomedicineTerm": "Rheumatic fever"
    },
    {
        "namasteCode": "NAM020",
        "namasteTerm": "Unmada",
        "icd11Tm2Code": "TM2-09",
        "icd11Tm2Term": "Psychiatric illness",
        "icd11BiomedicineCode": "6A20",
        "icd11BiomedicineTerm": "Schizophrenia"
    },
    {
        "namasteCode": "NAM021",
        "namasteTerm": "Netraroga (Netra Sukshmata)",
        "icd11Tm2Code": "TM2-19.1",
        "icd11Tm2Term": "Dry eye condition",
        "icd11BiomedicineCode": "9A60.0",
        "icd11BiomedicineTerm": "Keratoconjunctivitis sicca"
    },
    {
        "namasteCode": "NAM022",
        "namasteTerm": "Pratishyaya (Alarjik)",
        "icd11Tm2Code": "TM2-04.1",
        "icd11Tm2Term": "Allergic nasal condition",
        "icd11BiomedicineCode": "CA01.0",
        "icd11BiomedicineTerm": "Allergic rhinitis with asthma"
    },
    {
        "namasteCode": "NAM023",
        "namasteTerm": "Karnaroga",
        "icd11Tm2Code": "TM2-12",
        "icd11Tm2Term": "Ear disorder",
        "icd11BiomedicineCode": "AA60",
        "icd11BiomedicineTerm": "Otitis media"
    },
    {
        "namasteCode": "NAM024",
        "namasteTerm": "Rajayakshma",
        "icd11Tm2Code": "TM2-04",
        "icd11Tm2Term": "Wasting disorder",
        "icd11BiomedicineCode": "1B21",
        "icd11BiomedicineTerm": "Pulmonary tuberculosis"
    }
]

# This route serves your main HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Optional: serve a simple empty favicon to avoid 404s in the browser
@app.route('/favicon.ico')
def favicon():
    return ('', 204)

# This is the API endpoint that will handle the autocomplete search.
@app.route('/api/autocomplete', methods=['GET'])
def autocomplete():
    # Get the search query from the URL parameters
    query = request.args.get('query', '').lower()
    
    # Filter the data based on the query.
    filtered_results = [
        item for item in MOCK_DATABASE if
        query in item['namasteTerm'].lower() or
        query in item['icd11Tm2Term'].lower() or
        query in item['icd11BiomedicineTerm'].lower() or
        query in item['namasteCode'].lower() or
        query in item['icd11Tm2Code'].lower() or
        query in item['icd11BiomedicineCode'].lower()
    ]
    
    # Return the filtered results as a JSON response.
    return jsonify(filtered_results)

# This part runs the development server.
if __name__ == '__main__':
    # We change the host to '0.0.0.0' to make it accessible externally
    # (e.g., if you're deploying it on a server)
    # and debug=True for automatic restarts on code changes.
    app.run(host='0.0.0.0', debug=True)