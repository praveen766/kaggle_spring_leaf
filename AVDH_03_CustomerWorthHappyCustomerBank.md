

    import numpy as np
    import pandas as pd
    import os as os
    import datetime  as dt
    import calendar as cal
    from __future__ import division  ### to make sure that division results in float numbers
    pd.set_option('display.max_columns', None)
    import time


    pd.__version__




    '0.16.1'




    os.chdir("/home/local/ANT/pravengs/MISC/AVDH_03_CustomerWorthHappyCustomerBank")
    print os.getcwd()

    /home/local/ANT/pravengs/MISC/AVDH_03_CustomerWorthHappyCustomerBank



    ! ls -lrth

    total 18M
    -rw-r--r-- 1 pravengs domain^users 1.3K Sep  5 12:46 Customer worth for Happy customer bank - Shortcut.lnk
    -rw-r--r-- 1 pravengs domain^users 5.2M Sep  5 12:46 Test_bCtAN1w.csv
    -rw-r--r-- 1 pravengs domain^users   13 Sep  5 12:46 sample_submission.csv
    -rw-r--r-- 1 pravengs domain^users  13M Sep  5 12:47 Train_nyOWmfK.csv



    ## importing files
    train =pd.read_csv("Train_nyOWmfK.csv")


    test =pd.read_csv("Test_bCtAN1w.csv")


    print train.shape
    print train.columns
    print "\n"
    print test.shape
    print test.columns

    (87020, 26)
    Index([u'ID', u'Gender', u'City', u'Monthly_Income', u'DOB',
           u'Lead_Creation_Date', u'Loan_Amount_Applied', u'Loan_Tenure_Applied',
           u'Existing_EMI', u'Employer_Name', u'Salary_Account',
           u'Mobile_Verified', u'Var5', u'Var1', u'Loan_Amount_Submitted',
           u'Loan_Tenure_Submitted', u'Interest_Rate', u'Processing_Fee',
           u'EMI_Loan_Submitted', u'Filled_Form', u'Device_Type', u'Var2',
           u'Source', u'Var4', u'LoggedIn', u'Disbursed'],
          dtype='object')
    
    
    (37717, 24)
    Index([u'ID', u'Gender', u'City', u'Monthly_Income', u'DOB',
           u'Lead_Creation_Date', u'Loan_Amount_Applied', u'Loan_Tenure_Applied',
           u'Existing_EMI', u'Employer_Name', u'Salary_Account',
           u'Mobile_Verified', u'Var5', u'Var1', u'Loan_Amount_Submitted',
           u'Loan_Tenure_Submitted', u'Interest_Rate', u'Processing_Fee',
           u'EMI_Loan_Submitted', u'Filled_Form', u'Device_Type', u'Var2',
           u'Source', u'Var4'],
          dtype='object')



    sdty=list(set(train.dtypes))
    sdty




    [dtype('O'), dtype('int64'), dtype('float64')]




    cat_count=int_count=float_count=0
    for i in train.columns:
        if train[i].dtypes=='O':
            cat_count+=1
        if train[i].dtypes=='int64':
            int_count+=1
        if train[i].dtypes=='float64':
            float_count+=1
    
    print "cat count " , cat_count
    print "int count " , int_count
    print "float count " , float_count

    cat count  13
    int count  5
    float count  8



    #Finding the levels of categorical variables
    cat_var=[]
    for i in train.columns:
        if train[i].dtypes=='O':
            print i , len(train[i].unique())
            cat_var.append((i,len(train[i].unique())))

    ID 87020
    Gender 2
    City 698
    DOB 11345
    Lead_Creation_Date 92
    Employer_Name 43568
    Salary_Account 58
    Mobile_Verified 2
    Var1 19
    Filled_Form 2
    Device_Type 2
    Var2 7
    Source 30



    #Finding the levels of categorical variables
    cat_var_test=[]
    for i in test.columns:
        if test[i].dtypes=='O':
            print i , len(test[i].unique())
            cat_var_test.append((i,len(test[i].unique())))

    ID 37717
    Gender 2
    City 611
    DOB 9181
    Lead_Creation_Date 92
    Employer_Name 22522
    Salary_Account 58
    Mobile_Verified 2
    Var1 19
    Filled_Form 2
    Device_Type 2
    Var2 7
    Source 28



    cat_var




    [('ID', 87020),
     ('Gender', 2),
     ('City', 698),
     ('DOB', 11345),
     ('Lead_Creation_Date', 92),
     ('Employer_Name', 43568),
     ('Salary_Account', 58),
     ('Mobile_Verified', 2),
     ('Var1', 19),
     ('Filled_Form', 2),
     ('Device_Type', 2),
     ('Var2', 7),
     ('Source', 30)]




    for (k,v) in cat_var:
        if k!='ID':
            print k,train[k].unique()
            print "\n"
            print k,train[k].value_counts(dropna=False)
            print "\n"
            print k,train[k].value_counts(dropna=False,normalize=True)

    Gender ['Female' 'Male']
    
    
    Gender Male      49848
    Female    37172
    dtype: int64
    
    
    Gender Male      0.572834
    Female    0.427166
    dtype: float64
    City ['Delhi' 'Mumbai' 'Panchkula' 'Saharsa' 'Bengaluru' 'Sindhudurg' 'Kochi'
     'Surat' 'Pune' 'Bhubaneswar' 'Howrah' 'Chennai' 'Ludhiana' 'Lucknow'
     'Bardhaman' 'Indore' 'Hyderabad' 'Udaipur' 'Faridabad' 'Angul' 'Kolkata'
     'Lakhisarai' 'Visakhapatnam' 'Patna' 'Gautam Buddha Nagar' 'Chandigarh'
     'Cuddalore' 'Ghaziabad' 'Meerut' 'Ahmedabad' 'Vijayawada' 'Rourkela'
     'Dibrugarh' 'Madurai' 'Haridwar' 'Panipat' 'Vadodara' 'Gurgaon' 'Dehradun'
     'Coimbatore' 'Hooghly' 'Bastar' 'Jaipur' 'Valsad' 'Bharuch'
     'Dakshina Kannada' 'Buxar' 'Banka' 'Rupnagar' 'VISNAGAR' 'Nagpur'
     'Anantapur' 'Thiruvalla' 'Kutch' 'Prakasam' 'Koppal' 'Amravati' 'Guwahati'
     'Bhopal' 'Shimoga' 'Bijnor' 'Bhilwara' 'Palwal' 'Bathinda' 'Bhiwadi'
     'Jammu' 'Kottayam' 'Gwalior' 'Agra' 'Satara' 'Varanasi' 'Kaithal'
     'Asansol' 'Panaji' 'Jodhpur' 'Alwar' 'Ambala' 'Mysore' 'Amareli'
     'Hamirpur' 'Morvi' 'Noida' 'Midnapore East' 'Beawar' 'Dindigul' 'Sitapur'
     'Neemuch' 'Jalandhar' 'Raipur' 'Kanpur Nagar' 'Bulandshahr' 'Ganganagar'
     'Vellore' 'Aurangabad' 'Ambur' 'Amritsar' 'Birbhum' 'Warangal' 'Thane'
     'Cachar' 'Ramanathapuram' 'Rewari' 'Tanuku' 'North 24 Parganas' 'Daman'
     'Firozpur' 'Hubli' 'Bolangir' 'Mehsana' 'Pondicherry' 'Vapi' 'Ghazipur'
     'Patiala' 'Ponda' 'Baleswar' 'Kanchipuram' 'Pathankot' 'Yamuna Nagar'
     'Kohima' 'Sidhi' 'Hapur' 'Rajkot' 'Sonitpur' 'Tirunelveli' 'Deoghar'
     'Jagatsinghpur' 'Jhabua' 'Ajmer' 'Ranchi' 'Nashik' 'Moradabad' 'South Goa'
     'Kapurthala' 'ADIPUR' 'Durgapur' 'Patan' 'Viluppuram' 'Rishikesh'
     'Dhanbad' 'Rewa' 'Gulbarga' 'Burdwan' 'Gandhidham' 'Guntur' 'Khammam'
     'Rudrapur' 'Kupwara' 'Rohtak' 'Kanpur' 'Faizabad' 'Sonipat' 'Gorkakhpur'
     'Sambalpur' 'West Godavari' 'East Khasi Hills' 'Karnal' 'Jharsuguda'
     'Wayanad' 'Ernakulam' 'Kharagpur' 'Navi Mumbai' 'Muzaffarpur' 'Amreli'
     'Rangareddy' 'Akola' 'Kodad' 'Margao' 'Salem' 'Bhandara' 'Mahasamund'
     'Aligarh' 'Ratnagiri' 'Kota' 'East Singhbhum' 'Erode' 'Purulia'
     'Kendujhar' 'Almora' 'Morena' 'Krishna' 'Chhindwara' 'Chhatarpur' 'Rohtas'
     'Pilibhit' 'Shivpuri' 'Jamnagar' 'Ambikapur' 'Karimnagar' 'Silvassa'
     'Bhavnagar' 'Shilong' 'Cuttack' 'Dadra & nagar Haveli' 'Kurnool' 'Sangli'
     'Gandhinagar' 'Mangalore' 'Barabanki' 'Ambedkar Nagar' 'Belgaum'
     'Gorakhpur' 'Bhadrak' 'Dakshin Dinajpur' 'Alleppey' 'Nabha' 'Krishnagiri'
     'Vizianagaram' 'Chamarajanagar' 'Kolhapur' 'Secunderabad' 'Tiruchirapalli'
     'Namakkal' 'Jalpaiguri' 'Kamrup Rural' 'Alappuzha' 'Shahpura' 'Tezpur'
     'Mathura' 'Bellary' 'Gonda' 'Jamshedpur' 'Kurukshetra' 'Solan' 'Thrissur'
     'Guna' 'Hisar' 'Haldwani' 'Sonbhadra' 'Sibsagar' 'Sagar' 'Anand'
     'Surendranagar' 'Udupi and Uttara Kannada' 'Nawanshahr' 'Kozhikode'
     'Mohali' 'Hospet' 'Kumbakonam' 'Rayagada' 'Raigarh' 'Navsari' 'Tumkur'
     'Bettiah' 'Ratlam' 'Harda' 'Tiruppur' 'Satna' 'Jhunjhunu' 'Gaya'
     'Nalgonda' 'Purnia' 'Rajahmundry' 'Siliguri' 'Hosur' 'VALLABH VIDYANAGAR'
     'Jabalpur' 'Durg' 'Mokokchung' 'Ahmednagar' 'Thiruvananthapuram' 'Deoria'
     'Sant Kabir Nagar' 'Mayurbhanj' 'Chandrapur' 'Karad' 'Koraput' 'Allahabad'
     'Nanded' 'Dahod' 'Khurdha' 'Mandya' 'Bomdila' 'Thoothukudi' 'Kadapa'
     'Perambalur' 'Jhajjar' 'Andman & Nicobar' 'Bidar' 'Mahbubnagar' 'Banswara'
     'Chittoor' 'Dholpur' 'Nilgiris' 'VIRPUR' 'Srikakulam' 'Rajpura'
     'South 24 Parganas' 'Papum Pare' 'Barpeta' 'Badaun' 'Sirsa' 'Baramulla'
     'Jalgaon' 'Pollachi' 'Nellore' 'Chittorgarh' 'Kannur' 'Yavatmal'
     'Behrampur' 'Kushinagar' 'Kashipur' 'Agartala' 'Dhamtari' 'Shimla'
     'Midnapore West' 'Theni' 'KAMREJ' 'Ujjain' 'Buldhana' 'Jalore' 'Thanjavur'
     'Ongole' 'East Godavari' 'Baddi' 'Saharanpur' 'Karur' 'Kanyakumari'
     'Damoh' 'Etah' 'Bilaspur' 'Bokaro' 'Medak' 'Aluva' 'Tadipatri' 'Latur'
     'Bahadurgarh' 'Ganjam' 'Hassan' 'Sehore' 'Tirupati' 'Hanumangarh' 'Sikar'
     'Bhilai' 'Barmer' 'Margoa' 'Bijapur' 'GANDEVI' 'Darrang' 'Solapur'
     'Pratapgarh' 'Pudukkottai' 'Palakkad' 'Karauli' 'Barwani' 'Roorkee'
     'Siddharthnagar' 'Magadh' 'Malappuram' 'Fatehabad' 'Samastipur' 'Kheda'
     'Nadia' 'Moga' 'GODHRA' 'Srinagar' 'Kalka' 'Bhiwani' 'Modasa' 'Dharmapuri'
     'Ichalkaranji' 'Farrukhabad' 'Nagapattinam' 'Davanagere' 'Mau' 'Dhenkanal'
     'SURENDERNAGAR' 'MANDVI' 'Ankleshwar' 'Fatehgarh Sahib' 'Hoshiarpur'
     'Sabarkantha' 'Nayagarh' 'Rae Bareli' 'Sirohi' 'Nalanda' 'Raigad' 'Siwan'
     'Kollam' 'Korba' 'Mandsaur' 'Pauri Garhwal' 'Banaskantha' 'Bhojpur'
     'UMBERGAON' 'Washim' 'Adilabad' 'Banaskhantha' 'Dindori' 'Malda'
     'Balaghat' 'Wardha' 'Kakinada' 'Tinsukia' 'Dhule' 'Jajapur'
     'Jyotiba Phule Nagar' 'Halol' 'Sonepur' 'Bhagalpur' 'Kendrapara'
     'Motihari' 'Bharatpur' 'Janigir - Champa' 'Begusarai' 'Narsinghpur'
     'Darjeeling' 'Nizamabad' 'BARDOLI' 'Churu' 'Keonjhar' 'Bikaner' 'Azamgarh'
     'Nagercoil' 'Jhansi' 'Dausa' 'Mundra' 'Goa' 'Kangra' 'Proddattur'
     'Uttar Dinajpur' 'Ballia' 'Kanpur Dehat' 'Veraval' 'Poonch'
     'Muzaffarnagar' 'Vyara' 'Bandipore' 'Unnao' 'Dimapur' 'Nandurbar' 'Dhar'
     'Bankura' 'Sultanpur' 'Betul' 'Gangtok' 'Rajsamand' 'LUNAWADA'
     'Murshidabad' 'Bareilly' 'sri ganganagar' 'Pathanamthitta' 'Hajipur'
     'Bargarh' 'Anuppur' 'Nagaon' 'Malegaon' 'Khargone' 'Virudhunagar'
     'DHANGARDHA' 'Pontashaib' 'Kaushambi' 'Cooch Behar' 'Haveri' 'Sitamarhi'
     'Pakur' 'Anantnag' 'Ariyalur' 'Kolar' 'North Cachar Hills' 'PALANPUR'
     'Idukki' 'Banda' 'West Singhbhum' 'Faridkot' 'Ramban' 'Daman & Diu'
     'Ashoknagar' 'Tiruvannamalai' 'Burhanpur' 'Chikkaballapur' 'Sanga Reddy'
     'Dharwad' 'Bagalkote' 'Travancore' 'Porbandar' 'Gurdaspur' 'Deogarh'
     'Katihar' 'Chidambaram' 'Mahendragarh' 'Chamoli' 'Shajapur' 'Kadi' 'Pali'
     'Dumka' 'Kodagu' 'Baran' 'Bagpat' 'Kishtwar' 'Fatehpur' 'Madhubani'
     'Silchar' 'Darbhanga' 'Nagaur' 'Mirzapur' 'Imphal West' 'Puri' 'Jind'
     'Gondia' 'Parbhani' 'Lunglei' 'Surguja' 'Upper Subansiri' 'Saran' nan
     'Baramati' 'Nainital' 'Udham Singh Nagar' 'Junagadh' 'Anjaw' 'Marigaon'
     'Bhind' 'Dewas' 'Panchmahal' 'Udalguri' 'Chitrakoot' 'Chapra' 'Araria'
     'Jaunpur' 'Tandur' 'Basti' 'Seraikela Kharsawan' 'Osmanabad' 'Sangrur'
     'Nadiad' 'Imphal East' 'Sivagangai' 'Chikkamagaluru' 'Tiruvallur' 'UDWADA'
     'Sangamner' 'Kathua' 'Mandla' 'Lakhimpur Kheri' 'Gadag' 'Jagadalpur'
     'Fazilka' 'MAHUVA' 'Bahraich' 'Koriya' 'Malout' 'Yadgir' 'Godda'
     'Jharkhand' 'Mancherial' 'Lohardaga' 'Kishanganj' 'Champawat' 'Karnataka'
     'Jalna' 'Bhuj' 'Samba' 'Madhepura' 'Phagwara' 'Garhwa' 'Jhalawar'
     'Damanjodi' 'Etawah' 'Gajapati' 'Shahdol' 'Munger' 'Churachandpur'
     'Kailashahar' 'Katni' 'Lakhimpur' 'Rajnandgaon' 'Rajgarh' 'VIJAPUR'
     'Kasaragod' 'Aizawl' 'Jorhat' 'Sawai Madhopur' 'Tiruvarur' 'Kandhamal'
     'Hingoli' 'Lalitpur' 'Barnala' 'Narmada' 'Sundargarh' 'Raichur' 'Itanagar'
     'Bundi' 'Dhubri' 'Auraiya' 'Panch Mahals' 'Una' 'Hoshangabad'
     'Maharajganj' 'Firozabad' 'Ropar' 'Jaisalmer' 'SAYAN' 'Chitradurga' 'Beed'
     'BHILAD' 'Gadchiroli' 'Sheopur' 'Hardoi' 'Mewat' 'Nabarangpur' 'Chandauli'
     'Chinnamiram' 'Ramgarh' 'Kargil' 'Palamu' 'Mansa' 'Chatra' 'NALIYA'
     'Khanna' 'Suryapet' 'Jagdalpur' 'Mandi' 'Jashpur' 'Balasore'
     'Gandhi Nagar' 'Mahabub Nagar' 'Golaghat' 'Khagaria' 'Bongaigaon'
     'Vidisha' 'AHMEDB' 'Khandwa' 'Siddipet' 'ANJAR' 'Kamrup Metropolitian'
     'Sheikhpura' 'Seoni' 'KHAMBHAT' 'Sirmaur' 'Bageshwar' 'Kabri Anglong'
     'Pithoragarh' 'KALOL' 'Nalbari' 'CHOTILA' 'IDAR' 'Umaria' 'Goalpara'
     'Chandel' 'Tirur' 'Udhampur' 'Dantewada' 'Jamtara' 'Hailakandi' 'Koderma'
     'Kannauj' 'BHACHAU' 'Jamui' 'Muktsar' 'Abohar' 'West Garo Hills' 'DEESA'
     'Boudh' 'Datia' 'Gumla' 'Surendra Nagar' 'Rampur' 'BILIMORA' 'Ri-Bhoi'
     'Gopal Ganj' 'CHIKHLI (GUJ.)' 'Hazaribagh' 'Gadwal' 'Kokrajhar'
     'Shahjahanpur' 'Giridih' 'Dungarpur' 'Raisen' 'Namchi' 'SOMNATH JUNAGADHA'
     'Tarn Taran' 'Mainpuri' 'Thoubal' 'SILVASA' 'Reasi' 'Nawadah' 'AMALSAD'
     'Jalaun' 'Jaintia Hills' 'Dhalai' 'Himatnagar' 'Tonk' 'Malabar' 'Pulwama'
     'BAJWA' 'DHANDHUKA' 'Janjgir-Champa' 'DWARKA' 'RADHANPUR' 'Doda'
     'Narayanpur' 'KAPADWANJ' 'Baksa' 'Tamenglong' 'DHORAJI' 'Siruguppa'
     'Lakshadweep' 'Lohit']
    
    
    City Delhi                  12527
    Bengaluru              10824
    Mumbai                 10795
    Hyderabad               7272
    Chennai                 6916
    Pune                    5207
    Kolkata                 2888
    Ahmedabad               1788
    Jaipur                  1331
    Gurgaon                 1212
    Coimbatore              1147
    NaN                     1003
    Thane                    905
    Chandigarh               870
    Surat                    802
    Visakhapatnam            764
    Indore                   734
    Vadodara                 624
    Nagpur                   594
    Lucknow                  580
    Ghaziabad                560
    Bhopal                   513
    Kochi                    492
    Patna                    461
    Faridabad                447
    Madurai                  375
    Noida                    373
    Gautam Buddha Nagar      338
    Dehradun                 314
    Raipur                   289
                           ...  
    Imphal East                1
    RADHANPUR                  1
    Munger                     1
    Modasa                     1
    Champawat                  1
    SAYAN                      1
    Bandipore                  1
    Magadh                     1
    GANDEVI                    1
    Nabha                      1
    Tonk                       1
    Umaria                     1
    IDAR                       1
    Siruguppa                  1
    Dantewada                  1
    Pulwama                    1
    Narayanpur                 1
    Gadwal                     1
    Upper Subansiri            1
    Gopal Ganj                 1
    Boudh                      1
    Kabri Anglong              1
    KAPADWANJ                  1
    Dhalai                     1
    Beawar                     1
    Kishanganj                 1
    Madhepura                  1
    KAMREJ                     1
    Kandhamal                  1
    Damoh                      1
    dtype: int64
    
    
    City Delhi                  0.143955
    Bengaluru              0.124385
    Mumbai                 0.124052
    Hyderabad              0.083567
    Chennai                0.079476
    Pune                   0.059837
    Kolkata                0.033188
    Ahmedabad              0.020547
    Jaipur                 0.015295
    Gurgaon                0.013928
    Coimbatore             0.013181
    NaN                    0.011526
    Thane                  0.010400
    Chandigarh             0.009998
    Surat                  0.009216
    Visakhapatnam          0.008780
    Indore                 0.008435
    Vadodara               0.007171
    Nagpur                 0.006826
    Lucknow                0.006665
    Ghaziabad              0.006435
    Bhopal                 0.005895
    Kochi                  0.005654
    Patna                  0.005298
    Faridabad              0.005137
    Madurai                0.004309
    Noida                  0.004286
    Gautam Buddha Nagar    0.003884
    Dehradun               0.003608
    Raipur                 0.003321
                             ...   
    Imphal East            0.000011
    RADHANPUR              0.000011
    Munger                 0.000011
    Modasa                 0.000011
    Champawat              0.000011
    SAYAN                  0.000011
    Bandipore              0.000011
    Magadh                 0.000011
    GANDEVI                0.000011
    Nabha                  0.000011
    Tonk                   0.000011
    Umaria                 0.000011
    IDAR                   0.000011
    Siruguppa              0.000011
    Dantewada              0.000011
    Pulwama                0.000011
    Narayanpur             0.000011
    Gadwal                 0.000011
    Upper Subansiri        0.000011
    Gopal Ganj             0.000011
    Boudh                  0.000011
    Kabri Anglong          0.000011
    KAPADWANJ              0.000011
    Dhalai                 0.000011
    Beawar                 0.000011
    Kishanganj             0.000011
    Madhepura              0.000011
    KAMREJ                 0.000011
    Kandhamal              0.000011
    Damoh                  0.000011
    dtype: float64
    DOB ['23-May-78' '07-Oct-85' '10-Oct-81' ..., '17-Feb-68' '21-Feb-69'
     '27-Nov-69']
    
    
    DOB 11-Nov-80    306
    02-Jan-70    226
    01-Jan-70    148
    01-Jan-90    131
    01-Jan-80    111
    01-Jan-86     99
    01-Jan-89     97
    01-Jan-85     95
    01-Jan-88     92
    01-Jun-85     78
    01-Jun-86     76
    01-Jan-91     75
    01-Jan-87     75
    11-Nov-88     71
    01-Jan-84     65
    01-Jul-86     63
    01-Jun-88     61
    01-Jul-89     61
    05-Jun-89     58
    01-Jun-87     57
    10-Jun-86     57
    01-Jun-90     56
    01-Jun-84     56
    01-Jun-89     55
    01-Jul-87     55
    15-May-90     54
    01-Jul-88     53
    10-Jul-88     53
    01-Jun-82     52
    01-Jul-90     51
                ... 
    12-Feb-54      1
    09-Apr-62      1
    11-Jun-64      1
    28-Sep-75      1
    10-Mar-61      1
    25-Apr-77      1
    25-Apr-70      1
    25-Apr-71      1
    22-Feb-78      1
    08-Jan-71      1
    05-Jul-57      1
    16-Jun-58      1
    07-Feb-95      1
    13-Aug-67      1
    15-Feb-55      1
    01-Jun-57      1
    20-Oct-63      1
    18-Oct-95      1
    07-Oct-77      1
    14-Dec-74      1
    26-Jun-62      1
    05-Nov-73      1
    14-May-70      1
    03-Sep-80      1
    17-Feb-60      1
    14-Dec-77      1
    13-Jul-97      1
    24-Jul-75      1
    18-Oct-96      1
    31-Jan-62      1
    dtype: int64
    
    
    DOB 11-Nov-80    0.003516
    02-Jan-70    0.002597
    01-Jan-70    0.001701
    01-Jan-90    0.001505
    01-Jan-80    0.001276
    01-Jan-86    0.001138
    01-Jan-89    0.001115
    01-Jan-85    0.001092
    01-Jan-88    0.001057
    01-Jun-85    0.000896
    01-Jun-86    0.000873
    01-Jan-91    0.000862
    01-Jan-87    0.000862
    11-Nov-88    0.000816
    01-Jan-84    0.000747
    01-Jul-86    0.000724
    01-Jun-88    0.000701
    01-Jul-89    0.000701
    05-Jun-89    0.000667
    01-Jun-87    0.000655
    10-Jun-86    0.000655
    01-Jun-90    0.000644
    01-Jun-84    0.000644
    01-Jun-89    0.000632
    01-Jul-87    0.000632
    15-May-90    0.000621
    01-Jul-88    0.000609
    10-Jul-88    0.000609
    01-Jun-82    0.000598
    01-Jul-90    0.000586
                   ...   
    12-Feb-54    0.000011
    09-Apr-62    0.000011
    11-Jun-64    0.000011
    28-Sep-75    0.000011
    10-Mar-61    0.000011
    25-Apr-77    0.000011
    25-Apr-70    0.000011
    25-Apr-71    0.000011
    22-Feb-78    0.000011
    08-Jan-71    0.000011
    05-Jul-57    0.000011
    16-Jun-58    0.000011
    07-Feb-95    0.000011
    13-Aug-67    0.000011
    15-Feb-55    0.000011
    01-Jun-57    0.000011
    20-Oct-63    0.000011
    18-Oct-95    0.000011
    07-Oct-77    0.000011
    14-Dec-74    0.000011
    26-Jun-62    0.000011
    05-Nov-73    0.000011
    14-May-70    0.000011
    03-Sep-80    0.000011
    17-Feb-60    0.000011
    14-Dec-77    0.000011
    13-Jul-97    0.000011
    24-Jul-75    0.000011
    18-Oct-96    0.000011
    31-Jan-62    0.000011
    dtype: float64
    Lead_Creation_Date ['15-May-15' '04-May-15' '19-May-15' '09-May-15' '20-May-15' '01-May-15'
     '02-May-15' '03-May-15' '13-May-15' '05-May-15' '08-May-15' '24-May-15'
     '12-May-15' '07-May-15' '10-May-15' '06-May-15' '11-May-15' '26-May-15'
     '17-May-15' '21-May-15' '18-May-15' '14-May-15' '16-May-15' '27-May-15'
     '25-May-15' '23-May-15' '22-May-15' '30-May-15' '28-May-15' '31-May-15'
     '29-May-15' '01-Jun-15' '27-Jun-15' '02-Jun-15' '11-Jun-15' '06-Jun-15'
     '03-Jun-15' '07-Jun-15' '04-Jun-15' '10-Jun-15' '19-Jun-15' '05-Jun-15'
     '14-Jun-15' '15-Jun-15' '09-Jun-15' '23-Jun-15' '13-Jun-15' '08-Jun-15'
     '12-Jun-15' '22-Jun-15' '18-Jun-15' '16-Jun-15' '17-Jun-15' '24-Jun-15'
     '25-Jun-15' '20-Jun-15' '29-Jun-15' '21-Jun-15' '30-Jun-15' '26-Jun-15'
     '28-Jun-15' '03-Jul-15' '01-Jul-15' '07-Jul-15' '02-Jul-15' '16-Jul-15'
     '04-Jul-15' '30-Jul-15' '26-Jul-15' '17-Jul-15' '06-Jul-15' '10-Jul-15'
     '21-Jul-15' '05-Jul-15' '12-Jul-15' '14-Jul-15' '15-Jul-15' '11-Jul-15'
     '08-Jul-15' '29-Jul-15' '20-Jul-15' '09-Jul-15' '22-Jul-15' '13-Jul-15'
     '23-Jul-15' '19-Jul-15' '28-Jul-15' '25-Jul-15' '18-Jul-15' '27-Jul-15'
     '24-Jul-15' '31-Jul-15']
    
    
    Lead_Creation_Date 03-Jul-15    2315
    23-Jul-15    1994
    30-Jul-15    1297
    27-Jul-15    1292
    31-Jul-15    1268
    29-Jul-15    1236
    20-Jul-15    1231
    22-Jun-15    1201
    21-Jul-15    1201
    15-Jul-15    1193
    28-Jul-15    1191
    26-May-15    1190
    18-Jul-15    1188
    22-Jul-15    1188
    23-Jun-15    1187
    17-Jun-15    1154
    04-Jun-15    1132
    05-May-15    1128
    06-Jul-15    1126
    29-Jun-15    1088
    04-May-15    1088
    13-May-15    1081
    18-May-15    1078
    03-Jun-15    1066
    27-May-15    1064
    07-Jul-15    1055
    18-Jun-15    1049
    26-Jun-15    1047
    25-May-15    1045
    09-Jun-15    1044
                 ... 
    08-May-15     860
    13-Jul-15     854
    20-Jun-15     820
    24-Jun-15     815
    30-May-15     808
    05-Jun-15     804
    10-Jul-15     779
    09-May-15     760
    13-Jun-15     750
    11-Jun-15     748
    19-May-15     725
    02-May-15     725
    06-Jun-15     717
    25-Jun-15     709
    21-Jun-15     691
    23-May-15     686
    26-Jul-15     673
    05-Jul-15     630
    28-Jun-15     629
    01-May-15     608
    11-Jul-15     598
    19-Jul-15     597
    17-May-15     571
    07-Jun-15     559
    03-May-15     527
    24-May-15     502
    31-May-15     498
    12-Jul-15     475
    10-May-15     459
    14-Jun-15     373
    dtype: int64
    
    
    Lead_Creation_Date 03-Jul-15    0.026603
    23-Jul-15    0.022914
    30-Jul-15    0.014905
    27-Jul-15    0.014847
    31-Jul-15    0.014571
    29-Jul-15    0.014204
    20-Jul-15    0.014146
    22-Jun-15    0.013801
    21-Jul-15    0.013801
    15-Jul-15    0.013709
    28-Jul-15    0.013687
    26-May-15    0.013675
    18-Jul-15    0.013652
    22-Jul-15    0.013652
    23-Jun-15    0.013641
    17-Jun-15    0.013261
    04-Jun-15    0.013009
    05-May-15    0.012963
    06-Jul-15    0.012940
    29-Jun-15    0.012503
    04-May-15    0.012503
    13-May-15    0.012422
    18-May-15    0.012388
    03-Jun-15    0.012250
    27-May-15    0.012227
    07-Jul-15    0.012124
    18-Jun-15    0.012055
    26-Jun-15    0.012032
    25-May-15    0.012009
    09-Jun-15    0.011997
                   ...   
    08-May-15    0.009883
    13-Jul-15    0.009814
    20-Jun-15    0.009423
    24-Jun-15    0.009366
    30-May-15    0.009285
    05-Jun-15    0.009239
    10-Jul-15    0.008952
    09-May-15    0.008734
    13-Jun-15    0.008619
    11-Jun-15    0.008596
    19-May-15    0.008331
    02-May-15    0.008331
    06-Jun-15    0.008239
    25-Jun-15    0.008148
    21-Jun-15    0.007941
    23-May-15    0.007883
    26-Jul-15    0.007734
    05-Jul-15    0.007240
    28-Jun-15    0.007228
    01-May-15    0.006987
    11-Jul-15    0.006872
    19-Jul-15    0.006860
    17-May-15    0.006562
    07-Jun-15    0.006424
    03-May-15    0.006056
    24-May-15    0.005769
    31-May-15    0.005723
    12-Jul-15    0.005459
    10-May-15    0.005275
    14-Jun-15    0.004286
    dtype: float64
    Employer_Name ['CYBOSOL' 'TATA CONSULTANCY SERVICES LTD (TCS)' 'ALCHEMIST HOSPITALS LTD'
     ..., 'UTTAM VALUE STEEL LTD,WARDHA' 'MAYO COLLEGE'
     'BANGALORE INSTITUTE OF TECHNOLOGY']
    
    
    Employer_Name 0                                                     4914
    TATA CONSULTANCY SERVICES LTD (TCS)                    550
    COGNIZANT TECHNOLOGY SOLUTIONS INDIA PVT LTD           404
    ACCENTURE SERVICES PVT LTD                             324
    GOOGLE                                                 301
    HCL TECHNOLOGIES LTD                                   250
    ICICI BANK LTD                                         239
    INDIAN AIR FORCE                                       191
    INFOSYS TECHNOLOGIES                                   181
    GENPACT                                                179
    IBM CORPORATION                                        173
    INDIAN ARMY                                            171
    TYPE SLOWLY FOR AUTO FILL                              162
    WIPRO TECHNOLOGIES                                     155
    HDFC BANK LTD                                          148
    IKYA HUMAN CAPITAL SOLUTIONS LTD                       142
    STATE GOVERNMENT                                       134
    INDIAN RAILWAY                                         130
    INDIAN NAVY                                            128
    ARMY                                                   126
    WIPRO BPO                                              116
    OTHERS                                                 115
    CONVERGYS INDIA SERVICES PVT LTD                       113
    TECH MAHINDRA LTD                                      113
    SERCO BPO PVT LTD                                      108
    IBM GLOBAL SERVICES INDIA LTD                          104
    CONCENTRIX DAKSH SERVICES INDIA PVT LTD                 99
    CAPGEMINI INDIA PVT LTD                                 96
    RANDSTAD INDIA LTD                                      96
    ADECCO INDIA PVT LTD                                    95
                                                          ... 
    IRRIGATION DEPARTMENT                                    1
    DH CONSULTANTS PVT LTD                                   1
    D.P. MUKHERJEE & CO.                                     1
    RAMESH RAMAVARAPU                                        1
    BARMALT PVT LTD                                          1
    BRLPS(JEEVIKA)                                           1
    ESSILOR 20 20 OPTICS PVT LTD                             1
    ESMS                                                     1
    GOVT HIGH SCHOOL BALAGANCHI  C.R.PATNA TALUK HASSA       1
    PRIME TIME                                               1
    JAGANNATH CORPOR PROJECTS PVT LTD                        1
    MRRSOFT                                                  1
    SHAIK                                                    1
    ASSAM GRAMIN VIKASH BANK                                 1
    RAJA VIKRAM                                              1
    SAMSUNG ELECTRONIC PVT LTD                               1
    LUPIN LIMITED                                            1
    VIPHOUSING & PROPERTIEES                                 1
    ONE POINT ONE SOLUTIONS                                  1
    PUSHPAK INFRASTRUCTURE                                   1
    DR. BATRAS POSITIVE HEALTH CLINIC PVT LTD.               1
    CMSS                                                     1
    ATHIYA ORGANIZATIONAL COMPETENCIES (P) LIMITED           1
    ADP INDIA PVT LTD(NEW NAME CDK GLOBAL PRIVATE LTD        1
    FUSION PRINTS PVT LTD                                    1
    BIGBASKET                                                1
    G HEALTHCARE                                             1
    EBC PUBLISHING PVT LTD                                   1
    TATA INTERNET SERVICES LTD                               1
    RAEMSH                                                   1
    dtype: int64
    
    
    Employer_Name 0                                                     0.056470
    TATA CONSULTANCY SERVICES LTD (TCS)                   0.006320
    COGNIZANT TECHNOLOGY SOLUTIONS INDIA PVT LTD          0.004643
    ACCENTURE SERVICES PVT LTD                            0.003723
    GOOGLE                                                0.003459
    HCL TECHNOLOGIES LTD                                  0.002873
    ICICI BANK LTD                                        0.002746
    INDIAN AIR FORCE                                      0.002195
    INFOSYS TECHNOLOGIES                                  0.002080
    GENPACT                                               0.002057
    IBM CORPORATION                                       0.001988
    INDIAN ARMY                                           0.001965
    TYPE SLOWLY FOR AUTO FILL                             0.001862
    WIPRO TECHNOLOGIES                                    0.001781
    HDFC BANK LTD                                         0.001701
    IKYA HUMAN CAPITAL SOLUTIONS LTD                      0.001632
    STATE GOVERNMENT                                      0.001540
    INDIAN RAILWAY                                        0.001494
    INDIAN NAVY                                           0.001471
    ARMY                                                  0.001448
    WIPRO BPO                                             0.001333
    OTHERS                                                0.001322
    CONVERGYS INDIA SERVICES PVT LTD                      0.001299
    TECH MAHINDRA LTD                                     0.001299
    SERCO BPO PVT LTD                                     0.001241
    IBM GLOBAL SERVICES INDIA LTD                         0.001195
    CONCENTRIX DAKSH SERVICES INDIA PVT LTD               0.001138
    CAPGEMINI INDIA PVT LTD                               0.001103
    RANDSTAD INDIA LTD                                    0.001103
    ADECCO INDIA PVT LTD                                  0.001092
                                                            ...   
    IRRIGATION DEPARTMENT                                 0.000011
    DH CONSULTANTS PVT LTD                                0.000011
    D.P. MUKHERJEE & CO.                                  0.000011
    RAMESH RAMAVARAPU                                     0.000011
    BARMALT PVT LTD                                       0.000011
    BRLPS(JEEVIKA)                                        0.000011
    ESSILOR 20 20 OPTICS PVT LTD                          0.000011
    ESMS                                                  0.000011
    GOVT HIGH SCHOOL BALAGANCHI  C.R.PATNA TALUK HASSA    0.000011
    PRIME TIME                                            0.000011
    JAGANNATH CORPOR PROJECTS PVT LTD                     0.000011
    MRRSOFT                                               0.000011
    SHAIK                                                 0.000011
    ASSAM GRAMIN VIKASH BANK                              0.000011
    RAJA VIKRAM                                           0.000011
    SAMSUNG ELECTRONIC PVT LTD                            0.000011
    LUPIN LIMITED                                         0.000011
    VIPHOUSING & PROPERTIEES                              0.000011
    ONE POINT ONE SOLUTIONS                               0.000011
    PUSHPAK INFRASTRUCTURE                                0.000011
    DR. BATRAS POSITIVE HEALTH CLINIC PVT LTD.            0.000011
    CMSS                                                  0.000011
    ATHIYA ORGANIZATIONAL COMPETENCIES (P) LIMITED        0.000011
    ADP INDIA PVT LTD(NEW NAME CDK GLOBAL PRIVATE LTD     0.000011
    FUSION PRINTS PVT LTD                                 0.000011
    BIGBASKET                                             0.000011
    G HEALTHCARE                                          0.000011
    EBC PUBLISHING PVT LTD                                0.000011
    TATA INTERNET SERVICES LTD                            0.000011
    RAEMSH                                                0.000011
    dtype: float64
    Salary_Account ['HDFC Bank' 'ICICI Bank' 'State Bank of India' 'HSBC' 'Yes Bank' nan
     'Kotak Bank' 'Indian Overseas Bank' 'Bank of Maharasthra' 'Axis Bank'
     'Central Bank of India' 'Standard Chartered Bank' 'Andhra Bank'
     'Bank of India' 'IndusInd Bank' 'Corporation bank' 'UCO Bank'
     'The Ratnakar Bank Ltd' 'Citibank' 'Karur Vysya Bank'
     'Punjab National Bank' 'Lakshmi Vilas bank' 'Syndicate Bank'
     'Allahabad Bank' 'Bank of Baroda' 'Canara Bank'
     'Oriental Bank of Commerce' 'Vijaya Bank' 'State Bank of Hyderabad'
     'IDBI Bank' 'State Bank of Patiala' 'Union Bank of India' 'ING Vysya'
     'Federal Bank' 'Dena Bank' 'Punjab & Sind bank' 'J&K Bank' 'Deutsche Bank'
     'Tamil Nadu Mercantile Bank' 'Indian Bank' 'United Bank of India'
     'Abhyuday Co-op Bank Ltd' 'State Bank of Bikaner & Jaipur' 'Saraswat Bank'
     'State Bank of Travancore' 'Karnataka Bank' 'South Indian Bank'
     'State Bank of Mysore' 'Bank of Rajasthan' 'State Bank of Indore'
     'Dhanalakshmi Bank Ltd' 'Catholic Syrian Bank' 'India Bulls'
     'Kerala Gramin Bank' 'Firstrand Bank Limited' 'GIC Housing Finance Ltd'
     'B N P Paribas' 'Industrial And Commercial Bank Of China Limited']
    
    
    Salary_Account HDFC Bank                                          17695
    ICICI Bank                                         13636
    State Bank of India                                11843
    NaN                                                11764
    Axis Bank                                           8783
    Citibank                                            2376
    Kotak Bank                                          2067
    IDBI Bank                                           1550
    Punjab National Bank                                1201
    Bank of India                                       1170
    Bank of Baroda                                      1126
    Standard Chartered Bank                              995
    Canara Bank                                          990
    Union Bank of India                                  951
    Yes Bank                                             779
    ING Vysya                                            678
    Corporation bank                                     649
    Indian Overseas Bank                                 612
    State Bank of Hyderabad                              597
    Indian Bank                                          555
    Oriental Bank of Commerce                            524
    IndusInd Bank                                        503
    Andhra Bank                                          485
    Central Bank of India                                445
    Syndicate Bank                                       415
    Bank of Maharasthra                                  406
    State Bank of Bikaner & Jaipur                       331
    HSBC                                                 328
    Karur Vysya Bank                                     326
    State Bank of Mysore                                 255
    Federal Bank                                         253
    Vijaya Bank                                          252
    Allahabad Bank                                       238
    UCO Bank                                             237
    State Bank of Travancore                             227
    Karnataka Bank                                       200
    Saraswat Bank                                        195
    United Bank of India                                 183
    Dena Bank                                            182
    State Bank of Patiala                                177
    South Indian Bank                                    160
    Deutsche Bank                                        125
    Abhyuday Co-op Bank Ltd                              108
    The Ratnakar Bank Ltd                                 83
    Tamil Nadu Mercantile Bank                            71
    Punjab & Sind bank                                    66
    J&K Bank                                              59
    Lakshmi Vilas bank                                    50
    Dhanalakshmi Bank Ltd                                 42
    State Bank of Indore                                  18
    Catholic Syrian Bank                                  14
    India Bulls                                           11
    B N P Paribas                                          8
    GIC Housing Finance Ltd                                8
    Firstrand Bank Limited                                 7
    Bank of Rajasthan                                      5
    Kerala Gramin Bank                                     4
    Industrial And Commercial Bank Of China Limited        2
    dtype: int64
    
    
    Salary_Account HDFC Bank                                          0.203344
    ICICI Bank                                         0.156700
    State Bank of India                                0.136095
    NaN                                                0.135187
    Axis Bank                                          0.100931
    Citibank                                           0.027304
    Kotak Bank                                         0.023753
    IDBI Bank                                          0.017812
    Punjab National Bank                               0.013801
    Bank of India                                      0.013445
    Bank of Baroda                                     0.012940
    Standard Chartered Bank                            0.011434
    Canara Bank                                        0.011377
    Union Bank of India                                0.010929
    Yes Bank                                           0.008952
    ING Vysya                                          0.007791
    Corporation bank                                   0.007458
    Indian Overseas Bank                               0.007033
    State Bank of Hyderabad                            0.006860
    Indian Bank                                        0.006378
    Oriental Bank of Commerce                          0.006022
    IndusInd Bank                                      0.005780
    Andhra Bank                                        0.005573
    Central Bank of India                              0.005114
    Syndicate Bank                                     0.004769
    Bank of Maharasthra                                0.004666
    State Bank of Bikaner & Jaipur                     0.003804
    HSBC                                               0.003769
    Karur Vysya Bank                                   0.003746
    State Bank of Mysore                               0.002930
    Federal Bank                                       0.002907
    Vijaya Bank                                        0.002896
    Allahabad Bank                                     0.002735
    UCO Bank                                           0.002724
    State Bank of Travancore                           0.002609
    Karnataka Bank                                     0.002298
    Saraswat Bank                                      0.002241
    United Bank of India                               0.002103
    Dena Bank                                          0.002091
    State Bank of Patiala                              0.002034
    South Indian Bank                                  0.001839
    Deutsche Bank                                      0.001436
    Abhyuday Co-op Bank Ltd                            0.001241
    The Ratnakar Bank Ltd                              0.000954
    Tamil Nadu Mercantile Bank                         0.000816
    Punjab & Sind bank                                 0.000758
    J&K Bank                                           0.000678
    Lakshmi Vilas bank                                 0.000575
    Dhanalakshmi Bank Ltd                              0.000483
    State Bank of Indore                               0.000207
    Catholic Syrian Bank                               0.000161
    India Bulls                                        0.000126
    B N P Paribas                                      0.000092
    GIC Housing Finance Ltd                            0.000092
    Firstrand Bank Limited                             0.000080
    Bank of Rajasthan                                  0.000057
    Kerala Gramin Bank                                 0.000046
    Industrial And Commercial Bank Of China Limited    0.000023
    dtype: float64
    Mobile_Verified ['N' 'Y']
    
    
    Mobile_Verified Y    56481
    N    30539
    dtype: int64
    
    
    Mobile_Verified Y    0.649058
    N    0.350942
    dtype: float64
    Var1 ['HBXX' 'HBXA' 'HAXM' 'HAXB' 'HBXC' 'HBXD' 'HBXH' 'HAXA' 'HBXB' 'HAYT'
     'HCXD' 'HVYS' 'HAVC' 'HCXG' 'HAZD' 'HCYS' 'HCXF' 'HAXC' 'HAXF']
    
    
    Var1 HBXX    59294
    HBXC     9010
    HBXB     4479
    HAXA     2909
    HBXA     2123
    HAXB     2011
    HBXD     1964
    HAXC     1536
    HBXH      970
    HCXF      722
    HAYT      508
    HAVC      384
    HAXM      268
    HCXD      237
    HCYS      217
    HVYS      186
    HAZD      109
    HCXG       78
    HAXF       15
    dtype: int64
    
    
    Var1 HBXX    0.681384
    HBXC    0.103539
    HBXB    0.051471
    HAXA    0.033429
    HBXA    0.024397
    HAXB    0.023110
    HBXD    0.022570
    HAXC    0.017651
    HBXH    0.011147
    HCXF    0.008297
    HAYT    0.005838
    HAVC    0.004413
    HAXM    0.003080
    HCXD    0.002724
    HCYS    0.002494
    HVYS    0.002137
    HAZD    0.001253
    HCXG    0.000896
    HAXF    0.000172
    dtype: float64
    Filled_Form ['N' 'Y']
    
    
    Filled_Form N    67530
    Y    19490
    dtype: int64
    
    
    Filled_Form N    0.776028
    Y    0.223972
    dtype: float64
    Device_Type ['Web-browser' 'Mobile']
    
    
    Device_Type Web-browser    64316
    Mobile         22704
    dtype: int64
    
    
    Device_Type Web-browser    0.739094
    Mobile         0.260906
    dtype: float64
    Var2 ['G' 'B' 'C' 'E' 'F' 'D' 'A']
    
    
    Var2 B    37280
    G    33032
    C    14210
    E     1315
    D      634
    F      544
    A        5
    dtype: int64
    
    
    Var2 B    0.428407
    G    0.379591
    C    0.163296
    E    0.015111
    D    0.007286
    F    0.006251
    A    0.000057
    dtype: float64
    Source ['S122' 'S143' 'S134' 'S133' 'S159' 'S151' 'S137' 'S127' 'S144' 'S123'
     'S156' 'S153' 'S124' 'S161' 'S139' 'S154' 'S157' 'S138' 'S162' 'S141'
     'S158' 'S125' 'S129' 'S136' 'S130' 'S155' 'S160' 'S150' 'S135' 'S140']
    
    
    Source S122    38567
    S133    29885
    S159     5599
    S143     4332
    S127     1931
    S137     1724
    S134     1301
    S161      769
    S151      720
    S157      650
    S153      494
    S156      308
    S144      299
    S158      208
    S123       73
    S141       57
    S162       36
    S124       24
    S160       11
    S150       10
    S155        4
    S129        3
    S136        3
    S139        3
    S138        3
    S135        2
    S125        1
    S130        1
    S154        1
    S140        1
    dtype: int64
    
    
    Source S122    0.443197
    S133    0.343427
    S159    0.064342
    S143    0.049782
    S127    0.022190
    S137    0.019812
    S134    0.014951
    S161    0.008837
    S151    0.008274
    S157    0.007470
    S153    0.005677
    S156    0.003539
    S144    0.003436
    S158    0.002390
    S123    0.000839
    S141    0.000655
    S162    0.000414
    S124    0.000276
    S160    0.000126
    S150    0.000115
    S155    0.000046
    S129    0.000034
    S136    0.000034
    S139    0.000034
    S138    0.000034
    S135    0.000023
    S125    0.000011
    S130    0.000011
    S154    0.000011
    S140    0.000011
    dtype: float64



    # creating the age in years
    print "dob null count: ",train['DOB'].isnull().sum()
    print "lcd null count: ",train['Lead_Creation_Date'].isnull().sum()
    
    train['age_years'] =(pd.to_datetime(train['Lead_Creation_Date'])-pd.to_datetime(train['DOB'])).astype('timedelta64[D]')/365.25 

    dob null count:  0
    lcd null count:  0



    test['age_years'] =(pd.to_datetime(test['Lead_Creation_Date'])-pd.to_datetime(test['DOB'])).astype('timedelta64[D]')/365.25


    ## creating clusters for employer names
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import scale
    from sklearn.metrics import silhouette_samples, silhouette_score
    %pylab inline
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm
    import numpy as np

    Populating the interactive namespace from numpy and matplotlib



    clus_data=train[['Employer_Name','age_years','Monthly_Income']]


    test.columns




    Index([u'ID', u'Gender', u'City', u'Monthly_Income', u'DOB',
           u'Lead_Creation_Date', u'Loan_Amount_Applied', u'Loan_Tenure_Applied',
           u'Existing_EMI', u'Employer_Name', u'Salary_Account',
           u'Mobile_Verified', u'Var5', u'Var1', u'Loan_Amount_Submitted',
           u'Loan_Tenure_Submitted', u'Interest_Rate', u'Processing_Fee',
           u'EMI_Loan_Submitted', u'Filled_Form', u'Device_Type', u'Var2',
           u'Source', u'Var4', u'age_years'],
          dtype='object')




    clus_data_test=test[['Employer_Name','age_years','Monthly_Income']]


    #replacing inf and nan with zero in train
    clus_data.replace([np.inf, -np.inf,np.nan], 0,inplace=True)
    print  "\n";

    
    


    /usr/local/lib/python2.7/dist-packages/IPython/kernel/__main__.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      from IPython.kernel.zmq import kernelapp as app



    #replacing inf and nan with zero in test
    clus_data_test.replace([np.inf, -np.inf,np.nan], 0,inplace=True)
    print  "\n";

    
    


    /usr/local/lib/python2.7/dist-packages/IPython/kernel/__main__.py:2: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      from IPython.kernel.zmq import kernelapp as app



    clus_data_test.shape




    (37717, 3)




    ## scaling and creating dataframe
    # train
    scale_clus_data=scale(clus_data[['age_years','Monthly_Income']])
    scale_clus_data=pd.DataFrame(scale_clus_data,columns=['age_years','Monthly_Income'])
    scale_clus_data_df=pd.concat([clus_data[['Employer_Name']],scale_clus_data],axis=1)


    # test
    scale_clus_data_test=scale(clus_data_test[['age_years','Monthly_Income']])
    scale_clus_data_test=pd.DataFrame(scale_clus_data_test,columns=['age_years','Monthly_Income'])
    scale_clus_data_test_df=pd.concat([clus_data_test[['Employer_Name']],scale_clus_data_test],axis=1)


    scale_clus_data_test_df.shape,scale_clus_data_test_df.shape




    ((37717, 3), (37717, 3))




    clus_data.head(5)




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Employer_Name</th>
      <th>age_years</th>
      <th>Monthly_Income</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>CYBOSOL</td>
      <td>36.977413</td>
      <td>20000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TATA CONSULTANCY SERVICES LTD (TCS)</td>
      <td>29.571526</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ALCHEMIST HOSPITALS LTD</td>
      <td>33.604381</td>
      <td>22500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BIHAR GOVERNMENT</td>
      <td>27.438741</td>
      <td>35000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>GLOBAL EDGE SOFTWARE</td>
      <td>31.252567</td>
      <td>100000</td>
    </tr>
  </tbody>
</table>
</div>




    scale_clus_data_df.head(5)




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Employer_Name</th>
      <th>age_years</th>
      <th>Monthly_Income</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>CYBOSOL</td>
      <td>0.653989</td>
      <td>-0.017842</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TATA CONSULTANCY SERVICES LTD (TCS)</td>
      <td>0.092818</td>
      <td>-0.010953</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ALCHEMIST HOSPITALS LTD</td>
      <td>0.398402</td>
      <td>-0.016693</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BIHAR GOVERNMENT</td>
      <td>-0.068791</td>
      <td>-0.010953</td>
    </tr>
    <tr>
      <th>4</th>
      <td>GLOBAL EDGE SOFTWARE</td>
      <td>0.220196</td>
      <td>0.018898</td>
    </tr>
  </tbody>
</table>
</div>




    X_train=scale_clus_data_df[['age_years','Monthly_Income']].as_matrix()


    X_test=scale_clus_data_test_df[['age_years','Monthly_Income']].as_matrix()
kfit=kmeans.fit(X)
cluster_labels, len(cluster_labels), X.shape
silhouette_avg = silhouette_score(X, cluster_labels,sample_size=1000)

    range_n_clusters = [3,4, 5, 6,7,8]
    
    for n_clusters in range_n_clusters:
        # Create a subplot with 1 row and 2 columns
        #fig, (ax1, ax2) = plt.subplots(1, 2)
        #fig.set_size_inches(18, 7)
    
        # The 1st subplot is the silhouette plot
        # The silhouette coefficient can range from -1, 1 but in this example all
        # lie within [-0.1, 1]
        #ax1.set_xlim([-0.1, 1])
        # The (n_clusters+1)*10 is for inserting blank space between silhouette
        # plots of individual clusters, to demarcate them clearly.
        #ax1.set_ylim([0, len(X) + (n_clusters + 1) * 10])
    
        # Initialize the clusterer with n_clusters value and a random generator
        # seed of 10 for reproducibility.
        clusterer = KMeans(n_clusters=n_clusters, random_state=9876)
        cluster_labels = clusterer.fit_predict(X_train)
        cluster_labels_test = clusterer.fit_predict(X_test)
    
        # The silhouette_score gives the average value for all the samples.
        # This gives a perspective into the density and separation of the formed
        # clusters
        silhouette_avg = silhouette_score(X_train, cluster_labels,sample_size=1000)
        silhouette_avg_test = silhouette_score(X_test, cluster_labels_test,sample_size=1000)
        print("Train For n_clusters =", n_clusters,
              "The average silhouette_score is :", silhouette_avg)
        print("Test For n_clusters =", n_clusters,
              "The average silhouette_score is :", silhouette_avg_test)
    
        # Compute the silhouette scores for each sample
        # sample_silhouette_values = silhouette_samples(X, cluster_labels)
        
      

    ('Train For n_clusters =', 3, 'The average silhouette_score is :', 0.91526686895526999)
    ('Test For n_clusters =', 3, 'The average silhouette_score is :', 0.90994673623866884)
    ('Train For n_clusters =', 4, 'The average silhouette_score is :', 0.91108949898754021)
    ('Test For n_clusters =', 4, 'The average silhouette_score is :', 0.55977504755827834)
    ('Train For n_clusters =', 5, 'The average silhouette_score is :', 0.61968238718224211)
    ('Test For n_clusters =', 5, 'The average silhouette_score is :', 0.54435793933764598)
    ('Train For n_clusters =', 6, 'The average silhouette_score is :', 0.54350173708651683)
    ('Test For n_clusters =', 6, 'The average silhouette_score is :', 0.5711597429501134)
    ('Train For n_clusters =', 7, 'The average silhouette_score is :', 0.56409545871731059)
    ('Test For n_clusters =', 7, 'The average silhouette_score is :', 0.51987518743381533)
    ('Train For n_clusters =', 8, 'The average silhouette_score is :', 0.52275104268141714)
    ('Test For n_clusters =', 8, 'The average silhouette_score is :', 0.50894574071656207)



    clusterer3 = KMeans(n_clusters=3,random_state=9876)
    cluster_label3 = clusterer3.fit_predict(X_train)
    test_cluster_label3 = clusterer3.fit_predict(X_test)
    clusterer4 = KMeans(n_clusters=4,random_state=9876)
    cluster_label4 = clusterer4.fit_predict(X_train)
    test_cluster_label4 = clusterer4.fit_predict(X_test)



    clus3=pd.concat([clus_data,
                  pd.DataFrame(cluster_label3,columns=['cluster_label3'])],axis=1)
    
    #clus4=pd.concat([clus_data,
    #              pd.DataFrame(cluster_label4,columns=['cluster_label4'])],axis=1)


    test_clus3=pd.concat([clus_data_test,
                  pd.DataFrame(test_cluster_label3,columns=['cluster_label3'])],axis=1)
    
    #test_clus4=pd.concat([clus_data_test,
     #             pd.DataFrame(test_cluster_label4,columns=['cluster_label4'])],axis=1)


    clus_data_test.shape, X_test.shape




    ((37717, 3), (37717, 2))




    test_cluster_label3.shape




    (37717,)




    clus3.shape , clus4.shape , test_clus3.shape, test_clus4.shape




    ((87020, 4), (87020, 4), (37717, 4), (37717, 4))




    clus3.head(5)




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Employer_Name</th>
      <th>age_years</th>
      <th>Monthly_Income</th>
      <th>cluster_label3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>CYBOSOL</td>
      <td>36.977413</td>
      <td>20000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>TATA CONSULTANCY SERVICES LTD (TCS)</td>
      <td>29.571526</td>
      <td>35000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ALCHEMIST HOSPITALS LTD</td>
      <td>33.604381</td>
      <td>22500</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BIHAR GOVERNMENT</td>
      <td>27.438741</td>
      <td>35000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>GLOBAL EDGE SOFTWARE</td>
      <td>31.252567</td>
      <td>100000</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




    type(kfit)




    sklearn.cluster.k_means_.KMeans




    %pylab inline
    import matplotlib.pyplot as plt

    Populating the interactive namespace from numpy and matplotlib



    import seaborn as sns
    ax = sns.regplot(x="age_years", y="Monthly_Income", data=scale_clus_data_df)


    scale_clus_data_df.describe()




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age_years</th>
      <th>Monthly_Income</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>8.702000e+04</td>
      <td>8.702000e+04</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>-2.185029e-16</td>
      <td>1.224792e-18</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.000006e+00</td>
      <td>1.000006e+00</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-5.909949e+00</td>
      <td>-2.702641e-02</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-1.965849e-01</td>
      <td>-1.944891e-02</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>4.551734e-02</td>
      <td>-1.554535e-02</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>3.606445e-01</td>
      <td>-8.656709e-03</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.684012e+00</td>
      <td>2.041313e+02</td>
    </tr>
  </tbody>
</table>
</div>




    clus_data.describe()




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age_years</th>
      <th>Monthly_Income</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>87020.000000</td>
      <td>8.702000e+04</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>28.346595</td>
      <td>5.884997e+04</td>
    </tr>
    <tr>
      <th>std</th>
      <td>13.197275</td>
      <td>2.177511e+06</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-49.648186</td>
      <td>0.000000e+00</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>25.752225</td>
      <td>1.650000e+04</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>28.947296</td>
      <td>2.500000e+04</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>33.106092</td>
      <td>4.000000e+04</td>
    </tr>
    <tr>
      <th>max</th>
      <td>50.570842</td>
      <td>4.445544e+08</td>
    </tr>
  </tbody>
</table>
</div>




    #describing non categorical variables
    noncat_var=[]
    for i in train.columns:
        if train[i].dtypes!='O':
            print i , train[i].describe()
            print "nullcount:" ,train[i].isnull().sum()
            print "\n"
            noncat_var.append((i,len(train[i].unique())))

    Monthly_Income count    8.702000e+04
    mean     5.884997e+04
    std      2.177511e+06
    min      0.000000e+00
    25%      1.650000e+04
    50%      2.500000e+04
    75%      4.000000e+04
    max      4.445544e+08
    Name: Monthly_Income, dtype: float64
    nullcount: 0
    
    
    Loan_Amount_Applied count       86949.000000
    mean       230250.699928
    std        354206.759468
    min             0.000000
    25%             0.000000
    50%        100000.000000
    75%        300000.000000
    max      10000000.000000
    Name: Loan_Amount_Applied, dtype: float64
    nullcount: 71
    
    
    Loan_Tenure_Applied count    86949.000000
    mean         2.131399
    std          2.014193
    min          0.000000
    25%          0.000000
    50%          2.000000
    75%          4.000000
    max         10.000000
    Name: Loan_Tenure_Applied, dtype: float64
    nullcount: 71
    
    
    Existing_EMI count       86949.000000
    mean         3696.227824
    std         39810.211920
    min             0.000000
    25%             0.000000
    50%             0.000000
    75%          3500.000000
    max      10000000.000000
    Name: Existing_EMI, dtype: float64
    nullcount: 71
    
    
    Var5 count    87020.000000
    mean         4.961503
    std          5.670385
    min          0.000000
    25%          0.000000
    50%          2.000000
    75%         11.000000
    max         18.000000
    Name: Var5, dtype: float64
    nullcount: 0
    
    
    Loan_Amount_Submitted count      52407.000000
    mean      395010.590188
    std       308248.136255
    min        50000.000000
    25%       200000.000000
    50%       300000.000000
    75%       500000.000000
    max      3000000.000000
    Name: Loan_Amount_Submitted, dtype: float64
    nullcount: 34613
    
    
    Loan_Tenure_Submitted count    52407.000000
    mean         3.891369
    std          1.165359
    min          1.000000
    25%          3.000000
    50%          4.000000
    75%          5.000000
    max          6.000000
    Name: Loan_Tenure_Submitted, dtype: float64
    nullcount: 34613
    
    
    Interest_Rate count    27726.000000
    mean        19.197474
    std          5.834213
    min         11.990000
    25%         15.250000
    50%         18.000000
    75%         20.000000
    max         37.000000
    Name: Interest_Rate, dtype: float64
    nullcount: 59294
    
    
    Processing_Fee count    27420.000000
    mean      5131.150839
    std       4725.837644
    min        200.000000
    25%       2000.000000
    50%       4000.000000
    75%       6250.000000
    max      50000.000000
    Name: Processing_Fee, dtype: float64
    nullcount: 59600
    
    
    EMI_Loan_Submitted count     27726.000000
    mean      10999.528377
    std        7512.323050
    min        1176.410000
    25%        6491.600000
    50%        9392.970000
    75%       12919.040000
    max      144748.280000
    Name: EMI_Loan_Submitted, dtype: float64
    nullcount: 59294
    
    
    Var4 count    87020.000000
    mean         2.949805
    std          1.697720
    min          0.000000
    25%          1.000000
    50%          3.000000
    75%          5.000000
    max          7.000000
    Name: Var4, dtype: float64
    nullcount: 0
    
    
    LoggedIn count    87020.000000
    mean         0.029350
    std          0.168785
    min          0.000000
    25%          0.000000
    50%          0.000000
    75%          0.000000
    max          1.000000
    Name: LoggedIn, dtype: float64
    nullcount: 0
    
    
    Disbursed count    87020.000000
    mean         0.014629
    std          0.120062
    min          0.000000
    25%          0.000000
    50%          0.000000
    75%          0.000000
    max          1.000000
    Name: Disbursed, dtype: float64
    nullcount: 0
    
    
    age_years count    87020.000000
    mean        28.346595
    std         13.197275
    min        -49.648186
    25%         25.752225
    50%         28.947296
    75%         33.106092
    max         50.570842
    Name: age_years, dtype: float64
    nullcount: 0
    
    



    ## event rate:
    print train['Disbursed'].value_counts(dropna=False)
    print "\n"
    print train['Disbursed'].value_counts(dropna=False,normalize=True)

    0    85747
    1     1273
    dtype: int64
    
    
    0    0.985371
    1    0.014629
    dtype: float64



    train1=train


    train1['la_diff']=train1['Loan_Amount_Applied']-train1['Loan_Amount_Submitted']


    train1['la_diff'].describe()




    count      52371.000000
    mean     -154271.627294
    std       365952.215488
    min     -3000000.000000
    25%      -340000.000000
    50%            0.000000
    75%            0.000000
    max      8249999.000000
    Name: la_diff, dtype: float64




    train1.columns




    Index([u'ID', u'Gender', u'City', u'Monthly_Income', u'DOB',
           u'Lead_Creation_Date', u'Loan_Amount_Applied', u'Loan_Tenure_Applied',
           u'Existing_EMI', u'Employer_Name', u'Salary_Account',
           u'Mobile_Verified', u'Var5', u'Var1', u'Loan_Amount_Submitted',
           u'Loan_Tenure_Submitted', u'Interest_Rate', u'Processing_Fee',
           u'EMI_Loan_Submitted', u'Filled_Form', u'Device_Type', u'Var2',
           u'Source', u'Var4', u'LoggedIn', u'Disbursed', u'age_years', u'la_diff',
           u'LAbyMI', u'LAbyTenure', u'MIbyage', u'age_years_imp'],
          dtype='object')




    for i in range(100):
        ptile_la_diff=np.percentile(train1['la_diff'],i)
        ptile_age=np.percentile(train['age_years'],i)
        ptile_age_imp=np.percentile(train['age_years_imp'],i)
        ptile_mi=np.percentile(train['Monthly_Income'],i)
        print i,  ptile_la_diff, ptile_age,ptile_age_imp,ptile_mi

    0 -3000000.0 -49.6481861739 18.0013689254 0.0
    1 -1200000.0 -46.7345927447 20.6707734428 2583.0
    2 -1000000.0 -42.5026694045 21.4674880219 7500.0
    3 -810000.0 19.6824093087 22.0095824778 8846.56
    4 -700000.0 21.0212183436 22.379192334 10000.0
    5 -620000.0 21.7467488022 22.7405886379 10000.0
    6 -550000.0 22.1437371663 22.9924709103 10000.0
    7 -510000.0 22.5188227242 23.1978097194 10729.95
    8 -470000.0 22.8473648186 23.4442162902 11300.0
    9 -440000.0 23.0636550308 23.6851471595 12000.0
    10 -420000.0 23.2908966461 23.8959616701 12000.0
    11 -400000.0 23.5263518138 24.0492813142 12400.99
    12 -380000.0 23.7754962355 24.219028063 13000.0
    13 -360000.0 23.9561943874 24.4106776181 13200.0
    14 -350000.0 24.1067761807 24.5941136208 14000.0
    15 -340000.0 24.2929500342 24.7661875428 14000.0
    16 -320000.0 24.4873374401 24.9089664613 14800.0
    17 -300000.0 24.6570841889 25.0212183436 15000.0
    18 -290000.0 24.8268309377 25.1389459274 15000.0
    19 -260000.0 24.9527720739 25.273100616 15000.0
    20 -220000.0 25.067761807 25.4072553046 15000.0
    21 -190000.0 25.1882272416 25.5468856947 15000.0
    22 -50000.0 25.3256125941 25.7002053388 15500.0
    23 0.0 25.4592744695 25.8316221766 16000.0
    24 0.0 25.6016427105 25.954825462 16000.0
    25 0.0 25.7522245038 26.0636550308 16500.0
    26 0.0 25.8809034908 26.1764271047 17000.0
    27 0.0 25.9958932238 26.3189596167 17000.0
    28 0.0 26.0999315537 26.4558521561 17500.0
    29 0.0 26.2286105407 26.5872689938 18000.0
    30 0.0 26.3737166324 26.726899384 18000.0
    31 0.0 26.5023956194 26.8552772074 18087.56
    32 0.0 26.6447638604 26.9568788501 18687.12
    33 0.0 26.7761806982 27.06091718 19000.0
    34 0.0 26.8966461328 27.1704312115 19800.0
    35 0.0 26.9924709103 27.3073237509 20000.0
    36 0.0 27.1019849418 27.4360027379 20000.0
    37 0.0 27.2197125257 27.5619438741 20000.0
    38 0.0 27.356605065 27.704312115 20000.0
    39 0.0 27.4880219028 27.8466803559 20000.0
    40 0.0 27.613963039 27.9561943874 20609.2
    41 0.0 27.7672826831 28.0547570157 21000.0
    42 0.0 27.8932238193 28.1752224504 21500.0
    43 0.0 27.9972621492 28.3203285421 22000.0
    44 0.0 28.1013004791 28.4709103354 22000.0
    45 0.0 28.2327173169 28.6160164271 22800.0
    46 0.0 28.3771115674 28.7748117728 23000.0
    47 0.0 28.5284052019 28.9062286105 23800.0
    48 0.0 28.681724846 29.0130047912 24000.0
    49 0.0 28.8323066393 29.1225188227 25000.0
    50 0.0 28.9472963723 29.2594113621 25000.0
    51 0.0 29.0513347023 29.4045174538 25000.0
    52 0.0 29.1690622861 29.5523613963 25000.0
    53 20000.0 29.311430527 29.7138945927 25000.0
    54 40000.0 29.4599863107 29.87816564 25000.0
    55 50000.0 29.607118412 29.9958932238 25000.0
    56 90000.0 29.7823408624 30.1108829569 26000.0
    57 130000.0 29.9219712526 30.257299561 26215.32
    58 210000.0 30.0396988364 30.257299561 27000.0
    59 380000.0 30.1662149213 30.257299561 28000.0
    60 1234000.0 30.3271731691 30.3271731691 28000.0
    61 nan 30.4887063655 30.4887063655 29000.0
    62 nan 30.6611909651 30.6611909651 30000.0
    63 nan 30.8554962355 30.8554962355 30000.0
    64 nan 30.9897330595 30.9897330595 30000.0
    65 nan 31.1348391513 31.1348391513 30000.0
    66 nan 31.3100616016 31.3100616016 31000.0
    67 nan 31.5126625599 31.5126625599 32000.0
    68 nan 31.7207392197 31.7207392197 33000.0
    69 nan 31.9151266256 31.9151266256 34000.0
    70 nan 32.0739219713 32.0739219713 35000.0
    71 nan 32.2518822724 32.2518822724 35000.0
    72 nan 32.4599589322 32.4599589322 36000.0
    73 nan 32.7118412047 32.7118412047 37500.0
    74 nan 32.9365092402 32.9365092402 39000.0
    75 nan 33.106091718 33.106091718 40000.0
    76 nan 33.3278576318 33.3278576318 40000.0
    77 nan 33.6043805613 33.6043805613 41600.0
    78 nan 33.8945927447 33.8945927447 42000.0
    79 nan 34.1190965092 34.1190965092 44000.0
    80 nan 34.4202600958 34.4202600958 45000.0
    81 nan 34.6529774127 34.6529774127 47000.0
    82 nan 34.945927447 34.945927447 49983.48
    83 nan 35.1841204654 35.1841204654 50000.0
    84 nan 35.4907597536 35.4907597536 50000.0
    85 nan 35.9041752225 35.9041752225 51000.0
    86 nan 36.2381930185 36.2381930185 54000.0
    87 nan 36.7817385352 36.7817385352 55000.0
    88 nan 37.1909650924 37.1909650924 58333.0
    89 nan 37.7905544148 37.7905544148 60000.0
    90 nan 38.3493497604 38.3493497604 62000.0
    91 nan 39.0253251198 39.0253251198 67500.0
    92 nan 39.8083504449 39.8083504449 72000.0
    93 nan 40.5028610541 40.5028610541 77585.75
    94 nan 41.4702258727 41.4702258727 84000.0
    95 nan 42.6119096509 42.6119096509 95000.0
    96 nan 43.9726214921 43.9726214921 100000.0
    97 nan 45.3810540726 45.3810540726 120000.0
    98 nan 46.2785489391 46.2785489391 160000.0
    99 nan 48.1505817933 48.1505817933 250000.0



    age_avg=train[train['age_years']>=18]['age_years'].mean()
    #Imputing age
    train['age_years_imp']=train['age_years'].map(lambda x : age_avg if x<18 else x)



    age_avg_test=test[test['age_years']>=18]['age_years'].mean()
    #Imputing age
    test['age_years_imp']=test['age_years'].map(lambda x : age_avg if x<18 else x)
from collections import Counter
ct = Counter(tt['Loan_Tenure_Submitted'])
ct.most_common()   # Returns all unique items and their counts
ct.most_common(1)  # Returns the highest occurring itemfrom sklearn.preprocessing import Imputer
#imputing lean tenure using the most frequent
#from statistics import mode
#imp_lts = Imputer(missing_values='NaN', strategy='most_frequent', axis=0)

from collections import Counter
counter = Counter(tt['Interest_Rate'])
max_count = max(counter.values())
mode_ir = [k for k,v in counter.items() if v == max_count]
mode_ir


    ##imputing NaN
    #Loan submitted by loan applied 
    #Loan tenure submitted by Loan tenure applied
    #intrestest rate by median rate
    def imp_ls(row):
        if np.isnan(row['Loan_Amount_Submitted'])==True:
            val=row['Loan_Amount_Applied']
        else:
            val=row['Loan_Amount_Submitted']
        return val
    def imp_lt(row):
        if np.isnan(row['Loan_Tenure_Submitted'])==True:
            val=row['Loan_Tenure_Applied']
        else:
            val=row['Loan_Tenure_Submitted']
        return val
    
    median_ir=train['Interest_Rate'].median()
    
    train['Loan_Amount_Submitted_imp']=train.apply(imp_ls,axis=1)
    train['Loan_Tenure_Submitted_imp']=train.apply(imp_lt,axis=1)
    train['Interest_Rate_imp']=train['Interest_Rate'].map(lambda x: median_ir if np.isnan(x)==True else x)


    test['Loan_Amount_Submitted_imp']=test.apply(imp_ls,axis=1)
    test['Loan_Tenure_Submitted_imp']=test.apply(imp_lt,axis=1)
    test['Interest_Rate_imp']=test['Interest_Rate'].map(lambda x: median_ir if np.isnan(x)==True else x)


    for i in range(100):
        ptile_ls=np.percentile(train['Loan_Amount_Submitted'],i)
        ptile_lsi=np.percentile(train['Loan_Amount_Submitted_imp'],i)
        ptile_lt=np.percentile(train['Loan_Tenure_Submitted'],i)
        ptile_lti=np.percentile(train['Loan_Tenure_Submitted_imp'],i)
        ptile_ir=np.percentile(train['Interest_Rate'],i)
        ptile_iri=np.percentile(train['Interest_Rate_imp'],i)
        
        print i,  "ls: ", ptile_ls, "lsi: ",ptile_lsi, "lt: ",ptile_lt,"lti: ",ptile_lti, "lr: ",ptile_ir,"lri: ",ptile_iri

    0 ls:  50000.0 lsi:  0.0 lt:  1.0 lti:  0.0 lr:  11.99 lri:  11.99
    1 ls:  80000.0 lsi:  0.0 lt:  1.0 lti:  0.0 lr:  13.0 lri:  13.0
    2 ls:  100000.0 lsi:  0.0 lt:  1.0 lti:  0.0 lr:  13.5 lri:  13.5
    3 ls:  100000.0 lsi:  0.0 lt:  2.0 lti:  0.0 lr:  13.99 lri:  13.99
    4 ls:  100000.0 lsi:  0.0 lt:  2.0 lti:  0.0 lr:  13.99 lri:  13.99
    5 ls:  100000.0 lsi:  0.0 lt:  2.0 lti:  0.0 lr:  14.5 lri:  14.5
    6 ls:  100000.0 lsi:  0.0 lt:  2.0 lti:  0.0 lr:  14.85 lri:  14.85
    7 ls:  100000.0 lsi:  0.0 lt:  2.0 lti:  0.0 lr:  14.85 lri:  14.85
    8 ls:  100000.0 lsi:  0.0 lt:  2.0 lti:  0.0 lr:  15.25 lri:  15.25
    9 ls:  100000.0 lsi:  0.0 lt:  3.0 lti:  0.0 lr:  15.25 lri:  15.25
    10 ls:  140000.0 lsi:  0.0 lt:  3.0 lti:  0.0 lr:  15.5 lri:  15.5
    11 ls:  160000.0 lsi:  0.0 lt:  3.0 lti:  0.0 lr:  15.5 lri:  15.5
    12 ls:  190000.0 lsi:  30.0 lt:  3.0 lti:  0.0 lr:  16.0 lri:  16.0
    13 ls:  200000.0 lsi:  50000.0 lt:  3.0 lti:  0.0 lr:  16.75 lri:  16.75
    14 ls:  200000.0 lsi:  50000.0 lt:  3.0 lti:  0.0 lr:  16.75 lri:  16.75
    15 ls:  200000.0 lsi:  75000.0 lt:  3.0 lti:  1.0 lr:  17.0 lri:  17.0
    16 ls:  200000.0 lsi:  100000.0 lt:  3.0 lti:  1.0 lr:  18.0 lri:  18.0
    17 ls:  200000.0 lsi:  100000.0 lt:  3.0 lti:  1.0 lr:  18.25 lri:  18.0
    18 ls:  200000.0 lsi:  100000.0 lt:  3.0 lti:  1.0 lr:  18.25 lri:  18.0
    19 ls:  200000.0 lsi:  100000.0 lt:  4.0 lti:  1.0 lr:  18.4 lri:  18.0
    20 ls:  210000.0 lsi:  100000.0 lt:  4.0 lti:  1.0 lr:  19.0 lri:  18.0
    21 ls:  230000.0 lsi:  100000.0 lt:  4.0 lti:  2.0 lr:  20.0 lri:  18.0
    22 ls:  250000.0 lsi:  100000.0 lt:  4.0 lti:  2.0 lr:  20.0 lri:  18.0
    23 ls:  270000.0 lsi:  100000.0 lt:  4.0 lti:  2.0 lr:  20.0 lri:  18.0
    24 ls:  290000.0 lsi:  100000.0 lt:  4.0 lti:  2.0 lr:  20.0 lri:  18.0
    25 ls:  300000.0 lsi:  100000.0 lt:  4.0 lti:  2.0 lr:  20.0 lri:  18.0
    26 ls:  300000.0 lsi:  100000.0 lt:  4.0 lti:  2.0 lr:  21.5 lri:  18.0
    27 ls:  300000.0 lsi:  100000.0 lt:  4.0 lti:  2.0 lr:  25.5 lri:  18.0
    28 ls:  300000.0 lsi:  100000.0 lt:  4.0 lti:  2.0 lr:  28.5 lri:  18.0
    29 ls:  300000.0 lsi:  100000.0 lt:  4.0 lti:  2.0 lr:  31.5 lri:  18.0
    30 ls:  300000.0 lsi:  100000.0 lt:  4.0 lti:  2.0 lr:  31.5 lri:  18.0
    31 ls:  300000.0 lsi:  100000.0 lt:  4.0 lti:  2.0 lr:  35.5 lri:  18.0
    32 ls:  320000.0 lsi:  130000.0 lt:  4.0 lti:  3.0 lr:  nan lri:  18.0
    33 ls:  330000.0 lsi:  150000.0 lt:  4.0 lti:  3.0 lr:  nan lri:  18.0
    34 ls:  350000.0 lsi:  170000.0 lt:  4.0 lti:  3.0 lr:  nan lri:  18.0
    35 ls:  360000.0 lsi:  200000.0 lt:  4.0 lti:  3.0 lr:  nan lri:  18.0
    36 ls:  370000.0 lsi:  200000.0 lt:  4.0 lti:  3.0 lr:  nan lri:  18.0
    37 ls:  390000.0 lsi:  200000.0 lt:  5.0 lti:  3.0 lr:  nan lri:  18.0
    38 ls:  400000.0 lsi:  200000.0 lt:  5.0 lti:  3.0 lr:  nan lri:  18.0
    39 ls:  410000.0 lsi:  200000.0 lt:  5.0 lti:  3.0 lr:  nan lri:  18.0
    40 ls:  420000.0 lsi:  200000.0 lt:  5.0 lti:  3.0 lr:  nan lri:  18.0
    41 ls:  450000.0 lsi:  200000.0 lt:  5.0 lti:  3.0 lr:  nan lri:  18.0
    42 ls:  460000.0 lsi:  200000.0 lt:  5.0 lti:  3.0 lr:  nan lri:  18.0
    43 ls:  490000.0 lsi:  200000.0 lt:  5.0 lti:  3.0 lr:  nan lri:  18.0
    44 ls:  500000.0 lsi:  200000.0 lt:  5.0 lti:  3.0 lr:  nan lri:  18.0
    45 ls:  500000.0 lsi:  200000.0 lt:  5.0 lti:  3.0 lr:  nan lri:  18.0
    46 ls:  500000.0 lsi:  200000.0 lt:  5.0 lti:  3.0 lr:  nan lri:  18.0
    47 ls:  500000.0 lsi:  200000.0 lt:  5.0 lti:  3.0 lr:  nan lri:  18.0
    48 ls:  500000.0 lsi:  200000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    49 ls:  520000.0 lsi:  220000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    50 ls:  550000.0 lsi:  240000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    51 ls:  600000.0 lsi:  250000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    52 ls:  640000.0 lsi:  280000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    53 ls:  710000.0 lsi:  290000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    54 ls:  790000.0 lsi:  300000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    55 ls:  870000.0 lsi:  300000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    56 ls:  1000000.0 lsi:  300000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    57 ls:  1000000.0 lsi:  300000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    58 ls:  1100000.0 lsi:  300000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    59 ls:  1360000.0 lsi:  300000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    60 ls:  1800000.0 lsi:  300000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    61 ls:  nan lsi:  300000.0 lt:  nan lti:  4.0 lr:  nan lri:  18.0
    62 ls:  nan lsi:  300000.0 lt:  nan lti:  4.0 lr:  nan lri:  18.0
    63 ls:  nan lsi:  300000.0 lt:  nan lti:  4.0 lr:  nan lri:  18.0
    64 ls:  nan lsi:  310000.0 lt:  nan lti:  4.0 lr:  nan lri:  18.0
    65 ls:  nan lsi:  320000.0 lt:  nan lti:  4.0 lr:  nan lri:  18.0
    66 ls:  nan lsi:  330000.0 lt:  nan lti:  4.0 lr:  nan lri:  18.0
    67 ls:  nan lsi:  350000.0 lt:  nan lti:  4.0 lr:  nan lri:  18.0
    68 ls:  nan lsi:  360000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    69 ls:  nan lsi:  370000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    70 ls:  nan lsi:  390000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    71 ls:  nan lsi:  400000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    72 ls:  nan lsi:  400000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    73 ls:  nan lsi:  420000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    74 ls:  nan lsi:  440000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    75 ls:  nan lsi:  450000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    76 ls:  nan lsi:  490000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    77 ls:  nan lsi:  500000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    78 ls:  nan lsi:  500000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    79 ls:  nan lsi:  500000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    80 ls:  nan lsi:  500000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    81 ls:  nan lsi:  500000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    82 ls:  nan lsi:  500000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    83 ls:  nan lsi:  500000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    84 ls:  nan lsi:  500000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    85 ls:  nan lsi:  500000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.25
    86 ls:  nan lsi:  510000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.25
    87 ls:  nan lsi:  540000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.4
    88 ls:  nan lsi:  600000.0 lt:  nan lti:  5.0 lr:  nan lri:  19.0
    89 ls:  nan lsi:  640000.0 lt:  nan lti:  5.0 lr:  nan lri:  20.0
    90 ls:  nan lsi:  700000.0 lt:  nan lti:  5.0 lr:  nan lri:  20.0
    91 ls:  nan lsi:  740000.0 lt:  nan lti:  5.0 lr:  nan lri:  20.0
    92 ls:  nan lsi:  810000.0 lt:  nan lti:  5.0 lr:  nan lri:  20.0
    93 ls:  nan lsi:  920000.0 lt:  nan lti:  5.0 lr:  nan lri:  20.0
    94 ls:  nan lsi:  1000000.0 lt:  nan lti:  5.0 lr:  nan lri:  20.0
    95 ls:  nan lsi:  1000000.0 lt:  nan lti:  5.0 lr:  nan lri:  24.0
    96 ls:  nan lsi:  1000000.0 lt:  nan lti:  5.0 lr:  nan lri:  28.5
    97 ls:  nan lsi:  1040000.0 lt:  nan lti:  5.0 lr:  nan lri:  31.5
    98 ls:  nan lsi:  1200000.0 lt:  nan lti:  5.0 lr:  nan lri:  31.5
    99 ls:  nan lsi:  1500000.0 lt:  nan lti:  5.0 lr:  nan lri:  33.0



    for i in range(100):
        ptile_ls=np.percentile(test['Loan_Amount_Submitted'],i)
        ptile_lsi=np.percentile(test['Loan_Amount_Submitted_imp'],i)
        ptile_lt=np.percentile(test['Loan_Tenure_Submitted'],i)
        ptile_lti=np.percentile(test['Loan_Tenure_Submitted_imp'],i)
        ptile_ir=np.percentile(test['Interest_Rate'],i)
        ptile_iri=np.percentile(test['Interest_Rate_imp'],i)
        
        print i,  "ls: ", ptile_ls, "lsi: ",ptile_lsi, "lt: ",ptile_lt,"lti: ",ptile_lti, "lr: ",ptile_ir,"lri: ",ptile_iri

    0 ls:  50000.0 lsi:  0.0 lt:  1.0 lti:  0.0 lr:  11.99 lri:  11.99
    1 ls:  80000.0 lsi:  0.0 lt:  1.0 lti:  0.0 lr:  13.0 lri:  13.0
    2 ls:  100000.0 lsi:  0.0 lt:  1.0 lti:  0.0 lr:  13.5 lri:  13.5
    3 ls:  100000.0 lsi:  0.0 lt:  2.0 lti:  0.0 lr:  13.99 lri:  13.99
    4 ls:  100000.0 lsi:  0.0 lt:  2.0 lti:  0.0 lr:  13.99 lri:  13.99
    5 ls:  100000.0 lsi:  0.0 lt:  2.0 lti:  0.0 lr:  14.49 lri:  14.49
    6 ls:  100000.0 lsi:  0.0 lt:  2.0 lti:  0.0 lr:  14.85 lri:  14.85
    7 ls:  100000.0 lsi:  0.0 lt:  2.0 lti:  0.0 lr:  14.85 lri:  14.85
    8 ls:  100000.0 lsi:  0.0 lt:  2.0 lti:  0.0 lr:  15.0 lri:  15.0
    9 ls:  100000.0 lsi:  0.0 lt:  3.0 lti:  0.0 lr:  15.25 lri:  15.25
    10 ls:  140000.0 lsi:  0.0 lt:  3.0 lti:  0.0 lr:  15.5 lri:  15.5
    11 ls:  160000.0 lsi:  0.0 lt:  3.0 lti:  0.0 lr:  15.5 lri:  15.5
    12 ls:  190000.0 lsi:  25000.0 lt:  3.0 lti:  0.0 lr:  16.0 lri:  16.0
    13 ls:  200000.0 lsi:  50000.0 lt:  3.0 lti:  0.0 lr:  16.75 lri:  16.75
    14 ls:  200000.0 lsi:  60000.0 lt:  3.0 lti:  0.0 lr:  16.75 lri:  16.75
    15 ls:  200000.0 lsi:  90000.0 lt:  3.0 lti:  1.0 lr:  17.0 lri:  17.0
    16 ls:  200000.0 lsi:  100000.0 lt:  3.0 lti:  1.0 lr:  18.0 lri:  18.0
    17 ls:  200000.0 lsi:  100000.0 lt:  3.0 lti:  1.0 lr:  18.25 lri:  18.0
    18 ls:  200000.0 lsi:  100000.0 lt:  3.0 lti:  1.0 lr:  18.25 lri:  18.0
    19 ls:  200000.0 lsi:  100000.0 lt:  4.0 lti:  1.0 lr:  18.4 lri:  18.0
    20 ls:  200000.0 lsi:  100000.0 lt:  4.0 lti:  2.0 lr:  19.0 lri:  18.0
    21 ls:  230000.0 lsi:  100000.0 lt:  4.0 lti:  2.0 lr:  20.0 lri:  18.0
    22 ls:  250000.0 lsi:  100000.0 lt:  4.0 lti:  2.0 lr:  20.0 lri:  18.0
    23 ls:  270000.0 lsi:  100000.0 lt:  4.0 lti:  2.0 lr:  20.0 lri:  18.0
    24 ls:  290000.0 lsi:  100000.0 lt:  4.0 lti:  2.0 lr:  20.0 lri:  18.0
    25 ls:  300000.0 lsi:  100000.0 lt:  4.0 lti:  2.0 lr:  20.0 lri:  18.0
    26 ls:  300000.0 lsi:  100000.0 lt:  4.0 lti:  2.0 lr:  20.0 lri:  18.0
    27 ls:  300000.0 lsi:  100000.0 lt:  4.0 lti:  2.0 lr:  24.0 lri:  18.0
    28 ls:  300000.0 lsi:  100000.0 lt:  4.0 lti:  2.0 lr:  28.5 lri:  18.0
    29 ls:  300000.0 lsi:  100000.0 lt:  4.0 lti:  2.0 lr:  31.5 lri:  18.0
    30 ls:  300000.0 lsi:  100000.0 lt:  4.0 lti:  2.0 lr:  31.5 lri:  18.0
    31 ls:  300000.0 lsi:  100000.0 lt:  4.0 lti:  3.0 lr:  33.0 lri:  18.0
    32 ls:  320000.0 lsi:  130000.0 lt:  4.0 lti:  3.0 lr:  37.0 lri:  18.0
    33 ls:  330000.0 lsi:  150000.0 lt:  4.0 lti:  3.0 lr:  nan lri:  18.0
    34 ls:  350000.0 lsi:  180000.0 lt:  4.0 lti:  3.0 lr:  nan lri:  18.0
    35 ls:  360000.0 lsi:  200000.0 lt:  4.0 lti:  3.0 lr:  nan lri:  18.0
    36 ls:  370000.0 lsi:  200000.0 lt:  4.0 lti:  3.0 lr:  nan lri:  18.0
    37 ls:  390000.0 lsi:  200000.0 lt:  5.0 lti:  3.0 lr:  nan lri:  18.0
    38 ls:  400000.0 lsi:  200000.0 lt:  5.0 lti:  3.0 lr:  nan lri:  18.0
    39 ls:  400000.0 lsi:  200000.0 lt:  5.0 lti:  3.0 lr:  nan lri:  18.0
    40 ls:  420000.0 lsi:  200000.0 lt:  5.0 lti:  3.0 lr:  nan lri:  18.0
    41 ls:  440000.0 lsi:  200000.0 lt:  5.0 lti:  3.0 lr:  nan lri:  18.0
    42 ls:  460000.0 lsi:  200000.0 lt:  5.0 lti:  3.0 lr:  nan lri:  18.0
    43 ls:  490000.0 lsi:  200000.0 lt:  5.0 lti:  3.0 lr:  nan lri:  18.0
    44 ls:  500000.0 lsi:  200000.0 lt:  5.0 lti:  3.0 lr:  nan lri:  18.0
    45 ls:  500000.0 lsi:  200000.0 lt:  5.0 lti:  3.0 lr:  nan lri:  18.0
    46 ls:  500000.0 lsi:  200000.0 lt:  5.0 lti:  3.0 lr:  nan lri:  18.0
    47 ls:  500000.0 lsi:  200000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    48 ls:  500000.0 lsi:  200000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    49 ls:  520000.0 lsi:  220000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    50 ls:  550000.0 lsi:  240000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    51 ls:  600000.0 lsi:  250000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    52 ls:  640000.0 lsi:  280000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    53 ls:  700000.0 lsi:  290000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    54 ls:  770000.0 lsi:  300000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    55 ls:  850000.0 lsi:  300000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    56 ls:  1000000.0 lsi:  300000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    57 ls:  1000000.0 lsi:  300000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    58 ls:  1040000.0 lsi:  300000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    59 ls:  1200000.0 lsi:  300000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    60 ls:  1500000.0 lsi:  300000.0 lt:  5.0 lti:  4.0 lr:  nan lri:  18.0
    61 ls:  nan lsi:  300000.0 lt:  nan lti:  4.0 lr:  nan lri:  18.0
    62 ls:  nan lsi:  300000.0 lt:  nan lti:  4.0 lr:  nan lri:  18.0
    63 ls:  nan lsi:  300000.0 lt:  nan lti:  4.0 lr:  nan lri:  18.0
    64 ls:  nan lsi:  310000.0 lt:  nan lti:  4.0 lr:  nan lri:  18.0
    65 ls:  nan lsi:  320000.0 lt:  nan lti:  4.0 lr:  nan lri:  18.0
    66 ls:  nan lsi:  330000.0 lt:  nan lti:  4.0 lr:  nan lri:  18.0
    67 ls:  nan lsi:  350000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    68 ls:  nan lsi:  360000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    69 ls:  nan lsi:  370000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    70 ls:  nan lsi:  390000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    71 ls:  nan lsi:  400000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    72 ls:  nan lsi:  400000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    73 ls:  nan lsi:  420000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    74 ls:  nan lsi:  440000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    75 ls:  nan lsi:  450000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    76 ls:  nan lsi:  490000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    77 ls:  nan lsi:  500000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    78 ls:  nan lsi:  500000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    79 ls:  nan lsi:  500000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    80 ls:  nan lsi:  500000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    81 ls:  nan lsi:  500000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    82 ls:  nan lsi:  500000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    83 ls:  nan lsi:  500000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    84 ls:  nan lsi:  500000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.0
    85 ls:  nan lsi:  500000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.25
    86 ls:  nan lsi:  520000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.25
    87 ls:  nan lsi:  550000.0 lt:  nan lti:  5.0 lr:  nan lri:  18.4
    88 ls:  nan lsi:  600000.0 lt:  nan lti:  5.0 lr:  nan lri:  19.0
    89 ls:  nan lsi:  640000.0 lt:  nan lti:  5.0 lr:  nan lri:  20.0
    90 ls:  nan lsi:  700000.0 lt:  nan lti:  5.0 lr:  nan lri:  20.0
    91 ls:  nan lsi:  750000.0 lt:  nan lti:  5.0 lr:  nan lri:  20.0
    92 ls:  nan lsi:  820000.0 lt:  nan lti:  5.0 lr:  nan lri:  20.0
    93 ls:  nan lsi:  920000.0 lt:  nan lti:  5.0 lr:  nan lri:  20.0
    94 ls:  nan lsi:  1000000.0 lt:  nan lti:  5.0 lr:  nan lri:  23.0
    95 ls:  nan lsi:  1000000.0 lt:  nan lti:  5.0 lr:  nan lri:  26.5
    96 ls:  nan lsi:  1000000.0 lt:  nan lti:  5.0 lr:  nan lri:  28.5
    97 ls:  nan lsi:  1050000.0 lt:  nan lti:  5.0 lr:  nan lri:  31.5
    98 ls:  nan lsi:  1200000.0 lt:  nan lti:  5.0 lr:  nan lri:  31.5
    99 ls:  nan lsi:  1500000.0 lt:  nan lti:  5.0 lr:  nan lri:  33.0



    ## categorical variable transformation all varaibles except Employer_Name whihc has large number of levels
    #dummy OHE
    '''
    ID 87020
    Gender 2
    City 698
    DOB 11345
    Lead_Creation_Date 92
    Employer_Name 43568
    Salary_Account 58
    Mobile_Verified 2
    Var1 19
    Filled_Form 2
    Device_Type 2
    Var2 7
    Source 30
    '''
    '''
    ,'City', 'Employer_Name', 'Salary_Account','Mobile_Verified', 'Var1','Filled_Form','Device_Type','Var2','Source']]
    '''
    
    cat_features_train = train[['Gender','City','Salary_Account','Mobile_Verified', 'Var1','Filled_Form','Device_Type','Var2','Source']]
    cat_features_test = test[['Gender','City','Salary_Account','Mobile_Verified', 'Var1','Filled_Form','Device_Type','Var2','Source']]


    cat_features_train = pd.concat([pd.get_dummies(cat_features_train[col]
                                             , prefix=col
                                            ) for col in cat_features_train], axis=1)


    cat_features_test = pd.concat([pd.get_dummies(cat_features_test[col]
                                             , prefix=col
                                            ) for col in cat_features_test], axis=1)


    cat_features_train.shape, cat_features_test.shape




    ((87020, 818), (37717, 729))


# dropping the unwanted levels in cat_features
cat_features.columns=cat_features.columns.droplevel([0])

    cat_features_train.head(5)




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender_Female</th>
      <th>Gender_Male</th>
      <th>City_ADIPUR</th>
      <th>City_AHMEDB</th>
      <th>City_AMALSAD</th>
      <th>City_ANJAR</th>
      <th>City_Abohar</th>
      <th>City_Adilabad</th>
      <th>City_Agartala</th>
      <th>City_Agra</th>
      <th>City_Ahmedabad</th>
      <th>City_Ahmednagar</th>
      <th>City_Aizawl</th>
      <th>City_Ajmer</th>
      <th>City_Akola</th>
      <th>City_Alappuzha</th>
      <th>City_Aligarh</th>
      <th>City_Allahabad</th>
      <th>City_Alleppey</th>
      <th>City_Almora</th>
      <th>City_Aluva</th>
      <th>City_Alwar</th>
      <th>City_Amareli</th>
      <th>City_Ambala</th>
      <th>City_Ambedkar Nagar</th>
      <th>City_Ambikapur</th>
      <th>City_Ambur</th>
      <th>City_Amravati</th>
      <th>City_Amreli</th>
      <th>City_Amritsar</th>
      <th>City_Anand</th>
      <th>City_Anantapur</th>
      <th>City_Anantnag</th>
      <th>City_Andman &amp; Nicobar</th>
      <th>City_Angul</th>
      <th>City_Anjaw</th>
      <th>City_Ankleshwar</th>
      <th>City_Anuppur</th>
      <th>City_Araria</th>
      <th>City_Ariyalur</th>
      <th>City_Asansol</th>
      <th>City_Ashoknagar</th>
      <th>City_Auraiya</th>
      <th>City_Aurangabad</th>
      <th>City_Azamgarh</th>
      <th>City_BAJWA</th>
      <th>City_BARDOLI</th>
      <th>City_BHACHAU</th>
      <th>City_BHILAD</th>
      <th>City_BILIMORA</th>
      <th>City_Badaun</th>
      <th>City_Baddi</th>
      <th>City_Bagalkote</th>
      <th>City_Bageshwar</th>
      <th>City_Bagpat</th>
      <th>City_Bahadurgarh</th>
      <th>City_Bahraich</th>
      <th>City_Baksa</th>
      <th>City_Balaghat</th>
      <th>City_Balasore</th>
      <th>City_Baleswar</th>
      <th>City_Ballia</th>
      <th>City_Banaskantha</th>
      <th>City_Banaskhantha</th>
      <th>City_Banda</th>
      <th>City_Bandipore</th>
      <th>City_Banka</th>
      <th>City_Bankura</th>
      <th>City_Banswara</th>
      <th>City_Barabanki</th>
      <th>City_Baramati</th>
      <th>City_Baramulla</th>
      <th>City_Baran</th>
      <th>City_Bardhaman</th>
      <th>City_Bareilly</th>
      <th>City_Bargarh</th>
      <th>City_Barmer</th>
      <th>City_Barnala</th>
      <th>City_Barpeta</th>
      <th>City_Barwani</th>
      <th>City_Bastar</th>
      <th>City_Basti</th>
      <th>City_Bathinda</th>
      <th>City_Beawar</th>
      <th>City_Beed</th>
      <th>City_Begusarai</th>
      <th>City_Behrampur</th>
      <th>City_Belgaum</th>
      <th>City_Bellary</th>
      <th>City_Bengaluru</th>
      <th>City_Bettiah</th>
      <th>City_Betul</th>
      <th>City_Bhadrak</th>
      <th>City_Bhagalpur</th>
      <th>City_Bhandara</th>
      <th>City_Bharatpur</th>
      <th>City_Bharuch</th>
      <th>City_Bhavnagar</th>
      <th>City_Bhilai</th>
      <th>City_Bhilwara</th>
      <th>City_Bhind</th>
      <th>City_Bhiwadi</th>
      <th>City_Bhiwani</th>
      <th>City_Bhojpur</th>
      <th>City_Bhopal</th>
      <th>City_Bhubaneswar</th>
      <th>City_Bhuj</th>
      <th>City_Bidar</th>
      <th>City_Bijapur</th>
      <th>City_Bijnor</th>
      <th>City_Bikaner</th>
      <th>City_Bilaspur</th>
      <th>City_Birbhum</th>
      <th>City_Bokaro</th>
      <th>City_Bolangir</th>
      <th>City_Bomdila</th>
      <th>City_Bongaigaon</th>
      <th>City_Boudh</th>
      <th>City_Bulandshahr</th>
      <th>City_Buldhana</th>
      <th>City_Bundi</th>
      <th>City_Burdwan</th>
      <th>City_Burhanpur</th>
      <th>City_Buxar</th>
      <th>City_CHIKHLI (GUJ.)</th>
      <th>City_CHOTILA</th>
      <th>City_Cachar</th>
      <th>City_Chamarajanagar</th>
      <th>City_Chamoli</th>
      <th>City_Champawat</th>
      <th>City_Chandauli</th>
      <th>City_Chandel</th>
      <th>City_Chandigarh</th>
      <th>City_Chandrapur</th>
      <th>City_Chapra</th>
      <th>City_Chatra</th>
      <th>City_Chennai</th>
      <th>City_Chhatarpur</th>
      <th>City_Chhindwara</th>
      <th>City_Chidambaram</th>
      <th>City_Chikkaballapur</th>
      <th>City_Chikkamagaluru</th>
      <th>City_Chinnamiram</th>
      <th>City_Chitradurga</th>
      <th>City_Chitrakoot</th>
      <th>City_Chittoor</th>
      <th>City_Chittorgarh</th>
      <th>City_Churachandpur</th>
      <th>City_Churu</th>
      <th>City_Coimbatore</th>
      <th>City_Cooch Behar</th>
      <th>City_Cuddalore</th>
      <th>City_Cuttack</th>
      <th>City_DEESA</th>
      <th>City_DHANDHUKA</th>
      <th>City_DHANGARDHA</th>
      <th>City_DHORAJI</th>
      <th>City_DWARKA</th>
      <th>City_Dadra &amp; nagar Haveli</th>
      <th>City_Dahod</th>
      <th>City_Dakshin Dinajpur</th>
      <th>City_Dakshina Kannada</th>
      <th>City_Daman</th>
      <th>City_Daman &amp; Diu</th>
      <th>City_Damanjodi</th>
      <th>City_Damoh</th>
      <th>City_Dantewada</th>
      <th>City_Darbhanga</th>
      <th>City_Darjeeling</th>
      <th>City_Darrang</th>
      <th>City_Datia</th>
      <th>City_Dausa</th>
      <th>City_Davanagere</th>
      <th>City_Dehradun</th>
      <th>City_Delhi</th>
      <th>City_Deogarh</th>
      <th>City_Deoghar</th>
      <th>City_Deoria</th>
      <th>City_Dewas</th>
      <th>City_Dhalai</th>
      <th>City_Dhamtari</th>
      <th>City_Dhanbad</th>
      <th>City_Dhar</th>
      <th>City_Dharmapuri</th>
      <th>City_Dharwad</th>
      <th>City_Dhenkanal</th>
      <th>City_Dholpur</th>
      <th>City_Dhubri</th>
      <th>City_Dhule</th>
      <th>City_Dibrugarh</th>
      <th>City_Dimapur</th>
      <th>City_Dindigul</th>
      <th>City_Dindori</th>
      <th>City_Doda</th>
      <th>City_Dumka</th>
      <th>City_Dungarpur</th>
      <th>City_Durg</th>
      <th>City_Durgapur</th>
      <th>City_East Godavari</th>
      <th>City_East Khasi Hills</th>
      <th>City_East Singhbhum</th>
      <th>City_Ernakulam</th>
      <th>City_Erode</th>
      <th>City_Etah</th>
      <th>City_Etawah</th>
      <th>City_Faizabad</th>
      <th>City_Faridabad</th>
      <th>City_Faridkot</th>
      <th>City_Farrukhabad</th>
      <th>City_Fatehabad</th>
      <th>City_Fatehgarh Sahib</th>
      <th>City_Fatehpur</th>
      <th>City_Fazilka</th>
      <th>City_Firozabad</th>
      <th>City_Firozpur</th>
      <th>City_GANDEVI</th>
      <th>City_GODHRA</th>
      <th>City_Gadag</th>
      <th>City_Gadchiroli</th>
      <th>City_Gadwal</th>
      <th>City_Gajapati</th>
      <th>City_Gandhi Nagar</th>
      <th>City_Gandhidham</th>
      <th>City_Gandhinagar</th>
      <th>City_Ganganagar</th>
      <th>City_Gangtok</th>
      <th>City_Ganjam</th>
      <th>City_Garhwa</th>
      <th>City_Gautam Buddha Nagar</th>
      <th>City_Gaya</th>
      <th>City_Ghaziabad</th>
      <th>City_Ghazipur</th>
      <th>City_Giridih</th>
      <th>City_Goa</th>
      <th>City_Goalpara</th>
      <th>City_Godda</th>
      <th>City_Golaghat</th>
      <th>City_Gonda</th>
      <th>City_Gondia</th>
      <th>City_Gopal Ganj</th>
      <th>City_Gorakhpur</th>
      <th>City_Gorkakhpur</th>
      <th>City_Gulbarga</th>
      <th>City_Gumla</th>
      <th>City_Guna</th>
      <th>City_Guntur</th>
      <th>City_Gurdaspur</th>
      <th>City_Gurgaon</th>
      <th>City_Guwahati</th>
      <th>City_Gwalior</th>
      <th>City_Hailakandi</th>
      <th>City_Hajipur</th>
      <th>City_Haldwani</th>
      <th>City_Halol</th>
      <th>City_Hamirpur</th>
      <th>City_Hanumangarh</th>
      <th>City_Hapur</th>
      <th>City_Harda</th>
      <th>City_Hardoi</th>
      <th>City_Haridwar</th>
      <th>City_Hassan</th>
      <th>City_Haveri</th>
      <th>City_Hazaribagh</th>
      <th>City_Himatnagar</th>
      <th>City_Hingoli</th>
      <th>City_Hisar</th>
      <th>City_Hooghly</th>
      <th>City_Hoshangabad</th>
      <th>City_Hoshiarpur</th>
      <th>City_Hospet</th>
      <th>City_Hosur</th>
      <th>City_Howrah</th>
      <th>City_Hubli</th>
      <th>City_Hyderabad</th>
      <th>City_IDAR</th>
      <th>City_Ichalkaranji</th>
      <th>City_Idukki</th>
      <th>City_Imphal East</th>
      <th>City_Imphal West</th>
      <th>City_Indore</th>
      <th>City_Itanagar</th>
      <th>City_Jabalpur</th>
      <th>City_Jagadalpur</th>
      <th>City_Jagatsinghpur</th>
      <th>City_Jagdalpur</th>
      <th>City_Jaintia Hills</th>
      <th>City_Jaipur</th>
      <th>City_Jaisalmer</th>
      <th>City_Jajapur</th>
      <th>City_Jalandhar</th>
      <th>City_Jalaun</th>
      <th>City_Jalgaon</th>
      <th>City_Jalna</th>
      <th>City_Jalore</th>
      <th>City_Jalpaiguri</th>
      <th>City_Jammu</th>
      <th>City_Jamnagar</th>
      <th>City_Jamshedpur</th>
      <th>City_Jamtara</th>
      <th>City_Jamui</th>
      <th>City_Janigir - Champa</th>
      <th>City_Janjgir-Champa</th>
      <th>City_Jashpur</th>
      <th>City_Jaunpur</th>
      <th>City_Jhabua</th>
      <th>City_Jhajjar</th>
      <th>City_Jhalawar</th>
      <th>City_Jhansi</th>
      <th>City_Jharkhand</th>
      <th>City_Jharsuguda</th>
      <th>City_Jhunjhunu</th>
      <th>City_Jind</th>
      <th>City_Jodhpur</th>
      <th>City_Jorhat</th>
      <th>City_Junagadh</th>
      <th>City_Jyotiba Phule Nagar</th>
      <th>City_KALOL</th>
      <th>City_KAMREJ</th>
      <th>City_KAPADWANJ</th>
      <th>City_KHAMBHAT</th>
      <th>City_Kabri Anglong</th>
      <th>City_Kadapa</th>
      <th>City_Kadi</th>
      <th>City_Kailashahar</th>
      <th>City_Kaithal</th>
      <th>City_Kakinada</th>
      <th>City_Kalka</th>
      <th>City_Kamrup Metropolitian</th>
      <th>City_Kamrup Rural</th>
      <th>City_Kanchipuram</th>
      <th>City_Kandhamal</th>
      <th>City_Kangra</th>
      <th>City_Kannauj</th>
      <th>City_Kannur</th>
      <th>City_Kanpur</th>
      <th>City_Kanpur Dehat</th>
      <th>City_Kanpur Nagar</th>
      <th>City_Kanyakumari</th>
      <th>City_Kapurthala</th>
      <th>City_Karad</th>
      <th>City_Karauli</th>
      <th>City_Kargil</th>
      <th>City_Karimnagar</th>
      <th>City_Karnal</th>
      <th>City_Karnataka</th>
      <th>City_Karur</th>
      <th>City_Kasaragod</th>
      <th>City_Kashipur</th>
      <th>City_Kathua</th>
      <th>City_Katihar</th>
      <th>City_Katni</th>
      <th>City_Kaushambi</th>
      <th>City_Kendrapara</th>
      <th>City_Kendujhar</th>
      <th>City_Keonjhar</th>
      <th>City_Khagaria</th>
      <th>City_Khammam</th>
      <th>City_Khandwa</th>
      <th>City_Khanna</th>
      <th>City_Kharagpur</th>
      <th>City_Khargone</th>
      <th>City_Kheda</th>
      <th>City_Khurdha</th>
      <th>City_Kishanganj</th>
      <th>City_Kishtwar</th>
      <th>City_Kochi</th>
      <th>City_Kodad</th>
      <th>City_Kodagu</th>
      <th>City_Koderma</th>
      <th>City_Kohima</th>
      <th>City_Kokrajhar</th>
      <th>City_Kolar</th>
      <th>City_Kolhapur</th>
      <th>City_Kolkata</th>
      <th>City_Kollam</th>
      <th>City_Koppal</th>
      <th>City_Koraput</th>
      <th>City_Korba</th>
      <th>City_Koriya</th>
      <th>City_Kota</th>
      <th>City_Kottayam</th>
      <th>City_Kozhikode</th>
      <th>City_Krishna</th>
      <th>City_Krishnagiri</th>
      <th>City_Kumbakonam</th>
      <th>City_Kupwara</th>
      <th>City_Kurnool</th>
      <th>City_Kurukshetra</th>
      <th>City_Kushinagar</th>
      <th>City_Kutch</th>
      <th>City_LUNAWADA</th>
      <th>City_Lakhimpur</th>
      <th>City_Lakhimpur Kheri</th>
      <th>City_Lakhisarai</th>
      <th>City_Lakshadweep</th>
      <th>City_Lalitpur</th>
      <th>City_Latur</th>
      <th>City_Lohardaga</th>
      <th>City_Lohit</th>
      <th>City_Lucknow</th>
      <th>City_Ludhiana</th>
      <th>City_Lunglei</th>
      <th>City_MAHUVA</th>
      <th>City_MANDVI</th>
      <th>City_Madhepura</th>
      <th>City_Madhubani</th>
      <th>City_Madurai</th>
      <th>City_Magadh</th>
      <th>City_Mahabub Nagar</th>
      <th>City_Maharajganj</th>
      <th>City_Mahasamund</th>
      <th>City_Mahbubnagar</th>
      <th>City_Mahendragarh</th>
      <th>City_Mainpuri</th>
      <th>City_Malabar</th>
      <th>City_Malappuram</th>
      <th>City_Malda</th>
      <th>City_Malegaon</th>
      <th>City_Malout</th>
      <th>City_Mancherial</th>
      <th>City_Mandi</th>
      <th>City_Mandla</th>
      <th>City_Mandsaur</th>
      <th>City_Mandya</th>
      <th>City_Mangalore</th>
      <th>City_Mansa</th>
      <th>City_Margao</th>
      <th>City_Margoa</th>
      <th>City_Marigaon</th>
      <th>City_Mathura</th>
      <th>City_Mau</th>
      <th>City_Mayurbhanj</th>
      <th>City_Medak</th>
      <th>City_Meerut</th>
      <th>City_Mehsana</th>
      <th>City_Mewat</th>
      <th>City_Midnapore East</th>
      <th>City_Midnapore West</th>
      <th>City_Mirzapur</th>
      <th>City_Modasa</th>
      <th>City_Moga</th>
      <th>City_Mohali</th>
      <th>City_Mokokchung</th>
      <th>City_Moradabad</th>
      <th>City_Morena</th>
      <th>City_Morvi</th>
      <th>City_Motihari</th>
      <th>City_Muktsar</th>
      <th>City_Mumbai</th>
      <th>City_Mundra</th>
      <th>City_Munger</th>
      <th>City_Murshidabad</th>
      <th>City_Muzaffarnagar</th>
      <th>City_Muzaffarpur</th>
      <th>City_Mysore</th>
      <th>City_NALIYA</th>
      <th>City_Nabarangpur</th>
      <th>City_Nabha</th>
      <th>City_Nadia</th>
      <th>City_Nadiad</th>
      <th>City_Nagaon</th>
      <th>City_Nagapattinam</th>
      <th>City_Nagaur</th>
      <th>City_Nagercoil</th>
      <th>City_Nagpur</th>
      <th>City_Nainital</th>
      <th>City_Nalanda</th>
      <th>City_Nalbari</th>
      <th>City_Nalgonda</th>
      <th>City_Namakkal</th>
      <th>City_Namchi</th>
      <th>City_Nanded</th>
      <th>City_Nandurbar</th>
      <th>City_Narayanpur</th>
      <th>City_Narmada</th>
      <th>City_Narsinghpur</th>
      <th>City_Nashik</th>
      <th>City_Navi Mumbai</th>
      <th>City_Navsari</th>
      <th>City_Nawadah</th>
      <th>City_Nawanshahr</th>
      <th>City_Nayagarh</th>
      <th>City_Neemuch</th>
      <th>City_Nellore</th>
      <th>City_Nilgiris</th>
      <th>City_Nizamabad</th>
      <th>City_Noida</th>
      <th>City_North 24 Parganas</th>
      <th>City_North Cachar Hills</th>
      <th>City_Ongole</th>
      <th>City_Osmanabad</th>
      <th>City_PALANPUR</th>
      <th>City_Pakur</th>
      <th>City_Palakkad</th>
      <th>City_Palamu</th>
      <th>City_Pali</th>
      <th>City_Palwal</th>
      <th>City_Panaji</th>
      <th>City_Panch Mahals</th>
      <th>City_Panchkula</th>
      <th>City_Panchmahal</th>
      <th>City_Panipat</th>
      <th>City_Papum Pare</th>
      <th>City_Parbhani</th>
      <th>City_Patan</th>
      <th>City_Pathanamthitta</th>
      <th>City_Pathankot</th>
      <th>City_Patiala</th>
      <th>City_Patna</th>
      <th>City_Pauri Garhwal</th>
      <th>City_Perambalur</th>
      <th>City_Phagwara</th>
      <th>City_Pilibhit</th>
      <th>City_Pithoragarh</th>
      <th>City_Pollachi</th>
      <th>City_Ponda</th>
      <th>City_Pondicherry</th>
      <th>City_Pontashaib</th>
      <th>City_Poonch</th>
      <th>City_Porbandar</th>
      <th>City_Prakasam</th>
      <th>City_Pratapgarh</th>
      <th>City_Proddattur</th>
      <th>City_Pudukkottai</th>
      <th>City_Pulwama</th>
      <th>City_Pune</th>
      <th>City_Puri</th>
      <th>City_Purnia</th>
      <th>City_Purulia</th>
      <th>City_RADHANPUR</th>
      <th>City_Rae Bareli</th>
      <th>City_Raichur</th>
      <th>City_Raigad</th>
      <th>City_Raigarh</th>
      <th>City_Raipur</th>
      <th>City_Raisen</th>
      <th>City_Rajahmundry</th>
      <th>City_Rajgarh</th>
      <th>City_Rajkot</th>
      <th>City_Rajnandgaon</th>
      <th>City_Rajpura</th>
      <th>City_Rajsamand</th>
      <th>City_Ramanathapuram</th>
      <th>City_Ramban</th>
      <th>City_Ramgarh</th>
      <th>City_Rampur</th>
      <th>City_Ranchi</th>
      <th>City_Rangareddy</th>
      <th>City_Ratlam</th>
      <th>City_Ratnagiri</th>
      <th>City_Rayagada</th>
      <th>City_Reasi</th>
      <th>City_Rewa</th>
      <th>City_Rewari</th>
      <th>City_Ri-Bhoi</th>
      <th>City_Rishikesh</th>
      <th>City_Rohtak</th>
      <th>City_Rohtas</th>
      <th>City_Roorkee</th>
      <th>City_Ropar</th>
      <th>City_Rourkela</th>
      <th>City_Rudrapur</th>
      <th>City_Rupnagar</th>
      <th>City_SAYAN</th>
      <th>City_SILVASA</th>
      <th>City_SOMNATH JUNAGADHA</th>
      <th>City_SURENDERNAGAR</th>
      <th>City_Sabarkantha</th>
      <th>City_Sagar</th>
      <th>City_Saharanpur</th>
      <th>City_Saharsa</th>
      <th>City_Salem</th>
      <th>City_Samastipur</th>
      <th>City_Samba</th>
      <th>City_Sambalpur</th>
      <th>City_Sanga Reddy</th>
      <th>City_Sangamner</th>
      <th>City_Sangli</th>
      <th>City_Sangrur</th>
      <th>City_Sant Kabir Nagar</th>
      <th>City_Saran</th>
      <th>City_Satara</th>
      <th>City_Satna</th>
      <th>City_Sawai Madhopur</th>
      <th>City_Secunderabad</th>
      <th>City_Sehore</th>
      <th>City_Seoni</th>
      <th>City_Seraikela Kharsawan</th>
      <th>City_Shahdol</th>
      <th>City_Shahjahanpur</th>
      <th>City_Shahpura</th>
      <th>City_Shajapur</th>
      <th>City_Sheikhpura</th>
      <th>City_Sheopur</th>
      <th>City_Shilong</th>
      <th>City_Shimla</th>
      <th>City_Shimoga</th>
      <th>City_Shivpuri</th>
      <th>City_Sibsagar</th>
      <th>City_Siddharthnagar</th>
      <th>City_Siddipet</th>
      <th>City_Sidhi</th>
      <th>City_Sikar</th>
      <th>City_Silchar</th>
      <th>City_Siliguri</th>
      <th>City_Silvassa</th>
      <th>City_Sindhudurg</th>
      <th>City_Sirmaur</th>
      <th>City_Sirohi</th>
      <th>City_Sirsa</th>
      <th>City_Siruguppa</th>
      <th>City_Sitamarhi</th>
      <th>City_Sitapur</th>
      <th>City_Sivagangai</th>
      <th>City_Siwan</th>
      <th>City_Solan</th>
      <th>City_Solapur</th>
      <th>City_Sonbhadra</th>
      <th>City_Sonepur</th>
      <th>City_Sonipat</th>
      <th>City_Sonitpur</th>
      <th>City_South 24 Parganas</th>
      <th>City_South Goa</th>
      <th>City_Srikakulam</th>
      <th>City_Srinagar</th>
      <th>City_Sultanpur</th>
      <th>City_Sundargarh</th>
      <th>City_Surat</th>
      <th>City_Surendra Nagar</th>
      <th>City_Surendranagar</th>
      <th>City_Surguja</th>
      <th>City_Suryapet</th>
      <th>City_Tadipatri</th>
      <th>City_Tamenglong</th>
      <th>City_Tandur</th>
      <th>City_Tanuku</th>
      <th>City_Tarn Taran</th>
      <th>City_Tezpur</th>
      <th>City_Thane</th>
      <th>City_Thanjavur</th>
      <th>City_Theni</th>
      <th>City_Thiruvalla</th>
      <th>City_Thiruvananthapuram</th>
      <th>City_Thoothukudi</th>
      <th>City_Thoubal</th>
      <th>City_Thrissur</th>
      <th>City_Tinsukia</th>
      <th>City_Tiruchirapalli</th>
      <th>City_Tirunelveli</th>
      <th>City_Tirupati</th>
      <th>City_Tiruppur</th>
      <th>City_Tirur</th>
      <th>City_Tiruvallur</th>
      <th>City_Tiruvannamalai</th>
      <th>City_Tiruvarur</th>
      <th>City_Tonk</th>
      <th>City_Travancore</th>
      <th>City_Tumkur</th>
      <th>City_UDWADA</th>
      <th>City_UMBERGAON</th>
      <th>City_Udaipur</th>
      <th>City_Udalguri</th>
      <th>City_Udham Singh Nagar</th>
      <th>City_Udhampur</th>
      <th>City_Udupi and Uttara Kannada</th>
      <th>City_Ujjain</th>
      <th>City_Umaria</th>
      <th>City_Una</th>
      <th>City_Unnao</th>
      <th>City_Upper Subansiri</th>
      <th>City_Uttar Dinajpur</th>
      <th>City_VALLABH VIDYANAGAR</th>
      <th>City_VIJAPUR</th>
      <th>City_VIRPUR</th>
      <th>City_VISNAGAR</th>
      <th>City_Vadodara</th>
      <th>City_Valsad</th>
      <th>City_Vapi</th>
      <th>City_Varanasi</th>
      <th>City_Vellore</th>
      <th>City_Veraval</th>
      <th>City_Vidisha</th>
      <th>City_Vijayawada</th>
      <th>City_Viluppuram</th>
      <th>City_Virudhunagar</th>
      <th>City_Visakhapatnam</th>
      <th>City_Vizianagaram</th>
      <th>City_Vyara</th>
      <th>City_Warangal</th>
      <th>City_Wardha</th>
      <th>City_Washim</th>
      <th>City_Wayanad</th>
      <th>City_West Garo Hills</th>
      <th>City_West Godavari</th>
      <th>City_West Singhbhum</th>
      <th>City_Yadgir</th>
      <th>City_Yamuna Nagar</th>
      <th>City_Yavatmal</th>
      <th>City_sri ganganagar</th>
      <th>Salary_Account_Abhyuday Co-op Bank Ltd</th>
      <th>Salary_Account_Allahabad Bank</th>
      <th>Salary_Account_Andhra Bank</th>
      <th>Salary_Account_Axis Bank</th>
      <th>Salary_Account_B N P Paribas</th>
      <th>Salary_Account_Bank of Baroda</th>
      <th>Salary_Account_Bank of India</th>
      <th>Salary_Account_Bank of Maharasthra</th>
      <th>Salary_Account_Bank of Rajasthan</th>
      <th>Salary_Account_Canara Bank</th>
      <th>Salary_Account_Catholic Syrian Bank</th>
      <th>Salary_Account_Central Bank of India</th>
      <th>Salary_Account_Citibank</th>
      <th>Salary_Account_Corporation bank</th>
      <th>Salary_Account_Dena Bank</th>
      <th>Salary_Account_Deutsche Bank</th>
      <th>Salary_Account_Dhanalakshmi Bank Ltd</th>
      <th>Salary_Account_Federal Bank</th>
      <th>Salary_Account_Firstrand Bank Limited</th>
      <th>Salary_Account_GIC Housing Finance Ltd</th>
      <th>Salary_Account_HDFC Bank</th>
      <th>Salary_Account_HSBC</th>
      <th>Salary_Account_ICICI Bank</th>
      <th>Salary_Account_IDBI Bank</th>
      <th>Salary_Account_ING Vysya</th>
      <th>Salary_Account_India Bulls</th>
      <th>Salary_Account_Indian Bank</th>
      <th>Salary_Account_Indian Overseas Bank</th>
      <th>Salary_Account_IndusInd Bank</th>
      <th>Salary_Account_Industrial And Commercial Bank Of China Limited</th>
      <th>Salary_Account_J&amp;K Bank</th>
      <th>Salary_Account_Karnataka Bank</th>
      <th>Salary_Account_Karur Vysya Bank</th>
      <th>Salary_Account_Kerala Gramin Bank</th>
      <th>Salary_Account_Kotak Bank</th>
      <th>Salary_Account_Lakshmi Vilas bank</th>
      <th>Salary_Account_Oriental Bank of Commerce</th>
      <th>Salary_Account_Punjab &amp; Sind bank</th>
      <th>Salary_Account_Punjab National Bank</th>
      <th>Salary_Account_Saraswat Bank</th>
      <th>Salary_Account_South Indian Bank</th>
      <th>Salary_Account_Standard Chartered Bank</th>
      <th>Salary_Account_State Bank of Bikaner &amp; Jaipur</th>
      <th>Salary_Account_State Bank of Hyderabad</th>
      <th>Salary_Account_State Bank of India</th>
      <th>Salary_Account_State Bank of Indore</th>
      <th>Salary_Account_State Bank of Mysore</th>
      <th>Salary_Account_State Bank of Patiala</th>
      <th>Salary_Account_State Bank of Travancore</th>
      <th>Salary_Account_Syndicate Bank</th>
      <th>Salary_Account_Tamil Nadu Mercantile Bank</th>
      <th>Salary_Account_The Ratnakar Bank Ltd</th>
      <th>Salary_Account_UCO Bank</th>
      <th>Salary_Account_Union Bank of India</th>
      <th>Salary_Account_United Bank of India</th>
      <th>Salary_Account_Vijaya Bank</th>
      <th>Salary_Account_Yes Bank</th>
      <th>Mobile_Verified_N</th>
      <th>Mobile_Verified_Y</th>
      <th>Var1_HAVC</th>
      <th>Var1_HAXA</th>
      <th>Var1_HAXB</th>
      <th>Var1_HAXC</th>
      <th>Var1_HAXF</th>
      <th>Var1_HAXM</th>
      <th>Var1_HAYT</th>
      <th>Var1_HAZD</th>
      <th>Var1_HBXA</th>
      <th>Var1_HBXB</th>
      <th>Var1_HBXC</th>
      <th>Var1_HBXD</th>
      <th>Var1_HBXH</th>
      <th>Var1_HBXX</th>
      <th>Var1_HCXD</th>
      <th>Var1_HCXF</th>
      <th>Var1_HCXG</th>
      <th>Var1_HCYS</th>
      <th>Var1_HVYS</th>
      <th>Filled_Form_N</th>
      <th>Filled_Form_Y</th>
      <th>Device_Type_Mobile</th>
      <th>Device_Type_Web-browser</th>
      <th>Var2_A</th>
      <th>Var2_B</th>
      <th>Var2_C</th>
      <th>Var2_D</th>
      <th>Var2_E</th>
      <th>Var2_F</th>
      <th>Var2_G</th>
      <th>Source_S122</th>
      <th>Source_S123</th>
      <th>Source_S124</th>
      <th>Source_S125</th>
      <th>Source_S127</th>
      <th>Source_S129</th>
      <th>Source_S130</th>
      <th>Source_S133</th>
      <th>Source_S134</th>
      <th>Source_S135</th>
      <th>Source_S136</th>
      <th>Source_S137</th>
      <th>Source_S138</th>
      <th>Source_S139</th>
      <th>Source_S140</th>
      <th>Source_S141</th>
      <th>Source_S143</th>
      <th>Source_S144</th>
      <th>Source_S150</th>
      <th>Source_S151</th>
      <th>Source_S153</th>
      <th>Source_S154</th>
      <th>Source_S155</th>
      <th>Source_S156</th>
      <th>Source_S157</th>
      <th>Source_S158</th>
      <th>Source_S159</th>
      <th>Source_S160</th>
      <th>Source_S161</th>
      <th>Source_S162</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




    cat_features_test.head(5)




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender_Female</th>
      <th>Gender_Male</th>
      <th>City_ADIPUR</th>
      <th>City_AHMEDB</th>
      <th>City_AMALSAD</th>
      <th>City_ANJAR</th>
      <th>City_Abohar</th>
      <th>City_Adilabad</th>
      <th>City_Agartala</th>
      <th>City_Agra</th>
      <th>City_Ahmedabad</th>
      <th>City_Ahmednagar</th>
      <th>City_Aizawl</th>
      <th>City_Ajmer</th>
      <th>City_Akola</th>
      <th>City_Alappuzha</th>
      <th>City_Aligarh</th>
      <th>City_Allahabad</th>
      <th>City_Alleppey</th>
      <th>City_Almora</th>
      <th>City_Aluva</th>
      <th>City_Alwar</th>
      <th>City_Amareli</th>
      <th>City_Ambala</th>
      <th>City_Ambedkar Nagar</th>
      <th>City_Ambikapur</th>
      <th>City_Ambur</th>
      <th>City_Amravati</th>
      <th>City_Amreli</th>
      <th>City_Amritsar</th>
      <th>City_Anand</th>
      <th>City_Anantapur</th>
      <th>City_Andman &amp; Nicobar</th>
      <th>City_Angul</th>
      <th>City_Ankleshwar</th>
      <th>City_Anuppur</th>
      <th>City_Araria</th>
      <th>City_Ariyalur</th>
      <th>City_Asansol</th>
      <th>City_Ashoknagar</th>
      <th>City_Aurangabad</th>
      <th>City_BARDOLI</th>
      <th>City_BHACHAU</th>
      <th>City_BILIMORA</th>
      <th>City_Baddi</th>
      <th>City_Bagalkote</th>
      <th>City_Bagpat</th>
      <th>City_Bahadurgarh</th>
      <th>City_Bahraich</th>
      <th>City_Balaghat</th>
      <th>City_Balasore</th>
      <th>City_Baleswar</th>
      <th>City_Ballia</th>
      <th>City_Balrampur</th>
      <th>City_Banaskantha</th>
      <th>City_Banaskhantha</th>
      <th>City_Banka</th>
      <th>City_Bankura</th>
      <th>City_Barabanki</th>
      <th>City_Baramati</th>
      <th>City_Baran</th>
      <th>City_Bardhaman</th>
      <th>City_Bareilly</th>
      <th>City_Bargarh</th>
      <th>City_Barmer</th>
      <th>City_Barnala</th>
      <th>City_Barpeta</th>
      <th>City_Bastar</th>
      <th>City_Bathinda</th>
      <th>City_Beawar</th>
      <th>City_Beed</th>
      <th>City_Begusarai</th>
      <th>City_Behrampur</th>
      <th>City_Belgaum</th>
      <th>City_Bellary</th>
      <th>City_Bengaluru</th>
      <th>City_Bettiah</th>
      <th>City_Betul</th>
      <th>City_Bhabua</th>
      <th>City_Bhadrak</th>
      <th>City_Bhagalpur</th>
      <th>City_Bhandara</th>
      <th>City_Bharatpur</th>
      <th>City_Bharuch</th>
      <th>City_Bhavnagar</th>
      <th>City_Bhilai</th>
      <th>City_Bhilwara</th>
      <th>City_Bhiwadi</th>
      <th>City_Bhiwani</th>
      <th>City_Bhojpur</th>
      <th>City_Bhopal</th>
      <th>City_Bhubaneswar</th>
      <th>City_Bhuj</th>
      <th>City_Bidar</th>
      <th>City_Bijapur</th>
      <th>City_Bijnor</th>
      <th>City_Bikaner</th>
      <th>City_Bilaspur</th>
      <th>City_Birbhum</th>
      <th>City_Bokaro</th>
      <th>City_Bolangir</th>
      <th>City_Bongaigaon</th>
      <th>City_Boudh</th>
      <th>City_Budgam</th>
      <th>City_Bulandshahr</th>
      <th>City_Buldhana</th>
      <th>City_Bundi</th>
      <th>City_Burdwan</th>
      <th>City_Burhanpur</th>
      <th>City_Buxar</th>
      <th>City_Chamarajanagar</th>
      <th>City_Champhai</th>
      <th>City_Chandauli</th>
      <th>City_Chandigarh</th>
      <th>City_Chandrapur</th>
      <th>City_Chapra</th>
      <th>City_Chatra</th>
      <th>City_Chennai</th>
      <th>City_Chhatarpur</th>
      <th>City_Chhindwara</th>
      <th>City_Chidambaram</th>
      <th>City_Chikkaballapur</th>
      <th>City_Chikkamagaluru</th>
      <th>City_Chitradurga</th>
      <th>City_Chittoor</th>
      <th>City_Chittorgarh</th>
      <th>City_Churachandpur</th>
      <th>City_Churu</th>
      <th>City_Coimbatore</th>
      <th>City_Cooch Behar</th>
      <th>City_Cuddalore</th>
      <th>City_Cuttack</th>
      <th>City_DEESA</th>
      <th>City_DWARKA</th>
      <th>City_Dahod</th>
      <th>City_Dakshin Dinajpur</th>
      <th>City_Dakshina Kannada</th>
      <th>City_Daman</th>
      <th>City_Daman &amp; Diu</th>
      <th>City_Damoh</th>
      <th>City_Dantewada</th>
      <th>City_Darjeeling</th>
      <th>City_Darrang</th>
      <th>City_Datia</th>
      <th>City_Dausa</th>
      <th>City_Davanagere</th>
      <th>City_Dehradun</th>
      <th>City_Delhi</th>
      <th>City_Deogarh</th>
      <th>City_Deoghar</th>
      <th>City_Deoria</th>
      <th>City_Dewas</th>
      <th>City_Dhamtari</th>
      <th>City_Dhanbad</th>
      <th>City_Dhar</th>
      <th>City_Dharmapuri</th>
      <th>City_Dharwad</th>
      <th>City_Dhenkanal</th>
      <th>City_Dhubri</th>
      <th>City_Dhule</th>
      <th>City_Dibrugarh</th>
      <th>City_Dimapur</th>
      <th>City_Dindigul</th>
      <th>City_Dindori</th>
      <th>City_Doda</th>
      <th>City_Dungarpur</th>
      <th>City_Durg</th>
      <th>City_Durgapur</th>
      <th>City_East Godavari</th>
      <th>City_East Khasi Hills</th>
      <th>City_East Singhbhum</th>
      <th>City_Ernakulam</th>
      <th>City_Erode</th>
      <th>City_Etah</th>
      <th>City_Faizabad</th>
      <th>City_Faridabad</th>
      <th>City_Farrukhabad</th>
      <th>City_Fatehabad</th>
      <th>City_Fatehgarh Sahib</th>
      <th>City_Fazilka</th>
      <th>City_Firozabad</th>
      <th>City_Firozpur</th>
      <th>City_Gadag</th>
      <th>City_Gadchiroli</th>
      <th>City_Gadwal</th>
      <th>City_Gajapati</th>
      <th>City_Gandhi Nagar</th>
      <th>City_Gandhidham</th>
      <th>City_Gandhinagar</th>
      <th>City_Ganganagar</th>
      <th>City_Gangtok</th>
      <th>City_Ganjam</th>
      <th>City_Gautam Buddha Nagar</th>
      <th>City_Gaya</th>
      <th>City_Geyzing</th>
      <th>City_Ghaziabad</th>
      <th>City_Ghazipur</th>
      <th>City_Giridih</th>
      <th>City_Goa</th>
      <th>City_Goalpara</th>
      <th>City_Golaghat</th>
      <th>City_Gonda</th>
      <th>City_Gondia</th>
      <th>City_Gopal Ganj</th>
      <th>City_Gorakhpur</th>
      <th>City_Gorkakhpur</th>
      <th>City_Gulbarga</th>
      <th>City_Guna</th>
      <th>City_Guntur</th>
      <th>City_Gurdaspur</th>
      <th>City_Gurgaon</th>
      <th>City_Guwahati</th>
      <th>City_Gwalior</th>
      <th>City_Hajipur</th>
      <th>City_Haldia</th>
      <th>City_Haldwani</th>
      <th>City_Halol</th>
      <th>City_Hanumangarh</th>
      <th>City_Hapur</th>
      <th>City_Hardoi</th>
      <th>City_Haridwar</th>
      <th>City_Hassan</th>
      <th>City_Haveri</th>
      <th>City_Himat Nagar</th>
      <th>City_Himatnagar</th>
      <th>City_Hisar</th>
      <th>City_Hooghly</th>
      <th>City_Hoshiarpur</th>
      <th>City_Hospet</th>
      <th>City_Hosur</th>
      <th>City_Howrah</th>
      <th>City_Hubli</th>
      <th>City_Hyderabad</th>
      <th>City_IDAR</th>
      <th>City_Ichalkaranji</th>
      <th>City_Idukki</th>
      <th>City_Imphal East</th>
      <th>City_Imphal West</th>
      <th>City_Indore</th>
      <th>City_Itanagar</th>
      <th>City_Jabalpur</th>
      <th>City_Jagadalpur</th>
      <th>City_Jagatsinghpur</th>
      <th>City_Jagdalpur</th>
      <th>City_Jaintia Hills</th>
      <th>City_Jaipur</th>
      <th>City_Jaisalmer</th>
      <th>City_Jajapur</th>
      <th>City_Jalandhar</th>
      <th>City_Jalaun</th>
      <th>City_Jalgaon</th>
      <th>City_Jalna</th>
      <th>City_Jalpaiguri</th>
      <th>City_Jammu</th>
      <th>City_Jamnagar</th>
      <th>City_Jamshedpur</th>
      <th>City_Jamtara</th>
      <th>City_Jamui</th>
      <th>City_Janjgir-Champa</th>
      <th>City_Jashpur</th>
      <th>City_Jaunpur</th>
      <th>City_Jhabua</th>
      <th>City_Jhajjar</th>
      <th>City_Jhalawar</th>
      <th>City_Jhansi</th>
      <th>City_Jharkhand</th>
      <th>City_Jharsuguda</th>
      <th>City_Jhunjhunu</th>
      <th>City_Jind</th>
      <th>City_Jodhpur</th>
      <th>City_Jorhat</th>
      <th>City_Junagadh</th>
      <th>City_Jyotiba Phule Nagar</th>
      <th>City_KALOL</th>
      <th>City_KAPADWANJ</th>
      <th>City_KHAMBHAT</th>
      <th>City_Kabri Anglong</th>
      <th>City_Kadapa</th>
      <th>City_Kadi</th>
      <th>City_Kailashahar</th>
      <th>City_Kaithal</th>
      <th>City_Kakinada</th>
      <th>City_Kalahandi</th>
      <th>City_Kalka</th>
      <th>City_Kamrup Metropolitian</th>
      <th>City_Kamrup Rural</th>
      <th>City_Kanchipuram</th>
      <th>City_Kangra</th>
      <th>City_Kannur</th>
      <th>City_Kanpur</th>
      <th>City_Kanpur Nagar</th>
      <th>City_Kanyakumari</th>
      <th>City_Kapurthala</th>
      <th>City_Karad</th>
      <th>City_Karauli</th>
      <th>City_Karim Ganj</th>
      <th>City_Karimnagar</th>
      <th>City_Karnal</th>
      <th>City_Karnataka</th>
      <th>City_Karur</th>
      <th>City_Kasaragod</th>
      <th>City_Kashipur</th>
      <th>City_Kathua</th>
      <th>City_Katihar</th>
      <th>City_Katni</th>
      <th>City_Kaushambi</th>
      <th>City_Kendrapara</th>
      <th>City_Kendujhar</th>
      <th>City_Keonjhar</th>
      <th>City_Khammam</th>
      <th>City_Khandwa</th>
      <th>City_Khanna</th>
      <th>City_Kharagpur</th>
      <th>City_Khargone</th>
      <th>City_Kheda</th>
      <th>City_Khurdha</th>
      <th>City_Kishanganj</th>
      <th>City_Kochi</th>
      <th>City_Kodad</th>
      <th>City_Kohima</th>
      <th>City_Kolar</th>
      <th>City_Kolhapur</th>
      <th>City_Kolkata</th>
      <th>City_Kollam</th>
      <th>City_Koppal</th>
      <th>City_Koraput</th>
      <th>City_Korba</th>
      <th>City_Koriya</th>
      <th>City_Kota</th>
      <th>City_Kottayam</th>
      <th>City_Kozhikode</th>
      <th>City_Krishna</th>
      <th>City_Krishnagiri</th>
      <th>City_Kullu</th>
      <th>City_Kumbakonam</th>
      <th>City_Kurnool</th>
      <th>City_Kurukshetra</th>
      <th>City_Kushinagar</th>
      <th>City_Kutch</th>
      <th>City_Lakhimpur</th>
      <th>City_Lakhimpur Kheri</th>
      <th>City_Lalitpur</th>
      <th>City_Latehar</th>
      <th>City_Latur</th>
      <th>City_Leh</th>
      <th>City_Lohardaga</th>
      <th>City_Lucknow</th>
      <th>City_Ludhiana</th>
      <th>City_Lunglei</th>
      <th>City_MANDVI</th>
      <th>City_Madurai</th>
      <th>City_Mahabub Nagar</th>
      <th>City_Mahamaya Nagar</th>
      <th>City_Maharajganj</th>
      <th>City_Mahasamund</th>
      <th>City_Mahbubnagar</th>
      <th>City_Mahendragarh</th>
      <th>City_Malabar</th>
      <th>City_Malappuram</th>
      <th>City_Malda</th>
      <th>City_Malegaon</th>
      <th>City_Malkangiri</th>
      <th>City_Mancherial</th>
      <th>City_Mandi</th>
      <th>City_Mandla</th>
      <th>City_Mandsaur</th>
      <th>City_Mandya</th>
      <th>City_Mangalore</th>
      <th>City_Mansa</th>
      <th>City_Margao</th>
      <th>City_Margoa</th>
      <th>City_Mathura</th>
      <th>City_Mau</th>
      <th>City_Mayurbhanj</th>
      <th>City_Medak</th>
      <th>City_Meerut</th>
      <th>City_Mehsana</th>
      <th>City_Mewat</th>
      <th>City_Midnapore East</th>
      <th>City_Midnapore West</th>
      <th>City_Mirzapur</th>
      <th>City_Modasa</th>
      <th>City_Moga</th>
      <th>City_Mohali</th>
      <th>City_Monghyr</th>
      <th>City_Moradabad</th>
      <th>City_Morena</th>
      <th>City_Morvi</th>
      <th>City_Motihari</th>
      <th>City_Muktsar</th>
      <th>City_Mumbai</th>
      <th>City_Mundra</th>
      <th>City_Munger</th>
      <th>City_Murshidabad</th>
      <th>City_Muzaffarnagar</th>
      <th>City_Muzaffarpur</th>
      <th>City_Mysore</th>
      <th>City_Nabarangpur</th>
      <th>City_Nabha</th>
      <th>City_Nadia</th>
      <th>City_Nadiad</th>
      <th>City_Nagaon</th>
      <th>City_Nagapattinam</th>
      <th>City_Nagaur</th>
      <th>City_Nagercoil</th>
      <th>City_Nagpur</th>
      <th>City_Nalanda</th>
      <th>City_Nalbari</th>
      <th>City_Nalgonda</th>
      <th>City_Namakkal</th>
      <th>City_Nanded</th>
      <th>City_Nandurbar</th>
      <th>City_Narmada</th>
      <th>City_Narsinghpur</th>
      <th>City_Nashik</th>
      <th>City_Navi Mumbai</th>
      <th>City_Navsari</th>
      <th>City_Nawadah</th>
      <th>City_Nawanshahr</th>
      <th>City_Nayagarh</th>
      <th>City_Neemuch</th>
      <th>City_Nellore</th>
      <th>City_Nilgiris</th>
      <th>City_Nizamabad</th>
      <th>City_Noida</th>
      <th>City_North 24 Parganas</th>
      <th>City_Ongole</th>
      <th>City_Osmanabad</th>
      <th>City_PALANPUR</th>
      <th>City_Pakur</th>
      <th>City_Palakkad</th>
      <th>City_Palamu</th>
      <th>City_Pali</th>
      <th>City_Palwal</th>
      <th>City_Panaji</th>
      <th>City_Panchkula</th>
      <th>City_Panchmahal</th>
      <th>City_Panipat</th>
      <th>City_Panna</th>
      <th>City_Papum Pare</th>
      <th>City_Parbhani</th>
      <th>City_Patan</th>
      <th>City_Pathanamthitta</th>
      <th>City_Pathankot</th>
      <th>City_Patiala</th>
      <th>City_Patna</th>
      <th>City_Pauri Garhwal</th>
      <th>City_Perambalur</th>
      <th>City_Phagwara</th>
      <th>City_Pilibhit</th>
      <th>City_Pollachi</th>
      <th>City_Ponda</th>
      <th>City_Pondicherry</th>
      <th>City_Pontashaib</th>
      <th>City_Poonch</th>
      <th>City_Porbandar</th>
      <th>City_Prakasam</th>
      <th>City_Pratapgarh</th>
      <th>City_Proddattur</th>
      <th>City_Pudukkottai</th>
      <th>City_Pune</th>
      <th>City_Puri</th>
      <th>City_Purnia</th>
      <th>City_Purulia</th>
      <th>City_RAJPIPLA</th>
      <th>City_Rae Bareli</th>
      <th>City_Raichur</th>
      <th>City_Raigad</th>
      <th>City_Raigarh</th>
      <th>City_Raipur</th>
      <th>City_Rajahmundry</th>
      <th>City_Rajgarh</th>
      <th>City_Rajkot</th>
      <th>City_Rajnandgaon</th>
      <th>City_Rajouri</th>
      <th>City_Rajpura</th>
      <th>City_Rajsamand</th>
      <th>City_Ramanagara</th>
      <th>City_Ramanathapuram</th>
      <th>City_Ramgarh</th>
      <th>City_Rampur</th>
      <th>City_Ranchi</th>
      <th>City_Rangareddy</th>
      <th>City_Ratlam</th>
      <th>City_Ratnagiri</th>
      <th>City_Rayagada</th>
      <th>City_Reasi</th>
      <th>City_Rewa</th>
      <th>City_Rewari</th>
      <th>City_Rohtak</th>
      <th>City_Rohtas</th>
      <th>City_Roorkee</th>
      <th>City_Ropar</th>
      <th>City_Rourkela</th>
      <th>City_Rudraprayag</th>
      <th>City_Rudrapur</th>
      <th>City_SANAND</th>
      <th>City_SILVASSA</th>
      <th>City_SURENDERNAGAR</th>
      <th>City_Sagar</th>
      <th>City_Saharanpur</th>
      <th>City_Saharsa</th>
      <th>City_Saiha</th>
      <th>City_Salem</th>
      <th>City_Samastipur</th>
      <th>City_Samba</th>
      <th>City_Sambalpur</th>
      <th>City_Sanga Reddy</th>
      <th>City_Sangamner</th>
      <th>City_Sangli</th>
      <th>City_Sangrur</th>
      <th>City_Satara</th>
      <th>City_Satna</th>
      <th>City_Secunderabad</th>
      <th>City_Sehore</th>
      <th>City_Shahdol</th>
      <th>City_Shahjahanpur</th>
      <th>City_Shahpura</th>
      <th>City_Shajapur</th>
      <th>City_Sheopur</th>
      <th>City_Shilong</th>
      <th>City_Shimla</th>
      <th>City_Shimoga</th>
      <th>City_Shivpuri</th>
      <th>City_Sibsagar</th>
      <th>City_Siddharthnagar</th>
      <th>City_Siddipet</th>
      <th>City_Sidhi</th>
      <th>City_Sikar</th>
      <th>City_Silchar</th>
      <th>City_Siliguri</th>
      <th>City_Silvassa</th>
      <th>City_Sindhudurg</th>
      <th>City_Sirmaur</th>
      <th>City_Sirohi</th>
      <th>City_Sirsa</th>
      <th>City_Sitamarhi</th>
      <th>City_Sivagangai</th>
      <th>City_Siwan</th>
      <th>City_Solan</th>
      <th>City_Solapur</th>
      <th>City_Sonbhadra</th>
      <th>City_Sonepur</th>
      <th>City_Sonipat</th>
      <th>City_South 24 Parganas</th>
      <th>City_South Goa</th>
      <th>City_Srikakulam</th>
      <th>City_Srinagar</th>
      <th>City_Sriperumbudur</th>
      <th>City_Sultanpur</th>
      <th>City_Sundargarh</th>
      <th>City_Surat</th>
      <th>City_Surendra Nagar</th>
      <th>City_Surguja</th>
      <th>City_Suryapet</th>
      <th>City_Tanuku</th>
      <th>City_Tarn Taran</th>
      <th>City_Tawang</th>
      <th>City_Tezpur</th>
      <th>City_Thane</th>
      <th>City_Thanjavur</th>
      <th>City_Theni</th>
      <th>City_Thiruvalla</th>
      <th>City_Thiruvananthapuram</th>
      <th>City_Thoothukudi</th>
      <th>City_Thrissur</th>
      <th>City_Tinsukia</th>
      <th>City_Tiruchirapalli</th>
      <th>City_Tirunelveli</th>
      <th>City_Tirupati</th>
      <th>City_Tiruppur</th>
      <th>City_Tirur</th>
      <th>City_Tiruvallur</th>
      <th>City_Tiruvannamalai</th>
      <th>City_Tiruvarur</th>
      <th>City_Tonk</th>
      <th>City_Tumkur</th>
      <th>City_Udaipur</th>
      <th>City_Udham Singh Nagar</th>
      <th>City_Udhampur</th>
      <th>City_Udupi and Uttara Kannada</th>
      <th>City_Ujjain</th>
      <th>City_Una</th>
      <th>City_Unnao</th>
      <th>City_Upper Subansiri</th>
      <th>City_Uttar Dinajpur</th>
      <th>City_VIRPUR</th>
      <th>City_VISNAGAR</th>
      <th>City_Vadodara</th>
      <th>City_Valsad</th>
      <th>City_Vapi</th>
      <th>City_Varanasi</th>
      <th>City_Vellore</th>
      <th>City_Veraval</th>
      <th>City_Vidisha</th>
      <th>City_Vijayawada</th>
      <th>City_Viluppuram</th>
      <th>City_Virudhunagar</th>
      <th>City_Visakhapatnam</th>
      <th>City_Vizianagaram</th>
      <th>City_Vyara</th>
      <th>City_WAGHODIA</th>
      <th>City_Warangal</th>
      <th>City_Wardha</th>
      <th>City_Washim</th>
      <th>City_Wayanad</th>
      <th>City_West Godavari</th>
      <th>City_West Singhbhum</th>
      <th>City_Yadgir</th>
      <th>City_Yamuna Nagar</th>
      <th>City_Yavatmal</th>
      <th>City_sri ganganagar</th>
      <th>Salary_Account_Abhyuday Co-op Bank Ltd</th>
      <th>Salary_Account_Ahmedabad Mercantile Cooperative Bank</th>
      <th>Salary_Account_Allahabad Bank</th>
      <th>Salary_Account_Andhra Bank</th>
      <th>Salary_Account_Axis Bank</th>
      <th>Salary_Account_B N P Paribas</th>
      <th>Salary_Account_Bank of Baroda</th>
      <th>Salary_Account_Bank of India</th>
      <th>Salary_Account_Bank of Maharasthra</th>
      <th>Salary_Account_Bank of Rajasthan</th>
      <th>Salary_Account_Canara Bank</th>
      <th>Salary_Account_Catholic Syrian Bank</th>
      <th>Salary_Account_Central Bank of India</th>
      <th>Salary_Account_Citibank</th>
      <th>Salary_Account_Corporation bank</th>
      <th>Salary_Account_Dena Bank</th>
      <th>Salary_Account_Deutsche Bank</th>
      <th>Salary_Account_Dhanalakshmi Bank Ltd</th>
      <th>Salary_Account_Federal Bank</th>
      <th>Salary_Account_Firstrand Bank Limited</th>
      <th>Salary_Account_GIC Housing Finance Ltd</th>
      <th>Salary_Account_HDFC Bank</th>
      <th>Salary_Account_HSBC</th>
      <th>Salary_Account_ICICI Bank</th>
      <th>Salary_Account_IDBI Bank</th>
      <th>Salary_Account_ING Vysya</th>
      <th>Salary_Account_India Bulls</th>
      <th>Salary_Account_Indian Bank</th>
      <th>Salary_Account_Indian Overseas Bank</th>
      <th>Salary_Account_IndusInd Bank</th>
      <th>Salary_Account_Industrial And Commercial Bank Of China Limited</th>
      <th>Salary_Account_J&amp;K Bank</th>
      <th>Salary_Account_Karnataka Bank</th>
      <th>Salary_Account_Karur Vysya Bank</th>
      <th>Salary_Account_Kotak Bank</th>
      <th>Salary_Account_Lakshmi Vilas bank</th>
      <th>Salary_Account_Oriental Bank of Commerce</th>
      <th>Salary_Account_Punjab &amp; Sind bank</th>
      <th>Salary_Account_Punjab National Bank</th>
      <th>Salary_Account_Saraswat Bank</th>
      <th>Salary_Account_South Indian Bank</th>
      <th>Salary_Account_Standard Chartered Bank</th>
      <th>Salary_Account_State Bank of Bikaner &amp; Jaipur</th>
      <th>Salary_Account_State Bank of Hyderabad</th>
      <th>Salary_Account_State Bank of India</th>
      <th>Salary_Account_State Bank of Indore</th>
      <th>Salary_Account_State Bank of Mysore</th>
      <th>Salary_Account_State Bank of Patiala</th>
      <th>Salary_Account_State Bank of Travancore</th>
      <th>Salary_Account_Syndicate Bank</th>
      <th>Salary_Account_Tamil Nadu Mercantile Bank</th>
      <th>Salary_Account_The Ratnakar Bank Ltd</th>
      <th>Salary_Account_UCO Bank</th>
      <th>Salary_Account_Union Bank of India</th>
      <th>Salary_Account_United Bank of India</th>
      <th>Salary_Account_Vijaya Bank</th>
      <th>Salary_Account_Yes Bank</th>
      <th>Mobile_Verified_N</th>
      <th>Mobile_Verified_Y</th>
      <th>Var1_HAVC</th>
      <th>Var1_HAXA</th>
      <th>Var1_HAXB</th>
      <th>Var1_HAXC</th>
      <th>Var1_HAXF</th>
      <th>Var1_HAXM</th>
      <th>Var1_HAYT</th>
      <th>Var1_HAZD</th>
      <th>Var1_HBXA</th>
      <th>Var1_HBXB</th>
      <th>Var1_HBXC</th>
      <th>Var1_HBXD</th>
      <th>Var1_HBXH</th>
      <th>Var1_HBXX</th>
      <th>Var1_HCXD</th>
      <th>Var1_HCXF</th>
      <th>Var1_HCXG</th>
      <th>Var1_HCYS</th>
      <th>Var1_HVYS</th>
      <th>Filled_Form_N</th>
      <th>Filled_Form_Y</th>
      <th>Device_Type_Mobile</th>
      <th>Device_Type_Web-browser</th>
      <th>Var2_A</th>
      <th>Var2_B</th>
      <th>Var2_C</th>
      <th>Var2_D</th>
      <th>Var2_E</th>
      <th>Var2_F</th>
      <th>Var2_G</th>
      <th>Source_S122</th>
      <th>Source_S123</th>
      <th>Source_S124</th>
      <th>Source_S126</th>
      <th>Source_S127</th>
      <th>Source_S129</th>
      <th>Source_S131</th>
      <th>Source_S132</th>
      <th>Source_S133</th>
      <th>Source_S134</th>
      <th>Source_S136</th>
      <th>Source_S137</th>
      <th>Source_S138</th>
      <th>Source_S139</th>
      <th>Source_S141</th>
      <th>Source_S142</th>
      <th>Source_S143</th>
      <th>Source_S144</th>
      <th>Source_S150</th>
      <th>Source_S151</th>
      <th>Source_S153</th>
      <th>Source_S155</th>
      <th>Source_S156</th>
      <th>Source_S157</th>
      <th>Source_S158</th>
      <th>Source_S159</th>
      <th>Source_S161</th>
      <th>Source_S162</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>


# creating the age 
tran_sample=train.iloc[0:1000,]
tran_sample['age']=(pd.to_datetime(tran_sample['Lead_Creation_Date'])-pd.to_datetime(tran_sample['DOB']))  # differncein time delta object represented in days
tran_sample['age_days']=tran_sample['age'].astype('timedelta64[D]') # converting the difffernce to days use [h] for hours etc
tran_sample['age_years']=tran_sample['age_days']/365.25 # converting the days to years
#new derived features
tran_sample['LAbyMI']=tran_sample[u'Loan_Amount_Applied']/tran_sample[u'Monthly_Income']
tran_sample['LAbyTenure']=tran_sample[u'Loan_Amount_Applied']/tran_sample[u'Loan_Tenure_Applied']
tran_sample['MIbyage']=tran_sample[u'Monthly_Income']/tran_sample[u'age_years']

    #new derived features train
    train['LAbyMI']=train[u'Loan_Amount_Applied']/train[u'Monthly_Income']
    train['LAbyTenure']=train[u'Loan_Amount_Applied']/train[u'Loan_Tenure_Applied']
    train['MIbyage']=train[u'Monthly_Income']/train[u'age_years_imp']
    train['la_diff']=train['Loan_Amount_Applied']-train['Loan_Amount_Submitted_imp']
    train['lt_diff']=train['Loan_Tenure_Applied']-train['Loan_Tenure_Submitted_imp']


    #new derived features test
    test['LAbyMI']=test[u'Loan_Amount_Applied']/test[u'Monthly_Income']
    test['LAbyTenure']=test[u'Loan_Amount_Applied']/test[u'Loan_Tenure_Applied']
    test['MIbyage']=test[u'Monthly_Income']/test[u'age_years_imp']
    test['la_diff']=test['Loan_Amount_Applied']-test['Loan_Amount_Submitted_imp']
    test['lt_diff']=test['Loan_Tenure_Applied']-test['Loan_Tenure_Submitted_imp']


    train.columns




    Index([u'ID', u'Gender', u'City', u'Monthly_Income', u'DOB',
           u'Lead_Creation_Date', u'Loan_Amount_Applied', u'Loan_Tenure_Applied',
           u'Existing_EMI', u'Employer_Name', u'Salary_Account',
           u'Mobile_Verified', u'Var5', u'Var1', u'Loan_Amount_Submitted',
           u'Loan_Tenure_Submitted', u'Interest_Rate', u'Processing_Fee',
           u'EMI_Loan_Submitted', u'Filled_Form', u'Device_Type', u'Var2',
           u'Source', u'Var4', u'LoggedIn', u'Disbursed', u'age_years',
           u'age_years_imp', u'Loan_Amount_Submitted_imp', u'Interest_Rate_imp',
           u'Loan_Tenure_Submitted_imp', u'LAbyMI', u'LAbyTenure', u'MIbyage'],
          dtype='object')




    train_clus=pd.concat([train,clus3[['cluster_label3']]],axis=1)


    test_clus=pd.concat([test,test_clus3[['cluster_label3']]],axis=1)


    #describing non categorical variables
    noncat_var=[]
    for i in train_clus.columns:
        if train_clus[i].dtypes!='O':
            print i , train_clus[i].describe()
            print "nullcount:" ,train_clus[i].isnull().sum()
            print "\n"
            noncat_var.append((i,len(train_clus[i].unique())))

    Monthly_Income count    8.702000e+04
    mean     5.884997e+04
    std      2.177511e+06
    min      0.000000e+00
    25%      1.650000e+04
    50%      2.500000e+04
    75%      4.000000e+04
    max      4.445544e+08
    Name: Monthly_Income, dtype: float64
    nullcount: 0
    
    
    Loan_Amount_Applied count       86949.000000
    mean       230250.699928
    std        354206.759468
    min             0.000000
    25%             0.000000
    50%        100000.000000
    75%        300000.000000
    max      10000000.000000
    Name: Loan_Amount_Applied, dtype: float64
    nullcount: 71
    
    
    Loan_Tenure_Applied count    86949.000000
    mean         2.131399
    std          2.014193
    min          0.000000
    25%          0.000000
    50%          2.000000
    75%          4.000000
    max         10.000000
    Name: Loan_Tenure_Applied, dtype: float64
    nullcount: 71
    
    
    Existing_EMI count       86949.000000
    mean         3696.227824
    std         39810.211920
    min             0.000000
    25%             0.000000
    50%             0.000000
    75%          3500.000000
    max      10000000.000000
    Name: Existing_EMI, dtype: float64
    nullcount: 71
    
    
    Var5 count    87020.000000
    mean         4.961503
    std          5.670385
    min          0.000000
    25%          0.000000
    50%          2.000000
    75%         11.000000
    max         18.000000
    Name: Var5, dtype: float64
    nullcount: 0
    
    
    Loan_Amount_Submitted count      52407.000000
    mean      395010.590188
    std       308248.136255
    min        50000.000000
    25%       200000.000000
    50%       300000.000000
    75%       500000.000000
    max      3000000.000000
    Name: Loan_Amount_Submitted, dtype: float64
    nullcount: 34613
    
    
    Loan_Tenure_Submitted count    52407.000000
    mean         3.891369
    std          1.165359
    min          1.000000
    25%          3.000000
    50%          4.000000
    75%          5.000000
    max          6.000000
    Name: Loan_Tenure_Submitted, dtype: float64
    nullcount: 34613
    
    
    Interest_Rate count    27726.000000
    mean        19.197474
    std          5.834213
    min         11.990000
    25%         15.250000
    50%         18.000000
    75%         20.000000
    max         37.000000
    Name: Interest_Rate, dtype: float64
    nullcount: 59294
    
    
    Processing_Fee count    27420.000000
    mean      5131.150839
    std       4725.837644
    min        200.000000
    25%       2000.000000
    50%       4000.000000
    75%       6250.000000
    max      50000.000000
    Name: Processing_Fee, dtype: float64
    nullcount: 59600
    
    
    EMI_Loan_Submitted count     27726.000000
    mean      10999.528377
    std        7512.323050
    min        1176.410000
    25%        6491.600000
    50%        9392.970000
    75%       12919.040000
    max      144748.280000
    Name: EMI_Loan_Submitted, dtype: float64
    nullcount: 59294
    
    
    Var4 count    87020.000000
    mean         2.949805
    std          1.697720
    min          0.000000
    25%          1.000000
    50%          3.000000
    75%          5.000000
    max          7.000000
    Name: Var4, dtype: float64
    nullcount: 0
    
    
    LoggedIn count    87020.000000
    mean         0.029350
    std          0.168785
    min          0.000000
    25%          0.000000
    50%          0.000000
    75%          0.000000
    max          1.000000
    Name: LoggedIn, dtype: float64
    nullcount: 0
    
    
    Disbursed count    87020.000000
    mean         0.014629
    std          0.120062
    min          0.000000
    25%          0.000000
    50%          0.000000
    75%          0.000000
    max          1.000000
    Name: Disbursed, dtype: float64
    nullcount: 0
    
    
    age_years count    87020.000000
    mean        28.346595
    std         13.197275
    min        -49.648186
    25%         25.752225
    50%         28.947296
    75%         33.106092
    max         50.570842
    Name: age_years, dtype: float64
    nullcount: 0
    
    
    age_years_imp count    87020.000000
    mean        30.257300
    std          5.884408
    min         18.001369
    25%         26.063655
    50%         29.259411
    75%         33.106092
    max         50.570842
    Name: age_years_imp, dtype: float64
    nullcount: 0
    
    
    Loan_Amount_Submitted_imp count       86985.000000
    mean       323207.650756
    std        333634.521087
    min             0.000000
    25%        100000.000000
    50%        240000.000000
    75%        450000.000000
    max      10000000.000000
    Name: Loan_Amount_Submitted_imp, dtype: float64
    nullcount: 35
    
    
    Interest_Rate_imp count    87020.000000
    mean        18.381535
    std          3.340079
    min         11.990000
    25%         18.000000
    50%         18.000000
    75%         18.000000
    max         37.000000
    Name: Interest_Rate_imp, dtype: float64
    nullcount: 0
    
    
    Loan_Tenure_Submitted_imp count    86985.000000
    mean         3.193390
    std          1.780125
    min          0.000000
    25%          2.000000
    50%          4.000000
    75%          5.000000
    max         10.000000
    Name: Loan_Tenure_Submitted_imp, dtype: float64
    nullcount: 35
    
    
    LAbyMI count    8.663800e+04
    mean              inf
    std               NaN
    min      0.000000e+00
    25%      0.000000e+00
    50%      5.555556e+00
    75%      1.136364e+01
    max               inf
    Name: LAbyMI, dtype: float64
    nullcount: 382
    
    
    LAbyTenure count    5.858600e+04
    mean              inf
    std               NaN
    min      0.000000e+00
    25%      5.000000e+04
    50%      1.000000e+05
    75%      1.500000e+05
    max               inf
    Name: LAbyTenure, dtype: float64
    nullcount: 28434
    
    
    MIbyage count       87020.000000
    mean         1919.757826
    std         75629.248224
    min             0.000000
    25%           576.104101
    50%           830.415606
    75%          1280.080053
    max      16693071.893261
    Name: MIbyage, dtype: float64
    nullcount: 0
    
    
    la_diff count      86949.000000
    mean      -92920.670658
    std       293876.417647
    min     -3000000.000000
    25%            0.000000
    50%            0.000000
    75%            0.000000
    max      8249999.000000
    Name: la_diff, dtype: float64
    nullcount: 71
    
    
    lt_diff count    86949.000000
    mean        -1.061818
    std          1.901581
    min         -5.000000
    25%          0.000000
    50%          0.000000
    75%          0.000000
    max          4.000000
    Name: lt_diff, dtype: float64
    nullcount: 71
    
    
    cluster_label3 count    87020.000000
    mean         0.050425
    std          0.313506
    min          0.000000
    25%          0.000000
    50%          0.000000
    75%          0.000000
    max          2.000000
    Name: cluster_label3, dtype: float64
    nullcount: 0
    
    

train.drop(['Loan_Amount_Submitrained_imp','Loan_Tenure_Submitrained_imp'],axis=1,inplace=True)
print"\n"

    noncat_var




    [('Monthly_Income', 5825),
     ('Loan_Amount_Applied', 278),
     ('Loan_Tenure_Applied', 12),
     ('Existing_EMI', 3754),
     ('Var5', 19),
     ('Loan_Amount_Submitted', 204),
     ('Loan_Tenure_Submitted', 7),
     ('Interest_Rate', 74),
     ('Processing_Fee', 572),
     ('EMI_Loan_Submitted', 4531),
     ('Var4', 8),
     ('LoggedIn', 2),
     ('Disbursed', 2),
     ('age_years', 11956),
     ('age_years_imp', 10375),
     ('Loan_Amount_Submitted_imp', 336),
     ('Interest_Rate_imp', 73),
     ('Loan_Tenure_Submitted_imp', 12),
     ('LAbyMI', 6347),
     ('LAbyTenure', 347),
     ('MIbyage', 68792),
     ('la_diff', 404),
     ('lt_diff', 11),
     ('cluster_label3', 3)]




    train.head(5)




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ID</th>
      <th>Gender</th>
      <th>City</th>
      <th>Monthly_Income</th>
      <th>DOB</th>
      <th>Lead_Creation_Date</th>
      <th>Loan_Amount_Applied</th>
      <th>Loan_Tenure_Applied</th>
      <th>Existing_EMI</th>
      <th>Employer_Name</th>
      <th>Salary_Account</th>
      <th>Mobile_Verified</th>
      <th>Var5</th>
      <th>Var1</th>
      <th>Loan_Amount_Submitted</th>
      <th>Loan_Tenure_Submitted</th>
      <th>Interest_Rate</th>
      <th>Processing_Fee</th>
      <th>EMI_Loan_Submitted</th>
      <th>Filled_Form</th>
      <th>Device_Type</th>
      <th>Var2</th>
      <th>Source</th>
      <th>Var4</th>
      <th>LoggedIn</th>
      <th>Disbursed</th>
      <th>age_years</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>ID000002C20</td>
      <td>Female</td>
      <td>Delhi</td>
      <td>20000</td>
      <td>23-May-78</td>
      <td>15-May-15</td>
      <td>300000</td>
      <td>5</td>
      <td>0</td>
      <td>CYBOSOL</td>
      <td>HDFC Bank</td>
      <td>N</td>
      <td>0</td>
      <td>HBXX</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>N</td>
      <td>Web-browser</td>
      <td>G</td>
      <td>S122</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>36.977413</td>
    </tr>
    <tr>
      <th>1</th>
      <td>ID000004E40</td>
      <td>Male</td>
      <td>Mumbai</td>
      <td>35000</td>
      <td>07-Oct-85</td>
      <td>04-May-15</td>
      <td>200000</td>
      <td>2</td>
      <td>0</td>
      <td>TATA CONSULTANCY SERVICES LTD (TCS)</td>
      <td>ICICI Bank</td>
      <td>Y</td>
      <td>13</td>
      <td>HBXA</td>
      <td>200000</td>
      <td>2</td>
      <td>13.25</td>
      <td>NaN</td>
      <td>6762.9</td>
      <td>N</td>
      <td>Web-browser</td>
      <td>G</td>
      <td>S122</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>29.571526</td>
    </tr>
    <tr>
      <th>2</th>
      <td>ID000007H20</td>
      <td>Male</td>
      <td>Panchkula</td>
      <td>22500</td>
      <td>10-Oct-81</td>
      <td>19-May-15</td>
      <td>600000</td>
      <td>4</td>
      <td>0</td>
      <td>ALCHEMIST HOSPITALS LTD</td>
      <td>State Bank of India</td>
      <td>Y</td>
      <td>0</td>
      <td>HBXX</td>
      <td>450000</td>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>N</td>
      <td>Web-browser</td>
      <td>B</td>
      <td>S143</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>33.604381</td>
    </tr>
    <tr>
      <th>3</th>
      <td>ID000008I30</td>
      <td>Male</td>
      <td>Saharsa</td>
      <td>35000</td>
      <td>30-Nov-87</td>
      <td>09-May-15</td>
      <td>1000000</td>
      <td>5</td>
      <td>0</td>
      <td>BIHAR GOVERNMENT</td>
      <td>State Bank of India</td>
      <td>Y</td>
      <td>10</td>
      <td>HBXX</td>
      <td>920000</td>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>N</td>
      <td>Web-browser</td>
      <td>B</td>
      <td>S143</td>
      <td>3</td>
      <td>0</td>
      <td>0</td>
      <td>27.438741</td>
    </tr>
    <tr>
      <th>4</th>
      <td>ID000009J40</td>
      <td>Male</td>
      <td>Bengaluru</td>
      <td>100000</td>
      <td>17-Feb-84</td>
      <td>20-May-15</td>
      <td>500000</td>
      <td>2</td>
      <td>25000</td>
      <td>GLOBAL EDGE SOFTWARE</td>
      <td>HDFC Bank</td>
      <td>Y</td>
      <td>17</td>
      <td>HBXX</td>
      <td>500000</td>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>N</td>
      <td>Web-browser</td>
      <td>B</td>
      <td>S134</td>
      <td>3</td>
      <td>1</td>
      <td>0</td>
      <td>31.252567</td>
    </tr>
  </tbody>
</table>
</div>




    pd.crosstab(index=train['LoggedIn'],columns=train['Disbursed'])




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Disbursed</th>
      <th>0</th>
      <th>1</th>
    </tr>
    <tr>
      <th>LoggedIn</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>84435</td>
      <td>31</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1312</td>
      <td>1242</td>
    </tr>
  </tbody>
</table>
</div>




    tt=train
tt['isla_sub']=tt['Loan_Amount_Submitted'].isnull()
tt['isla_tenure']=tt['Loan_Tenure_Submitted'].isnull()
tt['is_loan_emi']=tt['EMI_Loan_Submitted'].isnull()## for understanding th relationshipo between columns
ct1=pd.crosstab(index=tt['LoggedIn'],columns=[tt['isla_sub'],tt['Disbursed']])
ct2=pd.crosstab(index=tt['LoggedIn'],columns=[tt['isla_tenure'],tt['Disbursed']])
ct3=pd.crosstab(index=tt['LoggedIn'],columns=[tt['is_loan_emi'],tt['Disbursed']])

    ct1




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>isla_sub</th>
      <th colspan="2" halign="left">False</th>
      <th colspan="2" halign="left">True</th>
    </tr>
    <tr>
      <th>Disbursed</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
    </tr>
    <tr>
      <th>LoggedIn</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>50270</td>
      <td>28</td>
      <td>34165</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1093</td>
      <td>1016</td>
      <td>219</td>
      <td>226</td>
    </tr>
  </tbody>
</table>
</div>




    ct2




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>isla_tenure</th>
      <th colspan="2" halign="left">False</th>
      <th colspan="2" halign="left">True</th>
    </tr>
    <tr>
      <th>Disbursed</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
    </tr>
    <tr>
      <th>LoggedIn</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>50270</td>
      <td>28</td>
      <td>34165</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1093</td>
      <td>1016</td>
      <td>219</td>
      <td>226</td>
    </tr>
  </tbody>
</table>
</div>




    ct3




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>is_loan_emi</th>
      <th colspan="2" halign="left">False</th>
      <th colspan="2" halign="left">True</th>
    </tr>
    <tr>
      <th>Disbursed</th>
      <th>0</th>
      <th>1</th>
      <th>0</th>
      <th>1</th>
    </tr>
    <tr>
      <th>LoggedIn</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>26404</td>
      <td>6</td>
      <td>58031</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>731</td>
      <td>585</td>
      <td>581</td>
      <td>657</td>
    </tr>
  </tbody>
</table>
</div>




    len(noncat_var), len(cat_var) , train.shape




    (26, 13, (87020, 39))




    noncat_var




    [('Monthly_Income', 5825),
     ('Loan_Amount_Applied', 278),
     ('Loan_Tenure_Applied', 12),
     ('Existing_EMI', 3754),
     ('Var5', 19),
     ('Loan_Amount_Submitted', 204),
     ('Loan_Tenure_Submitted', 7),
     ('Interest_Rate', 74),
     ('Processing_Fee', 572),
     ('EMI_Loan_Submitted', 4531),
     ('Var4', 8),
     ('LoggedIn', 2),
     ('Disbursed', 2),
     ('age_years', 11956),
     ('la_diff', 622),
     ('LAbyMI', 6347),
     ('LAbyTenure', 347),
     ('MIbyage', 68792),
     ('age_years_imp', 10375),
     ('isla_sub', 2),
     ('isla_tenure', 2),
     ('is_loan_emi', 2),
     ('Interest_Rate_imp', 73),
     ('Loan_Amount_Submitted_imp', 12),
     ('Loan_Tenure_Submitted_imp', 12),
     ('lt_diff', 11),
     ('cluster_label3', 3),
     ('cluster_label4', 4)]




    excl_list=['Interest_Rate'
               ,'Loan_Amount_Submitted'
               ,'Loan_Tenure_Submitted'
               ,'LoggedIn'
               ,'age_years'
               ,'isla_sub'
               ,'isla_tenure'
               ,'is_loan_emi'
              ]


    noncat_varl=[x for (x,v) in noncat_var if x not in excl_list]


    len(noncat_varl), noncat_varl




    (19,
     ['Monthly_Income',
      'Loan_Amount_Applied',
      'Loan_Tenure_Applied',
      'Existing_EMI',
      'Var5',
      'Processing_Fee',
      'EMI_Loan_Submitted',
      'Var4',
      'Disbursed',
      'age_years_imp',
      'Loan_Amount_Submitted_imp',
      'Interest_Rate_imp',
      'Loan_Tenure_Submitted_imp',
      'LAbyMI',
      'LAbyTenure',
      'MIbyage',
      'la_diff',
      'lt_diff',
      'cluster_label3'])




    keep_var=noncat_varl+['ID']


    keep_var




    ['Monthly_Income',
     'Loan_Amount_Applied',
     'Loan_Tenure_Applied',
     'Existing_EMI',
     'Var5',
     'Processing_Fee',
     'EMI_Loan_Submitted',
     'Var4',
     'Disbursed',
     'age_years_imp',
     'Loan_Amount_Submitted_imp',
     'Interest_Rate_imp',
     'Loan_Tenure_Submitted_imp',
     'LAbyMI',
     'LAbyTenure',
     'MIbyage',
     'la_diff',
     'lt_diff',
     'cluster_label3',
     'ID']




    len(keep_var)




    20




    keep_var_test=[x for x in keep_var if x not in ['Disbursed']]


    len(keep_var_test),keep_var_test




    (19,
     ['Monthly_Income',
      'Loan_Amount_Applied',
      'Loan_Tenure_Applied',
      'Existing_EMI',
      'Var5',
      'Processing_Fee',
      'EMI_Loan_Submitted',
      'Var4',
      'age_years_imp',
      'Loan_Amount_Submitted_imp',
      'Interest_Rate_imp',
      'Loan_Tenure_Submitted_imp',
      'LAbyMI',
      'LAbyTenure',
      'MIbyage',
      'la_diff',
      'lt_diff',
      'cluster_label3',
      'ID'])




    cat_features.shape, cat_features.columns




    ((87020, 818),
     Index([u'Gender_Female', u'Gender_Male', u'City_ADIPUR', u'City_AHMEDB',
            u'City_AMALSAD', u'City_ANJAR', u'City_Abohar', u'City_Adilabad',
            u'City_Agartala', u'City_Agra', 
            ...
            u'Source_S153', u'Source_S154', u'Source_S155', u'Source_S156',
            u'Source_S157', u'Source_S158', u'Source_S159', u'Source_S160',
            u'Source_S161', u'Source_S162'],
           dtype='object', length=818))




    cat_features_train.shape




    (87020, 818)




    cat_features_test.shape




    (37717, 729)




    train.shape, train_clus.shape, test.shape, test_clus.shape




    ((87020, 36), (87020, 37), (37717, 34), (37717, 35))




    cat_train_cols=list(cat_features_train.columns)
    cat_test_cols=list(cat_features_test.columns)


    len(cat_train_cols), len(cat_test_cols),len(set(cat_train_cols)), len(set(cat_test_cols))




    (818, 729, 818, 729)




    cat_fet_cols=list(set(cat_train_cols).intersection(set(cat_test_cols)))
    len(cat_fet_cols), type(cat_fet_cols)




    (698, list)




    # concatenating the dfs 
    train_data_model=pd.concat([train_clus[keep_var],cat_features_train[cat_fet_cols]],axis=1)


    test_data_model=pd.concat([test_clus[keep_var_test],cat_features_test[cat_fet_cols]],axis=1)


    train_data_model.shape,cat_features_train.shape, len(keep_var)




    ((87020, 718), (87020, 818), 20)




    test_data_model.shape,cat_features_test.shape, len(keep_var_test)




    ((37717, 717), (37717, 729), 19)




    # model features and target
    model_features=[x for x in train_data_model.columns if x not in ['ID','Disbursed']]
    target=[x for x in train_data_model.columns if x in ['Disbursed']]


    len(model_features), type(model_features), target, type(target)




    (716, list, ['Disbursed'], list)




    #replacing inf and nan with zero in train
    train_data_model.replace([np.inf, -np.inf,np.nan], 0,inplace=True)
    print  "\n";

    
    



    #replacing inf and nan with zero in train
    test_data_model.replace([np.inf, -np.inf,np.nan], 0,inplace=True)
    print  "\n";

    
    



    noncat_var




    [('Monthly_Income', 5825),
     ('Loan_Amount_Applied', 278),
     ('Loan_Tenure_Applied', 12),
     ('Existing_EMI', 3754),
     ('Var5', 19),
     ('Loan_Amount_Submitted', 204),
     ('Loan_Tenure_Submitted', 7),
     ('Interest_Rate', 74),
     ('Processing_Fee', 572),
     ('EMI_Loan_Submitted', 4531),
     ('Var4', 8),
     ('LoggedIn', 2),
     ('Disbursed', 2),
     ('age_years', 11956)]




    noncat_var_scale=[x for (x,v) in noncat_var if x not in ['Disbursed','LoggedIn'] ]


    noncat_var_scale




    ['Monthly_Income',
     'Loan_Amount_Applied',
     'Loan_Tenure_Applied',
     'Existing_EMI',
     'Var5',
     'Loan_Amount_Submitted',
     'Loan_Tenure_Submitted',
     'Interest_Rate',
     'Processing_Fee',
     'EMI_Loan_Submitted',
     'Var4',
     'age_years']




    #### Scaling the non cat continuous
    from sklearn import preprocessing
    train_scaled=preprocessing.scale(train[noncat_var_scale])


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-544-1bbf21f561cb> in <module>()
          1 #### Scaling the non cat continuous
          2 from sklearn import preprocessing
    ----> 3 train_scaled=preprocessing.scale(train[noncat_var_scale])
    

    /usr/local/lib/python2.7/dist-packages/sklearn/preprocessing/data.pyc in scale(X, axis, with_mean, with_std, copy)
        115     :class:`sklearn.pipeline.Pipeline`)
        116     """
    --> 117     X = check_array(X, accept_sparse='csr', copy=copy, ensure_2d=False)
        118     warn_if_not_float(X, estimator='The scale function')
        119     if sparse.issparse(X):


    /usr/local/lib/python2.7/dist-packages/sklearn/utils/validation.pyc in check_array(array, accept_sparse, dtype, order, copy, force_all_finite, ensure_2d, allow_nd, ensure_min_samples, ensure_min_features)
        350                              array.ndim)
        351         if force_all_finite:
    --> 352             _assert_all_finite(array)
        353 
        354     shape_repr = _shape_repr(array.shape)


    /usr/local/lib/python2.7/dist-packages/sklearn/utils/validation.pyc in _assert_all_finite(X)
         50             and not np.isfinite(X).all()):
         51         raise ValueError("Input contains NaN, infinity"
    ---> 52                          " or a value too large for %r." % X.dtype)
         53 
         54 


    ValueError: Input contains NaN, infinity or a value too large for dtype('float64').



    train_scaled=preprocessing.scale(train3[X[i]])


    ## splitting in to train and val ( 80/20)
    from sklearn.cross_validation import train_test_split
    train_model, val_model = train_test_split(train_data_model, test_size=0.20, random_state=9876)


    train_model.shape, val_model.shape




    ((69616, 839), (17404, 839))




    ##modeling 
    ### importing libraries
    from sklearn import ensemble
    from sklearn.metrics import roc_curve, auc
    from sklearn import cross_validation


    ### putting it all together in a function for the Submission
    
    def rf_model(X,y,train_ds, val_ds,test_ds):
        
        ## initial random forest classifier with full train data
        clf = ensemble.RandomForestClassifier(n_estimators=500,random_state=9876,n_jobs=16)
        clf.fit(train_ds[X], train_ds[y])
        
        ## predicting class on train ,val and test
        train_pred_class=clf.predict(train_ds[X])
        val_pred_class=clf.predict(val_ds[X])
        test_pred_class=clf.predict(test_ds[X])
    
        ## predicting probabilities on train, val  and test
        train_pred_prob=clf.predict_proba(train_ds[X])
        val_pred_prob=clf.predict_proba(val_ds[X])
        test_pred_prob=clf.predict_proba(test_ds[X])
    
    
        ##taking the probabilities for predicted class=1 (2 nd column in the array)
        train_pred_prob=train_pred_prob[:,1]
        val_pred_prob=val_pred_prob[:,1]
        test_pred_prob=test_pred_prob[:,1]
        
        #cf table
        cf_mat_train=pd.crosstab(train_ds[y], train_pred_class, rownames=['actual'], colnames=['preds'])
        cf_mat_val=pd.crosstab(val_ds[y], val_pred_class, rownames=['actual'], colnames=['preds'])
        
        ## train metrics
        train_err=(cf_mat_train.iloc[0,1]+cf_mat_train.iloc[1,0])/(cf_mat_train.iloc[0,1]+cf_mat_train.iloc[1,0]+cf_mat_train.iloc[0,0]+cf_mat_train.iloc[1,1])  ## error rate
        train_acc=(cf_mat_train.iloc[0,0]+cf_mat_train.iloc[1,1])/(cf_mat_train.iloc[0,1]+cf_mat_train.iloc[1,0]+cf_mat_train.iloc[0,0]+cf_mat_train.iloc[1,1]) ## accuracy
        train_recall =cf_mat_train.iloc[1,1]/(cf_mat_train.iloc[1,1]+cf_mat_train.iloc[1,0]) ###recall  or hit rate or tpr or sensitivity
        train_spc=cf_mat_train.iloc[0,0]/(cf_mat_train.iloc[0,0]+cf_mat_train.iloc[0,1])  ##tnr or specificity
        train_prec=cf_mat_train.iloc[1,1]/(cf_mat_train.iloc[1,1]+cf_mat_train.iloc[0,1]) ### precision  or positive predicted value(ppv) 
        train_npv =cf_mat_train.iloc[0,0]/(cf_mat_train.iloc[0,0]+cf_mat_train.iloc[1,0]) ###negative predicted value
        train_fpr =cf_mat_train.iloc[0,1]/(cf_mat_train.iloc[0,0]+cf_mat_train.iloc[0,1]) ###false positive rate or fall out  
        train_fdr =cf_mat_train.iloc[0,1]/(cf_mat_train.iloc[0,1]+cf_mat_train.iloc[1,1]) ###false discovery rate
        train_fnr =cf_mat_train.iloc[1,0]/(cf_mat_train.iloc[1,0]+cf_mat_train.iloc[1,1]) ###false negative rate
        train_f1score=(2*train_recall*train_prec)/(train_recall+train_prec)
    
        ## val metrics
        
        val_err=(cf_mat_val.iloc[0,1]+cf_mat_val.iloc[1,0])/(cf_mat_val.iloc[0,1]+cf_mat_val.iloc[1,0]+cf_mat_val.iloc[0,0]+cf_mat_val.iloc[1,1])  ## error rate
        val_acc=(cf_mat_val.iloc[0,0]+cf_mat_val.iloc[1,1])/(cf_mat_val.iloc[0,1]+cf_mat_val.iloc[1,0]+cf_mat_val.iloc[0,0]+cf_mat_val.iloc[1,1]) ## accuracy
        val_recall =cf_mat_val.iloc[1,1]/(cf_mat_val.iloc[1,1]+cf_mat_val.iloc[1,0]) ###recall  or hit rate or tpr or sensitivity
        val_spc=cf_mat_val.iloc[0,0]/(cf_mat_val.iloc[0,0]+cf_mat_val.iloc[0,1])  ##tnr or specificity
        val_prec=cf_mat_val.iloc[1,1]/(cf_mat_val.iloc[1,1]+cf_mat_val.iloc[0,1]) ### precision  or positive predicted value(ppv) 
        val_npv =cf_mat_val.iloc[0,0]/(cf_mat_val.iloc[0,0]+cf_mat_val.iloc[1,0]) ###negative predicted value
        val_fpr =cf_mat_val.iloc[0,1]/(cf_mat_val.iloc[0,0]+cf_mat_val.iloc[0,1]) ###false positive rate or fall out  
        val_fdr =cf_mat_val.iloc[0,1]/(cf_mat_val.iloc[0,1]+cf_mat_val.iloc[1,1]) ###false discovery rate
        val_fnr =cf_mat_val.iloc[1,0]/(cf_mat_val.iloc[1,0]+cf_mat_val.iloc[1,1]) ###false negative rate
        val_f1score=(2*val_recall*val_prec)/(val_recall+val_prec)
        
        
        train_met_dict={
            "accuracy":train_acc*100
            ,"error":train_err*100
            ,"precision":train_prec*100
            ,"recall":train_recall*100
            ,"FDR":train_fdr*100
            ,"FNR":train_fnr*100
            ,"F1 SCORE":train_f1score*100
        }
    
        val_met_dict={
            "accuracy":val_acc*100
            ,"error":val_err*100
            ,"precision":val_prec*100
            ,"recall":val_recall*100
            ,"FDR":val_fdr*100
            ,"FNR":val_fnr*100
            ,"F1 SCORE":val_f1score*100
        }
        
    
        ## feature importance
        feat_index = np.argsort(clf.feature_importances_)[::-1] ## sorting the indices of feature importance in decending order
        fet_imp = clf.feature_importances_[feat_index] ##using the descending sorted index and arranging the feature importance array 
        
        fet_imp_names = [X[i] for i in feat_index] ## collecting the feature names from the index
        
        ##Putting the sorted feature importance and feature names in a dataframe
        d = {'v_imp_names': pd.Series(fet_imp_names),
             'v_imp_values': pd.Series(fet_imp)
            }
        v_imp_df = pd.DataFrame(d)
        
        #train AUC
        fpr_train, tpr_train, thresholds_train = roc_curve(train_ds[y], train_pred_prob)
        roc_auc_train = auc(fpr_train, tpr_train)
    
        #val AUC
        fpr_val, tpr_val, thresholds_val = roc_curve(val_ds[y], val_pred_prob)
        roc_auc_val = auc(fpr_val, tpr_val)
        
        
        ret_dict={"train_pred_class":train_pred_class
                  ,"test_pred_class":test_pred_class
                  ,"val_pred_class":val_pred_class
                  ,"train_pred_prob":train_pred_prob
                  ,"test_pred_prob":test_pred_prob
                  ,"val_pred_prob":val_pred_prob
                  ,"cf_mat_train":cf_mat_train
                  ,"cf_mat_val":cf_mat_val
                  ,"train_met_dict":train_met_dict
                  ,"val_met_dict":val_met_dict
                  ,"v_imp_df":v_imp_df
                  ,"train_auc":roc_auc_train
                  ,"train_fpr_auc":fpr_train
                  ,"train_tpr_auc":tpr_train
                  ,"train_thresholds_auc":thresholds_train
                  ,"val_auc":roc_auc_val
                  ,"val_fpr_auc":fpr_val
                  ,"val_tpr_auc":tpr_val
                  ,"val_thresholds_auc":thresholds_val
                 }
        return ret_dict


    X=model_features
    y='Disbursed'
    
    t0_rf1=time.time()
    
    rf1=rf_model(X,y,train_model,val_model,test_data_model)
    
    t1_rf1=time.time()
    
    delta_rf1=t1_rf1-t0_rf1
    
    print "running time in seconds : ", delta_rf1


    running time in seconds :  45.9121940136



    rf1['cf_mat_val']




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>preds</th>
      <th>0</th>
      <th>1</th>
    </tr>
    <tr>
      <th>actual</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>17128</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>271</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




    rf1['cf_mat_train']




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>preds</th>
      <th>0</th>
      <th>1</th>
    </tr>
    <tr>
      <th>actual</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>68614</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8</td>
      <td>994</td>
    </tr>
  </tbody>
</table>
</div>




    print rf1['val_met_dict']
    print "\n"
    print rf1['train_met_dict']

    {'FNR': 100.0, 'recall': 0.0, 'precision': 0.0, 'FDR': 100.0, 'F1 SCORE': nan, 'error': 1.5858423350953803, 'accuracy': 98.414157664904621}
    
    
    {'FNR': 0.79840319361277434, 'recall': 99.201596806387229, 'precision': 100.0, 'FDR': 0.0, 'F1 SCORE': 99.599198396793582, 'error': 0.011491611123879567, 'accuracy': 99.988508388876113}



    #submission rf1
    sub_rf1=pd.concat([test_data_model['ID'],pd.DataFrame(rf1['test_pred_prob'])],axis=1)
    sub_rf1.columns=['ID','Disbursed']
    sub_rf1.to_csv('av3_sub_rf1.csv',sep=',',index=None)


    ### putting it all together in a function for the Submission
    from sklearn import linear_model
    def log_model(X,y,train_ds, val_ds):
        
        ## initial random forest classifier with full train data
        clf = linear_model.LogisticRegression(random_state =9876,C=0.01,solver='newton-cg')
        clf.fit(train_ds[X], train_ds[y])
        
        ## predicting class on train ,val and test
        train_pred_class=clf.predict(train_ds[X])
        val_pred_class=clf.predict(val_ds[X])
        #test_pred_class=clf.predict(test_ds[X])
    
        ## predicting probabilities on train, val  and test
        train_pred_prob=clf.predict_proba(train_ds[X])
        val_pred_prob=clf.predict_proba(val_ds[X])
        #test_pred_prob=clf.predict_proba(test_ds[X])
    
    
        ##taking the probabilities for predicted class=1 (2 nd column in the array)
        train_pred_prob=train_pred_prob[:,1]
        val_pred_prob=val_pred_prob[:,1]
        #test_pred_prob=test_pred_prob[:,1]
        
        #cf table
        cf_mat_train=pd.crosstab(train_ds[y], train_pred_class, rownames=['actual'], colnames=['preds'])
        cf_mat_val=pd.crosstab(val_ds[y], val_pred_class, rownames=['actual'], colnames=['preds'])
        
        ## train metrics
        train_err=(cf_mat_train.iloc[0,1]+cf_mat_train.iloc[1,0])/(cf_mat_train.iloc[0,1]+cf_mat_train.iloc[1,0]+cf_mat_train.iloc[0,0]+cf_mat_train.iloc[1,1])  ## error rate
        train_acc=(cf_mat_train.iloc[0,0]+cf_mat_train.iloc[1,1])/(cf_mat_train.iloc[0,1]+cf_mat_train.iloc[1,0]+cf_mat_train.iloc[0,0]+cf_mat_train.iloc[1,1]) ## accuracy
        train_recall =cf_mat_train.iloc[1,1]/(cf_mat_train.iloc[1,1]+cf_mat_train.iloc[1,0]) ###recall  or hit rate or tpr or sensitivity
        train_spc=cf_mat_train.iloc[0,0]/(cf_mat_train.iloc[0,0]+cf_mat_train.iloc[0,1])  ##tnr or specificity
        train_prec=cf_mat_train.iloc[1,1]/(cf_mat_train.iloc[1,1]+cf_mat_train.iloc[0,1]) ### precision  or positive predicted value(ppv) 
        train_npv =cf_mat_train.iloc[0,0]/(cf_mat_train.iloc[0,0]+cf_mat_train.iloc[1,0]) ###negative predicted value
        train_fpr =cf_mat_train.iloc[0,1]/(cf_mat_train.iloc[0,0]+cf_mat_train.iloc[0,1]) ###false positive rate or fall out  
        train_fdr =cf_mat_train.iloc[0,1]/(cf_mat_train.iloc[0,1]+cf_mat_train.iloc[1,1]) ###false discovery rate
        train_fnr =cf_mat_train.iloc[1,0]/(cf_mat_train.iloc[1,0]+cf_mat_train.iloc[1,1]) ###false negative rate
        train_f1score=(2*train_recall*train_prec)/(train_recall+train_prec)
    
        ## val metrics
        
        val_err=(cf_mat_val.iloc[0,1]+cf_mat_val.iloc[1,0])/(cf_mat_val.iloc[0,1]+cf_mat_val.iloc[1,0]+cf_mat_val.iloc[0,0]+cf_mat_val.iloc[1,1])  ## error rate
        val_acc=(cf_mat_val.iloc[0,0]+cf_mat_val.iloc[1,1])/(cf_mat_val.iloc[0,1]+cf_mat_val.iloc[1,0]+cf_mat_val.iloc[0,0]+cf_mat_val.iloc[1,1]) ## accuracy
        val_recall =cf_mat_val.iloc[1,1]/(cf_mat_val.iloc[1,1]+cf_mat_val.iloc[1,0]) ###recall  or hit rate or tpr or sensitivity
        val_spc=cf_mat_val.iloc[0,0]/(cf_mat_val.iloc[0,0]+cf_mat_val.iloc[0,1])  ##tnr or specificity
        val_prec=cf_mat_val.iloc[1,1]/(cf_mat_val.iloc[1,1]+cf_mat_val.iloc[0,1]) ### precision  or positive predicted value(ppv) 
        val_npv =cf_mat_val.iloc[0,0]/(cf_mat_val.iloc[0,0]+cf_mat_val.iloc[1,0]) ###negative predicted value
        val_fpr =cf_mat_val.iloc[0,1]/(cf_mat_val.iloc[0,0]+cf_mat_val.iloc[0,1]) ###false positive rate or fall out  
        val_fdr =cf_mat_val.iloc[0,1]/(cf_mat_val.iloc[0,1]+cf_mat_val.iloc[1,1]) ###false discovery rate
        val_fnr =cf_mat_val.iloc[1,0]/(cf_mat_val.iloc[1,0]+cf_mat_val.iloc[1,1]) ###false negative rate
        val_f1score=(2*val_recall*val_prec)/(val_recall+val_prec)
        
        
        train_met_dict={
            "accuracy":train_acc*100
            ,"error":train_err*100
            ,"precision":train_prec*100
            ,"recall":train_recall*100
            ,"FDR":train_fdr*100
            ,"FNR":train_fnr*100
            ,"F1 SCORE":train_f1score*100
        }
    
        val_met_dict={
            "accuracy":val_acc*100
            ,"error":val_err*100
            ,"precision":val_prec*100
            ,"recall":val_recall*100
            ,"FDR":val_fdr*100
            ,"FNR":val_fnr*100
            ,"F1 SCORE":val_f1score*100
        }
        
    
    '''    ## feature importance
        feat_index = np.argsort(clf.feature_importances_)[::-1] ## sorting the indices of feature importance in decending order
        fet_imp = clf.feature_importances_[feat_index] ##using the descending sorted index and arranging the feature importance array 
        
        fet_imp_names = [X[i] for i in feat_index] ## collecting the feature names from the index
        
        ##Putting the sorted feature importance and feature names in a dataframe
        d = {'v_imp_names': pd.Series(fet_imp_names),
             'v_imp_values': pd.Series(fet_imp)
            }
        v_imp_df = pd.DataFrame(d)
    '''    
        #train AUC
        fpr_train, tpr_train, thresholds_train = roc_curve(train_ds[y], train_pred_prob)
        roc_auc_train = auc(fpr_train, tpr_train)
    
        #val AUC
        fpr_val, tpr_val, thresholds_val = roc_curve(val_ds[y], val_pred_prob)
        roc_auc_val = auc(fpr_val, tpr_val)
        
        
        ret_dict={"train_pred_class":train_pred_class
                  #,"test_pred_class":test_pred_class
                  ,"val_pred_class":val_pred_class
                  ,"train_pred_prob":train_pred_prob
                  #,"test_pred_prob":test_pred_prob
                  ,"val_pred_prob":val_pred_prob
                  ,"cf_mat_train":cf_mat_train
                  ,"cf_mat_val":cf_mat_val
                  ,"train_met_dict":train_met_dict
                  ,"val_met_dict":val_met_dict
                 # ,"v_imp_df":v_imp_df
                  ,"train_auc":roc_auc_train
                  ,"train_fpr_auc":fpr_train
                  ,"train_tpr_auc":tpr_train
                  ,"train_thresholds_auc":thresholds_train
                  ,"val_auc":roc_auc_val
                  ,"val_fpr_auc":fpr_val
                  ,"val_tpr_auc":tpr_val
                  ,"val_thresholds_auc":thresholds_val
                 }
        return ret_dict


      File "<ipython-input-708-2a43492278ce>", line 89
        fpr_train, tpr_train, thresholds_train = roc_curve(train_ds[y], train_pred_prob)
        ^
    IndentationError: unexpected indent


X=model_features
y='Disbursed'
logmodel1=log_model(X,y,train_model,val_model)

    logmodel1['cf_mat_val']


    logmodel1['cf_mat_train']


    rf1.keys()




    ['train_pred_class',
     'cf_mat_val',
     'val_thresholds_auc',
     'train_pred_prob',
     'train_tpr_auc',
     'train_thresholds_auc',
     'v_imp_df',
     'val_pred_class',
     'train_auc',
     'train_fpr_auc',
     'val_met_dict',
     'val_auc',
     'cf_mat_train',
     'val_pred_prob',
     'val_tpr_auc',
     'train_met_dict',
     'val_fpr_auc']




    rf1['cf_mat_val']




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>preds</th>
      <th>0</th>
      <th>1</th>
    </tr>
    <tr>
      <th>actual</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>17128</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>271</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




    rf1['cf_mat_train']




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>preds</th>
      <th>0</th>
      <th>1</th>
    </tr>
    <tr>
      <th>actual</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>68614</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8</td>
      <td>994</td>
    </tr>
  </tbody>
</table>
</div>




    ## creating a second features from only the important variables from First features which has impportane >.1%
    fet2=list(rf1['v_imp_df']['v_imp_names'][rf1['v_imp_df']['v_imp_values']>=0.001])


    fet2 , len(fet2)




    (['MIbyage',
      'age_years_imp',
      'Monthly_Income',
      'LAbyMI',
      'Var5',
      'Existing_EMI',
      'la_diff',
      'LAbyTenure',
      'EMI_Loan_Submitted',
      'Loan_Amount_Applied',
      'Processing_Fee',
      'Interest_Rate_imp',
      'Loan_Tenure_Submitted_imp',
      'Loan_Amount_Submitted_imp',
      'Loan_Tenure_Applied',
      'Var4',
      'Salary_Account_HDFC Bank',
      'Salary_Account_ICICI Bank',
      'Source_S133',
      'City_Delhi',
      'Source_S122',
      'City_Mumbai',
      'City_Bengaluru',
      'Salary_Account_Axis Bank',
      'City_Pune',
      'Var2_G',
      'Var2_B',
      'lt_diff',
      'Salary_Account_State Bank of India',
      'City_Hyderabad',
      'Source_S143',
      'City_Chennai',
      'Gender_Male',
      'Gender_Female',
      'Salary_Account_Citibank',
      'Source_S134',
      'City_Kolkata',
      'Filled_Form_N',
      'Filled_Form_Y',
      'Salary_Account_Kotak Bank',
      'Var1_HAXB',
      'City_Gurgaon',
      'Source_S159',
      'Var1_HBXA',
      'Var1_HBXC',
      'Var1_HAXC',
      'Var1_HAXA',
      'City_Jaipur',
      'Var1_HBXD',
      'City_Ahmedabad',
      'Salary_Account_Standard Chartered Bank',
      'City_Indore',
      'City_Chandigarh',
      'Var2_C',
      'Mobile_Verified_N',
      'cluster_label4',
      'Var1_HBXX',
      'Mobile_Verified_Y',
      'cluster_label3',
      'City_Bhubaneswar',
      'Salary_Account_HSBC',
      'Var2_E',
      'Salary_Account_Punjab National Bank',
      'City_Nagpur',
      'Salary_Account_IDBI Bank',
      'City_Coimbatore',
      'Source_S127',
      'City_Thane',
      'Salary_Account_Indian Bank',
      'Device_Type_Web-browser',
      'City_Ghaziabad',
      'Device_Type_Mobile',
      'City_Lucknow',
      'City_Vadodara',
      'Salary_Account_Bank of Baroda',
      'Var1_HCXF',
      'Salary_Account_Deutsche Bank',
      'City_Visakhapatnam',
      'Salary_Account_Central Bank of India',
      'Salary_Account_Corporation bank',
      'Salary_Account_ING Vysya',
      'City_Nashik',
      'City_Faridabad',
      'Salary_Account_Union Bank of India',
      'City_Surat',
      'Source_S137'],
     86)




    X=fet2
    y='Disbursed'
    rf2=rf_model(X,y,train_model,val_model)


    rf2.keys()




    ['train_pred_class',
     'cf_mat_val',
     'val_thresholds_auc',
     'train_pred_prob',
     'train_tpr_auc',
     'train_thresholds_auc',
     'v_imp_df',
     'val_pred_class',
     'train_auc',
     'train_fpr_auc',
     'val_met_dict',
     'val_auc',
     'cf_mat_train',
     'val_pred_prob',
     'val_tpr_auc',
     'train_met_dict',
     'val_fpr_auc']




    rf2['cf_mat_train']




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>preds</th>
      <th>0</th>
      <th>1</th>
    </tr>
    <tr>
      <th>actual</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>68614</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8</td>
      <td>994</td>
    </tr>
  </tbody>
</table>
</div>




    rf2['cf_mat_val']




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>preds</th>
      <th>0</th>
      <th>1</th>
    </tr>
    <tr>
      <th>actual</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>17128</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>271</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




    fet3=list(rf2['v_imp_df']['v_imp_names'][rf2['v_imp_df']['v_imp_values']>=0.005])


    len(fet3)




    37




    X=fet3
    y='Disbursed'
    rf3=rf_model(X,y,train_model,val_model)


    rf3['cf_mat_train']




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>preds</th>
      <th>0</th>
      <th>1</th>
    </tr>
    <tr>
      <th>actual</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>68614</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8</td>
      <td>994</td>
    </tr>
  </tbody>
</table>
</div>




    rf3['cf_mat_val']




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>preds</th>
      <th>0</th>
      <th>1</th>
    </tr>
    <tr>
      <th>actual</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>17130</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>271</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>


s1=set(list(train_model[X].columns))
s2=set(list(train_model.columns))
l1=train_model[X].columns
l2=train_model.columns
print len(s1), len(s2), len(l1), len(l2)
from collections import Counter
Counter(l1)

    # Adaboost
    from sklearn.ensemble import AdaBoostClassifier
    
    ### putting it all together in a function for the Submission
    
    def ab_model(X,y,train_ds, val_ds,test_ds):
        
        ## adaboost
        clf = AdaBoostClassifier(n_estimators=500)
        clf.fit(train_ds[X], train_ds[y])
        
        ## predicting class on train ,val and test
        train_pred_class=clf.predict(train_ds[X])
        val_pred_class=clf.predict(val_ds[X])
        #test_pred_class=clf.predict(test_ds[X])
    
        ## predicting probabilities on train, val  and test
        train_pred_prob=clf.predict_proba(train_ds[X])
        val_pred_prob=clf.predict_proba(val_ds[X])
        #test_pred_prob=clf.predict_proba(test_ds[X])
    
    
        ##taking the probabilities for predicted class=1 (2 nd column in the array)
        train_pred_prob=train_pred_prob[:,1]
        val_pred_prob=val_pred_prob[:,1]
        #test_pred_prob=test_pred_prob[:,1]
        
        #cf table
        cf_mat_train=pd.crosstab(train_ds[y], train_pred_class, rownames=['actual'], colnames=['preds'])
        cf_mat_val=pd.crosstab(val_ds[y], val_pred_class, rownames=['actual'], colnames=['preds'])
        
        ## train metrics
        train_err=(cf_mat_train.iloc[0,1]+cf_mat_train.iloc[1,0])/(cf_mat_train.iloc[0,1]+cf_mat_train.iloc[1,0]+cf_mat_train.iloc[0,0]+cf_mat_train.iloc[1,1])  ## error rate
        train_acc=(cf_mat_train.iloc[0,0]+cf_mat_train.iloc[1,1])/(cf_mat_train.iloc[0,1]+cf_mat_train.iloc[1,0]+cf_mat_train.iloc[0,0]+cf_mat_train.iloc[1,1]) ## accuracy
        train_recall =cf_mat_train.iloc[1,1]/(cf_mat_train.iloc[1,1]+cf_mat_train.iloc[1,0]) ###recall  or hit rate or tpr or sensitivity
        train_spc=cf_mat_train.iloc[0,0]/(cf_mat_train.iloc[0,0]+cf_mat_train.iloc[0,1])  ##tnr or specificity
        train_prec=cf_mat_train.iloc[1,1]/(cf_mat_train.iloc[1,1]+cf_mat_train.iloc[0,1]) ### precision  or positive predicted value(ppv) 
        train_npv =cf_mat_train.iloc[0,0]/(cf_mat_train.iloc[0,0]+cf_mat_train.iloc[1,0]) ###negative predicted value
        train_fpr =cf_mat_train.iloc[0,1]/(cf_mat_train.iloc[0,0]+cf_mat_train.iloc[0,1]) ###false positive rate or fall out  
        train_fdr =cf_mat_train.iloc[0,1]/(cf_mat_train.iloc[0,1]+cf_mat_train.iloc[1,1]) ###false discovery rate
        train_fnr =cf_mat_train.iloc[1,0]/(cf_mat_train.iloc[1,0]+cf_mat_train.iloc[1,1]) ###false negative rate
        train_f1score=(2*train_recall*train_prec)/(train_recall+train_prec)
    
        ## val metrics
        
        val_err=(cf_mat_val.iloc[0,1]+cf_mat_val.iloc[1,0])/(cf_mat_val.iloc[0,1]+cf_mat_val.iloc[1,0]+cf_mat_val.iloc[0,0]+cf_mat_val.iloc[1,1])  ## error rate
        val_acc=(cf_mat_val.iloc[0,0]+cf_mat_val.iloc[1,1])/(cf_mat_val.iloc[0,1]+cf_mat_val.iloc[1,0]+cf_mat_val.iloc[0,0]+cf_mat_val.iloc[1,1]) ## accuracy
        val_recall =cf_mat_val.iloc[1,1]/(cf_mat_val.iloc[1,1]+cf_mat_val.iloc[1,0]) ###recall  or hit rate or tpr or sensitivity
        val_spc=cf_mat_val.iloc[0,0]/(cf_mat_val.iloc[0,0]+cf_mat_val.iloc[0,1])  ##tnr or specificity
        val_prec=cf_mat_val.iloc[1,1]/(cf_mat_val.iloc[1,1]+cf_mat_val.iloc[0,1]) ### precision  or positive predicted value(ppv) 
        val_npv =cf_mat_val.iloc[0,0]/(cf_mat_val.iloc[0,0]+cf_mat_val.iloc[1,0]) ###negative predicted value
        val_fpr =cf_mat_val.iloc[0,1]/(cf_mat_val.iloc[0,0]+cf_mat_val.iloc[0,1]) ###false positive rate or fall out  
        val_fdr =cf_mat_val.iloc[0,1]/(cf_mat_val.iloc[0,1]+cf_mat_val.iloc[1,1]) ###false discovery rate
        val_fnr =cf_mat_val.iloc[1,0]/(cf_mat_val.iloc[1,0]+cf_mat_val.iloc[1,1]) ###false negative rate
        val_f1score=(2*val_recall*val_prec)/(val_recall+val_prec)
        
        
        train_met_dict={
            "accuracy":train_acc*100
            ,"error":train_err*100
            ,"precision":train_prec*100
            ,"recall":train_recall*100
            ,"FDR":train_fdr*100
            ,"FNR":train_fnr*100
            ,"F1 SCORE":train_f1score*100
        }
    
        val_met_dict={
            "accuracy":val_acc*100
            ,"error":val_err*100
            ,"precision":val_prec*100
            ,"recall":val_recall*100
            ,"FDR":val_fdr*100
            ,"FNR":val_fnr*100
            ,"F1 SCORE":val_f1score*100
        }
        
    
        ## feature importance
        feat_index = np.argsort(clf.feature_importances_)[::-1] ## sorting the indices of feature importance in decending order
        fet_imp = clf.feature_importances_[feat_index] ##using the descending sorted index and arranging the feature importance array 
        
        fet_imp_names = [X[i] for i in feat_index] ## collecting the feature names from the index
        
        ##Putting the sorted feature importance and feature names in a dataframe
        d = {'v_imp_names': pd.Series(fet_imp_names),
             'v_imp_values': pd.Series(fet_imp)
            }
        v_imp_df = pd.DataFrame(d)
        
        #train AUC
        fpr_train, tpr_train, thresholds_train = roc_curve(train_ds[y], train_pred_prob)
        roc_auc_train = auc(fpr_train, tpr_train)
    
        #val AUC
        fpr_val, tpr_val, thresholds_val = roc_curve(val_ds[y], val_pred_prob)
        roc_auc_val = auc(fpr_val, tpr_val)
        
        
        ret_dict={"train_pred_class":train_pred_class
                  ,"test_pred_class":test_pred_class
                  ,"val_pred_class":val_pred_class
                  ,"train_pred_prob":train_pred_prob
                  ,"test_pred_prob":test_pred_prob
                  ,"val_pred_prob":val_pred_prob
                  ,"cf_mat_train":cf_mat_train
                  ,"cf_mat_val":cf_mat_val
                  ,"train_met_dict":train_met_dict
                  ,"val_met_dict":val_met_dict
                  ,"v_imp_df":v_imp_df
                  ,"train_auc":roc_auc_train
                  ,"train_fpr_auc":fpr_train
                  ,"train_tpr_auc":tpr_train
                  ,"train_thresholds_auc":thresholds_train
                  ,"val_auc":roc_auc_val
                  ,"val_fpr_auc":fpr_val
                  ,"val_tpr_auc":tpr_val
                  ,"val_thresholds_auc":thresholds_val
                 }
        return ret_dict


    X=model_features
    y='Disbursed'
    
    t0_ab1=time.time()
    
    ab1=ab_model(X,y,train_model,val_model,test_data_model)
    
    t1_ab1=time.time()
    
    delta_ab1=t1_ab1-t0_ab1
    
    print "running time in seconds : ", delta_ab1

    running time in seconds :  250.644831896



    print ab1['cf_mat_val']
    print ab1['cf_mat_train']
    
    print ab1['val_met_dict']
    print "\n"
    print rf1['train_met_dict']
    #submission ab1
    sub_ab1=pd.concat([test_data_model['ID'],pd.DataFrame(ab1['test_pred_prob'])],axis=1)
    sub_ab1.columns=['ID','Disbursed']
    sub_ab1.to_csv('av3_sub_ab1.csv',sep=',',index=None)


    preds       0  1
    actual          
    0       17132  1
    1         271  0
    preds       0  1
    actual          
    0       68608  6
    1         999  3
    {'FNR': 100.0, 'recall': 0.0, 'precision': 0.0, 'FDR': 100.0, 'F1 SCORE': nan, 'error': 1.5628591128476212, 'accuracy': 98.437140887152381}
    
    
    {'FNR': 0.79840319361277434, 'recall': 99.201596806387229, 'precision': 100.0, 'FDR': 0.0, 'F1 SCORE': 99.599198396793582, 'error': 0.011491611123879567, 'accuracy': 99.988508388876113}



     ## adaboost
    clf = AdaBoostClassifier(n_estimators=100)
    clf.fit(train_ds[X], train_ds[y])
        
    ## predicting class on train ,val and test
    train_pred_class=clf.predict(train_ds[X])
    val_pred_class=clf.predict(val_ds[X])
    #test_pred_class=clf.predict(test_ds[X])
    
    ## predicting probabilities on train, val  and test
    train_pred_prob=clf.predict_proba(train_ds[X])
    val_pred_prob=clf.predict_proba(val_ds[X])
    #test_pred_prob=clf.predict_proba(test_ds[X])
    
    
    ##taking the probabilities for predicted class=1 (2 nd column in the array)
    train_pred_prob=train_pred_prob[:,1]
    val_pred_prob=val_pred_prob[:,1]
    #test_pred_prob=test_pred_prob[:,1]
     


    #cf table
    cf_mat_train=pd.crosstab(train_ds[y], train_pred_class, rownames=['actual'], colnames=['preds'])
    cf_mat_val=pd.crosstab(val_ds[y], val_pred_class, rownames=['actual'], colnames=['preds'])


    cf_mat_train




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>preds</th>
      <th>0</th>
      <th>1</th>
    </tr>
    <tr>
      <th>actual</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>68612</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1001</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




    cf_mat_val




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>preds</th>
      <th>0</th>
    </tr>
    <tr>
      <th>actual</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>17133</td>
    </tr>
    <tr>
      <th>1</th>
      <td>271</td>
    </tr>
  </tbody>
</table>
</div>




    X=model_features
    y='Disbursed'
    adaboost1=adaboost_model(X,y,train_model,val_model)


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-427-1daf6033e6dc> in <module>()
          1 X=model_features
          2 y='Disbursed'
    ----> 3 adaboost1=adaboost_model(X,y,train_model,val_model)
    

    <ipython-input-426-cf94b2a9d835> in adaboost_model(X, y, train_ds, val_ds)
         44     ## val metrics
         45 
    ---> 46     val_err=(cf_mat_val.iloc[0,1]+cf_mat_val.iloc[1,0])/(cf_mat_val.iloc[0,1]+cf_mat_val.iloc[1,0]+cf_mat_val.iloc[0,0]+cf_mat_val.iloc[1,1])  ## error rate
         47     val_acc=(cf_mat_val.iloc[0,0]+cf_mat_val.iloc[1,1])/(cf_mat_val.iloc[0,1]+cf_mat_val.iloc[1,0]+cf_mat_val.iloc[0,0]+cf_mat_val.iloc[1,1]) ## accuracy
         48     val_recall =cf_mat_val.iloc[1,1]/(cf_mat_val.iloc[1,1]+cf_mat_val.iloc[1,0]) ###recall  or hit rate or tpr or sensitivity


    /usr/local/lib/python2.7/dist-packages/pandas-0.16.1-py2.7-linux-x86_64.egg/pandas/core/indexing.pyc in __getitem__(self, key)
       1176     def __getitem__(self, key):
       1177         if type(key) is tuple:
    -> 1178             return self._getitem_tuple(key)
       1179         else:
       1180             return self._getitem_axis(key, axis=0)


    /usr/local/lib/python2.7/dist-packages/pandas-0.16.1-py2.7-linux-x86_64.egg/pandas/core/indexing.pyc in _getitem_tuple(self, tup)
       1415                 continue
       1416 
    -> 1417             retval = getattr(retval, self.name)._getitem_axis(key, axis=axis)
       1418 
       1419             # if the dim was reduced, then pass a lower-dim the next time


    /usr/local/lib/python2.7/dist-packages/pandas-0.16.1-py2.7-linux-x86_64.egg/pandas/core/indexing.pyc in _getitem_axis(self, key, axis)
       1469                 self._is_valid_integer(key, axis)
       1470 
    -> 1471             return self._get_loc(key, axis=axis)
       1472 
       1473     def _convert_to_indexer(self, obj, axis=0, is_setter=False):


    /usr/local/lib/python2.7/dist-packages/pandas-0.16.1-py2.7-linux-x86_64.egg/pandas/core/indexing.pyc in _get_loc(self, key, axis)
         90 
         91     def _get_loc(self, key, axis=0):
    ---> 92         return self.obj._ixs(key, axis=axis)
         93 
         94     def _slice(self, obj, axis=0, kind=None):


    /usr/local/lib/python2.7/dist-packages/pandas-0.16.1-py2.7-linux-x86_64.egg/pandas/core/series.pyc in _ixs(self, i, axis)
        491             values = self.values
        492             if isinstance(values, np.ndarray):
    --> 493                 return _index.get_value_at(values, i)
        494             else:
        495                 return values[i]


    pandas/index.pyx in pandas.index.get_value_at (pandas/index.c:2358)()


    pandas/src/util.pxd in util.get_value_at (pandas/index.c:15287)()


    IndexError: index out of bounds



    X=fet2
    y='Disbursed'
    adaboost2=adaboost_model(X,y,train_model,val_model)


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-433-cfe060c5989d> in <module>()
          1 X=fet2
          2 y='Disbursed'
    ----> 3 adaboost2=adaboost_model(X,y,train_model,val_model)
    

    <ipython-input-426-cf94b2a9d835> in adaboost_model(X, y, train_ds, val_ds)
         31 
         32     ## train metrics
    ---> 33     train_err=(cf_mat_train.iloc[0,1]+cf_mat_train.iloc[1,0])/(cf_mat_train.iloc[0,1]+cf_mat_train.iloc[1,0]+cf_mat_train.iloc[0,0]+cf_mat_train.iloc[1,1])  ## error rate
         34     train_acc=(cf_mat_train.iloc[0,0]+cf_mat_train.iloc[1,1])/(cf_mat_train.iloc[0,1]+cf_mat_train.iloc[1,0]+cf_mat_train.iloc[0,0]+cf_mat_train.iloc[1,1]) ## accuracy
         35     train_recall =cf_mat_train.iloc[1,1]/(cf_mat_train.iloc[1,1]+cf_mat_train.iloc[1,0]) ###recall  or hit rate or tpr or sensitivity


    /usr/local/lib/python2.7/dist-packages/pandas-0.16.1-py2.7-linux-x86_64.egg/pandas/core/indexing.pyc in __getitem__(self, key)
       1176     def __getitem__(self, key):
       1177         if type(key) is tuple:
    -> 1178             return self._getitem_tuple(key)
       1179         else:
       1180             return self._getitem_axis(key, axis=0)


    /usr/local/lib/python2.7/dist-packages/pandas-0.16.1-py2.7-linux-x86_64.egg/pandas/core/indexing.pyc in _getitem_tuple(self, tup)
       1415                 continue
       1416 
    -> 1417             retval = getattr(retval, self.name)._getitem_axis(key, axis=axis)
       1418 
       1419             # if the dim was reduced, then pass a lower-dim the next time


    /usr/local/lib/python2.7/dist-packages/pandas-0.16.1-py2.7-linux-x86_64.egg/pandas/core/indexing.pyc in _getitem_axis(self, key, axis)
       1469                 self._is_valid_integer(key, axis)
       1470 
    -> 1471             return self._get_loc(key, axis=axis)
       1472 
       1473     def _convert_to_indexer(self, obj, axis=0, is_setter=False):


    /usr/local/lib/python2.7/dist-packages/pandas-0.16.1-py2.7-linux-x86_64.egg/pandas/core/indexing.pyc in _get_loc(self, key, axis)
         90 
         91     def _get_loc(self, key, axis=0):
    ---> 92         return self.obj._ixs(key, axis=axis)
         93 
         94     def _slice(self, obj, axis=0, kind=None):


    /usr/local/lib/python2.7/dist-packages/pandas-0.16.1-py2.7-linux-x86_64.egg/pandas/core/series.pyc in _ixs(self, i, axis)
        491             values = self.values
        492             if isinstance(values, np.ndarray):
    --> 493                 return _index.get_value_at(values, i)
        494             else:
        495                 return values[i]


    pandas/index.pyx in pandas.index.get_value_at (pandas/index.c:2358)()


    pandas/src/util.pxd in util.get_value_at (pandas/index.c:15287)()


    IndexError: index out of bounds



    adaboost1['cf_mat_train']


    train_model.shape




    (69616, 833)




    train_ds.shape




    (69616, 833)




    ## initial random forest classifier with full train data
    clf = ensemble.RandomForestClassifier(n_estimators=100,random_state=9876,n_jobs=16)
    clf.fit(train_ds[X], train_ds[y])
        
    ## predicting class on train and test
    train_pred_class=clf.predict(train_ds[X])
    test_pred_class=clf.predict(test_ds[X])
    
    ## predicting probabilities on train and test
    train_pred_prob=clf.predict_proba(train_ds[X])
    test_pred_prob=clf.predict_proba(test_ds[X])
    
    ##taking the probabilities for predicted class=1 (2 nd column in the array)
    train_pred_prob=train_pred_prob[:,1]
    test_pred_prob=test_pred_prob[:,1]
        
    ## creating the confusion matrix for train
    cf_mat_train=pd.crosstab(train_ds[y], train_pred_class, rownames=['actual'], colnames=['preds'])


    cf_mat_train




<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>preds</th>
      <th>0</th>
      <th>1</th>
    </tr>
    <tr>
      <th>actual</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>68614</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>1002</td>
    </tr>
  </tbody>
</table>
</div>




    ## train metrics
    rf_train_err=(cf_mat_train.iloc[0,1]+cf_mat_train.iloc[1,0])/(cf_mat_train.iloc[0,1]+cf_mat_train.iloc[1,0]+cf_mat_train.iloc[0,0]+cf_mat_train.iloc[1,1])  ## error rate
    rf_train_acc=(cf_mat_train.iloc[0,0]+cf_mat_train.iloc[1,1])/(cf_mat_train.iloc[0,1]+cf_mat_train.iloc[1,0]+cf_mat_train.iloc[0,0]+cf_mat_train.iloc[1,1]) ## accuracy
    rf_train_recall =cf_mat_train.iloc[1,1]/(cf_mat_train.iloc[1,1]+cf_mat_train.iloc[1,0]) ###recall  or hit rate or tpr or sensitivity
    rf_train_spc=cf_mat_train.iloc[0,0]/(cf_mat_train.iloc[0,0]+cf_mat_train.iloc[0,1])  ##tnr or specificity
    rf_train_prec=cf_mat_train.iloc[1,1]/(cf_mat_train.iloc[1,1]+cf_mat_train.iloc[0,1]) ### precision  or positive predicted value(ppv) 
    rf_train_npv =cf_mat_train.iloc[0,0]/(cf_mat_train.iloc[0,0]+cf_mat_train.iloc[1,0]) ###negative predicted value
    rf_train_fpr =cf_mat_train.iloc[0,1]/(cf_mat_train.iloc[0,0]+cf_mat_train.iloc[0,1]) ###false positive rate or fall out  
    rf_train_fdr =cf_mat_train.iloc[0,1]/(cf_mat_train.iloc[0,1]+cf_mat_train.iloc[1,1]) ###false discovery rate
    rf_train_fnr =cf_mat_train.iloc[1,0]/(cf_mat_train.iloc[1,0]+cf_mat_train.iloc[1,1]) ###false negative rate
    
    train_met_dict={
        "accuracy":rf_train_acc*100
        ,"error":rf_train_err*100
        ,"precision":rf_train_prec*100
        ,"recall":rf_train_recall*100
        ,"FDR":rf_train_fdr*100
        ,"FNR":rf_train_fnr*100
    }


    train_met_dict




    {'FDR': 0.0,
     'FNR': 0.0,
     'accuracy': 100.0,
     'error': 0.0,
     'precision': 100.0,
     'recall': 100.0}




    ## feature importance
    feat_index = np.argsort(clf.feature_importances_)[::-1] ## sorting the indices of feature importance in decending order
    fet_imp = clf.feature_importances_[feat_index] ##using the descending sorted index and arranging the feature importance array 
        
    fet_imp_names = [X[i] for i in feat_index] ## collecting the feature names from the index


    len(X)




    831




    len(clf.feature_importances_)




    835




    len(X), type(X)




    (831, list)




    type(feat_index)




    numpy.ndarray




    len(feat_index)




    835




    ##Putting the sorted feature importance and feature names in a dataframe
    d = {'v_imp_names': pd.Series(fet_imp_names),
            'v_imp_values': pd.Series(fet_imp)
        }
    v_imp_df = pd.DataFrame(d)
        
    #train AUC
    fpr, tpr, thresholds = roc_curve(train_ds[y], train_pred_prob)
    roc_auc = auc(fpr, tpr)
    ret_dict={"train_pred_class":train_pred_class
                ,"test_pred_class":test_pred_class
                ,"train_pred_prob":train_pred_prob
                ,"test_pred_prob":test_pred_prob
                ,"cf_mat_train":cf_mat_train
                ,"train_met_dict":train_met_dict
                ,"v_imp_df":v_imp_df
                ,"train_auc":roc_auc
                ,"fpr_auc":fpr
                ,"tpr_auc":tpr
                ,"thresholds_auc":thresholds
                }


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-179-ccbf236f91b5> in <module>()
          3 fet_imp = clf.feature_importances_[feat_index] ##using the descending sorted index and arranging the feature importance array
          4 
    ----> 5 fet_imp_names = [X[i] for i in feat_index] ## collecting the feature names from the index
          6 
          7 ##Putting the sorted feature importance and feature names in a dataframe


    IndexError: list index out of range



    ret_dict.keys()


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-178-941dfd862e6f> in <module>()
    ----> 1 ret_dict.keys()
    

    NameError: name 'ret_dict' is not defined

tran_sample['DOB_int']=pd.to_datetime(tran_sample['DOB'])
tran_sample['LCD_int']=pd.to_datetime(tran_sample['Lead_Creation_Date'])
tran_sample['age_days'].dtypes
tran_sample.head(5)