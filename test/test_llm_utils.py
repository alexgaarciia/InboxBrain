import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.llm_utils import call_mistral_llm

email_body = """
Hola,

¿Podrías por favor hacerme un resumen de los datos del Excel adjunto y destacar si hay alguna tendencia relevante?

Gracias,
Andrea
"""

excel_content = """
Sheet: Ventas_Q1

Columnas: Mes, Región, Ingresos, Costes, Beneficio

Primeras filas:
Enero, Norte, 12000, 8000, 4000
Febrero, Norte, 13500, 8500, 5000
Marzo, Norte, 14000, 9000, 5000

Valores únicos por región: Norte, Sur, Este, Oeste
"""

response = call_mistral_llm(email_body=email_body, excel_content=excel_content)
print("LLM response:\n")
print(response)
