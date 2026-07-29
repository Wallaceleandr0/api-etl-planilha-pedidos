from fastapi import FastAPI, HTTPException, UploadFile, File
from tratar_dados import tratar_planilha_saldo

app = FastAPI()

@app.post('/tratar')
async def dados(arquivo: UploadFile = File(...)):
    if not arquivo.filename.endswith('.xlsx'):
        raise HTTPException(
            status_code = 400,
            detail='Envie um arquivo .xlsx'
        )
    
    return tratar_planilha_saldo(arquivo.file)