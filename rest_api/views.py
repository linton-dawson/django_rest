import json
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import exception_handler

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from rest_api.serializers import Slot1Serializer, Slot2Serializer
from .models import Slot1, Slot2

class Slot1ViewSet(viewsets.ModelViewSet):
    queryset = Slot1.objects.all()
    serializer_class = Slot1Serializer
    http_method_names = ['post']

    def create(self, request):
        data = request.data
        resp = {}
        part_valid = True
        all_valid, resp['trigger'] = (True,'') if data['values'] else (False,data['invalid_trigger'])
        pick_first = False if 'pick_first' not in data else data['pick_first'] 
        support_multiple = True if 'support_multiple' not in data else data['support_multiple'] 
        resp['parameters'] = {}
        for val in data['values']:
            if val['entity_type'] not in data['type'] or val['value'] not in data['supported_values']:
                all_valid = False
                resp['trigger'] = data['invalid_trigger']
            elif val['entity_type'] in data['type'] and val['value'] in data['supported_values']:
                if data['key'] not in resp['parameters']:
                    resp['parameters'][data['key']] = int(val['value']) if pick_first or not support_multiple else list()
                if not pick_first:
                    resp['parameters']['ids_stated'].append(val['value'].upper())
        resp['partially_filled'] = False if all_valid or not data['values'] else True
        resp['filled'] = all_valid
        return Response(data=resp)

class Slot2ViewSet(viewsets.ModelViewSet):
    queryset = Slot2.objects.all()
    serializer_class = Slot2Serializer
    http_method_names = ['post']
    def create(self, request):
        data = request.data
        resp = {}
        all_valid, resp['trigger'] = (True,'') if data['values'] else (False,data['invalid_trigger'])
        pick_first = False if 'pick_first' not in data else data['pick_first'] 
        support_multiple = True if 'support_multiple' not in data else data['support_multiple'] 
        resp['parameters'] = {}
        for val in data['values']:
            exec(data['var_name'] + '=' + str(val['value']))
            print('constraint' not in data or (data['constraint'] and eval(data['constraint'])))
            if val['entity_type'] not in data['type'] or not('constraint' in data and eval(data['constraint'])):
                all_valid = False
                resp['trigger'] = data['invalid_trigger']
            elif val['entity_type'] in data['type'] and ('constraint' not in data or (data['constraint'] and eval(data['constraint']))):
                if data['key'] not in resp['parameters']:
                    resp['parameters'][data['key']] = int(val['value']) if pick_first or not support_multiple else list()
                if not pick_first:
                    resp['parameters'][data['key']].append(val['value'])
        resp['partially_filled'] = False if all_valid or not data['values'] else True
        resp['filled'] = all_valid
        return Response(data=resp)