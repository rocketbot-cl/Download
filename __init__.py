# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import requests


"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

if module == "Download":
    url = GetParams("url")
    file_folder = GetParams("file_folder")
    local_filename = GetParams("file_name")    
    var_ = GetParams("result")    

    #local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True,verify=False) as r:

        r.raise_for_status()
        if not local_filename:
            local_filename = r.headers['content-disposition'].split("=")[1]
        
        local_filename = os.path.join(os.sep, *file_folder.split(os.sep),*local_filename.split("/"))
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush()

    try:
        SetVar( var_,  local_filename)
    except Exception as e:
        raise Exception(e)
