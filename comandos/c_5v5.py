import random

async def organizar_5v5(interaction, *nomes):
    if not nomes:
        await interaction.response.send_message('Por favor, forneça uma lista de nomes separados por `ESPAÇO` para organizar os times.')
        return

    nomes = list(nomes)
    if len(nomes) > 10:
        await interaction.response.send_message('Por favor, forneça no máximo 10 nomes.')
        return
    elif len(nomes) < 10:
        await interaction.response.send_message('Por favor, forneça pelo menos 10 nomes.')
        return

    random.shuffle(nomes)

    tamanho = int(len(nomes) / 2)
    time1 = nomes[:tamanho]
    time2 = nomes[tamanho:]

    resposta = f'**Time 1:** {", ".join(time1)}\n'
    resposta += f'**Time 2:** {", ".join(time2)}\n'

    await interaction.response.send_message(resposta)
