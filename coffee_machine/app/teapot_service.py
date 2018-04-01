from datetime import datetime
import json
from flask import Flask, Response, request
from decoy_config import get_decoy
from models import TeaCup
from tea_exceptions import NoSuchThingy


application = Flask(__name__)

GLOBAL_HEADERS = {
    'Accept-Additions': 'milk-type:soy, syrup-type:Raspberry, pastry:pita',
    'Content-Type': 'application/json'
}


def _report_alert(desc):
    decoy = get_decoy()

    alert = {
        "severity": 1,
        "timestamp": datetime.utcnow().isoformat(),
        "originating_ip": request.remote_addr,
        "event_type": "teapot_interaction",
        "event_description": desc
    }

    decoy.report_alert(alert)


@application.route('/', methods=['POST', 'BREW'])
def brew():
    _report_alert('Brew requested')
    teacup = TeaCup(request.get_json() or {})

    if teacup.options.get('type') == 'coffee':
        _report_alert('User attempted to make coffee in a teapot')
        return Response(status=418, response=json.dumps({'error': 'I\'m a teapot'}))

    teacup.save()

    return Response(status=201, response=json.dumps(teacup.options), headers=GLOBAL_HEADERS)


@application.route('/<teacup_id>/', methods=['GET'])
def retrieve(teacup_id):
    _report_alert('Retrieve tea cup requested')

    try:
        return Response(status=200, response=json.dumps(TeaCup.get_by_id(teacup_id).options))
    except NoSuchThingy:
        return Response(status=404)


@application.route('/', methods=['PROPFIND'])
def propfind():
    _report_alert('Propfind requested')

    return Response(status=200, response='What is coffee? Coffee is a drink. And when do we need '
                                         'to drink? When we are thirsty. Thirsty for coffee?')


@application.route('/<teacup_id>/', methods=['WHEN'])
def when(teacup_id):
    _report_alert('Milk pouring stop requested')
    try:
        teacup = TeaCup.get_by_id(teacup_id)
    except NoSuchThingy:
        return Response(status=404)

    got_milk = 'milk' in teacup.options

    if not got_milk:
        return Response(status=406)

    teacup.options['milk_stopped_pouring'] = True
    teacup.save()

    return Response(status=204)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5555)
