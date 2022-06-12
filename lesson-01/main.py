from LinkedList import LinkedList
from cache import LRUCache

if __name__ == '__main__':
    cache = LRUCache(4)

    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'James')

    print(cache.get('Jesse'))  # вернёт 'James'
    cache.rem('Walter')
    print(cache.get('Walter'))  # вернёт ''

    cache.set('a', '1')
    cache.set('b', '2')
    cache.set('c', '3')
    cache.set('d', '4')
    cache.set('e', '5')
    cache.set('f', '6')
    cache.get('c')
    cache.get('c')
    cache.get('d')
    cache.get('f')
    cache.get('e')
    cache.set('g', '7')

    print('=' * 100)
    cache.queue_list.print()
