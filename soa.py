import streamlit as st

# Sample data from your table
data = [
    (5.9, 'Anis/Majid/Tareque/Newaz/Nabil/Dilruba+Arsila+SCD/FD'),
    (29.3, 'Anis/Majid/Tareque/Newaz/Nabil/Dilruba/Somnath+Arsila/Masrul+Majid+SCD/FD'),
    (117.0, 'Anis/Majid/Tareque/Newaz/Nabil/Dilruba/Somnath+Zinnia/Isha+Ram/Akhilesh+Yogesh'),
    (234.0, 'SCD/Factory Director+Zinnia/Isha+Ram+Yogesh+Cuthbert, Vicky/….'),
    (2925.3, 'SCD/Factory Director+Zinnia/Isha+Ram+Yogesh+Cuthbert, Vicky/….+Ritesh.Tiwari'),
    (5850.5, 'Yogesh+Ritesh'),
]

# Streamlit app
st.title('SOA Finder')

# User input for BDT million value
bdt_value = st.number_input('Enter BDT Mln value:')

# Function to find the corresponding SOA
def find_soa(bdt_value):
    for value, soa in data:
        if bdt_value <= value:
            return soa
    return "No matching SOA found"

# Display the result
if bdt_value:
    soa = find_soa(bdt_value)
    st.write(f'SOA for BDT {bdt_value} Mln: {soa}')
