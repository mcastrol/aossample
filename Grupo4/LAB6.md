# LAB 6 - Api Gateways

## Objetivo del lab

Aprender a crear una API REST y a configurarla desde AWS.
Tendremos dos tutoriales distintos.
    - 1.1 Crear una API REST importando un ejemplo.
    - 1.2 Desarrollar una API Gateway con integración Lambda.

## Pasos del laboratorio

### 1.1 Tutorial crear una API REST importando un ejemplo

En este primer laboratorio, importaremos una API REST de ejemplo directamente y la configuraremos:
Aqui esta el link del tutorial completo por amazon:  [Link al tutorial de Amazon para crear un API importando un ejemplo][url1]

[url1]: https://docs.aws.amazon.com/es_es/apigateway/latest/developerguide/api-gateway-create-api-from-example.html

### 1.2 Tutorial desarrollar una API Gateway con intergración Lambda.

Aqui esta el link del tutorial completo por amazon:  [Link al tutorial de Amazon para crear un API importando un ejemplo][url2]

[url2]: https://docs.aws.amazon.com/es_es/apigateway/latest/developerguide/api-gateway-create-api-as-simple-proxy-for-lambda.html

**Apuntes:**

- En este caso, nosotros hemos escogido usar Pyhton, ya que nos sentimos más comodos que con Node.js.
- Tendremos que crear un metodo de tipo "función Lambda".
- ! IMPORTANTE ! --> En la creación del ANY, marcar "Integración de Proxy de Lambda"

