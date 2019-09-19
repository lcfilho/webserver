from aiohttp import web
import logging
import asyncio
import jinja2
import aiohttp_jinja2
from pathlib import Path
from source.conta_zeros_Luis import conta_zeros
from source.converte_romano_Luis import numero_para_romano
from source.validacpf_luis import valida_cpf
from source.gera_senha_Luis import  gera_senha
from source.classifica_senha import classifica_senha
from source.criptografia_senhas import hash_md5
   
   
log = logging.getLogger(__file__)


@aiohttp_jinja2.template('indexx.html')
def basic_handler(request):
    return {'app': request.app}

@aiohttp_jinja2.template('zeros.jinja2')
async def zeros(request):
    string = request.match_info['string']
    context = conta_zeros(string)
    return {'zeros':context}

@aiohttp_jinja2.template('romanos.jinja2')
async def romano(request):    
    numero = request.match_info['numero']      
    context = numero_para_romano(int(numero))
        
    return {'romano':context}
  
@aiohttp_jinja2.template('cpf.jinja2')
async def validacpf(request):    
    cpf = request.match_info['cpf'] 
    context = valida_cpf(cpf)
    return  {'validacpf':context}

@aiohttp_jinja2.template('senha.jinja2')
async def senha(request):
    senha1= gera_senha(15)
    senhas_dict = {"GERADOR DE SENHA": senha1 ,

                    "CLASSIFICA SENHA": classifica_senha(senha1) ,

                    "HASH_MD5": hash_md5(senha1)}
    return  {'senha':senhas_dict}


@asyncio.coroutine
def init(loop):
    logging.basicConfig(level=logging.DEBUG)
    PROJECT_ROOT = Path(__file__).parent
    templates = PROJECT_ROOT / 'templates'
  
    app = web.Application(loop=loop)        
    loader = jinja2.FileSystemLoader([templates])       
    aiohttp_jinja2.setup(app, loader=loader)    

    app.router.add_route('GET', '/', basic_handler, name='indexx.html')
    app.router.add_route('GET', '/romano/{numero}',romano,name='romanos.jinja2' )    
    app.router.add_route('GET','/validacpf/{cpf}', validacpf, name = 'cpf.jinja2')   
    app.router.add_route('GET','/gera_senha', senha,name = 'senha.jinja2')
    app.router.add_route('GET', '/dist_zeros/{string}', zeros, name= 'zeros.jinja2')
    
    
    webserver = app.make_handler()
    server = yield from loop.create_server(webserver, '127.1.1.1',9999)
    print("http://127.1.1.1:9999")
    return server, webserver


loop = asyncio.get_event_loop()
server, webserver = loop.run_until_complete(init(loop))
try:
    loop.run_forever()
except KeyboardInterrupt:
    loop.run_until_complete(webserver.finish_connections())
