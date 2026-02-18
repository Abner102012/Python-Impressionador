faturamento = {
    'jan': 'R$ 95.141,98',
    'fev': 'R$ 95.425,16',
    'mar': 'R$ 89.716,31',
    'abr': 'R$ 78.459,99',
    'mai': 'R$ 71.087,28',
    'jun': 'R$ 83.911,06',
    'jul': 'R$ 56.467,26',
    'ago': 'R$ 88.513,58',
    'set': 'R$ 66.552,49',
    'out': 'R$ 80.164,07',
    'nov': 'R$ 66.964,33',
    'dez': 'R$ 71.525,25',
}

def transformar_numero(texto):
    texto = texto.replace("R$", "").replace(" ", "").replace(".", "").replace(",", ".")
    return float(texto)

def calcular_imposto_men(valor_faturamento):
    iss = valor_faturamento * 0.05
    pis = valor_faturamento * 0.0065 
    cofins = valor_faturamento * 0.03
    return iss + pis + cofins

def calcular_imposto_tri(valor_faturamento):
    ir = valor_faturamento * 0.048
    csll = valor_faturamento * 0.0288  
    
    # Correção do nome da variável: adicional_ir
    if valor_faturamento > 20000:
        adicional_ir = (valor_faturamento - 20000) * 0.1 
    else:
        adicional_ir = 0
        
    return ir + csll + adicional_ir

faturamento_imposto = {}
for mes in faturamento:
    valor_faturamento = transformar_numero(faturamento[mes])
    imposto_mensal = calcular_imposto_men(valor_faturamento)
    imposto_trimensal = calcular_imposto_tri(valor_faturamento)
    faturamento_imposto[mes] = (valor_faturamento, imposto_mensal, imposto_trimensal)

# Exemplo de visualização
print(f"{'Mês':<5} | {'Faturamento':<12} | {'Imp. Mensal':<12} | {'Imp. Trimestral':<12}")
for mes, valores in faturamento_imposto.items():
    print(f"{mes:<5} | R$ {valores[0]:>10.2f} | R$ {valores[1]:>10.2f} | R$ {valores[2]:>10.2f}")