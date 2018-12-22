Menu
====
1. Primeiros Passos
  * [Contribuindo](#contribuindo)
  * [Preparando o ambiente local](#preparando-o-ambiente-local)

2. Criando e Adicionando
  * [Criar um novo post](#criar-um-novo-post)
  * [Adicionar eventos](#adicionar-eventos)
  * [Adicionar ladies](#adicionar-ladies)

3. Deploy
  * [Atualizando o site](#atualizando-o-site)


Contribuindo
============

1. Fork o projeto
2. Crie uma branch para a feature em que trabalhará: `git checkout -b new_feature`
3. Faça commit das suas alterações: `git commit -m 'Add some feature'`
4. Faça push desses commits para sua branch: `git push origin new_feature`
5. Envie um pull request para o nosso repositório

Obs.: Nós usamos inglês como linguagem padrão dos commits (:


Preparando o ambiente local
--------------------------

- Antes de mais nada, verifique se você tem o **Python 3.6** instalado na sua máquina.


Criar um novo Post
------------------
<!--- TODO --->


Criar uma nova Página
---------------------
<!--- TODO --->


Adicionar Eventos
-----------------
<!--- TODO --->


Adicionar Ladies
----------------

Para adicionar uma nova lady, edite o arquivo `blog/content/ladies.yml` . Ele possui o seguinte formato:


```yaml
- name: NOME DA LADY
  cidade: origem da lady
  url: portfolio ou curriculum da lady
  github: github da lady (apenas o nome de usuário)
  twitter: twitter da lady (apenas o nome de usuário)
  facebook: facebook da lady (apenas o nome de usuário)
  image: NOME DA IMAGEM DA LADY
```

O `NOME DA IMAGEM DA LADY` pode ser:

#### Caminho relativo

O endereço da foto em nosso projeto.

*Exemplo:* `nomedalady.jpg`

Nesse caso, a nova imagem deverá ser inserida no diretório `blog/static/blog/img/ladies`

**Atenção:** A imagem precisa ser `100px por 100px`.


Editar Layout
-------------
<!--- TODO --->


Atualizando o site
------------------

O deploy leva cerca de 2 minutos e acontece através da ferramenta de integração contínua Circle CI.

__** Atenção: Sempre confira se as alterações no ambiente local se comportam como o esperado antes de mandar PR para a master **__
