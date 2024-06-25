from model import patient_prediction
import streamlit as st
import numpy as np

st.set_page_config("Severity of Proteinuria in Pregnent Women")
st.sidebar.title(
    "Using Algorithm To Predict Severity Of Proteinuria Among Pregnant Women")
st.sidebar.subheader(
    "The descriptions for the features with respect to proteinuria and pregnancy, including normal ranges and potential side effects:")

st.sidebar.write(""" Proteinuria
                 
Description: 
                 
                 Proteinuria is the presence of excessive amounts of protein in the urine. It is a hallmark of kidney damage or dysfunction and can be associated with various health complications during pregnancy.
Normal Range: <300 mg/24 hours
Side Effects:
                 
                  Proteinuria can lead to symptoms such as edema (swelling), hypertension (high blood pressure), and decreased urine output. If left untreated, severe proteinuria can lead to kidney damage, requiring dialysis or a kidney transplant.""")
st.sidebar.write(""" BMI
                 
 Description:
                                

                 Body mass index (BMI) is a measure of body fat based on height and weight. Elevated BMI can increase the risk of developing kidney disease, which may be associated with proteinuria during pregnancy.
                 
Normal Range: 18.5-24.9 kg/m
 
Side Effects: 

                 Elevated BMI can increase the risk of developing various health complications, including kidney disease, diabetes, and cardiovascular disease. If left untreated, these conditions can lead to serious health issues and even death.""")

st.sidebar.write("""Blood Pressure
                 

Description:
                 
                  Blood pressure is a measure of the force of blood against the walls of blood vessels. Elevated blood pressure can indicate kidney damage or dysfunction, which may be associated with proteinuria during pregnancy.
Normal Range: <140/90 mmHg
Side Effects:
                 
                  Elevated blood pressure can lead to symptoms such as headaches, dizziness, and chest pain. If left untreated, severe hypertension can lead to organ damage, requiring medical intervention.""")

st.sidebar.write("""Serum Creatinine
                 
Description: 
                 
                 Serum creatinine is a waste product that is produced when the body breaks down muscle tissue. Elevated levels of creatinine in the blood can indicate kidney damage or dysfunction, which may be associated with proteinuria during pregnancy.
Normal Range: 35-71 umol/L
Side Effects: 
                 
                 Elevated creatinine levels can be a sign of kidney damage or dysfunction, which may lead to symptoms such as fatigue, nausea, and decreased urine output. If left untreated, severe kidney damage can lead to end-stage renal disease, requiring dialysis or a kidney transplant.""")

st.sidebar.write('''Serum Uric Acid
                 
Description:
                 
                  Serum uric acid is a waste product that is produced when the body breaks down purines. Elevated levels of uric acid in the blood can indicate kidney damage or dysfunction, which may be associated with proteinuria during pregnancy.
Normal Range: 350-720umol/L
Side Effects:
                 
                  Elevated uric acid levels can lead to symptoms such as joint pain, kidney stones, and gout. If left untreated, severe kidney damage can lead to end-stage renal disease, requiring dialysis or a kidney transplant.''')

st.sidebar.write("""GFR
                 
Description: 
                 
                 Glomerular filtration rate (GFR) is a measure of kidney function. Decreased GFR can indicate kidney damage or dysfunction, which may be associated with proteinuria during pregnancy.
Normal Range: 90-120 mL/min
Side Effects: 
                 
                 Decreased GFR can lead to symptoms such as fatigue, nausea, and decreased urine output. If left untreated, severe kidney damage can lead to end-stage renal disease, requiring dialysis or a kidney transplant.""")

st.sidebar.write("""Alanine Aminotransferase (ALT)
                 
Description:
                 
                  Alanine aminotransferase (ALT) is an enzyme found primarily in the liver. Elevated levels of ALT in the blood can indicate liver damage or dysfunction, which may be associated with proteinuria during pregnancy.
Normal Range: 7-56 IU/L
Side Effects:
                 
                  Elevated ALT levels can be a sign of liver damage or dysfunction, which may lead to symptoms such as fatigue, nausea, and abdominal pain. If left untreated, severe liver damage can lead to liver failure, requiring a liver transplant.

Aspartate Aminotransferase (AST)
                 
Description: 
                 
                 Aspartate aminotransferase (AST) is an enzyme found primarily in the liver and heart. Elevated levels of AST in the blood can indicate liver or heart damage or dysfunction, which may be associated with proteinuria during pregnancy.
Normal Range: 8-48 IU/L
Side Effects:
                 
                  Elevated AST levels can be a sign of liver or heart damage or dysfunction, which may lead to symptoms such as fatigue, nausea, and chest pain. If left untreated, severe liver or heart damage can lead to organ failure, requiring a transplant.
                 
Blood Urea Nitrogen (BUN)
                 
Description:
                 
                  Blood urea nitrogen (BUN) is a waste product that is produced when the body breaks down protein. It is typically removed from the blood by the kidneys and excreted in the urine. Elevated levels of BUN in the blood can indicate kidney damage or dysfunction, which may be associated with proteinuria during pregnancy.
Normal Range: 0.7-2 mmol/L
Side Effects:
                 
                  Elevated BUN levels can be a sign of kidney damage or dysfunction, which may lead to symptoms such as fatigue, nausea, and decreased urine output. If left untreated, severe kidney damage can lead to end-stage renal disease, requiring dialysis or a kidney transplant.""")
st.header("Please Fill the Details to check the Severity of Proteinuria.")
age = st.text_input('Age(years):', value=30)
bmi = st.text_input('BMI(kg/m*2):', value=24)
gravida = st.text_input(
    'Gravida:(Total number of confirmed pregnancies a female has had)', value=3)
sbp = st.text_input('Systolic Blood Pressure(mmHg):', value=140)
dbp = st.text_input('Diastolic Blood Pressure(mmHg):', value=90)
proteinuria = st.text_input('Proteinuria(mg/day):', value=300)
blood_urea_nitrogen = st.text_input('Blood_urea_nitrogen(mmol/L):', value=3)
serum_creatinine = st.text_input('Serum_creatinine(umol/L):', value=40)
serum_uric_acid = st.text_input('Serum_uric_acid(umol/L):', value=400)
gfr = st.text_input('Glomerular Filteration Rate(ml/min/1.73m*2):', value=130)
alanine_aminotransferase = st.text_input(
    'Alanine_aminotransferase(U/L):', value=10)
asparate_aminotransferase = st.text_input(
    'Asparate_aminotransferase(U/L):', value=14)
platelets = st.text_input('Platelets(10*9/L):', value=290)
albumin = st.text_input('Albumin(g/L):', value=35)
submit = st.button('Submit')




from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb


def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 105px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="orange",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.sidebar.markdown(str(foot), unsafe_allow_html=True)


def footer():
    myargs = [
        "Made ",
              "  by ",
         " Tushar Pandey"
        ]
    layout(*myargs)



if submit:
    st.subheader("Reports")
    info = np.array([[age, bmi, gravida, sbp, dbp, proteinuria, blood_urea_nitrogen, serum_creatinine,
                    serum_uric_acid, gfr, alanine_aminotransferase, asparate_aminotransferase, platelets, albumin]])
    info = info.astype(float)
    prediction = patient_prediction(info)
    st.write(prediction)


    if __name__ == "__main__":
        footer()