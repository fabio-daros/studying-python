def eat(food, is_healthy):
    if is_healthy:
        final = 'I want be healthy.'
    else:
        final = 'you only live once.'
    return f'I eat {food}, because {final}'


def sleep(hours):
    if hours > 8:
        return f'sleep for {hours} hours.'
    else:
        return f'sleep for {hours} hours.'
