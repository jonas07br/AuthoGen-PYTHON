def selecionar_autores_interativo(autores_disponiveis):
    """
    Permite ao usuário selecionar até 3 autores de forma interativa.
    
    Args:
        autores_disponiveis: lista de autores disponíveis
        
    Returns:
        lista com até 3 autores selecionados
    """
    print("\n=== SELEÇÃO DE AUTORES TARGET ===")
    print("\nAutores disponíveis:")
    
    for i, autor in enumerate(autores_disponiveis, 1):
        print(f"{i}. {autor}")
    
    print("\nDigite os números dos autores (separados por vírgula)")
    print("Exemplo: 1,3,5")
    print("Máximo: 3 autores")
    
    while True:
        try:
            entrada = input("\nSua seleção: ").strip()
            indices = [int(x.strip()) for x in entrada.split(',')]
            
            if len(indices) > 3:
                print("Erro: Selecione no máximo 3 autores!")
                continue
            
            if any(i < 1 or i > len(autores_disponiveis) for i in indices):
                print(f"Erro: Números devem estar entre 1 e {len(autores_disponiveis)}!")
                continue
            
            autores_selecionados = [autores_disponiveis[i-1] for i in indices]
            
            print("\nAutores selecionados:")
            for autor in autores_selecionados:
                print(f"  • {autor}")
            
            return autores_selecionados
            
        except ValueError:
            print("Erro: Digite números válidos separados por vírgula!")
        except KeyboardInterrupt:
            print("\n\nSeleção cancelada!")
            return []
