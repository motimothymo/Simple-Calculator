import time
import json

from . import app, calc_blueprint

#Services
@calc_blueprint.route('/<int:index>', methods=['GET'])
def prime_service(index):
    task = app.send_task(calc_blueprint.name + '.tasks.prime_service', kwargs={'index': index})
    time.sleep(3)
    result = app.AsyncResult(task.id).result
    print (result)  
    return json.dumps({"result": result, "id": task.id})

@calc_blueprint.route('/palindrome/<int:index>', methods=['GET'])
def prime_palindrome_service(index):
    task = app.send_task(calc_blueprint.name + '.tasks.prime_palindrome_service', kwargs={'index': index})
    time.sleep(3)
    result = app.AsyncResult(task.id).result
    print (result)  
    return json.dumps({"result": result, "id": task.id})