from app.funcao import funcao_ola

def test_ola_mundo():
    saida = funcao_ola()
    gabarito = "Hello World!"
    assert saida == gabarito