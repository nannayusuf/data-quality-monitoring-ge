# Sistema de Monitoramento de Qualidade de Dados com Great Expectations

## Estrutura do Projeto

```
projeto1_great_expectations/
├── airflow/                # DAGs e configurações do Airflow para orquestração
│   ├── dags/               # Definição de DAGs para validação automática
│   └── plugins/            # Plugins customizados para o Airflow
├── config/                 # Arquivos de configuração
│   ├── great_expectations/ # Configuração do Great Expectations
│   └── database/           # Configuração de conexões com bancos de dados
├── dashboard/              # Código para dashboard Streamlit
│   ├── app.py              # Aplicação principal do dashboard
│   └── components/         # Componentes reutilizáveis do dashboard
├── data/                   # Dados de exemplo e datasets
│   ├── raw/                # Dados brutos para validação
│   └── processed/          # Dados processados após validação
├── docs/                   # Documentação do projeto
│   ├── architecture/       # Diagramas e descrição da arquitetura
│   └── user_guide/         # Guia de uso do sistema
├── notebooks/              # Jupyter notebooks para análise exploratória
│   ├── exploratory/        # Análises exploratórias iniciais
│   └── validation/         # Notebooks de validação de dados
├── src/                    # Código-fonte principal
│   ├── expectations/       # Definições de expectativas de dados
│   ├── validation/         # Scripts de validação
│   ├── storage/            # Código para armazenamento de métricas
│   └── alerts/             # Sistema de alertas para falhas
└── tests/                  # Testes automatizados
    ├── unit/               # Testes unitários
    └── integration/        # Testes de integração
```

## Descrição dos Componentes

### airflow/
Contém as configurações e DAGs do Apache Airflow para orquestração do pipeline de validação. Os DAGs definem o fluxo de trabalho para execução automática das validações de qualidade.

### config/
Armazena arquivos de configuração para o Great Expectations, conexões com bancos de dados e outras configurações do sistema.

### dashboard/
Código para o dashboard Streamlit que visualiza métricas de qualidade e resultados das validações.

### data/
Diretório para armazenar dados de exemplo e datasets utilizados no projeto. Inclui dados brutos e processados.

### docs/
Documentação completa do projeto, incluindo diagramas de arquitetura, guias de uso e documentação técnica.

### notebooks/
Jupyter notebooks para análise exploratória de dados e desenvolvimento de validações.

### src/
Código-fonte principal do sistema, organizado em módulos para definição de expectativas, validação, armazenamento de métricas e alertas.

### tests/
Testes automatizados para garantir a qualidade do código e a correta funcionalidade do sistema.

## Arquivos Principais

- `src/expectations/expectations.py`: Define as expectativas de qualidade para os datasets
- `src/validation/validator.py`: Implementa a lógica de validação usando Great Expectations
- `airflow/dags/validation_dag.py`: Define o DAG para execução automática das validações
- `dashboard/app.py`: Aplicação Streamlit para visualização de métricas de qualidade
- `config/great_expectations/great_expectations.yml`: Configuração principal do Great Expectations

## Como Iniciar

1. Configure o ambiente virtual Python
2. Instale as dependências necessárias
3. Configure o Great Expectations com suas fontes de dados
4. Defina suas expectativas de qualidade
5. Configure o Airflow para orquestração
6. Execute o dashboard Streamlit para visualização

## Próximos Passos

- Implementar expectativas específicas para seus datasets
- Configurar armazenamento de métricas históricas
- Desenvolver sistema de alertas para falhas de validação
- Integrar com outras ferramentas de monitoramento
