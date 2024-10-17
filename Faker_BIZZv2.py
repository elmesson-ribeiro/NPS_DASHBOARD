import os
import pandas as pd
import faker
import random
import datetime

# Criando um objeto Faker para gerar dados aleatórios
fake = faker.Faker('pt_BR')

# Definindo os planos e seus respectivos valores
planos = {
    'fibra 100 MEGA': 79.90,
    'fibra 550 MEGA': 99.90,
    'fibra 350 MEGA': 89.90
}

# Motivos de cancelamento
motivos_cancelamento = [
    "Insatisfação com o produto ou serviço",
    "Atendimento ao cliente insatisfatório",
    "Preço elevado ou valor baixo percebido",
    "Mudança de circunstâncias",
    "Competição",
    "Experiência ruim por parte do usuário",
    "Mudança de prioridades ou interesses",
    "Falta de engajamento ou valor percebido",
    "Problemas de faturamento ou pagamento"
    "Falta de opções de planos"
    "Problemas com a conexão"
]

# Custo de aquisição por canal
custo_aquisicao = {
    'Site': 60,
    'Loja Física': 100,
    'Aplicativo': 70
}

# Função para gerar uma data aleatória entre 2023 e 2024
def gerar_data_assinatura():
    date_start = datetime.date(2023, 1, 1)
    date_end = datetime.date(2024, 12, 31)
    return fake.date_between_dates(date_start=date_start, date_end=date_end)

# Função para gerar uma data de churn aleatória ou None
def gerar_data_churn(data_assinatura):
    if random.random() < 0.07:  # 7% de churn
        date_end = datetime.date(2024, 12, 31)
        return fake.date_between_dates(date_start=data_assinatura, date_end=date_end)
    else:
        return None

# Função para calcular probabilidade de churn
def calcular_probabilidade_churn(satisfacao):
    return round(random.uniform(0, 1) * (6 - satisfacao) / 5, 2)

# Função para determinar se o cliente recebeu uma campanha de retenção
def recebeu_campanha(prob_churn):
    return random.choice([True , False]) if prob_churn > 0.9 else False

# Criando uma lista para armazenar os dados
dados = []

