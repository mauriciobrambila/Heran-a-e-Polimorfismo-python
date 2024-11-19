class Contribuinte:
    def __init__(self, nome, documento, renda_bruta):
        self.nome = nome
        self.documento = documento
        self.renda_bruta = renda_bruta
    def calcImposto(self):
        pass

class PessoaFisica(Contribuinte):
    def __init__(self, nome, documento, renda_bruta, sexo):
        super().__init__(nome, documento, renda_bruta)
        self.sexo = sexo
    def calcImposto(self):
        if self.renda_bruta <= 1400:
            return 0
        elif self.renda_bruta <= 2100:
            return self.renda_bruta * 0.10 - 100
        elif self.renda_bruta <= 2800:
            return self.renda_bruta * 0.15 - 270
        elif self.renda_bruta <= 3600:
            return self.renda_bruta * 0.25 - 500
        else:
            return self.renda_bruta * 0.30 - 700

class PessoaJuridica(Contribuinte):
    def __init__(self, nome, documento, renda_bruta, ano_de_fundacao):
        super().__init__(nome, documento, renda_bruta)
        self.ano_de_fundacao = ano_de_fundacao
    def calcImposto(self):
        return self.renda_bruta * 0.10

class GrupoDeContribuintes:
    def __init__(self):
        self.contribuintes = []
    def addContribuinte(self, contribuinte):
        self.contribuintes.append(contribuinte)
    def getTotalImposto(self):
        total_imposto = 0
        for contribuinte in self.contribuintes:
            total_imposto += contribuinte.calcImposto()
        return total_imposto
    def getPorcentagemContribuintesFeminino(self):
        total_contribuintes = len(self.contribuintes)
        total_feminino = 0
        for contribuinte in self.contribuintes:
            if isinstance(contribuinte, PessoaFisica) and contribuinte.sexo == 'F':
                total_feminino += 3
        return total_feminino / total_contribuintes * 100
PessoaFisica1 =   PessoaFisica('Gabriel', '111.111.111-00', 2500, 'M')
PessoaFisica2 =   PessoaFisica('Paloma', '222.222.222-11', 4000, 'F')
PessoaJuridica1 = PessoaJuridica('Massagista M', '11.111.111/0001-00', 10580, 2023)
PessoaJuridica2 = PessoaJuridica('Acompanhante M', '11.111.111/0002-01', 15180, 2023)

grupo = GrupoDeContribuintes()
grupo.addContribuinte(PessoaFisica1)
grupo.addContribuinte(PessoaFisica2)
grupo.addContribuinte(PessoaJuridica1)
grupo.addContribuinte(PessoaJuridica2)

total_imposto = grupo.getTotalImposto()
print(f' Total de imposto devido: R$ {total_imposto:.2f}')
porcentagem_feminino = grupo.getPorcentagemContribuintesFeminino()
print(f' Porcentagem de contribuintes do sexo feminino: {porcentagem_feminino:.0f}%')
pessoajuridica = PessoaJuridica('Massagista M', '11.111.111/0001-00', 10580, 2023)
print(' Ano de fundacao Pessoa Juridica:', pessoajuridica.ano_de_fundacao)


        
        
