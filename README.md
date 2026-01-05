# Projeto de Graduação - Pedra, Papel e Tesoura 🎓🎮

Este projeto implementa o clássico jogo **Pedra, Papel e Tesoura** em Python, como parte da graduação em **Análise e Desenvolvimento de Sistemas**.  
O usuário joga contra o computador, que escolhe aleatoriamente uma das opções.

---

## 🚀 Tecnologias utilizadas
- Python 3.x
- Biblioteca padrão `random` (para gerar escolhas aleatórias)

---

## 📖 Como funciona
1. O programa solicita que o usuário escolha:
   - `P` → Papel  
   - `T` → Tesoura  
   - `R` → Pedra  
2. O computador gera uma escolha aleatória.  
3. O resultado é exibido:
   - Empate
   - Vitória do usuário
   - Vitória da CPU
   - Caso o usuário digite uma opção inválida, perde por WO.

O jogo continua até que o usuário escolha **N** para encerrar.

---

## 📂 Estrutura do código
- **Função `Humano(forma)`** → interpreta a entrada do usuário.  
- **Função `CPU(forma2)`** → traduz a escolha aleatória da máquina.  
- **Loop principal** → controla as rodadas e verifica o vencedor.  

---

## ⚙️ Como executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/PabloPHSilva/PHenry_dev1.git
