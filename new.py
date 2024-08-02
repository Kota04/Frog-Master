import streamlit as st
import pandas as pd

# Sample Data
data = {
    'hashes': {
        'sha256_hash': '5961a204bb43bb63f2b98836a34afd1e16a6f3cb160fd17b4718b377273255ff',
        'sha3_384_hash': 'e0f1f8b1dc6bdab509c812590945bd4c7552a9d4c89b107b5e3942ba7b911f4abc43ec820d6bb3bf7a14c5890f3b2aca',
        'sha1_hash': '24960decb2b636b08461ab65e35561944d0f0b02',
        'md5_hash': '98fccb07a0d2a7658b6c42edb5eb1462'
    },
    'file_details': {
        'first_seen': '2024-08-01 08:01:20',
        'last_seen': '2024-08-01 08:36:41',
        'file_name': '98fccb07a0d2a7658b6c42edb5eb1462',
        'file_size': 102247,
        'file_type_mime': 'text/rtf',
        'file_type': 'rtf',
        'reporter': 'zbetcheckin',
        'origin_country': 'FR',
        'anonymous': 0,
        'signature': 'SnakeKeylogger',
        'imphash': None,
        'tlsh': 'T196A3F16D878F48A8CF09A277136A8E0442FCB33EB30555B634AC537037AD93E49A55BC',
        'telfhash': None,
        'gimphash': None,
        'ssdeep': '384:AOmdYo0tzP7QYAOQug5OkhgCSUSAYWxwUhM+3C6cq4BY+1PT4RlINDjT:ucGO4FOCZRRqN6+Y+1PT4RlGHT',
        'dhash_icon': None,
        'comment': None,
        'archive_pw': None,
        'tags': ['rtf', 'SnakeKeylogger'],
        'code_sign': None,
        'delivery_method': 'web_download',
        'intelligence': {
            'clamav': None,
            'downloads': '56',
            'uploads': '2',
            'mail': None
        },
        'file_information': [{'context': 'URLhaus', 'value': 'https://urlhaus.abuse.ch/url/3082266/'}],
        'ole_information': []
    },
    'yararules': {
        'yararules': 'No Yara rules available'
    },
    'vendor_intel': {
        'ANY.RUN': [{
            'malware_family': None,
            'verdict': 'No threats detected',
            'file_name': '98fccb07a0d2a7658b6c42edb5eb1462',
            'date': '2024-08-01 09:00:26',
            'analysis_url': 'https://app.any.run/tasks/0a134866-3b04-48b9-aff5-cbab6b898b87',
            'tags': []
        }],
        'CERT-PL_MWDB': {
            'detection': 'cve-2017-11882-shellcode',
            'link': 'https://mwdb.cert.pl/sample/5961a204bb43bb63f2b98836a34afd1e16a6f3cb160fd17b4718b377273255ff/'
        },
        'vxCube': {
            'verdict': 'malware2',
            'maliciousness': '100',
            'behaviour': [
                {'threat_level': 'malicious', 'rule': 'Connection attempt to an infection source by exploiting the app vulnerability'},
                {'threat_level': 'malicious', 'rule': 'Creating a process from a recently created file'},
                {'threat_level': 'malicious', 'rule': 'Launching a file downloaded from the Internet'},
                # Add more behavior rules here
            ]
        },
        'InQuest': {'verdict': 'MALICIOUS', 'url': None, 'details': []},
        'Triage': {
            'malware_family': None,
            'score': '8',
            'link': 'https://tria.ge/reports/240801-jw5srazglr/',
            'tags': ['discovery', 'execution'],
            'signatures': [
                {'signature': 'Blocklisted process makes network request', 'score': '8'},
                {'signature': 'Command and Scripting Interpreter: PowerShell', 'score': '8'},
                {'signature': 'Drops file in System32 directory', 'score': '5'},
                {'signature': 'Drops file in Windows directory', 'score': '4'},
                {'signature': 'System Location Discovery: System Language Discovery', 'score': '3'},
                {'signature': 'Office loads VBA resources, possible macro or embedded object present', 'score': '1'},
                # Add more signatures here
            ],
            'malware_config': []
        },
        'ReversingLabs': {'threat_name': None, 'status': 'UNKNOWN', 'first_seen': None, 'scanner_count': None, 'scanner_match': None, 'scanner_percent': None},
        'Spamhaus_HBL': [{'detection': 'suspicious', 'link': 'https://www.spamhaus.org/hbl/'}],
        'VMRay': {'verdict': 'malicious', 'malware_family': None, 'report_link': 'https://www.vmray.com/analyses/_mb/5961a204bb43/report/overview.html'},
        'FileScan-IO': {'verdict': None, 'threatlevel': None, 'confidence': None, 'report_link': 'https://www.filescan.io/uploads/66ab410b78d5c73fb1ca7795/reports//overview'}
    },
    'comments': [
        {'id': '98153', 'date_added': '2024-08-01 08:01:21', 'twitter_handle': 'zbetcheckin', 'display_name': 'zbet', 'comment': 'url : hxxp://192.3.179.145/45/kon/wethinkingentirethingstobegreatwithentirethingstobeamazingwithmeiamalwaysonlinethings__________weneedthingsgreatthing.doc'}
    ]
}

