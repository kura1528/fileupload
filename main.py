import os
import pandas as pd
import json
fileName = "/testapp/UploadExcel.xlsx"
#fileUpload = os.getenv(fileName)
applicationName = os.getenv("Application Name")
excel_data = pd.read_excel(os.path.join(fileName))
json_data = excel_data.to_json(orient='records')
print(excel_data)
json_file_path = os.path.join('output.json')
with open(json_file_path, 'w') as json_file:
	json_file.write(json_data)
print("Converted Successfully")
