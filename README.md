# Pub/Sub

## Ambiente utilizado

|                | **Versão** |
| :------------- | :--------: |
| ubuntu         |   18.04    |
| docker         |  19.03.9   |
| docker-compose |   1.25.4   |
| python         |   3.8.3    |
| php            |   7.4.6    |
| node           |  12.16.3   |
| npm            |   6.14.4   |
| go             |   1.14.3   |

## Redis

```
docker-compose up --build
```

## Instalação

### Python

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Node

```
npm install
```

### Go

```
go get github.com/gomodule/redigo/redis
```

### PHP

```
composer install
```

## Execução dos Subscribes

### Python

```
python subscribes/service_csv.py
python subscribes/service_excel.py
python subscribes/service_html.py
```

### Node

```
node subscribes/service_xml.js
```

### Go

```
go run subscribes/service_csv.go
```

### PHP

```
php subscribes/service_csv.php
```

## Execução do Publisher

```
python publisher.py
```