# Streamlit App
st.title("Malware Analysis Report")

# CSS for dark and light themes
dark_theme_css = """
<style>
body {
    background-color: #121212;
    color: #e0e0e0;
}
[data-testid="stHeader"] {
    background-color: black;
}
[data-testid="stSidebar"] {
    background-color: #1e1e1e;
    color: #e0e0e0;
}
[data-testid="stAppViewContainer"] {
    background-color: #121212;
}
[data-testid="stMarkdownContainer"] {
    color: #e0e0e0;
}
</style>
"""

light_theme_css = """
<style>
body {
    background-color: #ffffff;
    color: #000000;
}
[data-testid="stHeader"] {
    background-color: #f0f0f0;
}
[data-testid="stSidebar"] {
    background-color: #f0f0f0;
    color: #000000;
}
[data-testid="stAppViewContainer"] {
    background-color: #ffffff;
}
[data-testid="stMarkdownContainer"] {
    color: #000000;
}
</style>
"""

# Sidebar to choose theme
theme = st.sidebar.selectbox("Select Theme", ["Light", "Dark"])

if theme == "Dark":
    st.markdown(dark_theme_css, unsafe_allow_html=True)
else:
    st.markdown(light_theme_css, unsafe_allow_html=True)

# Create Streamlit tables
st.subheader("Hashes")
hashes_df = pd.DataFrame(list(data['hashes'].items()), columns=['Attribute', 'Value'])
st.dataframe(hashes_df)

st.subheader("File Details")
file_details_df = pd.DataFrame(list(data['file_details'].items()), columns=['Attribute', 'Value'])
st.dataframe(file_details_df)

st.subheader("Yara Rules")
yararules_df = pd.DataFrame(list(data['yararules'].items()), columns=['Attribute', 'Value'])
st.dataframe(yararules_df)

st.subheader("Vendor Intelligence")

# ANY.RUN
st.subheader("ANY.RUN")
any_run_df = pd.DataFrame(data['vendor_intel']['ANY.RUN'])
st.dataframe(any_run_df)

# CERT-PL_MWDB
st.subheader("CERT-PL_MWDB")
cert_pl_mwdb_df = pd.DataFrame(list(data['vendor_intel']['CERT-PL_MWDB'].items()), columns=['Attribute', 'Value'])
st.dataframe(cert_pl_mwdb_df)

# vxCube
st.subheader("vxCube")
vxcube_df = pd.DataFrame(data['vendor_intel']['vxCube'])
st.dataframe(vxcube_df)

# InQuest
st.subheader("InQuest")
inquest_df = pd.DataFrame(list(data['vendor_intel']['InQuest'].items()), columns=['Attribute', 'Value'])
st.dataframe(inquest_df)

# Triage
st.subheader("Triage")
triage_df = pd.DataFrame(list(data['vendor_intel']['Triage'].items()), columns=['Attribute', 'Value'])
st.dataframe(triage_df)

# ReversingLabs
st.subheader("ReversingLabs")
reversinglabs_df = pd.DataFrame(list(data['vendor_intel']['ReversingLabs'].items()), columns=['Attribute', 'Value'])
st.dataframe(reversinglabs_df)

# Spamhaus_HBL
st.subheader("Spamhaus_HBL")
spamhaus_hbl_df = pd.DataFrame(data['vendor_intel']['Spamhaus_HBL'])
st.dataframe(spamhaus_hbl_df)

# VMRay
st.subheader("VMRay")
vmray_df = pd.DataFrame(list(data['vendor_intel']['VMRay'].items()), columns=['Attribute', 'Value'])
st.dataframe(vmray_df)

# FileScan-IO
st.subheader("FileScan-IO")
filescan_io_df = pd.DataFrame(list(data['vendor_intel']['FileScan-IO'].items()), columns=['Attribute', 'Value'])
st.dataframe(filescan_io_df)

# Comments Table
st.subheader("Comments")
comments_df = pd.DataFrame(data['comments'])
st.dataframe(comments_df)
