
# Sistema bancário

Projeto para simular um ecossistema bancário com suas extremidades, validando o fim a fim da transação por inúmeros metodos diferentes (TED, PIX) com validação de cheque especial.

# Design
- Abstrai as funcionalidades especificas e regras de cada meio de pagamento(TED, PIX, Cartão, maquininha)
- Garante a escalabilidade de novas operações bancárias, novos sistemas de pagamentos sem alterações significativas no código
- Sem interação com banco de dados e/ou inputs externos, testado apenas com testes unitários para efeitos de estudos.

# UML

![Logo](docs/imgs/uml.png)

# RoadMap
- Implementar gravação e leitura de estados das entidades e informações bancárias em um banco de dados, junto com suas operações(atualizar saldo, etc).
- Implementar inputs externos para simular realmente uma interface de um app de banco.
- Implementar metodos de pagamento via PIX, Cartões e Maquininhas.
- Criar factories ou strategies para implementar o metodo de pagamento

# Use Cases
- Criar duas instancias de pessoas(origem e destinatário)
- Criar as contas e associamos a cada pessoa
- Instanciar o metodo de transação/pagamento:
    - TED
    - PIX
    - CARD
    - Withdraw
- Criar uma instancia do atual tipo de conta do usuário (corrente, salario e etc) para validar os metodos disponiveis/aplica regras com base no tipo da conta, que recebe a pessoa e o metodo de transação.
- Criar uma instancia de serviços de conta, que recebe o tipo da conta( salario, corrente)

- A implementação facilita, abstrai e modulariza a implementação e modificação facilmente das implementas, pois não dependemos de fato delas, e sim de interfaces e abstrações, vide exemplo abaixo. Claro que não implementamos as checagens especificas do PIX ou TED, mas isso ilustra a capacidade do sistema.
- Consulte o exemplo: [Exemplo](docs/examples/modularity.md)