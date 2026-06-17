from services.supabase_service import buscar_contatos

contatos = buscar_contatos()

for contato in contatos:
    print(contato)