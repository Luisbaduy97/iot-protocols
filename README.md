# iot-protocols

## Env
```python
virtualenv venv
pip install -r requirements.txt
```

## AMQP

### Iniciar un contenedor iteractivo de rabbitmq
* user: guest
* password: guest

```bash
docker run --rm -it --hostname my-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```

### Work queues
#### Iniciar un worker
```bash
cd amqp
python worker.py
```
#### Iniciar una nueva tarea
```bash
cd amqp
python new_task.py
```

### Publish/Subscribe
Suscribirse a una cola
```bash
cd amqp/cloud_amqp
python consume.py
```

Publicar en una cola
```bash
cd amqp/cloud_amqp
python publish.py
```


**Nota: puedes iniciar los worker que quieras**


