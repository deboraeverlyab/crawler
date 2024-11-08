import asyncio
from src.crawler import Crawler
from src.googledriveuploader import GoogleDriveUploader

async def main():
    url = "https://www.compras.rs.gov.br/editais/pesquisar"
    #palavras = ['Saúde', 'Gestão', 'Gestor', 'Gerente', 'Monitoramento', 'Hospital', 'Hospitalar', 'Hospitalares', 'Medica', 'PCR', 'Clínica', 'Extração', 'IST']
    palavras = ['Extração']

    crawler = Crawler(url)
    crawler.iniciar_driver()
    crawler.crawler(palavras)
    crawler.fechar_driver()

    # compartilhando no drive
    credentials_path = "pythonselenium-440223-152f243ca4a9.json"   # necessario mudar
    drive_folder_id = "1C69yH9rBdE5x-M6ny9QPDGSwz2odryRd"     # id pasta drive
    file_path = "resultado_pesquisa.csv"                

    # Instancia o uploader e faz o upload do arquivo
    uploader = GoogleDriveUploader(credentials_path, drive_folder_id)
    uploader.upload_file(file_path, file_name="resultado_final.csv")
