from fastapi import FastAPI, HTTPException, UploadFile, File
from tratar_dados import tratar_planilha_saldo
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://analise-pedidos-web.vercel.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/tratar')
async def dados(arquivo: UploadFile = File(...)):
    if not arquivo.filename.endswith('.xlsx'):
        raise HTTPException(
            status_code = 400,
            detail='Envie um arquivo .xlsx'
        )
    
    return tratar_planilha_saldo(arquivo.file)