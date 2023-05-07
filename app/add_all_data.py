from .models import *
import traceback
import json

def addStates():
    try:
        state = "Andhra Pradesh"
        districts = ['Anantapur', 'Chittoor', 'East Godavari', 'Guntur', 'YSR Kadapa district', 'Krishna', 'Kurnool', 'Nellore', 'Prakasam', 'Srikakulam', 'Visakhapatnam', 'Vizianagaram', 'West Godavari']
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = "Arunachal Pradesh"
        districts = ['Anjaw', 'Changlang', 'Dibang Valley', 'East Kameng', 'East Siang', 'Kamle', 'Kra Daadi', 'Kurung Kumey', 'Lepa-Rada', 'Lohit', 'Longding', 'Lower Dibang Valley', 'Lower Siang', 'Lower Subansiri', 'Namsai', 'Pakke-Kessang', 'Papum Pare', 'Shi-Yomi', 'Siang', 'Tawang', 'Tirap', 'Upper Siang', 'Upper Subansiri', 'West Kameng', 'West Siang']
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = "Assam"
        districts = ['Bajali', 'Baksa', 'Barpeta', 'Biswanath', 'Bongaigaon', 'Cachar', 'Charaideo', 'Chirang', 'Darrang', 'Dhemaji', 'Dhubri', 'Dibrugarh', 'Dima Hasao', 'Goalpara', 'Golaghat', 'Hailakandi', 'Hojai', 'Jorhat', 'Kamrup', '	Kamrup Metropolitan', 'Karbi Anglong', 'Karimganj', 'Kokrajhar', 'Lakhimpur', 'Majuli', 'Morigaon', 'Nagaon', 'Nalbari', 'Sivasagar', 'Sonitpur', 'South Salmara-Mankachar', 'Tinsukia', 'Udalguri', '	West Karbi Anglong']
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Bihar'
        districts = ['Araria', 'Arwal', 'Aurangabad', 'Banka', 'Begusarai', 'Bhagalpur', 'Bhojpur', 'Buxar', 'Darbhanga', 'East Champaran (Motihari)', 'Gaya', 'Gopalganj', 'Jamui', 'Jehanabad', 'Kaimur (Bhabua)', 'Katihar', 'Khagaria', 'Kishanganj', 'Lakhisarai', 'Madhepura', 'Madhubani', 'Munger (Monghyr)', 'Muzaffarpur', 'Nalanda', 'Nawada', 'Patna', 'Purnia (Purnea)', 'Rohtas', 'Saharsa', 'Samastipur', 'Saran', 'Sheikhpura', 'Sheohar', 'Sitamarhi', 'Siwan', 'Supaul', 'Vaishali', 'West Champaran', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Chhattisgarh'
        districts = ['Balod', 'Baloda Bazar', 'Balrampur', 'Bastar', 'Bemetara', 'Bijapur', 'Bilaspur', 'Dantewada (South Bastar)', 'Dhamtari', 'Durg', 'Gariyaband', 'Janjgir-Champa', 'Jashpur', 'Kabirdham (Kawardha)', 'Kanker (North Bastar)', 'Kondagaon', 'Korba', 'Korea (Koriya)', 'Mahasamund', 'Mungeli', 'Narayanpur', 'Raigarh', 'Raipur', 'Rajnandgaon', 'Sukma', 'Surajpur', 'Surguja', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Goa'
        districts = ['North Goa', 'South Goa', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Gujarat'
        districts = ['Ahmedabad', 'Amreli', 'Anand', 'Aravalli', 'Banaskantha (Palanpur)', 'Bharuch', 'Bhavnagar', 'Botad', 'Chhota Udepur', 'Dahod', 'Dangs (Ahwa)', 'Devbhoomi Dwarka', 'Gandhinagar', 'Gir Somnath', 'Jamnagar', 'Junagadh', 'Kachchh', 'Kheda (Nadiad)', 'Mahisagar', 'Mehsana', 'Morbi', 'Narmada (Rajpipla)', 'Navsari', 'Panchmahal (Godhra)', 'Patan', 'Porbandar', 'Rajkot', 'Sabarkantha (Himmatnagar)', 'Surat', 'Surendranagar', 'Tapi (Vyara)', 'Vadodara', 'Valsad', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Haryana'
        districts = ['Ambala', 'Bhiwani', 'Charkhi Dadri', 'Faridabad', 'Fatehabad', 'Gurugram (Gurgaon)', 'Hisar', 'Jhajjar', 'Jind', 'Kaithal', 'Karnal', 'Kurukshetra', 'Mahendragarh', 'Nuh', 'Palwal', 'Panchkula', 'Panipat', 'Rewari', 'Rohtak', 'Sirsa', 'Sonipat', 'Yamunanagar', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Himachal Pradesh'
        districts = ['Bilaspur', 'Chamba', 'Hamirpur', 'Kangra', 'Kinnaur', 'Kullu', 'Lahaul & Spiti', 'Mandi', 'Shimla', 'Sirmaur (Sirmour)', 'Solan', 'Una', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Jharkhand'
        districts = ['Bokaro', 'Chatra', 'Deoghar', 'Dhanbad', 'Dumka', 'East Singhbhum', 'Garhwa', 'Giridih', 'Godda', 'Gumla', 'Hazaribag', 'Jamtara', 'Khunti', 'Koderma', 'Latehar', 'Lohardaga', 'Pakur', 'Palamu', 'Ramgarh', 'Ranchi', 'Sahibganj', 'Seraikela-Kharsawan', 'Simdega', 'West Singhbhum', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Karnataka'
        districts = ['Bagalkot', 'Ballari (Bellary)', 'Belagavi (Belgaum)', 'Bengaluru (Bangalore) Rural', 'Bengaluru (Bangalore) Urban', 'Bidar', 'Chamarajanagar', 'Chikballapur', 'Chikkamagaluru (Chikmagalur)', 'Chitradurga', 'Dakshina Kannada', 'Davangere', 'Dharwad', 'Gadag', 'Hassan', 'Haveri', 'Kalaburagi (Gulbarga)', 'Kodagu', 'Kolar', 'Koppal', 'Mandya', 'Mysuru (Mysore)', 'Raichur', 'Ramanagara', 'Shivamogga (Shimoga)', 'Tumakuru (Tumkur)', 'Udupi', 'Uttara Kannada (Karwar)', 'Vijayapura (Bijapur)', 'Yadgir', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Kerala'
        districts = ['Alappuzha', 'Ernakulam', 'Idukki', 'Kannur', 'Kasaragod', 'Kollam', 'Kottayam', 'Kozhikode', 'Malappuram', 'Palakkad', 'Pathanamthitta', 'Thiruvananthapuram', 'Thrissur', 'Wayanad', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Madhya Pradesh'
        districts = ['Agar Malwa', 'Alirajpur', 'Anuppur', 'Ashoknagar', 'Balaghat', 'Barwani', 'Betul', 'Bhind', 'Bhopal', 'Burhanpur', 'Chhatarpur', 'Chhindwara', 'Damoh', 'Datia', 'Dewas', 'Dhar', 'Dindori', 'Guna', 'Gwalior', 'Harda', 'Hoshangabad', 'Indore', 'Jabalpur', 'Jhabua', 'Katni', 'Khandwa', 'Khargone', 'Mandla', 'Mandsaur', 'Morena', 'Narsinghpur', 'Neemuch', 'Panna', 'Raisen', 'Rajgarh', 'Ratlam', 'Rewa', 'Sagar', 'Satna', 'Sehore', 'Seoni', 'Shahdol', 'Shajapur', 'Sheopur', 'Shivpuri', 'Sidhi', 'Singrauli', 'Tikamgarh', 'Ujjain', 'Umaria', 'Vidisha', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Maharashtra'
        districts = ['Ahmednagar', 'Akola', 'Amravati', 'Aurangabad', 'Beed', 'Bhandara', 'Buldhana', 'Chandrapur', 'Dhule', 'Gadchiroli', 'Gondia', 'Hingoli', 'Jalgaon', 'Jalna', 'Kolhapur', 'Latur', 'Mumbai City', 'Mumbai Suburban', 'Nagpur', 'Nanded', 'Nandurbar', 'Nashik', 'Osmanabad', 'Palghar', 'Parbhani', 'Pune', 'Raigad', 'Ratnagiri', 'Sangli', 'Satara', 'Sindhudurg', 'Solapur', 'Thane', 'Wardha', 'Washim', 'Yavatmal', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Manipur'
        districts = ['Bishnupur', 'Chandel', 'Churachandpur', 'Imphal East', 'Imphal West', 'Jiribam', 'Kakching', 'Kamjong', 'Kangpokpi', 'Noney', 'Pherzawl', 'Senapati', 'Tamenglong', 'Tengnoupal', 'Thoubal', 'Ukhrul', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Meghalaya'
        districts = ['East Garo Hills', 'East Jaintia Hills', 'East Khasi Hills', 'North Garo Hills', 'Ri Bhoi', 'South Garo Hills', 'South West Garo Hills', 'South West Khasi Hills', 'West Garo Hills', 'West Jaintia Hills', 'West Khasi Hills', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Mizoram'
        districts = ['Aizawl', 'Champhai', 'Kolasib', 'Lawngtlai', 'Lunglei', 'Mamit', 'Saiha', 'Serchhip', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Nagaland'
        districts = ['Dimapur', 'Kiphire', 'Kohima', 'Longleng', 'Mokokchung', 'Mon', 'Peren', 'Phek', 'Tuensang', 'Wokha', 'Zunheboto', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Odisha'
        districts = ['Angul', 'Balangir', 'Balasore', 'Bargarh', 'Bhadrak', 'Boudh', 'Cuttack', 'Deogarh', 'Dhenkanal', 'Gajapati', 'Ganjam', 'Jagatsinghapur', 'Jajpur', 'Jharsuguda', 'Kalahandi', 'Kandhamal', 'Kendrapara', 'Kendujhar (Keonjhar)', 'Khordha', 'Koraput', 'Malkangiri', 'Mayurbhanj', 'Nabarangpur', 'Nayagarh', 'Nuapada', 'Puri', 'Rayagada', 'Sambalpur', 'Sonepur', 'Sundargarh', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Punjab'
        districts = ['Amritsar', 'Barnala', 'Bathinda', 'Faridkot', 'Fatehgarh Sahib', 'Fazilka', 'Ferozepur', 'Gurdaspur', 'Hoshiarpur', 'Jalandhar', 'Kapurthala', 'Ludhiana', 'Mansa', 'Moga', 'Muktsar', 'Nawanshahr (Shahid Bhagat Singh Nagar)', 'Pathankot', 'Patiala', 'Rupnagar', 'Sahibzada Ajit Singh Nagar (Mohali)', 'Sangrur', 'Tarn Taran', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Rajasthan'
        districts = ['Ajmer', 'Alwar', 'Banswara', 'Baran', 'Barmer', 'Bharatpur', 'Bhilwara', 'Bikaner', 'Bundi', 'Chittorgarh', 'Churu', 'Dausa', 'Dholpur', 'Dungarpur', 'Hanumangarh', 'Jaipur', 'Jaisalmer', 'Jalore', 'Jhalawar', 'Jhunjhunu', 'Jodhpur', 'Karauli', 'Kota', 'Nagaur', 'Pali', 'Pratapgarh', 'Rajsamand', 'Sawai Madhopur', 'Sikar', 'Sirohi', 'Sri Ganganagar', 'Tonk', 'Udaipur', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Sikkim'
        districts = ['East Sikkim', 'North Sikkim', 'South Sikkim', 'West Sikkim', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Tamil Nadu'
        districts = ['Ariyalur', 'Chengalpattu', 'Chennai', 'Coimbatore', 'Cuddalore', 'Dharmapuri', 'Dindigul', 'Erode', 'Kallakurichi', 'Kanchipuram', 'Kanyakumari', 'Karur', 'Krishnagiri', 'Madurai', 'Nagapattinam', 'Namakkal', 'Nilgiris', 'Perambalur', 'Pudukkottai', 'Ramanathapuram', 'Ranipet', 'Salem', 'Sivaganga', 'Tenkasi', 'Thanjavur', 'Theni', 'Thoothukudi (Tuticorin)', 'Tiruchirappalli', 'Tirunelveli', 'Tirupathur', 'Tiruppur', 'Tiruvallur', 'Tiruvannamalai', 'Tiruvarur', 'Vellore', 'Viluppuram', 'Virudhunagar', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Telangana'
        districts = ['Adilabad', 'Bhadradri Kothagudem', 'Hyderabad', 'Jagtial', 'Jangaon', 'Jayashankar Bhoopalpally', 'Jogulamba Gadwal', 'Kamareddy', 'Karimnagar', 'Khammam', 'Komaram Bheem Asifabad', 'Mahabubabad', 'Mahabubnagar', 'Mancherial', 'Medak', 'Medchal', 'Nagarkurnool', 'Nalgonda', 'Nirmal', 'Nizamabad', 'Peddapalli', 'Rajanna Sircilla', 'Rangareddy', 'Sangareddy', 'Siddipet', 'Suryapet', 'Vikarabad', 'Wanaparthy', 'Warangal (Rural)', 'Warangal (Urban)', 'Yadadri Bhuvanagiri', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Tripura'
        districts = ['Dhalai', 'Gomati', 'Khowai', 'North Tripura', 'Sepahijala', 'South Tripura', 'Unakoti', 'West Tripura', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Uttar Pradesh'
        districts = ['Agra', 'Aligarh', 'Allahabad', 'Ambedkar Nagar', 'Amethi (Chatrapati Sahuji Mahraj Nagar)', 'Amroha (J.P. Nagar)', 'Auraiya', 'Azamgarh', 'Baghpat', 'Bahraich', 'Ballia', 'Balrampur', 'Banda', 'Barabanki', 'Bareilly', 'Basti', 'Bhadohi', 'Bijnor', 'Budaun', 'Bulandshahr', 'Chandauli', 'Chitrakoot', 'Deoria', 'Etah', 'Etawah', 'Faizabad', 'Farrukhabad', 'Fatehpur', 'Firozabad', 'Gautam Buddha Nagar', 'Ghaziabad', 'Ghazipur', 'Gonda', 'Gorakhpur', 'Hamirpur', 'Hapur (Panchsheel Nagar)', 'Hardoi', 'Hathras', 'Jalaun', 'Jaunpur', 'Jhansi', 'Kannauj', 'Kanpur Dehat', 'Kanpur Nagar', 'Kanshiram Nagar (Kasganj)', 'Kaushambi', 'Kushinagar (Padrauna)', 'Lakhimpur - Kheri', 'Lalitpur', 'Lucknow', 'Maharajganj', 'Mahoba', 'Mainpuri', 'Mathura', 'Mau', 'Meerut', 'Mirzapur', 'Moradabad', 'Muzaffarnagar', 'Pilibhit', 'Pratapgarh', 'RaeBareli', 'Rampur', 'Saharanpur', 'Sambhal (Bhim Nagar)', 'Sant Kabir Nagar', 'Shahjahanpur', 'Shamali (Prabuddh Nagar)', 'Shravasti', 'Siddharth Nagar', 'Sitapur', 'Sonbhadra', 'Sultanpur', 'Unnao', 'Varanasi', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Uttarakhand'
        districts = ['Almora', 'Bageshwar', 'Chamoli', 'Champawat', 'Dehradun', 'Haridwar', 'Nainital', 'Pauri Garhwal', 'Pithoragarh', 'Rudraprayag', 'Tehri Garhwal', 'Udham Singh Nagar', 'Uttarkashi', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'West Bengal'
        districts = ['Alipurduar', 'Bankura', 'Birbhum', 'Cooch Behar', 'Dakshin Dinajpur (South Dinajpur)', 'Darjeeling', 'Hooghly', 'Howrah', 'Jalpaiguri', 'Jhargram', 'Kalimpong', 'Kolkata', 'Malda', 'Murshidabad', 'Nadia', 'North 24 Parganas', 'Paschim Medinipur (West Medinipur)', 'Paschim (West) Burdwan (Bardhaman)', 'Purba Burdwan (Bardhaman)', 'Purba Medinipur (East Medinipur)', 'Purulia', 'South 24 Parganas', 'Uttar Dinajpur (North Dinajpur)', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=False).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Andaman & Nicobar'
        districts = ['Nicobar', 'North and Middle Andaman', 'South Andaman', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=True).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Chandigarh'
        districts = ['Chandigarh', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=True).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Dadra & Nagar Haveli and Daman & Diu'
        districts = ['Daman', 'Diu', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=True).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Delhi'
        districts = ['Central Delhi', 'East Delhi', 'New Delhi', 'North Delhi', 'North East Delhi', 'North West Delhi', 'Shahdara', 'South Delhi', 'South East Delhi', 'South West Delhi', 'West Delhi', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=True).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Jammu & Kashmir'
        districts = ['Anantnag', 'Bandipore', 'Baramulla', 'Budgam', 'Doda', 'Ganderbal', 'Jammu', 'Kathua', 'Kishtwar', 'Kulgam', 'Kupwara', 'Poonch', 'Pulwama', 'Rajouri', 'Ramban', 'Reasi', 'Samba', 'Shopian', 'Srinagar', 'Udhampur', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=True).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Ladakh'
        districts = ['Kargil', 'Leh', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=True).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Lakshadweep'
        districts = ['Lakshadweep', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=True).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()

        state = 'Pondicherry'
        districts = ['Karaikal', 'Mahe', 'Puducherry', 'Yanam', ]
        if States.objects.filter(Name=state).exists() == False:
            States(Name=state, Is_Union_Territory=True).save()
        state = States.objects.filter(Name=state).first()
        for dis in districts:
            if Districts.objects.filter(Name=dis, state=state).exists() == False:
                Districts(Name=dis, state=state).save()
    except Exception as e:
        traceback.print_exc()
        print('\n\n')
    finally:
        return True