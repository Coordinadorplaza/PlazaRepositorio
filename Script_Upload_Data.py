import sys,json, simplejson, re
from linkaform_api import  base
from account_settings import *
import datetime


#----Record
def set_add_record(data):
    name = data.get('name','')
    date = data.get('fecha_hora','')
    user_deliver = data.get('user_deliver','').replace(' ','_').lower()
    checknew = data.get('checknew','').replace(' ','_').lower()
    cedula = data.get('cedula', '')
    telefono = data.get('telefono', '')
    direccion = data.get('direccion', '')
    silla = data.get('silla', '')
    aspecto = data.get('aspecto', '')
    url_img = data.get('img','')

    #----Create Name FIle
    now = datetime.datetime.now()
    fecha_hora_str = now.strftime("%Y%m%d%H%M%S")
    numero_aleatorio = hash(fecha_hora_str)
    numero_aleatorio = abs(numero_aleatorio) % (10 ** 8)







    #----Create Dic
    dic_response = {
        '6615c1390794eb4be10df57e' : name,
        '6615c1390794eb4be10df57f' : date,
        '66170f2d9604953d2a259b27' : user_deliver, 
        '662994d988cde2a293c78a86' : checknew, 
        '661af46b80dd3c6f373f2e62' : cedula,
        '661b00bb25137cd0d2f11a1f' : telefono, 
        '661b05cbd0182d377f815c6e' : direccion, 
        '661b01d91137e5ddd1bb98c5' : silla, 
        '663ae805cee7691b27f2747a' : aspecto, 
        '6615c1390794eb4be10df580' : {
            'file_name': f"{numero_aleatorio}.png",
            'file_url':url_img,
        },
    }

    #metadata = lkf_api.get_metadata(95435)
    metadata = script_obj.lkf_api.get_metadata(117320)
    metadata['answers'] = dic_response
    resp_create = script_obj.lkf_api.post_forms_answers_list(metadata)

    status_request = '400'
    if len(resp_create) == 1:
        status_request = resp_create[0].get('status_code','400')
    return status_request

if __name__ == "__main__":
    script_obj = base.LKF_Base(settings, sys_argv=sys.argv, use_api=True)
    script_obj.console_run()

    #-FILTROS
    data = script_obj.data
    data = data.get('data',[])

    dataFilter = data.get('formInformation',[])
    option = data.get('option',0)

    if option == 'add_record':
        response = set_add_record(dataFilter)
        sys.stdout.write(simplejson.dumps(response))