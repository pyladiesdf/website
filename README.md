# PyLadies DF Website

## Descrição do website das PyLadies DF

O website da PyLadies DF é um local para proporcionar um maior aprendizado e troca de conhecimentos
sobre programação. Possui sugestões de materiais para estudos, nossas mídias sociais, link para o
nosso blog e um fórum com as dúvidas mais recorrentes, que é respondido pela comudidade PyLadies.

## Como executar o projeto

### Requisitos do sistema

- Python 3.8.5

### Linux / Mac

``` console
$ cd website
$ python -m venv venv
$ source venv/bin/activate
(venv) $ pip install -U pip
(venv) $ pip install -r requirements.txt
(venv) $ python manage.py collectstatic
(venv) $ export DEBUG=True; python manage.py runserver
```

### Windows

``` console
$ cd website
$ virtualenv venv
$ venv\Scripts\activate
(venv) $ pip install -r requirements.txt
(venv) python manage.py collectstatic
(venv) $ python manage.py runserver
```
## Quem Fez este website

Esse website foi produzido pelas Pyladies DF.
