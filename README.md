# ⚽ Sistema de Treinamento de Robô de Futebol

Este projeto foi desenvolvido como um exercício prático para consolidar meus conhecimentos iniciais em **Programação Orientada a Objetos (POO)** utilizando Python. 🐍

## 📝 Sobre o Exercício
O objetivo foi criar uma classe chamada `RoboJogador` que simula as atividades de um atleta robótico. O desafio principal foi gerenciar o "estado" do robô (dentro ou fora de campo) e aplicar regras de segurança para seus atributos.

## 🛠️ Funcionalidades e Lógica Aplicada
* **Gerenciamento de Estado:** O robô possui métodos para `entrar_em_campo()` e `sair_do_campo()`, impedindo que ações de treino sejam feitas fora das quatro linhas.
* **Sistema de Potência:** O método `treinar_chute()` aumenta a força do robô, enquanto o `descansar()` a diminui.
* **Travas de Segurança (Boundaries):** * **Limite Superior:** A potência é travada em 100 para evitar sobrecarga nos motores.
    * **Limite Inferior:** Implementei uma verificação para que a potência nunca seja negativa (menor que 0), garantindo a integridade dos dados.

## 🚀 Tecnologias Utilizadas
* **Python 3**
* **PyCharm** (IDE utilizada no desenvolvimento)
* **Git/GitHub** (Versionamento)

---
Este é mais um passo na minha jornada como desenvolvedor! Aceito sugestões e feedbacks. 🚀
