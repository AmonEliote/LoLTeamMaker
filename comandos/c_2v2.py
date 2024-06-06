import random

async def organizar_2v2(ctx, *nomes):
    if not nomes:
        await ctx.send('Por favor, forneça uma lista de nomes separados por `ESPAÇO` para organizar os times.')
        return

    nomes = list(nomes)
    random.shuffle(nomes)

    num_nomes = len(nomes)
    num_times = num_nomes // 2  # Número de times será metade do número de nomes
    if num_nomes % 2 != 0:
        num_times += 1  # Adiciona um time extra se houver número ímpar de nomes

    times = [[] for _ in range(num_times)]

    for i, nome in enumerate(nomes):
        times[i % num_times].append(nome)

    resposta = ""
    for i, time in enumerate(times, 1):
        resposta += f'**Time {i}:** {", ".join(time)}\n'

    await ctx.send(resposta)