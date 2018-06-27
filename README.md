# rebirth - nome fantasia "COK Store"
Exemplo de webiste em Django

[![Build Status](https://travis-ci.org/alisonamerico/rebirth.svg?branch=master)](https://travis-ci.org/alisonamerico/rebirth)
[![Updates](https://pyup.io/repos/github/alisonamerico/rebirth/shield.svg)](https://pyup.io/repos/github/alisonamerico/rebirth/)
[![Python 3](https://pyup.io/repos/github/alisonamerico/rebirth/python-3-shield.svg)](https://pyup.io/repos/github/alisonamerico/rebirth/)
[![codecov](https://codecov.io/gh/alisonamerico/rebirth/branch/master/graph/badge.svg)](https://codecov.io/gh/alisonamerico/rebirth)

Para instalar ambiente de desenvolvimento:

Instale o python 3

Cria um virtualenv na raiz do projeto:

```
python3 -m venv .venv
```

Ative o virtualenv e instale as dependências de desenvolvimento:

```
source .venv/bin/activate
pip install requirements-dev.txt
```

Confira se o código está de acordo com a PEP8:

```
flake8 .
```

Para rodar os testes com cobertura:

```
pytest rebirth --cov=rebirth
```