'''
-----------------------------------------------------
Module Handles the data report creation
-----------------------------------------------------
Author: Top Aspirer
ID: HIM
Email: tendolloyd@gmail.com
Created:  Mar 07, 2025
'''

# This is to be started once at least 60% of the model is complete

import streamlit as st
import pandas as pnds
from fpdf import FPDF


# Create instance of FPDF class
pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hello World!')

# Save the PDF to a variable
pdf_output = pdf.output(dest='S').encode('latin1')






