# PythonAcumulaTotales.py

total_aprob_num_pdf = 0
total_aprob_num_editable = 0
total_aprob_letra_pdf = 0
total_aprob_letra_editable = 0
total_vig_pdf = 0
total_vig_editable = 0



#etiqueta Abre el archivo en modo lectura
#with open('C:\\Users\\hjorquera\\Desktop\\PLANIMETRIA\\PROCESO\\Proceso 20231030\\log_CuadraturaProvisoria.txt', 'r') as archivo:
#with open('C:\\Users\\hjorquera\\Desktop\\PLANIMETRIA\\PROCESO\\Proceso 20231030\\log_CuadraturaProvisoria 20231030.txt', 'r') as archivo:
with open('C:\\Users\\hjorquera\\Desktop\\PLANIMETRIA\\PROCESO\\Proceso 20231024\\log_CuadraturaProvisoria.txt', 'r') as archivo:
    # Lee cada linea del archivo
    for linea in archivo:
        if linea[0] == '0':
            # Divide la linea en campos separados por tabulaciones
            campos = linea.strip().split('\t')
        
            # Extrae la etiqueta y el valor de la tercera columna
            etiqueta = campos[1]
           
            if etiqueta  =='DOCUMENTOS APROBADOS/REV LETRA/01 PDF             ':
                valor = int(campos[2])
                total_aprob_letra_pdf += valor
            if etiqueta  =='DOCUMENTOS APROBADOS/REV LETRA/02 EDITABLE        ':
                valor = int(campos[2])
                total_aprob_letra_editable += valor
            if etiqueta == 'DOCUMENTOS APROBADOS/REV NUMERO/01 PDF            ': 
                valor = int(campos[2])
                total_aprob_num_pdf += valor
            if etiqueta == 'DOCUMENTOS APROBADOS/REV NUMERO/02 EDITABLE       ':
                valor = int(campos[2])
                total_aprob_num_editable += valor
            if etiqueta == 'DOCUMENTOS VIGENTES/01 PDF/CON OBSERVACIONES      ':
                valor = int(campos[2])
                total_vig_pdf += valor
            if etiqueta == 'DOCUMENTOS VIGENTES/01 PDF/SIN OBSERVACIONES      ':
                valor = int(campos[2])
                total_vig_pdf += valor
            if etiqueta == 'DOCUMENTOS VIGENTES/02 EDITABLE/CON OBSERVACIONES ':
                valor = int(campos[2])
                total_vig_editable += valor
            if etiqueta == 'DOCUMENTOS VIGENTES/02 EDITABLE/SIN OBSERVACIONES ':
                valor = int(campos[2])
                total_vig_editable += valor
        
# Imprime los totales por etiqueta
print(f'total_aprob_num_pdf: {total_aprob_num_pdf}')
print(f'total_aprob_num_editable: {total_aprob_num_editable}')
print(f'total_aprob_letra_pdf: {total_aprob_letra_pdf}')
print(f'total_aprob_letra_editable: {total_aprob_letra_editable}')
print(f'total_vig_pdf: {total_vig_pdf}')
print(f'total_vig_editable: {total_vig_editable}')