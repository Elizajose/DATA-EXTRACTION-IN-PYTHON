import tabula
import json

def pdf_to_json(pdf_path, json_path):
    # Extrai tabelas do PDF
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

    # Converte as tabelas para JSON
    json_data = []
    for table_num, table in enumerate(tables):
        table_json = table.to_ict(orient='records')
        json_data.append({f"table_{table_num + 1}": table_json})

    # Escreve o JSON para uma festa
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    pdf_path = "C:/Users/MICRO/Documents/TESTES EM PYTHON - EXTRAÇÃO/In_path/PDF.pdf"
    json_path = "C:/Users/MICRO/Documents/TESTES EM PYTHON - EXTRAÇÃO/Out_path/saida.json"
    pdf_to_json(pdf_path, json_path)