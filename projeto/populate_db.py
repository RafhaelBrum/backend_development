import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')

import django
django.setup()

from faker import Faker
import random
from datetime import timedelta
from app.models import Topico, Pagina, RegistroAcesso

fake = Faker()
        
def criar_dados_falsos():
    for _ in range(10):
        titulo = fake.company()
        topico = Topico.objects.create(titulo=titulo)

        for _ in range(3):
            conteudo = fake.paragraphs(nb=3)
            pagina = Pagina.objects.create(topico=topico, conteudo='\n'.join(conteudo))

            for _ in range(3):
                data_acesso = fake.date_time_this_decade(before_now=True, after_now=False)  
                data_acesso += timedelta(minutes=random.randint(1, 1440))
                RegistroAcesso.objects.create(pagina=pagina, data_acesso=data_acesso)

                
if __name__ == '__main__':
    criar_dados_falsos()
    print("Dados falsos criados com sucesso!")