import pygame


def inicializa():
    pygame.init()
    w = pygame.display.set_mode((640, 480))
    pygame.key.set_repeat(50)

    state = {
        "nave_x" : 0,
        "nave_y" : 0,
    }

    assets = {
        'player': pygame.image.load('mergulhador.png'),
        'fundo' : pygame.image.load('fundo.png')
    }

    state["tamanho_nave"] = assets['player'].get_size()

    return w, assets, state



def finaliza():
    pygame.quit()


def desenha(window, assets, state):
    window.fill((255,255,0))
    window.blit(assets["fundo"], (0,0))
    window.blit(assets["player"], (state["nave_x"],state["nave_y"]))
    pygame.display.update()


def recebe_eventos(state):
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False
        # if ev.type == pygame.KEYDOWN:
        #     if ev.key == pygame.K_RIGHT:
        #         state["nave_x"] += 20
        #     if ev.key == pygame.K_UP:
        #         state["nave_y"] -= 20
        #     if ev.key == pygame.K_LEFT:
        #         state["nave_x"] -= 20
        #     if ev.key == pygame.K_DOWN:
        #         state["nave_y"] += 20
        #     if state["nave_y"] > 410:
        #         state["nave_y"] -= 20
        #     if state['nave_y'] < 0:
        #         state["nave_y"] += 20
        #     if state['nave_x'] > 550:
        #         state['nave_x'] -= 20
        #     if state['nave_x'] < 0:
        #         state['nave_x'] += 20
        state['nave_x'] = (pygame.mouse.get_pos()[0] - 40)
        state['nave_y'] = (pygame.mouse.get_pos()[1] - 20)
        if state["nave_y"] > 410:
                state["nave_y"] -= 20
        if state['nave_y'] < 20:
                state["nave_y"] += 20
        if state['nave_x'] > 550:
                state['nave_x'] -= 20
        if state['nave_x'] < 0:
                state['nave_x'] += 20



    return True

def gameloop(window, assets, state):
    while recebe_eventos(state):
        desenha(window, assets, state)


if __name__ == '__main__':
    window, assets, state = inicializa()
    gameloop(window, assets, state)
    finaliza()