for _ in range(110000):
    data_assinatura = gerar_data_assinatura()
    plano_escolhido = random.choice(list(planos.keys()))
    canal_aquisicao = random.choice(['Site', 'Loja Física', 'Aplicativo'])
    
    satisfacao = random.randint(1, 5)
    probabilidade_churn = calcular_probabilidade_churn(satisfacao)
    campanha_retenção = recebeu_campanha(probabilidade_churn)
    
    data = {
        'ID Cliente': random.randint(11000, 99999),
        'Nome': fake.name(),
        'Data_Nascimento': fake.date_between(start_date='-64y', end_date='-20y'),
        'Plano': plano_escolhido,
        'Data de Assinatura': data_assinatura,
        'Data de Churn': gerar_data_churn(data_assinatura),
        'Motivo Cancelamento': None,
        'Valor Mensal': planos[plano_escolhido],
        'Receita Total': 0,  # Inicialmente zero, será calculado posteriormente
        'Segmento': random.choice(['Residencial', 'Empresarial']),
        'Regiões': random.choice(['ES - Barra de São Francisco', 
                                  'ES - Pancas', 
                                  'ES - São Gabriel da Palha',
                                'ES - Águia Branca',
                                'MG - Alvorada de Minas',
                                'MG - Angelândia',
                                'MG - Capelinha',
                                'MG - Conceição do Mato Dentro',
                                'MG - Conceição do Mato Dentro - Agua Fria',
                                'MG - Conceição do Mato Dentro - Alves',
                                'MG - Conceição do Mato Dentro - Barbeiro',
                                'MG - Conceição do Mato Dentro - Beco',
                                'MG - Conceição do Mato Dentro - Buraco',
                                'MG - Conceição do Mato Dentro - Cachoeira da Fumaça',
                                'MG - Conceição do Mato Dentro - Candeias',
                                'MG - Conceição do Mato Dentro - Capitão Felizardo',
                                'MG - Conceição do Mato Dentro - Costa Sena',
                                'MG - Conceição do Mato Dentro - Córregos',
                                'MG - Conceição do Mato Dentro - Farinha Fina',
                                'MG - Conceição do Mato Dentro - Itacolomi',
                                'MG - Conceição do Mato Dentro - Jacaré',
                                'MG - Conceição do Mato Dentro - Jassem',
                                'MG - Conceição do Mato Dentro - Meloso',
                                'MG - Conceição do Mato Dentro - Ouro Fino',
'MG - Conceição do Mato Dentro - Santo Antônio do Norte',
'MG - Conceição do Mato Dentro - São Sebastião do Bonsucesso',
'MG - Conceição do Mato Dentro - Tabuleiro',
'MG - Conceição do Mato Dentro - Tapera',
'MG - Conceição do Mato Dentro - Tijucal',
'MG - Conceição do Mato Dentro - Tres Barras',
'MG - Congonhas do Norte',
'MG - Couto de Magalhães de Minas',
'MG - Curvelo',
'MG - Datas',
'MG - Diamantina',
'MG - Felício dos Santos',
'MG - Franciscópolis',
'MG - Gonzaga',
'MG - Gouveia',
'MG - Governador Valadares - Goiabal',
'MG - Malacacheta',
'MG - Mantena',
'MG - Novo Cruzeiro',
'MG - Poté',
'MG - Presidente Kubitschek',
'MG - Rio Vermelho - Pedra Menina',
'MG - Santana do Riacho - Serra do Cipó',
'MG - Santo Antônio do Itambé',
'MG - Sardoá',
'MG - Senador Modestino Gonçalves',
'MG - Senhora do Porto',
'MG - Serra Azul de Minas',
'MG - Serro',
'MG - Setubinha',
'MG - São Gonçalo do Rio Preto',
'MG - Água Boa']),
        'Canal de Aquisição': canal_aquisicao,
        'Custo de Aquisição': custo_aquisicao[canal_aquisicao],
        'Pontuação de Satisfação': satisfacao,
        'Probabilidade de Churn': probabilidade_churn,
        'Recebeu Campanha de Retenção': campanha_retenção,
        'Contagem de Suporte': random.randint(0, 10),
        'NPS': random.randint(0, 10)
    }
    
    # Atribuir um motivo de cancelamento se o cliente cancelou
    if data['Data de Churn'] is not None:
        data['Motivo Cancelamento'] = random.choice(motivos_cancelamento)

    dados.append(data)

# Criando o DataFrame
df = pd.DataFrame(dados)

# Converte a coluna 'Data de Churn' para o tipo datetime
df['Data de Churn'] = pd.to_datetime(df['Data de Churn'])

# Calculando o tempo de ativação (dias)
df['Tempo de Ativação (Dias)'] = (pd.to_datetime(df['Data de Churn']).fillna(pd.Timestamp('2024-12-31')) - pd.to_datetime(df['Data de Assinatura'])).dt.days

# Extraindo o mês de cancelamento, garantindo que 'Data de Churn' esteja em formato datetime
df['Mês de Cancelamento'] = df['Data de Churn'].dt.strftime('%B')

# Calculando a receita total com base no tempo de assinatura
df['Receita Total'] = (pd.to_datetime('2024-12-31') - pd.to_datetime(df['Data de Assinatura'])).dt.days // 30 * df['Valor Mensal']

# Calculando a rentabilidade (Receita Total - CAC)
df['Rentabilidade (Lucro)'] = df['Receita Total'] - df['Custo de Aquisição']

# Criar DataFrames separados para clientes e motivos de cancelamento
motivo_df = pd.DataFrame({
    'Motivo Cancelamento': motivos_cancelamento
})

# Obtendo o diretório atual
current_directory = os.getcwd()

# Definindo o caminho do arquivo Excel dinamicamente
file_path = os.path.join(current_directory, 'churn_clientes_Bizz_expanded.xlsx')

# Salvando os DataFrames em um arquivo Excel com múltiplas planilhas
with pd.ExcelWriter(file_path) as writer:
    df.to_excel(writer, sheet_name='Clientes', index=False)
    motivo_df.to_excel(writer, sheet_name='Motivo_Cancelamentos', index=False)

print(f"Base de dados Churn gerada com sucesso! Arquivo salvo em: {file_path}")
