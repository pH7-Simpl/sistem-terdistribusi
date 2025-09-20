#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 16:52:27 2024

@author: widhi
"""
from zeep import Client

# URL WSDL menggunakan nama service Docker Compose
wsdl = 'http://soap-server:8000/?wsdl'

# Membuat klien SOAP berdasarkan WSDL
client = Client(wsdl=wsdl)

# Memanggil metode penjumlahan dari layanan SOAP server dan Menampilkan hasil penjumlahan
result = client.service.add(10, 5)
print(f'Hasil penjumlahan dari server SOAP: {result}')

# Uji kalkulasi bebas dengan Sympy
# Kalkulasi 1
expr = "sin(pi/4) + sqrt(2)"
result = client.service.calc(expr)
print(f'Hasil kalkulasi 1 "{expr}" = {result}')

# Kalkulasi 2
expr2 = "integrate(x**2, (x, 0, 3))"
result2 = client.service.calc(expr2)
print(f'Hasil kalkulasi 2 "{expr2}" = {result2}')